---
name: repo-wiki-initialize
description: Initialize a new repository wiki structure. Creates baseline MkDocs configuration, directory layout, placeholder pages, and state tracking files.
license: MIT
compatibility: Requires git, filesystem write access, uv (Python package manager)
metadata:
  version: 1.0.0
  parent_skill: repo-wiki
  category: documentation-initialization
allowed-tools: git ls mkdir cat uv
---

# Repo Wiki Initialize Skill

Create the baseline structure for a citation-backed repository wiki.

## Purpose

This skill sets up a new wiki from scratch for any codebase. It:

1. Detects the technology stack and project structure
2. Creates an appropriate information architecture
3. Generates `mkdocs.yml` configuration
4. Creates placeholder pages with managed blocks
5. Initializes state tracking in `.repo_wiki/`

## When to Use

Use this skill when:

- Starting documentation for a codebase from scratch
- The repository has no `docs/` directory yet
- You want to establish a baseline wiki structure

## Step-by-Step Instructions

### Step 1: Gather Repository Information

```bash
REPO_PATH="$(pwd)"
BASELINE_COMMIT="$(git rev-parse HEAD)"
REMOTE_URL="$(git config --get remote.origin.url)"
REPO_NAME="$(basename "$REPO_PATH")"
```

### Step 2: Detect Technology Stack

```bash
# Check for language markers
ls -la "$REPO_PATH" | grep -E "package.json|requirements.txt|go.mod|pom.xml|Cargo.toml"
```

### Step 3: Create Directory Structure

```bash
mkdir -p docs/getting-started docs/architecture docs/components docs/api docs/operations docs/adr
mkdir -p .repo_wiki/logs
```

### Step 4: Generate MkDocs Configuration

Create `mkdocs.yml` with site name, theme, navigation, and markdown extensions.

### Step 5: Create Placeholder Pages

Generate initial pages with managed blocks:
- `docs/index.md`
- `docs/getting-started/local-dev.md`
- `docs/architecture/overview.md`
- Component pages for each module

### Step 6: Initialize State Files

Create `.repo_wiki/state.json` and `.repo_wiki/manifest.json` with baseline commit.

## Success Criteria

- ✅ `mkdocs.yml` exists and is valid
- ✅ `docs/` directory created with all subdirectories
- ✅ Placeholder pages created with managed blocks
- ✅ `.repo_wiki/state.json` initialized
- ✅ `mkdocs build` succeeds

## Next Steps

After initialization:
1. **Index the codebase**: Read `repo-wiki-index/SKILL.md`
2. **Generate page content**: Read `repo-wiki-generate/SKILL.md`
