# Quick Start Guide

## For Cursor IDE Users

### 3 Simple Commands

Run these in your Cursor terminal:

#### 1️⃣ First-Time Setup

```bash
./scripts/wiki-init.sh
```

**What it does:**
- Creates `docs/` directory structure
- Generates `mkdocs.yml` configuration
- Creates placeholder pages with managed blocks
- Indexes your codebase
- Generates citation-backed documentation
- Validates the output

**When to use:** Once, when setting up documentation for a new repository.

**Time:** ~10-15 minutes (depends on repo size)

---

#### 2️⃣ Update After Changes

```bash
./scripts/wiki-update.sh
```

**What it does:**
- Detects code changes via git diff
- Identifies which documentation pages are affected
- Updates only the impacted pages
- Refreshes citations that may have shifted
- Creates pages for new modules
- Archives pages for deleted modules
- Validates the changes

**When to use:** After making code changes, before committing documentation updates.

**Time:** ~2-5 minutes (scales with change size)

---

#### 3️⃣ Validate Quality

```bash
./scripts/wiki-validate.sh
```

**What it does:**
- Validates all citations point to valid files and lines
- Checks internal links are not broken
- Verifies markdown syntax is correct
- Tests MkDocs build succeeds
- Generates validation report

**When to use:** 
- Before committing documentation
- In CI/CD pipelines
- To audit documentation quality

**Time:** <1 minute

---

## Step-by-Step First Run

### 1. Navigate to your repository

```bash
cd /path/to/your/repository
```

### 2. Run the initialization workflow

```bash
./scripts/wiki-init.sh
```

This will display each skill's instructions. Follow them step by step.

### 3. Build and preview

```bash
# Install MkDocs if needed
pip install mkdocs-material

# Serve locally
mkdocs serve
```

Open http://localhost:8000 in your browser to see your documentation!

### 4. Commit the results

```bash
git add docs/ mkdocs.yml .repo_wiki/
git commit -m "docs: initialize repository wiki with citations"
```

---

## Daily Usage

### After making code changes:

```bash
# 1. Commit your code changes first
git add src/
git commit -m "feat: add new authentication module"

# 2. Update documentation
./scripts/wiki-update.sh

# 3. Review the changes
git diff docs/

# 4. Commit documentation updates
git add docs/ .repo_wiki/
git commit -m "docs: update for authentication module changes"
```

---

## In Cursor IDE

### Using the Terminal

1. Open Cursor terminal (`` Ctrl+` `` or `Cmd+` `)
2. Run any of the three scripts
3. Follow the interactive prompts

### Using Tasks (Optional)

Add to `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Wiki: Initialize",
      "type": "shell",
      "command": "./scripts/wiki-init.sh",
      "problemMatcher": [],
      "group": "build"
    },
    {
      "label": "Wiki: Update",
      "type": "shell",
      "command": "./scripts/wiki-update.sh",
      "problemMatcher": [],
      "group": "build"
    },
    {
      "label": "Wiki: Validate",
      "type": "shell",
      "command": "./scripts/wiki-validate.sh",
      "problemMatcher": [],
      "group": "test"
    }
  ]
}
```

Then run via `Cmd+Shift+P` → "Tasks: Run Task" → Select task

---

## Command Options

All scripts accept an optional repository path:

```bash
# Run in current directory
./scripts/wiki-init.sh

# Run in specific directory
./scripts/wiki-init.sh /path/to/repo
```

---

## Troubleshooting

### Script not executable

```bash
chmod +x scripts/*.sh
```

### MkDocs not found

```bash
pip install mkdocs-material
```

### Python scripts fail

Make sure you have uv installed:

```bash
uv --version
```

### Git not initialized

```bash
git init
git add .
git commit -m "Initial commit"
```

---

## What Gets Created

After running `wiki-init.sh`, your repository will have:

```
your-repo/
├── docs/                          # Documentation
│   ├── index.md
│   ├── getting-started/
│   ├── architecture/
│   ├── components/
│   ├── api/
│   └── operations/
├── mkdocs.yml                     # MkDocs config
└── .repo_wiki/                    # State tracking
    ├── state.json
    ├── manifest.json
    ├── code_index.json
    └── logs/
```

---

## Next Steps

1. **Customize**: Edit `.repo_wiki/config.json` for preferences
2. **Preview**: Run `mkdocs serve` to view locally
3. **Deploy**: Use `mkdocs build` to generate static site
4. **Automate**: Add to CI/CD pipeline (see README.md)
5. **Extend**: Create custom templates in `skills/repo-wiki/assets/templates/`

---

## Getting Help

- **Full documentation**: See `README.md`
- **Skill details**: Read individual `SKILL.md` files
- **References**: Check `skills/repo-wiki/references/`
- **Implementation**: See `IMPLEMENTATION_SUMMARY.md`
