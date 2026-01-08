#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["click>=8.0"]
# ///
"""
Repo Wiki CLI - Mechanical operations for wiki generation.

Usage:
    uv run scripts/repo_wiki_cli.py init /path/to/repo
    uv run scripts/repo_wiki_cli.py index /path/to/repo
    uv run scripts/repo_wiki_cli.py detect /path/to/repo
    uv run scripts/repo_wiki_cli.py validate /path/to/repo
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import click


# Default ignore patterns
DEFAULT_IGNORE_PATTERNS = [
    ".git/**",
    "node_modules/**",
    "dist/**",
    "build/**",
    "__pycache__/**",
    "*.pyc",
    ".env",
    "*.pem",
    "*.key",
    "venv/**",
    ".venv/**",
    "coverage/**",
    ".next/**",
]


def get_git_info(repo_path: Path) -> dict:
    """Get git repository information."""
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_path,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
        commit = ""

    try:
        remote = subprocess.check_output(
            ["git", "config", "--get", "remote.origin.url"],
            cwd=repo_path,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
        remote = ""

    return {"commit": commit, "remote": remote}


def detect_tech_stack(repo_path: Path) -> dict:
    """Detect technology stack from file markers."""
    tech = {}

    markers = {
        "package.json": "nodejs",
        "requirements.txt": "python",
        "pyproject.toml": "python",
        "go.mod": "go",
        "Cargo.toml": "rust",
        "pom.xml": "java-maven",
        "build.gradle": "java-gradle",
        "Gemfile": "ruby",
        "composer.json": "php",
    }

    framework_markers = {
        "next.config.js": "nextjs",
        "next.config.ts": "nextjs",
        "next.config.mjs": "nextjs",
        "angular.json": "angular",
        "vue.config.js": "vue",
        "nuxt.config.js": "nuxt",
        "svelte.config.js": "svelte",
        "Dockerfile": "docker",
        "docker-compose.yml": "docker-compose",
        "docker-compose.yaml": "docker-compose",
        ".github/workflows": "github-actions",
        "terraform": "terraform",
        "helm": "helm",
    }

    for marker, tech_name in markers.items():
        if (repo_path / marker).exists():
            tech[tech_name] = True

    for marker, tech_name in framework_markers.items():
        if (repo_path / marker).exists():
            tech[tech_name] = True

    return tech


def find_components(repo_path: Path) -> list[dict]:
    """Find component directories."""
    components = []
    component_dirs = ["src", "lib", "packages", "apps", "app", "components", "modules"]

    for base_dir in component_dirs:
        base_path = repo_path / base_dir
        if base_path.exists() and base_path.is_dir():
            for item in base_path.iterdir():
                if item.is_dir() and not item.name.startswith("."):
                    file_count = sum(1 for _ in item.rglob("*") if _.is_file())
                    components.append(
                        {
                            "name": item.name,
                            "path": str(item.relative_to(repo_path)),
                            "file_count": file_count,
                        }
                    )

    return components


def find_entrypoints(repo_path: Path) -> list[str]:
    """Find main entry files."""
    entrypoints = []
    patterns = [
        "main.py",
        "main.ts",
        "main.js",
        "main.go",
        "index.ts",
        "index.js",
        "app.py",
        "app.ts",
        "app.js",
        "server.py",
        "server.ts",
        "server.js",
    ]

    for pattern in patterns:
        for match in repo_path.rglob(pattern):
            rel_path = str(match.relative_to(repo_path))
            if not any(
                ignore in rel_path
                for ignore in ["node_modules", "dist", "build", "__pycache__", ".next"]
            ):
                entrypoints.append(rel_path)

    return entrypoints[:10]  # Limit to 10


def find_config_files(repo_path: Path) -> list[str]:
    """Find configuration files."""
    configs = []
    config_patterns = [
        "*.config.js",
        "*.config.ts",
        "*.config.mjs",
        "tsconfig.json",
        "jest.config.*",
        "vite.config.*",
        "webpack.config.*",
        ".env.example",
        "config.yml",
        "config.yaml",
        "config.json",
    ]

    # Direct files
    direct_configs = [
        "package.json",
        "requirements.txt",
        "pyproject.toml",
        "Dockerfile",
        "docker-compose.yml",
        ".gitignore",
    ]

    for config in direct_configs:
        if (repo_path / config).exists():
            configs.append(config)

    return configs


def count_files_by_extension(repo_path: Path) -> dict[str, int]:
    """Count files by extension."""
    counts: dict[str, int] = {}

    for file in repo_path.rglob("*"):
        if file.is_file():
            rel_path = str(file.relative_to(repo_path))
            if any(
                ignore in rel_path
                for ignore in ["node_modules", "dist", "build", ".git", "__pycache__"]
            ):
                continue
            ext = file.suffix or "(no extension)"
            counts[ext] = counts.get(ext, 0) + 1

    # Sort by count and return top 10
    sorted_counts = dict(sorted(counts.items(), key=lambda x: -x[1])[:10])
    return sorted_counts


@click.group()
def cli():
    """Repo Wiki CLI - Mechanical operations for wiki generation."""
    pass


@cli.command()
@click.argument("repo_path", type=click.Path(exists=True))
def init(repo_path: str):
    """Initialize wiki structure in a repository."""
    repo = Path(repo_path).resolve()
    click.echo(f"Initializing wiki structure in: {repo}")

    # Get git info
    git_info = get_git_info(repo)

    # Create directories
    dirs = [
        "docs/getting-started",
        "docs/architecture",
        "docs/components",
        "docs/api",
        "docs/operations",
        "docs/adr",
        ".repo_wiki/logs",
    ]

    for d in dirs:
        (repo / d).mkdir(parents=True, exist_ok=True)
        click.echo(f"  Created: {d}")

    # Create state.json
    state = {
        "schema_version": "1.0",
        "baseline_commit": git_info["commit"],
        "last_run_commit": git_info["commit"],
        "repo_name": repo.name,
        "repo_remote_url": git_info["remote"],
        "created_at": datetime.utcnow().isoformat() + "Z",
        "last_updated_at": datetime.utcnow().isoformat() + "Z",
        "ignore_patterns": DEFAULT_IGNORE_PATTERNS,
    }

    state_file = repo / ".repo_wiki/state.json"
    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)
    click.echo(f"  Created: .repo_wiki/state.json")

    # Create manifest.json
    manifest = {
        "schema_version": "1.0",
        "baseline_commit": git_info["commit"],
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "pages": {},
    }

    manifest_file = repo / ".repo_wiki/manifest.json"
    with open(manifest_file, "w") as f:
        json.dump(manifest, f, indent=2)
    click.echo(f"  Created: .repo_wiki/manifest.json")

    # Create mkdocs.yml
    mkdocs_config = f"""site_name: {repo.name} Documentation
repo_url: {git_info['remote']}
edit_uri: blob/main/docs/

theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - search.suggest
    - search.highlight

nav:
  - Home: index.md
  - Getting Started:
      - Local Development: getting-started/local-dev.md
      - Configuration: getting-started/configuration.md
  - Architecture:
      - Overview: architecture/overview.md
  - Components: components/
  - Operations:
      - Build & Test: operations/build-and-test.md

markdown_extensions:
  - footnotes
  - admonition
  - toc:
      permalink: true

plugins:
  - search
"""

    mkdocs_file = repo / "mkdocs.yml"
    if not mkdocs_file.exists():
        with open(mkdocs_file, "w") as f:
            f.write(mkdocs_config)
        click.echo(f"  Created: mkdocs.yml")
    else:
        click.echo(f"  Skipped: mkdocs.yml (already exists)")

    # Create placeholder index.md
    index_content = f"""---
generated_by: repo-wiki-agent
baseline_commit: "{git_info['commit']}"
last_updated: "{datetime.now().strftime('%Y-%m-%d')}"
---

# {repo.name} Documentation

Welcome to the {repo.name} documentation.

<!-- BEGIN:REPO_WIKI_MANAGED -->
## Overview

This documentation is automatically generated and maintained.

**Last updated**: {datetime.now().strftime('%Y-%m-%d')}
**Commit**: `{git_info['commit'][:8] if git_info['commit'] else 'N/A'}`

## Quick Links

- [Getting Started](getting-started/local-dev.md)
- [Architecture](architecture/overview.md)
- [Components](components/)
- [Operations](operations/build-and-test.md)

<!-- END:REPO_WIKI_MANAGED -->

## About

This wiki is maintained by repo-wiki agent skills.
"""

    index_file = repo / "docs/index.md"
    if not index_file.exists():
        with open(index_file, "w") as f:
            f.write(index_content)
        click.echo(f"  Created: docs/index.md")

    click.echo(f"\n✅ Wiki structure initialized!")
    click.echo(f"   Next: Run 'index' command or use /wiki-init in Cursor to generate content")


@cli.command()
@click.argument("repo_path", type=click.Path(exists=True))
def index(repo_path: str):
    """Build code index for a repository."""
    repo = Path(repo_path).resolve()
    click.echo(f"Indexing repository: {repo}")

    # Ensure .repo_wiki exists
    wiki_dir = repo / ".repo_wiki"
    if not wiki_dir.exists():
        click.echo("❌ Wiki not initialized. Run 'init' first.")
        sys.exit(1)

    git_info = get_git_info(repo)
    tech_stack = detect_tech_stack(repo)
    components = find_components(repo)
    entrypoints = find_entrypoints(repo)
    configs = find_config_files(repo)
    file_counts = count_files_by_extension(repo)

    # Build index
    code_index = {
        "schema_version": "1.0",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "repository": repo.name,
        "commit": git_info["commit"],
        "statistics": {
            "by_extension": file_counts,
            "total_files": sum(file_counts.values()),
        },
        "technology_stack": tech_stack,
        "components": components,
        "entrypoints": entrypoints,
        "configuration_files": configs,
    }

    # Save index
    index_file = repo / ".repo_wiki/code_index.json"
    with open(index_file, "w") as f:
        json.dump(code_index, f, indent=2)

    click.echo(f"\n📊 Index Results:")
    click.echo(f"   Total files: {code_index['statistics']['total_files']}")
    click.echo(f"   Technology: {', '.join(tech_stack.keys()) or 'Unknown'}")
    click.echo(f"   Components: {len(components)}")
    click.echo(f"   Entrypoints: {len(entrypoints)}")
    click.echo(f"   Config files: {len(configs)}")

    click.echo(f"\n✅ Code index saved to .repo_wiki/code_index.json")


@cli.command()
@click.argument("repo_path", type=click.Path(exists=True))
def detect(repo_path: str):
    """Detect changes since last wiki update."""
    repo = Path(repo_path).resolve()
    click.echo(f"Detecting changes in: {repo}")

    # Load state
    state_file = repo / ".repo_wiki/state.json"
    if not state_file.exists():
        click.echo("❌ Wiki not initialized. Run 'init' first.")
        sys.exit(1)

    with open(state_file) as f:
        state = json.load(f)

    last_commit = state.get("last_run_commit", "")
    if not last_commit:
        click.echo("❌ No baseline commit found.")
        sys.exit(1)

    # Get current commit
    git_info = get_git_info(repo)
    current_commit = git_info["commit"]

    if last_commit == current_commit:
        click.echo("✅ No changes detected (same commit)")
        return

    click.echo(f"   Last commit: {last_commit[:8]}")
    click.echo(f"   Current:     {current_commit[:8]}")

    # Get diff
    try:
        diff_output = subprocess.check_output(
            ["git", "diff", "--name-status", f"{last_commit}..{current_commit}"],
            cwd=repo,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Git diff failed: {e}")
        sys.exit(1)

    # Parse changes
    changes = {"added": [], "modified": [], "deleted": [], "renamed": []}

    for line in diff_output.strip().split("\n"):
        if not line:
            continue
        parts = line.split("\t")
        status = parts[0]

        if status == "A":
            changes["added"].append(parts[1])
        elif status == "M":
            changes["modified"].append(parts[1])
        elif status == "D":
            changes["deleted"].append(parts[1])
        elif status.startswith("R"):
            changes["renamed"].append({"old": parts[1], "new": parts[2]})

    # Identify affected components
    affected_components = set()
    for file_list in [changes["added"], changes["modified"], changes["deleted"]]:
        for filepath in file_list:
            parts = Path(filepath).parts
            if len(parts) >= 2 and parts[0] in ["src", "lib", "packages", "app", "apps"]:
                affected_components.add(parts[1])

    # Identify impacted pages
    impacted_pages = set()
    if changes["added"] or changes["deleted"]:
        impacted_pages.add("docs/index.md")
        impacted_pages.add("docs/architecture/overview.md")

    for component in affected_components:
        impacted_pages.add(f"docs/components/{component}.md")

    # Check for config changes
    config_files = ["package.json", "requirements.txt", "Dockerfile", "docker-compose.yml"]
    for changed in changes["modified"] + changes["added"]:
        if any(changed.endswith(cf) for cf in config_files):
            impacted_pages.add("docs/getting-started/local-dev.md")
            impacted_pages.add("docs/operations/build-and-test.md")

    # Build change set
    change_set = {
        "last_commit": last_commit,
        "current_commit": current_commit,
        "added": changes["added"],
        "modified": changes["modified"],
        "deleted": changes["deleted"],
        "renamed": changes["renamed"],
        "affected_components": list(affected_components),
        "impacted_pages": list(impacted_pages),
        "detected_at": datetime.utcnow().isoformat() + "Z",
    }

    # Save change set
    change_file = repo / ".repo_wiki/change_set.json"
    with open(change_file, "w") as f:
        json.dump(change_set, f, indent=2)

    click.echo(f"\n📊 Changes Detected:")
    click.echo(f"   Added: {len(changes['added'])} files")
    click.echo(f"   Modified: {len(changes['modified'])} files")
    click.echo(f"   Deleted: {len(changes['deleted'])} files")
    click.echo(f"   Renamed: {len(changes['renamed'])} files")
    click.echo(f"\n   Affected components: {', '.join(affected_components) or 'None'}")
    click.echo(f"   Impacted pages: {len(impacted_pages)}")

    click.echo(f"\n✅ Change set saved to .repo_wiki/change_set.json")


@cli.command()
@click.argument("repo_path", type=click.Path(exists=True))
def validate(repo_path: str):
    """Validate wiki documentation."""
    repo = Path(repo_path).resolve()
    click.echo(f"Validating wiki in: {repo}")

    docs_dir = repo / "docs"
    if not docs_dir.exists():
        click.echo("❌ No docs/ directory found.")
        sys.exit(1)

    errors = []
    warnings = []

    # Find all markdown files
    md_files = list(docs_dir.rglob("*.md"))
    click.echo(f"   Found {len(md_files)} markdown files")

    # Check each file
    total_citations = 0
    valid_citations = 0

    for md_file in md_files:
        with open(md_file, errors="ignore") as f:
            content = f.read()

        rel_path = md_file.relative_to(repo)

        # Check managed blocks
        begin_count = content.count("<!-- BEGIN:REPO_WIKI_MANAGED -->")
        end_count = content.count("<!-- END:REPO_WIKI_MANAGED -->")
        if begin_count != end_count:
            errors.append(f"{rel_path}: Mismatched managed blocks (BEGIN: {begin_count}, END: {end_count})")

        # Check citations
        citation_pattern = r"`([^`]+)`\s+L(\d+)-L?(\d+)"
        citations = re.findall(citation_pattern, content)

        for filepath, start_line, end_line in citations:
            total_citations += 1
            target_file = repo / filepath

            if not target_file.exists():
                errors.append(f"{rel_path}: Citation references missing file: {filepath}")
            else:
                try:
                    line_count = sum(1 for _ in open(target_file, errors="ignore"))
                    start = int(start_line)
                    end = int(end_line)

                    if start > line_count or end > line_count:
                        errors.append(
                            f"{rel_path}: Citation {filepath} L{start}-L{end} invalid "
                            f"(file has {line_count} lines)"
                        )
                    else:
                        valid_citations += 1
                except Exception as e:
                    warnings.append(f"{rel_path}: Could not validate {filepath}: {e}")

        # Check internal links
        link_pattern = r"\[([^\]]+)\]\(([^)]+\.md)\)"
        links = re.findall(link_pattern, content)

        for link_text, link_target in links:
            if link_target.startswith("http"):
                continue
            target_path = md_file.parent / link_target
            if not target_path.exists():
                warnings.append(f"{rel_path}: Broken link to '{link_target}'")

    # Check mkdocs.yml
    mkdocs_file = repo / "mkdocs.yml"
    if mkdocs_file.exists():
        try:
            import yaml

            with open(mkdocs_file) as f:
                yaml.safe_load(f)
            click.echo("   mkdocs.yml: Valid YAML")
        except ImportError:
            click.echo("   mkdocs.yml: Skipped YAML validation (pyyaml not installed)")
        except Exception as e:
            errors.append(f"mkdocs.yml: Invalid YAML - {e}")
    else:
        warnings.append("mkdocs.yml not found")

    # Print results
    click.echo(f"\n📊 Validation Results:")
    click.echo(f"   Pages: {len(md_files)}")
    click.echo(f"   Citations: {valid_citations}/{total_citations} valid")

    if errors:
        click.echo(f"\n❌ Errors ({len(errors)}):")
        for error in errors[:10]:
            click.echo(f"   - {error}")
        if len(errors) > 10:
            click.echo(f"   ... and {len(errors) - 10} more")

    if warnings:
        click.echo(f"\n⚠️  Warnings ({len(warnings)}):")
        for warning in warnings[:10]:
            click.echo(f"   - {warning}")
        if len(warnings) > 10:
            click.echo(f"   ... and {len(warnings) - 10} more")

    if not errors and not warnings:
        click.echo(f"\n✅ Validation PASSED!")
        sys.exit(0)
    elif errors:
        click.echo(f"\n❌ Validation FAILED")
        sys.exit(1)
    else:
        click.echo(f"\n⚠️  Validation passed with warnings")
        sys.exit(0)


if __name__ == "__main__":
    cli()
