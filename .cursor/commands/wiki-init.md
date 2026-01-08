# Wiki Init - Generate Citation-Backed Repository Wiki

You are tasked with generating a complete, citation-backed wiki for a repository. Every technical claim must include file path and line number citations.

## Target Repository

The user will provide the repository path. If not provided, ask for it.

## Your Task

Generate a MkDocs-compatible documentation wiki with:
1. Proper directory structure
2. Citation-backed documentation pages
3. State tracking files
4. MkDocs configuration

## Step 1: Initialize Structure

First, gather repository information and create the base structure:

```bash
cd <REPO_PATH>

# Get repo info
BASELINE_COMMIT="$(git rev-parse HEAD)"
REMOTE_URL="$(git config --get remote.origin.url || echo '')"
REPO_NAME="$(basename "$(pwd)")"

# Create directories
mkdir -p docs/getting-started docs/architecture docs/components docs/api docs/operations docs/adr
mkdir -p .repo_wiki/logs
```

Then create `mkdocs.yml`:

```yaml
site_name: <REPO_NAME> Documentation
repo_url: <REMOTE_URL>
edit_uri: blob/main/docs/

theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - search.suggest

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
```

Create `.repo_wiki/state.json`:

```json
{
  "schema_version": "1.0",
  "baseline_commit": "<BASELINE_COMMIT>",
  "last_run_commit": "<BASELINE_COMMIT>",
  "repo_name": "<REPO_NAME>",
  "repo_remote_url": "<REMOTE_URL>",
  "created_at": "<ISO_TIMESTAMP>",
  "ignore_patterns": [".git/**", "node_modules/**", "dist/**", "build/**", "__pycache__/**"]
}
```

Create `.repo_wiki/manifest.json`:

```json
{
  "schema_version": "1.0",
  "baseline_commit": "<BASELINE_COMMIT>",
  "pages": {}
}
```

## Step 2: Index the Codebase

Scan the repository to understand its structure:

1. List all source files (excluding ignored patterns)
2. Detect technology stack (look for package.json, requirements.txt, go.mod, etc.)
3. Identify components (directories under src/, lib/, packages/, app/)
4. Find entrypoints (main.*, index.*, app.*, server.*)
5. Locate configuration files

Save findings to `.repo_wiki/code_index.json`.

## Step 3: Generate Documentation Pages

For each page, you MUST include citations in this format:

**Footnote style (preferred):**
```markdown
The service starts an HTTP server on port 3000[^1].

[^1]: `src/server.ts` L12-L48
```

**Or with permalinks if remote URL is available:**
```markdown
[^1]: [src/server.ts#L12-L48](https://github.com/org/repo/blob/<commit>/src/server.ts#L12-L48)
```

### Pages to Generate:

1. **docs/index.md** - Overview with links to all sections
2. **docs/getting-started/local-dev.md** - Setup instructions with citations to package.json, Dockerfile, etc.
3. **docs/architecture/overview.md** - System architecture with component citations
4. **docs/components/<name>.md** - One per major component, citing key files
5. **docs/operations/build-and-test.md** - Build/test commands with citations

### Managed Blocks

Use these markers for agent-managed content:

```markdown
<!-- BEGIN:REPO_WIKI_MANAGED -->
Agent-generated content here...
<!-- END:REPO_WIKI_MANAGED -->

## Team Notes
(Human edits preserved here)
```

## Step 4: Validate

After generating:

1. Verify all citations point to existing files
2. Check line numbers are valid
3. Ensure all internal links work
4. Test that `mkdocs build` would succeed (valid YAML, all referenced pages exist)

## Success Criteria

- [ ] `docs/` directory with all required pages
- [ ] `mkdocs.yml` is valid
- [ ] `.repo_wiki/state.json` initialized
- [ ] `.repo_wiki/manifest.json` tracks pages
- [ ] Every technical claim has a citation
- [ ] All citations are valid (file exists, lines valid)

## Citation Rules

IMPORTANT: Every non-trivial technical statement MUST have a citation:
- Default values and configuration
- API endpoints and routes
- Error handling behavior
- Data flow descriptions
- File purposes and responsibilities

DO NOT cite:
- Navigation text
- General descriptions labeled as interpretation
