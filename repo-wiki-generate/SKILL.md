---
name: repo-wiki-generate
description: Generate citation-backed documentation pages from code index. Creates markdown content with file path and line number citations for every technical claim.
license: MIT
compatibility: Requires filesystem access, uv (Python package manager), code index from repo-wiki-index
metadata:
  version: 1.0.0
  parent_skill: repo-wiki
  category: documentation-generation
allowed-tools: cat ls uv git
---

# Repo Wiki Generate Pages Skill

Generate citation-backed markdown documentation from the code index.

## Purpose

This skill transforms the code index into comprehensive documentation pages with:

1. Technical accuracy backed by source code citations
2. File paths and exact line ranges for every claim
3. Clickable permalinks to source code
4. Structured markdown with managed blocks

## When to Use

Use this skill:

- After running `repo-wiki-index`
- To fill in placeholder pages with actual content
- When generating documentation for the first time

## Step-by-Step Instructions

### Step 1: Load Index and Configuration

Load `.repo_wiki/code_index.json` and `.repo_wiki/state.json`.

### Step 2: Determine Citation Format

Choose between footnote or inline style based on config.

### Step 3: Generate Component Pages

For each component, create documentation with:
- Overview and purpose
- Key files with citations
- Public interfaces
- Configuration options

### Step 4: Generate Architecture Overview

Create system-level documentation with statistics and component relationships.

### Step 5: Generate Getting Started Pages

Document setup, installation, and running instructions.

### Step 6: Update Manifest

Track all citations in `.repo_wiki/manifest.json`.

## Citation Format

```markdown
The service starts an HTTP server[^1].

[^1]: [src/server.ts#L12-L48](https://github.com/org/repo/blob/abc1234/src/server.ts#L12-L48)
```

## Success Criteria

- ✅ All component pages have content
- ✅ Every technical claim has a citation
- ✅ Citations include file paths and line ranges
- ✅ MkDocs builds without errors

## Next Steps

After generation:
1. **Validate output**: Read `repo-wiki-validate/SKILL.md`
