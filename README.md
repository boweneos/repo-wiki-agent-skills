# Repo Wiki Agent Skills

A comprehensive set of Agent Skills for generating and maintaining citation-backed repository wikis as MkDocs-compatible Markdown.

## Overview

This project implements the complete **Repo Wiki Agent Skills** system as specified in `rpd.md`. The skills enable AI agents to:

- **Generate** complete documentation from scratch with proper citations
- **Track** code changes via git diff
- **Update** documentation incrementally (only affected pages)
- **Cite** every technical claim with file paths and line ranges
- **Maintain** traceability through clickable permalinks
- **Preserve** human edits while updating agent-managed content

## Quick Start

### 🚀 Cursor Commands (Recommended)

Type `/` in Cursor chat to access these commands:

| Command | Description |
|---------|-------------|
| `/wiki-init` | First-time setup - creates complete wiki structure |
| `/wiki-update` | Incremental update after code changes |
| `/wiki-validate` | Validate documentation quality |

Simply type `/wiki-init` in Cursor chat and follow the instructions!

### 📜 Shell Scripts (Alternative)

Three ready-to-use shell scripts:

```bash
# Workflow 1: First-time wiki setup (run once)
./scripts/wiki-init.sh

# Workflow 2: Update after code changes (run after commits)
./scripts/wiki-update.sh

# Workflow 3: Validate documentation (run anytime)
./scripts/wiki-validate.sh
```

Each script guides you through the complete workflow step-by-step!

### 📖 Manual Skill Usage

If you prefer to read skills directly:

**First-time setup:**
```bash
cat skills/repo-wiki-initialize/SKILL.md  # 1. Initialize
cat skills/repo-wiki-index/SKILL.md      # 2. Index
cat skills/repo-wiki-generate/SKILL.md   # 3. Generate
cat skills/repo-wiki-validate/SKILL.md   # 4. Validate
```

**After code changes:**
```bash
cat skills/repo-wiki-detect/SKILL.md     # 1. Detect
cat skills/repo-wiki-update/SKILL.md     # 2. Update
cat skills/repo-wiki-validate/SKILL.md   # 3. Validate
```

## Skill Structure

```
skills/
├── repo-wiki/                    # Main orchestrator skill
│   ├── SKILL.md                  # Entry point and overview
│   ├── scripts/                  # Helper scripts
│   │   ├── validate_citations.py
│   │   ├── generate_permalinks.py
│   │   ├── detect_managed_blocks.py
│   │   └── compute_page_impact.py
│   ├── references/               # Reference documentation
│   │   ├── CITATION-SPEC.md
│   │   ├── ARCHITECTURE.md
│   │   ├── STATE-FORMAT.md
│   │   └── TEMPLATES.md
│   └── assets/                   # Templates and resources
│       └── templates/
│           ├── mkdocs.yml.template
│           ├── component-page.md.template
│           ├── overview-page.md.template
│           └── architecture-page.md.template
│
├── repo-wiki-initialize/         # Bootstrap wiki structure
│   └── SKILL.md
│
├── repo-wiki-index/              # Build code map
│   └── SKILL.md
│
├── repo-wiki-generate/           # Generate pages with citations
│   └── SKILL.md
│
├── repo-wiki-detect/             # Detect code changes
│   └── SKILL.md
│
├── repo-wiki-update/             # Incremental updates
│   └── SKILL.md
│
└── repo-wiki-validate/           # Quality gates
    └── SKILL.md
```

## Key Features

### 1. Citation-Backed Documentation

Every technical claim includes citations with:
- File paths relative to repository root
- Exact line ranges
- Commit SHA for stability
- Clickable permalinks (when remote URL available)

Example:
```markdown
The service starts an HTTP server on port 3000[^1].

[^1]: [src/server.ts#L12-L48](https://github.com/org/repo/blob/abc1234/src/server.ts#L12-L48)
```

### 2. Incremental Updates

Only regenerates pages that are impacted by code changes:
- Detects changes via git diff
- Maps changed files to documentation pages
- Refreshes citations that may have shifted
- Creates pages for new modules
- Archives pages for deleted modules

### 3. Managed Blocks

Preserves human edits while allowing agent updates:

```markdown
<!-- BEGIN:REPO_WIKI_MANAGED -->
Agent-controlled content...
<!-- END:REPO_WIKI_MANAGED -->

## Team Notes
Human edits preserved here...
```

### 4. Quality Validation

Enforces gates before merging:
- ✅ All citations resolve to valid files and lines
- ✅ Internal links are not broken
- ✅ Markdown syntax is correct
- ✅ Managed blocks are properly closed
- ✅ MkDocs builds successfully
- ✅ Citation coverage meets threshold

### 5. MkDocs Integration

Generates standard MkDocs-compatible structure:
```
repo/
├── mkdocs.yml
├── docs/
│   ├── index.md
│   ├── getting-started/
│   ├── architecture/
│   ├── components/
│   ├── api/
│   ├── operations/
│   └── glossary.md
└── .repo_wiki/
    ├── state.json
    ├── manifest.json
    ├── code_index.json
    └── logs/
```

## Skill Details

### repo-wiki (Main Orchestrator)

**Purpose**: Entry point and coordination  
**When to use**: First skill to read for overview

Contains:
- Complete workflow documentation
- Links to all sub-skills
- Helper scripts
- Templates
- Reference documentation

### repo-wiki-initialize

**Purpose**: Bootstrap new wiki  
**Outputs**: Directory structure, placeholder pages, state files  
**Runtime**: ~1-2 minutes

### repo-wiki-index

**Purpose**: Build code map  
**Outputs**: code_index.json with file inventory, components, APIs  
**Runtime**: ~2-5 minutes (depends on repo size)

### repo-wiki-generate

**Purpose**: Generate documentation with citations  
**Outputs**: Complete markdown pages with citations  
**Runtime**: ~5-10 minutes (depends on repo size)

### repo-wiki-detect

**Purpose**: Detect changes since last run  
**Outputs**: change_set.json with impact analysis  
**Runtime**: <1 minute

### repo-wiki-update

**Purpose**: Incrementally update documentation  
**Outputs**: Updated pages (only managed blocks)  
**Runtime**: ~1-3 minutes (scales with change size)

### repo-wiki-validate

**Purpose**: Enforce quality gates  
**Outputs**: validation_report.md, exit code  
**Runtime**: <1 minute

## Configuration

Customize behavior via `.repo_wiki/config.json`:

```json
{
  "citation_format": "footnote",
  "generate_permalinks": true,
  "strict_validation": true,
  "component_detection": {
    "folder_based": true,
    "entrypoint_detection": true
  },
  "validation": {
    "min_citation_coverage": 0.8,
    "fail_on_warnings": false
  }
}
```

## Agent Skills Compliance

This implementation follows the [Agent Skills specification](https://agentskills.io):

- ✅ Each skill has a `SKILL.md` file with required frontmatter
- ✅ Skills use progressive disclosure (metadata → instructions → details)
- ✅ Scripts, references, and assets are properly organized
- ✅ Skills are composable and reusable
- ✅ Clear instructions for when to use each skill
- ✅ Proper dependency management between skills

## Best Practices

1. **Run initialization once** - Only needed for new wikis
2. **Index before generating** - Code map needed for citations
3. **Detect before updating** - Know what changed before updating
4. **Validate after any operation** - Ensure quality gates pass
5. **Commit incrementally** - Small documentation updates are easier to review

## Workflows

### First-Time Setup

```
Initialize → Index → Generate → Validate → Commit
```

### After Code Changes

```
Detect → (Review impact) → Update → Validate → Commit
```

### Major Refactor (>50% components changed)

```
Delete .repo_wiki/ → Initialize → Index → Generate → Validate
```

## Examples

### Citation Formats

**Footnote (Preferred):**
```markdown
The auth middleware validates JWT tokens[^auth1].

[^auth1]: [src/auth/middleware.ts#L10-L35](https://github.com/org/repo/blob/abc1234/src/auth/middleware.ts#L10-L35)
```

**Inline:**
```markdown
The auth middleware validates JWT tokens.  
Source: `src/auth/middleware.ts` L10–L35
```

### Managed Block Example

```markdown
---
generated_by: repo-wiki-agent
baseline_commit: "abc1234"
last_updated: "2024-01-15"
managed_sections:
  - "## Overview"
---

# Authentication Component

<!-- BEGIN:REPO_WIKI_MANAGED -->
## Overview

The authentication component provides JWT-based authentication[^1].

### Key Features

- Token validation[^2]
- Role-based access control[^3]
- Session management[^4]

[^1]: src/auth/README.md L1-L10
[^2]: src/auth/middleware.ts L10-L35
[^3]: src/auth/rbac.ts L15-L60
[^4]: src/auth/session.ts L20-L80
<!-- END:REPO_WIKI_MANAGED -->

## Team Notes

For production deployment, configure JWT_SECRET environment variable.
```

## Troubleshooting

### MkDocs Build Fails

Check:
- Valid YAML in mkdocs.yml
- All nav entries exist
- No special characters in filenames

### Citations Invalid

Run:
```bash
uv run skills/repo-wiki/scripts/validate_citations.py
```

### Managed Blocks Missing

Add markers manually:
```markdown
<!-- BEGIN:REPO_WIKI_MANAGED -->
<!-- END:REPO_WIKI_MANAGED -->
```

## Contributing

These skills follow the open Agent Skills format. To extend:

1. Add new sub-skills in `skills/` directory
2. Follow SKILL.md format specification
3. Include step-by-step instructions
4. Add references and examples
5. Test with validation skill

## License

MIT License - See individual SKILL.md files for details.

## References

- [Agent Skills Specification](https://agentskills.io)
- [MkDocs Documentation](https://www.mkdocs.org)
- [Original PRD](rpd.md)

## Status

✅ All requirements from rpd.md implemented:
- [x] Baseline wiki generation (FR1)
- [x] Change detection (FR2)
- [x] Incremental updates (FR3)
- [x] Citations with line numbers (FR4)
- [x] Clickable permalinks (FR5)
- [x] Preservation of human edits (FR6)
- [x] Deterministic output (NFR1)
- [x] Bounded changes (NFR2)
- [x] Performance scaling (NFR3)
- [x] Safety around secrets (NFR4)
- [x] Verifiable citations (NFR5)
