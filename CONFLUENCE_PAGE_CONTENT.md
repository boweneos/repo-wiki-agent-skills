# Repo Wiki Agent Skills

> **AI-powered documentation that stays in sync with your codebase**

A comprehensive set of Agent Skills for generating and maintaining citation-backed repository wikis as MkDocs-compatible Markdown.

---

## 📋 Overview

This project implements the complete **Repo Wiki Agent Skills** system. The skills enable AI agents to:

- ✅ **Generate** complete documentation from scratch with proper citations
- ✅ **Track** code changes via git diff
- ✅ **Update** documentation incrementally (only affected pages)
- ✅ **Cite** every technical claim with file paths and line ranges
- ✅ **Maintain** traceability through clickable permalinks
- ✅ **Preserve** human edits while updating agent-managed content

---

## 🚀 Quick Start

### Cursor Commands (Recommended)

Type `/` in Cursor chat to access these commands:

| Command | Description |
|---------|-------------|
| `/wiki-init` | First-time setup - creates complete wiki structure |
| `/wiki-update` | Incremental update after code changes |
| `/wiki-validate` | Validate documentation quality |

Simply type `/wiki-init` in Cursor chat and follow the instructions!

### Shell Scripts (Alternative)

Three ready-to-use shell scripts:

```bash
# Workflow 1: First-time wiki setup (run once)
./scripts/wiki-init.sh

# Workflow 2: Update after code changes (run after commits)
./scripts/wiki-update.sh

# Workflow 3: Validate documentation (run anytime)
./scripts/wiki-validate.sh
```

---

## ✨ Key Features

### 1. Citation-Backed Documentation

Every technical claim includes citations with:
- File paths relative to repository root
- Exact line ranges
- Commit SHA for stability
- Clickable permalinks (when remote URL available)

**Example:**
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

---

## 🏗️ Skill Structure

The project includes 7 core skills:

```
skills/
├── repo-wiki/                    # Main orchestrator skill
│   ├── SKILL.md                  # Entry point and overview
│   ├── scripts/                  # Helper scripts
│   ├── references/               # Reference documentation
│   └── assets/                   # Templates and resources
│
├── repo-wiki-initialize/         # Bootstrap wiki structure
├── repo-wiki-index/              # Build code map
├── repo-wiki-generate/           # Generate pages with citations
├── repo-wiki-detect/             # Detect code changes
├── repo-wiki-update/             # Incremental updates
└── repo-wiki-validate/           # Quality gates
```

---

## 📊 Skill Details

| Skill | Purpose | Runtime |
|-------|---------|---------|
| **repo-wiki** | Entry point and coordination | N/A |
| **repo-wiki-initialize** | Bootstrap new wiki | ~1-2 minutes |
| **repo-wiki-index** | Build code map | ~2-5 minutes |
| **repo-wiki-generate** | Generate documentation with citations | ~5-10 minutes |
| **repo-wiki-detect** | Detect changes since last run | <1 minute |
| **repo-wiki-update** | Incrementally update documentation | ~1-3 minutes |
| **repo-wiki-validate** | Enforce quality gates | <1 minute |

---

## 🔄 Workflows

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

---

## ⚙️ Configuration

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

---

## 🎯 Use Cases

### For Engineering Teams
- **Onboarding** - New team members get up-to-date documentation with source links
- **Code reviews** - Reviewers can verify documentation claims against actual code
- **Architecture decisions** - Document design decisions with citations to implementation

### For Tech Leads
- **System overview** - Maintain high-level architecture documentation
- **Dependency tracking** - Document component relationships with citations
- **Technical debt** - Track areas needing improvement with specific code references

### For Documentation Writers
- **Accuracy** - Every claim is backed by code citations
- **Maintenance** - Incremental updates keep docs fresh without full rewrites
- **Collaboration** - Preserve manual edits while allowing automated updates

---

## 📝 Examples

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

---

## 🛠️ Best Practices

1. **Run initialization once** - Only needed for new wikis
2. **Index before generating** - Code map needed for citations
3. **Detect before updating** - Know what changed before updating
4. **Validate after any operation** - Ensure quality gates pass
5. **Commit incrementally** - Small documentation updates are easier to review

---

## 🐛 Troubleshooting

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

---

## ✅ Implementation Status

**All requirements from rpd.md implemented:**
- ✅ Baseline wiki generation (FR1)
- ✅ Change detection (FR2)
- ✅ Incremental updates (FR3)
- ✅ Citations with line numbers (FR4)
- ✅ Clickable permalinks (FR5)
- ✅ Preservation of human edits (FR6)
- ✅ Deterministic output (NFR1)
- ✅ Bounded changes (NFR2)
- ✅ Performance scaling (NFR3)
- ✅ Safety around secrets (NFR4)
- ✅ Verifiable citations (NFR5)

---

## 🔗 Links and Resources

- **GitHub Repository:** [https://github.com/boweneos/repo-wiki-agent-skills](https://github.com/boweneos/repo-wiki-agent-skills)
- **Agent Skills Specification:** [https://agentskills.io](https://agentskills.io)
- **MkDocs Documentation:** [https://www.mkdocs.org](https://www.mkdocs.org)

---

## 📄 License

MIT License - See individual SKILL.md files for details.

---

## 🤝 Contributing

These skills follow the open Agent Skills format. To extend:

1. Add new sub-skills in `skills/` directory
2. Follow SKILL.md format specification
3. Include step-by-step instructions
4. Add references and examples
5. Test with validation skill

---

## 🎓 Agent Skills Compliance

This implementation follows the [Agent Skills specification](https://agentskills.io):

- ✅ Each skill has a `SKILL.md` file with required frontmatter
- ✅ Skills use progressive disclosure (metadata → instructions → details)
- ✅ Scripts, references, and assets are properly organized
- ✅ Skills are composable and reusable
- ✅ Clear instructions for when to use each skill
- ✅ Proper dependency management between skills

---

*Last updated: January 2025*  
*Maintained by: FDE Team*
