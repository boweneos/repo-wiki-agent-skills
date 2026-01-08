#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["click>=8.0", "anthropic>=0.18"]
# ///
"""
Repo Wiki LLM - Generate documentation using Claude API.

Usage:
    ANTHROPIC_API_KEY=xxx uv run scripts/repo_wiki_llm.py generate /path/to/repo
    ANTHROPIC_API_KEY=xxx uv run scripts/repo_wiki_llm.py generate /path/to/repo --component auth
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import click

try:
    import anthropic
except ImportError:
    anthropic = None


def get_api_client():
    """Get Anthropic API client."""
    if anthropic is None:
        click.echo("❌ anthropic package not installed. Run: uv pip install anthropic")
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        click.echo("❌ ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    return anthropic.Anthropic(api_key=api_key)


def load_code_index(repo: Path) -> dict:
    """Load the code index."""
    index_file = repo / ".repo_wiki/code_index.json"
    if not index_file.exists():
        click.echo("❌ Code index not found. Run 'repo_wiki_cli.py index' first.")
        sys.exit(1)

    with open(index_file) as f:
        return json.load(f)


def load_state(repo: Path) -> dict:
    """Load wiki state."""
    state_file = repo / ".repo_wiki/state.json"
    if not state_file.exists():
        click.echo("❌ Wiki not initialized. Run 'repo_wiki_cli.py init' first.")
        sys.exit(1)

    with open(state_file) as f:
        return json.load(f)


def read_file_with_lines(filepath: Path, max_lines: int = 500) -> tuple[str, int]:
    """Read file content with line numbers."""
    try:
        with open(filepath, errors="ignore") as f:
            lines = f.readlines()[:max_lines]
        
        numbered = []
        for i, line in enumerate(lines, 1):
            numbered.append(f"{i:4d}| {line.rstrip()}")
        
        return "\n".join(numbered), len(lines)
    except Exception as e:
        return f"Error reading file: {e}", 0


def find_component_files(repo: Path, component_path: str, max_files: int = 10) -> list[dict]:
    """Find key files in a component."""
    component_dir = repo / component_path
    if not component_dir.exists():
        return []

    files = []
    extensions = {".ts", ".tsx", ".js", ".jsx", ".py", ".go", ".rs", ".java"}

    for file in component_dir.rglob("*"):
        if file.is_file() and file.suffix in extensions:
            rel_path = str(file.relative_to(repo))
            if "node_modules" not in rel_path and "__pycache__" not in rel_path:
                content, line_count = read_file_with_lines(file, max_lines=200)
                files.append({
                    "path": rel_path,
                    "content": content,
                    "line_count": line_count,
                })
                if len(files) >= max_files:
                    break

    return files


def generate_component_doc(
    client: anthropic.Anthropic,
    repo: Path,
    component: dict,
    state: dict,
) -> str:
    """Generate documentation for a component using Claude."""
    
    component_name = component["name"]
    component_path = component["path"]
    
    click.echo(f"   Analyzing {component_name}...")
    
    # Get component files
    files = find_component_files(repo, component_path)
    
    if not files:
        return f"# {component_name}\n\nNo source files found in `{component_path}`.\n"

    # Build context
    file_context = "\n\n".join([
        f"### File: {f['path']} ({f['line_count']} lines)\n```\n{f['content']}\n```"
        for f in files
    ])

    prompt = f"""You are a technical documentation writer. Generate documentation for this code component with CITATIONS.

Component: {component_name}
Path: {component_path}
Repository: {repo.name}
Commit: {state.get('baseline_commit', 'unknown')[:8]}

Files in this component:
{file_context}

Generate a markdown documentation page with these requirements:

1. Start with YAML frontmatter:
```yaml
---
generated_by: repo-wiki-agent
baseline_commit: "{state.get('baseline_commit', '')}"
last_updated: "{datetime.now().strftime('%Y-%m-%d')}"
---
```

2. Include a managed block marker at the start of generated content:
<!-- BEGIN:REPO_WIKI_MANAGED -->

3. For EVERY technical claim, add a citation in this format:
   - Use footnotes: "The server starts on port 3000[^1]"
   - At the bottom: "[^1]: `{component_path}/server.ts` L12-L48"

4. Document:
   - Overview: What this component does
   - Key Files: List main files with their purposes (with citations)
   - Key Interfaces: Main exported functions/classes (with line citations)
   - Configuration: Any config options (with citations to defaults)

5. End with:
<!-- END:REPO_WIKI_MANAGED -->

## Notes
(Space for team documentation)

IMPORTANT: Every factual statement about the code MUST have a citation with file path and line numbers."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except Exception as e:
        click.echo(f"   ⚠️  Error generating docs for {component_name}: {e}")
        return f"# {component_name}\n\nError generating documentation: {e}\n"


def generate_overview_doc(
    client: anthropic.Anthropic,
    repo: Path,
    code_index: dict,
    state: dict,
) -> str:
    """Generate overview documentation."""
    
    click.echo("   Generating overview...")

    # Get some key files for context
    entrypoints = code_index.get("entrypoints", [])[:5]
    entrypoint_contents = []
    for ep in entrypoints:
        ep_path = repo / ep
        if ep_path.exists():
            content, _ = read_file_with_lines(ep_path, max_lines=100)
            entrypoint_contents.append(f"### {ep}\n```\n{content}\n```")

    prompt = f"""You are a technical documentation writer. Generate an architecture overview with CITATIONS.

Repository: {repo.name}
Technology Stack: {', '.join(code_index.get('technology_stack', {}).keys())}
Total Files: {code_index.get('statistics', {}).get('total_files', 0)}
Components: {json.dumps(code_index.get('components', []), indent=2)}
Entrypoints: {entrypoints}
Config Files: {code_index.get('configuration_files', [])}

Key entrypoint files:
{chr(10).join(entrypoint_contents) if entrypoint_contents else 'No entrypoints found'}

Generate markdown documentation with:

1. YAML frontmatter with generated_by, baseline_commit: "{state.get('baseline_commit', '')}", last_updated
2. Managed block markers
3. System Overview section
4. Technology Stack section  
5. Key Components section (list each with brief description)
6. Architecture notes

EVERY factual claim needs a citation: [^N]: `filepath` L##-L##

End with the closing managed block marker and a "## Design Decisions" section for humans."""

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except Exception as e:
        click.echo(f"   ⚠️  Error generating overview: {e}")
        return f"# Architecture Overview\n\nError: {e}\n"


@click.group()
def cli():
    """Repo Wiki LLM - Generate documentation using Claude API."""
    pass


@cli.command()
@click.argument("repo_path", type=click.Path(exists=True))
@click.option("--component", "-c", help="Generate docs for specific component only")
@click.option("--overview-only", is_flag=True, help="Generate only overview page")
def generate(repo_path: str, component: Optional[str], overview_only: bool):
    """Generate documentation using Claude API."""
    repo = Path(repo_path).resolve()
    click.echo(f"Generating documentation for: {repo}")

    # Check API
    client = get_api_client()

    # Load data
    code_index = load_code_index(repo)
    state = load_state(repo)

    components = code_index.get("components", [])

    if not components and not overview_only:
        click.echo("⚠️  No components found. Generating overview only.")
        overview_only = True

    # Generate overview
    if not component:
        overview = generate_overview_doc(client, repo, code_index, state)
        overview_file = repo / "docs/architecture/overview.md"
        overview_file.parent.mkdir(parents=True, exist_ok=True)
        with open(overview_file, "w") as f:
            f.write(overview)
        click.echo(f"   ✅ Created: docs/architecture/overview.md")

    if overview_only:
        click.echo("\n✅ Overview generated!")
        return

    # Generate component docs
    if component:
        # Find specific component
        comp = next((c for c in components if c["name"] == component), None)
        if not comp:
            click.echo(f"❌ Component '{component}' not found")
            sys.exit(1)
        components = [comp]

    for comp in components:
        doc = generate_component_doc(client, repo, comp, state)
        doc_file = repo / f"docs/components/{comp['name']}.md"
        doc_file.parent.mkdir(parents=True, exist_ok=True)
        with open(doc_file, "w") as f:
            f.write(doc)
        click.echo(f"   ✅ Created: docs/components/{comp['name']}.md")

    # Update manifest
    manifest_file = repo / ".repo_wiki/manifest.json"
    manifest = {"schema_version": "1.0", "generated_at": datetime.utcnow().isoformat() + "Z", "pages": {}}
    
    for md_file in (repo / "docs").rglob("*.md"):
        rel_path = str(md_file.relative_to(repo))
        manifest["pages"][rel_path] = {"generated_at": datetime.utcnow().isoformat() + "Z"}
    
    with open(manifest_file, "w") as f:
        json.dump(manifest, f, indent=2)

    click.echo(f"\n✅ Documentation generated!")
    click.echo(f"   Components: {len(components)}")
    click.echo(f"   Run 'mkdocs serve' to preview")


@cli.command()
@click.argument("repo_path", type=click.Path(exists=True))
def estimate(repo_path: str):
    """Estimate API cost for generation."""
    repo = Path(repo_path).resolve()
    
    code_index = load_code_index(repo)
    components = code_index.get("components", [])
    
    # Rough estimate: ~2000 tokens input + 1000 output per component
    # Plus overview: ~3000 tokens input + 1500 output
    
    component_tokens = len(components) * 3000
    overview_tokens = 4500
    total_tokens = component_tokens + overview_tokens
    
    # Claude pricing (approximate): $3/1M input, $15/1M output
    # Assume 60% input, 40% output
    input_tokens = total_tokens * 0.6
    output_tokens = total_tokens * 0.4
    
    cost = (input_tokens / 1_000_000 * 3) + (output_tokens / 1_000_000 * 15)
    
    click.echo(f"📊 Estimation for {repo.name}:")
    click.echo(f"   Components: {len(components)}")
    click.echo(f"   Estimated tokens: ~{total_tokens:,}")
    click.echo(f"   Estimated cost: ~${cost:.2f}")


if __name__ == "__main__":
    cli()
