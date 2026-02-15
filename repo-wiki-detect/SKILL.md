---
name: repo-wiki-detect
description: Detect code changes since last wiki update using git diff. Identifies added, modified, deleted, and renamed files to determine which documentation pages need updates.
license: MIT
compatibility: Requires git, uv (Python package manager), existing .repo_wiki/state.json
metadata:
  version: 1.0.0
  parent_skill: repo-wiki
  category: documentation-maintenance
allowed-tools: git cat uv
---

# Repo Wiki Detect Changes Skill

Detect code changes and determine documentation impact.

## Purpose

This skill analyzes what changed in the codebase since the last wiki update:

1. Files added, modified, deleted, or renamed
2. Components affected by changes
3. Documentation pages that need updates
4. Citations that may have shifted

## When to Use

Use this skill:

- After making code changes
- Before running `repo-wiki-update`
- To see what documentation will be affected

## Step-by-Step Instructions

### Step 1: Load Last Baseline Commit

```bash
LAST_COMMIT=$(uv run python -c "import json; print(json.load(open('.repo_wiki/state.json'))['last_run_commit'])")
CURRENT_COMMIT=$(git rev-parse HEAD)
```

### Step 2: Compute Git Diff

```bash
git diff --name-status "$LAST_COMMIT".."$CURRENT_COMMIT" > .repo_wiki/changes.diff
```

### Step 3: Parse Changes

Categorize into added, modified, deleted, renamed files.

### Step 4: Map Files to Components

Determine which components are affected by changes.

### Step 5: Identify Impacted Pages

Match changed files to existing documentation pages.

### Step 6: Detect New/Deleted Modules

Check for components that need new pages or archiving.

## Output Files

- `.repo_wiki/change_set.json` - Structured change data
- `.repo_wiki/logs/detection.log` - Summary report

## Success Criteria

- ✅ Change set created
- ✅ Impacted pages identified
- ✅ New modules detected
- ✅ Deleted modules identified

## Next Steps

After detection:
1. **Update documentation**: Read `repo-wiki-update/SKILL.md`
