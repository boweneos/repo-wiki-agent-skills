---
name: repo-wiki-update
description: Incrementally update documentation pages based on detected changes. Plans update strategy, refreshes citations, updates only impacted pages, and maintains traceability.
license: MIT
compatibility: Requires git, uv (Python package manager), change_set.json from repo-wiki-detect
metadata:
  version: 1.0.0
  parent_skill: repo-wiki
  category: documentation-maintenance
allowed-tools: cat ls uv git
---

# Repo Wiki Update Skill

Incrementally update documentation to reflect code changes.

## Purpose

This skill performs incremental updates by:

1. Planning which pages need updates
2. Refreshing citations that may have shifted
3. Updating only managed blocks in affected pages
4. Creating pages for new modules
5. Archiving pages for deleted modules
6. Preserving human edits

## When to Use

Use this skill:

- After running `repo-wiki-detect`
- When code has changed and you want incremental updates

## Step-by-Step Instructions

### Step 1: Load Change Set

Load `.repo_wiki/change_set.json` from detection phase.

### Step 2: Create Update Plan

Plan actions: update, create, archive pages.

### Step 3: Refresh Citations

Update line numbers for citations in modified files.

### Step 4: Update Component Pages

Regenerate managed blocks while preserving human edits.

### Step 5: Create New Module Pages

Generate pages for newly detected modules.

### Step 6: Archive Deleted Pages

Move pages for deleted modules to archive.

### Step 7: Update State

Record new commit in `.repo_wiki/state.json`.

## Managed Block Markers

```markdown
<!-- BEGIN:REPO_WIKI_MANAGED -->
Agent content here...
<!-- END:REPO_WIKI_MANAGED -->
```

## Success Criteria

- ✅ Only impacted pages updated
- ✅ Human edits preserved
- ✅ Citations refreshed
- ✅ State file updated

## Next Steps

After updating:
1. **Validate changes**: Read `repo-wiki-validate/SKILL.md`
