---
name: repo-wiki
description: Generate and maintain citation-backed repository wikis as MkDocs-compatible Markdown. Creates baseline docs, detects changes, and incrementally updates only affected pages with file path and line number citations.
license: MIT
compatibility: Requires git, filesystem access, and uv (Python package manager). Works with any git repository.
metadata:
  version: 1.0.0
  author: Agent Skills
  category: documentation
allowed-tools: cat ls git uv
---

# Repo Wiki Agent Skill

Generate and maintain a living, citation-backed wiki for any codebase as structured Markdown files compatible with MkDocs.

## What This Skill Does

This skill enables agents to:

1. **Generate baseline wiki** - Create complete documentation from scratch
2. **Track changes** - Detect code modifications via git diff
3. **Update incrementally** - Refresh only impacted pages, not entire wiki
4. **Add citations** - Link every technical claim to specific file paths and line ranges
5. **Maintain traceability** - Generate clickable permalinks to source code
6. **Preserve human edits** - Only update managed blocks, leave manual edits intact

## When to Use This Skill

Use this skill when you need to:

- Document a new codebase with comprehensive, citation-backed pages
- Keep documentation synchronized with code changes
- Provide trustworthy docs that reviewers can verify against source code
- Create onboarding materials for new engineers
- Generate architectural overviews with source traceability
- Maintain a "living wiki" that updates incrementally after each change

## How It Works

This skill is composed of specialized sub-skills that work together:

1. **repo-wiki-initialize** - Set up wiki structure and baseline
2. **repo-wiki-index** - Build a searchable code map
3. **repo-wiki-generate** - Create citation-backed markdown pages
4. **repo-wiki-detect** - Find changes since last run
5. **repo-wiki-update** - Incrementally refresh affected pages
6. **repo-wiki-validate** - Verify citations and quality gates

## Quick Start

### Generate a New Wiki

```bash
# Activate the initialize sub-skill
cat /path/to/skills/repo-wiki-initialize/SKILL.md

# Follow instructions to create baseline wiki
```

### Update Existing Wiki After Code Changes

```bash
# Activate the detect changes sub-skill
cat /path/to/skills/repo-wiki-detect/SKILL.md

# Then activate the update sub-skill
cat /path/to/skills/repo-wiki-update/SKILL.md
```

### Validate Wiki Quality

```bash
# Activate the validate sub-skill
cat /path/to/skills/repo-wiki-validate/SKILL.md
```

## Workflow Overview

### First-Time Wiki Creation

1. Read `repo-wiki-initialize/SKILL.md` for initialization instructions
2. Read `repo-wiki-index/SKILL.md` to build code map
3. Read `repo-wiki-generate/SKILL.md` to generate pages with citations
4. Read `repo-wiki-validate/SKILL.md` to verify output quality

### Incremental Updates (After Code Changes)

1. Read `repo-wiki-detect/SKILL.md` to identify changes
2. Read `repo-wiki-update/SKILL.md` to refresh impacted pages
3. Read `repo-wiki-validate/SKILL.md` to verify changes

## Output Structure

The skill generates a MkDocs-compatible documentation tree:

```
<repo>/
  mkdocs.yml                    # MkDocs configuration
  docs/
    index.md                    # Overview
    getting-started/
      local-dev.md
      configuration.md
    architecture/
      overview.md
      data-flow.md
      dependency-map.md
    components/
      <component-name>.md       # One per major component
    api/
      endpoints.md
    operations/
      build-and-test.md
      deploy.md
    glossary.md
  .repo_wiki/
    state.json                  # Tracks baseline commit & page mappings
    manifest.json               # Citations and source fingerprints
    logs/
```

## Citation Format

Every technical claim includes citations with file paths and line ranges:

**Inline Format:**
```markdown
The service starts an HTTP server on the configured port.
Source: `src/server.ts` L12–L48
```

**Footnote Format (Preferred):**
```markdown
The service starts an HTTP server[^1].

[^1]: `src/server.ts` L12–L48 (commit abc1234)
```

**Remote Permalink (When Git Remote Available):**
```markdown
[^1]: [src/server.ts#L12-L48](https://github.com/org/repo/blob/abc1234/src/server.ts#L12-L48)
```

## Key Principles

1. **Citation-backed**: Every non-trivial technical statement must have a citation
2. **Incremental**: Only update what changed, minimize diff size
3. **Deterministic**: Same commit = same output (modulo timestamps)
4. **Safe**: Exclude secrets, avoid overwriting manual edits
5. **Verifiable**: Citations must point to valid file:line ranges
6. **Reviewable**: Small PRs, stable formatting, link-checkable

## Reference Materials

For detailed information, see the `references/` directory:

- `references/CITATION-SPEC.md` - Citation format and coverage rules
- `references/ARCHITECTURE.md` - Skill design and module relationships
- `references/STATE-FORMAT.md` - State file schema and usage
- `references/TEMPLATES.md` - Page template specifications

## Scripts

Helper scripts are available in `scripts/` directory:

- `scripts/validate_citations.py` - Verify all citations resolve correctly
- `scripts/generate_permalinks.py` - Convert local citations to remote URLs
- `scripts/detect_managed_blocks.py` - Find and parse managed block markers
- `scripts/compute_page_impact.py` - Determine which pages need updates

## Assets

Templates and resources in `assets/` directory:

- `assets/templates/mkdocs.yml.template` - MkDocs config template
- `assets/templates/component-page.md.template` - Component page structure
- `assets/templates/overview-page.md.template` - Overview page structure
- `assets/templates/architecture-page.md.template` - Architecture page structure
