<div align="center">

# 📚 Repo Wiki Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![GitHub release](https://img.shields.io/github/v/release/agent-skills/repo-wiki-agent-skills)](https://github.com/agent-skills/repo-wiki-agent-skills/releases)
[![CI](https://github.com/agent-skills/repo-wiki-agent-skills/workflows/CI/badge.svg)](https://github.com/agent-skills/repo-wiki-agent-skills/actions)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-green.svg)](https://agentskills.io)
[![MkDocs](https://img.shields.io/badge/MkDocs-Compatible-blue.svg)](https://www.mkdocs.org)
[![PRD Complete](https://img.shields.io/badge/PRD-100%25-brightgreen.svg)](rpd.md)

**A comprehensive set of Agent Skills for generating and maintaining citation-backed repository wikis as MkDocs-compatible Markdown.**

[Features](#key-features) • [Quick Start](#quick-start) • [Documentation](#skill-structure) • [Examples](#examples) • [Contributing](#contributing)

</div>

---

## 📑 Table of Contents

- [Overview](#overview)
- [Quick Start](#-quick-start)
  - [Installation](#installation)
  - [Cursor Commands](#-cursor-commands-recommended)
  - [Shell Scripts](#-shell-scripts-alternative)
  - [Manual Skill Usage](#-manual-skill-usage)
- [Skill Structure](#skill-structure)
- [Key Features](#key-features)
- [Skill Details](#skill-details)
- [Configuration](#configuration)
- [Agent Skills Compliance](#agent-skills-compliance)
- [Best Practices](#best-practices)
- [Workflows](#workflows)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Status](#-status)
- [Releases](#-releases)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

---

## Overview

This project implements the complete **Repo Wiki Agent Skills** system as specified in `rpd.md`. The skills enable AI agents to:

- **Generate** complete documentation from scratch with proper citations
- **Track** code changes via git diff
- **Update** documentation incrementally (only affected pages)
- **Cite** every technical claim with file paths and line ranges
- **Maintain** traceability through clickable permalinks
- **Preserve** human edits while updating agent-managed content

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/agent-skills/repo-wiki-agent-skills.git
cd repo-wiki-agent-skills

# Install with uv (recommended)
uv pip install -e .

# Or with pip
pip install -e .
```

### 🎯 Cursor Commands (Recommended)

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
cat repo-wiki-initialize/SKILL.md  # 1. Initialize
cat repo-wiki-index/SKILL.md      # 2. Index
cat repo-wiki-generate/SKILL.md   # 3. Generate
cat repo-wiki-validate/SKILL.md   # 4. Validate
```

**After code changes:**
```bash
cat repo-wiki-detect/SKILL.md     # 1. Detect
cat repo-wiki-update/SKILL.md     # 2. Update
cat repo-wiki-validate/SKILL.md   # 3. Validate
```

## Skill Structure

```
repo-wiki-agent-skills/
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
uv run repo-wiki/scripts/validate_citations.py
```

### Managed Blocks Missing

Add markers manually:
```markdown
<!-- BEGIN:REPO_WIKI_MANAGED -->
<!-- END:REPO_WIKI_MANAGED -->
```

## Contributing

These skills follow the open Agent Skills format. To extend:

1. Add new sub-skills in the root directory
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

## 📊 Status

✅ **Production Ready** - All requirements from [rpd.md](rpd.md) implemented:

### Functional Requirements
- [x] Baseline wiki generation (FR1)
- [x] Change detection (FR2)
- [x] Incremental updates (FR3)
- [x] Citations with line numbers (FR4)
- [x] Clickable permalinks (FR5)
- [x] Preservation of human edits (FR6)

### Non-Functional Requirements
- [x] Deterministic output (NFR1)
- [x] Bounded changes (NFR2)
- [x] Performance scaling (NFR3)
- [x] Safety around secrets (NFR4)
- [x] Verifiable citations (NFR5)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for detailed information.

### Quick Start

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'feat: add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Install with development dependencies
uv pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .
ruff check --fix .
```

For more details, see [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built following the [Agent Skills Specification](https://agentskills.io)
- Compatible with [MkDocs](https://www.mkdocs.org) for beautiful documentation sites
- Inspired by the need for maintainable, citation-backed technical documentation

## 📦 Releases

See [RELEASE.md](RELEASE.md) for information on creating releases and the [Releases page](https://github.com/agent-skills/repo-wiki-agent-skills/releases) for downloads.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/agent-skills/repo-wiki-agent-skills/issues) - Report bugs or request features
- **Discussions**: [GitHub Discussions](https://github.com/agent-skills/repo-wiki-agent-skills/discussions) - Ask questions and share ideas
- **Security**: See [SECURITY.md](SECURITY.md) for security policy and vulnerability reporting
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
- **Documentation**: See [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) for detailed implementation notes
- **Changelog**: See [CHANGELOG.md](CHANGELOG.md) for version history

---

<div align="center">

**Made with ❤️ for better documentation**

⭐ Star us on GitHub if you find this useful!

</div>
