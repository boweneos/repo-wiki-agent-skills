# Wiki Validate - Documentation Quality Check

You are tasked with validating the documentation quality of a repository wiki.

## Target Repository

The user will provide the repository path. If not provided, ask for it.

## Prerequisites

The repository must have:
- `docs/` directory with documentation
- `.repo_wiki/` state files (optional but recommended)

## Your Task

Run comprehensive validation checks and report issues.

## Validation Checks

### 1. Citation Validity

For every citation in the documentation:

```markdown
[^1]: `src/server.ts` L12-L48
```

Verify:
- [ ] File `src/server.ts` exists
- [ ] File has at least 48 lines
- [ ] Lines 12-48 contain relevant code

**How to check:**
```bash
# Check file exists
test -f src/server.ts && echo "OK" || echo "MISSING"

# Check line count
wc -l < src/server.ts

# View cited lines
sed -n '12,48p' src/server.ts
```

### 2. Internal Link Integrity

For every internal link:

```markdown
[Getting Started](getting-started/local-dev.md)
```

Verify:
- [ ] Target file exists in `docs/`
- [ ] Anchor targets exist (if `#anchor` specified)

### 3. Managed Block Integrity

For pages with managed blocks:

```markdown
<!-- BEGIN:REPO_WIKI_MANAGED -->
...content...
<!-- END:REPO_WIKI_MANAGED -->
```

Verify:
- [ ] Every BEGIN has a matching END
- [ ] No nested managed blocks
- [ ] No orphaned markers

### 4. Frontmatter Validation

Each page should have:

```yaml
---
generated_by: repo-wiki-agent
baseline_commit: "abc1234"
last_updated: "2024-01-15"
---
```

Check:
- [ ] Frontmatter exists
- [ ] Required fields present
- [ ] Commit SHA is valid (if git available)

### 5. MkDocs Configuration

Verify `mkdocs.yml`:
- [ ] Valid YAML syntax
- [ ] All nav entries point to existing files
- [ ] Theme configuration is valid

### 6. Citation Coverage

For managed blocks, check that technical claims have citations:

**Should have citations:**
- "The server listens on port 3000" → needs citation
- "Default timeout is 30 seconds" → needs citation
- "Errors are logged to stderr" → needs citation

**No citation needed:**
- "This component handles authentication" (general description)
- Navigation links
- Section headers

## Output Format

Generate a validation report:

```markdown
# Validation Report

Generated: <timestamp>
Repository: <path>

## Summary

- Total Pages: X
- Citations Checked: Y
- Issues Found: Z

## Issues

### Critical (must fix)
- [ ] `docs/components/auth.md`: Citation `src/auth.ts L50-60` - file only has 45 lines

### Warnings (should fix)
- [ ] `docs/index.md`: Missing frontmatter field `baseline_commit`

### Info
- [ ] `docs/architecture/overview.md`: Low citation coverage (2 citations for 15 claims)

## Passed Checks

- [x] All internal links valid
- [x] MkDocs configuration valid
- [x] Managed blocks properly closed
```

## Quick Validation Commands

Run these to check specific aspects:

```bash
# Check if mkdocs builds
cd <REPO_PATH>
mkdocs build --strict 2>&1 | head -20

# Find all citations
grep -r "\[\^" docs/ | head -20

# Find managed blocks
grep -r "REPO_WIKI_MANAGED" docs/

# Check for broken internal links
grep -roh '\[.*\](.*\.md)' docs/ | sort -u
```

## Success Criteria

Validation passes if:
- [ ] Zero critical issues
- [ ] All citations resolve to valid files and lines
- [ ] All internal links work
- [ ] MkDocs builds without errors
- [ ] All managed blocks properly closed

## After Validation

If issues found:
1. List all issues clearly
2. Suggest fixes for each
3. Offer to fix automatically if possible

If validation passes:
```
✅ Validation PASSED
- X pages validated
- Y citations verified
- Ready to commit/deploy
```
