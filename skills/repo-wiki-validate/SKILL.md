---
name: repo-wiki-validate
description: Validate wiki quality and enforce gates. Checks citation validity, link integrity, formatting consistency, and coverage requirements before merging.
license: MIT
compatibility: Requires uv (Python package manager), markdown linting tools optional
metadata:
  version: 1.0.0
  parent_skill: repo-wiki
  category: documentation-validation
allowed-tools: cat ls uv git
---

# Repo Wiki Validate Skill

Enforce quality gates and validate wiki integrity.

## Purpose

This skill performs comprehensive validation:

1. **Citation validation** - All citations resolve to valid files and line ranges
2. **Link checking** - Internal links point to existing pages
3. **Format validation** - Markdown syntax correct, managed blocks closed
4. **Coverage validation** - Technical claims have citations
5. **Build verification** - MkDocs builds without errors

## When to Use

Use this skill:

- Before committing documentation changes
- After any documentation update
- In CI/CD pipelines as quality gate

## Validation Checks

### 1. Citation Validity

```bash
uv run skills/repo-wiki/scripts/validate_citations.py
```

### 2. Internal Links

Check all markdown links resolve to existing pages.

### 3. Markdown Syntax

Verify no unclosed code blocks or managed blocks.

### 4. MkDocs Build

```bash
mkdocs build --strict
```

## Success Criteria

- ✅ All citations resolve
- ✅ No broken links
- ✅ Markdown syntax valid
- ✅ MkDocs builds
- ✅ Coverage ≥80%

## Output

- `.repo_wiki/validation_report.md` - Detailed report
- Exit code 0 (pass) or 1 (fail)
