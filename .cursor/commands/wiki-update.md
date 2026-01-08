# Wiki Update - Incremental Documentation Update

You are tasked with updating an existing wiki after code changes. Only update affected pages, preserve human edits.

## Target Repository

The user will provide the repository path. If not provided, ask for it.

## Prerequisites

The repository must have:
- `.repo_wiki/state.json` (run `/wiki-init` first if missing)
- `docs/` directory with existing documentation

## Your Task

1. Detect what code changed since last update
2. Identify which documentation pages are affected
3. Update only those pages
4. Refresh citations that may have shifted
5. Create pages for new modules
6. Archive pages for deleted modules

## Step 1: Detect Changes

```bash
cd <REPO_PATH>

# Get commits
LAST_COMMIT=$(cat .repo_wiki/state.json | uv run python -c "import sys,json; print(json.load(sys.stdin)['last_run_commit'])")
CURRENT_COMMIT=$(git rev-parse HEAD)

# Get changed files
git diff --name-status "$LAST_COMMIT".."$CURRENT_COMMIT"
```

Categorize changes:
- **Added (A)**: New files - may need new doc pages
- **Modified (M)**: Changed files - update citations, refresh content
- **Deleted (D)**: Removed files - archive/remove doc references
- **Renamed (R)**: Moved files - update file paths in citations

## Step 2: Map Changes to Pages

For each changed file, determine affected documentation:

| Source Pattern | Affected Page |
|----------------|---------------|
| `src/<component>/**` | `docs/components/<component>.md` |
| `package.json`, `requirements.txt` | `docs/getting-started/local-dev.md` |
| `Dockerfile`, `docker-compose.*` | `docs/operations/build-and-test.md` |
| Any structural change | `docs/architecture/overview.md` |
| New component directory | Create new `docs/components/<name>.md` |

## Step 3: Update Affected Pages

For each affected page:

1. **Read the existing page**
2. **Identify managed blocks** (between `<!-- BEGIN:REPO_WIKI_MANAGED -->` and `<!-- END:REPO_WIKI_MANAGED -->`)
3. **Update ONLY managed blocks** - preserve content outside them
4. **Refresh citations** - update line numbers if code shifted
5. **Update frontmatter** - set new `last_updated` date and `baseline_commit`

### Citation Refresh

If a file was modified, its line numbers may have shifted. For each citation:
1. Find the referenced code block
2. Locate it in the new file version
3. Update line numbers

Example:
```markdown
# Before (code was at L12-L48)
[^1]: `src/server.ts` L12-L48

# After (code moved to L15-L51)
[^1]: `src/server.ts` L15-L51
```

## Step 4: Handle New Modules

If new component directories were added:

1. Create `docs/components/<name>.md`
2. Generate content with citations
3. Add to navigation in `mkdocs.yml`
4. Update `docs/index.md` component list

## Step 5: Handle Deleted Modules

If component directories were removed:

1. Add archived banner to the page:
```markdown
> **ARCHIVED**: This component was removed on <DATE>.
```
2. Move to `docs/archive/<name>.md` (or delete based on config)
3. Remove from `mkdocs.yml` navigation
4. Update `docs/index.md`

## Step 6: Update State

After all updates:

```json
// .repo_wiki/state.json
{
  "last_run_commit": "<CURRENT_COMMIT>",
  "last_updated_at": "<ISO_TIMESTAMP>"
}
```

Update `.repo_wiki/manifest.json` with new citation data.

## Success Criteria

- [ ] Only affected pages were modified
- [ ] Human edits outside managed blocks preserved
- [ ] All citations are valid with correct line numbers
- [ ] New modules have documentation
- [ ] Deleted modules are archived
- [ ] State files updated to current commit

## Important Rules

1. **NEVER overwrite human edits** - only modify managed blocks
2. **Always verify citations** - check files exist and lines are valid
3. **Minimize diff** - don't reformat unchanged content
4. **Track changes** - log what was updated in `.repo_wiki/logs/`
