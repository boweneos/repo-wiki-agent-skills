# Release Workflow Diagram

## Automated Release Process

```
┌─────────────────────────────────────────────────────────────────┐
│                     Developer Actions                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ Update Version   │
                    │ in pyproject.toml│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Update           │
                    │ CHANGELOG.md     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Commit Changes   │
                    │ git commit       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Create Tag       │
                    │ git tag vX.Y.Z   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Push Tag         │
                    │ git push --tags  │
                    └────────┬─────────┘
                             │
┌────────────────────────────┴────────────────────────────┐
│                  GitHub Actions Triggered                │
└─────────────────────────────────────────────────────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Checkout Code    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Setup Python     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Install Build    │
                    │ Dependencies     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Build Python     │
                    │ Packages         │
                    └────────┬─────────┘
                             │
                    ┌────────┴─────────┐
                    │                  │
                    ▼                  ▼
          ┌──────────────┐   ┌──────────────┐
          │ Create .whl  │   │ Create .tar.gz│
          │ (wheel)      │   │ (source dist) │
          └──────┬───────┘   └───────┬──────┘
                 │                   │
                 └────────┬──────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Create Archives  │
                 │ .tar.gz & .zip   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Extract Release  │
                 │ Notes from       │
                 │ CHANGELOG.md     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Create GitHub    │
                 │ Release          │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Upload Assets:   │
                 │ • .whl           │
                 │ • .tar.gz (dist) │
                 │ • .tar.gz (full) │
                 │ • .zip (full)    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Upload to PyPI   │
                 │ (if configured)  │
                 └────────┬─────────┘
                          │
┌─────────────────────────┴──────────────────────────┐
│                  Release Complete                   │
└────────────────────────────────────────────────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Users Can:       │
                 │ • Download assets│
                 │ • Install via pip│
                 │ • View changelog │
                 └──────────────────┘
```

## CI Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│              Push to main/develop or Pull Request               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ GitHub Actions   │
                    │ CI Triggered     │
                    └────────┬─────────┘
                             │
                    ┌────────┴─────────┐
                    │                  │
                    ▼                  ▼
          ┌──────────────┐   ┌──────────────┐
          │ Test Job     │   │ Validate Job │
          └──────┬───────┘   └───────┬──────┘
                 │                   │
                 ▼                   ▼
       ┌─────────────────┐  ┌──────────────┐
       │ Matrix Testing: │  │ Check SKILL  │
       │ • Ubuntu        │  │ files exist  │
       │ • macOS         │  └───────┬──────┘
       │ • Windows       │          │
       │                 │          ▼
       │ Python:         │  ┌──────────────┐
       │ • 3.10          │  │ Validate     │
       │ • 3.11          │  │ Python syntax│
       │ • 3.12          │  └───────┬──────┘
       └────────┬────────┘          │
                │                   ▼
                ▼           ┌──────────────┐
       ┌─────────────────┐  │ Check shell  │
       │ Run ruff lint   │  │ scripts      │
       └────────┬────────┘  └───────┬──────┘
                │                   │
                ▼                   │
       ┌─────────────────┐          │
       │ Run black check │          │
       └────────┬────────┘          │
                │                   │
                ▼                   │
       ┌─────────────────┐          │
       │ Run pytest      │          │
       └────────┬────────┘          │
                │                   │
                └────────┬──────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ All Checks Pass  │
                │ ✅ Ready to Merge│
                └──────────────────┘
```

## Asset Types Generated

### Python Packages
- **Wheel** (`.whl`): Binary distribution, fast installation
- **Source Distribution** (`.tar.gz`): Source code for pip

### Source Archives
- **TAR.GZ Archive**: Compressed source with all files
- **ZIP Archive**: Windows-friendly compressed source

## Version Types

### Stable Release
```
v1.2.3
├── Uploaded to PyPI
├── Marked as latest
└── Full release notes
```

### Pre-release
```
v1.2.3-alpha.1
v1.2.3-beta.1
v1.2.3-rc.1
├── NOT uploaded to PyPI
├── Marked as pre-release
└── Testing purposes
```

## Badge Status Flow

```
Code Push → CI Run → Badge Updates
                     ├── ✅ Passing (green)
                     └── ❌ Failing (red)

Tag Push → Release → Badge Updates
                    └── Version number updates
```

## Security

- ✅ Secrets stored in GitHub
- ✅ PyPI token optional
- ✅ No credentials in code
- ✅ Automated and secure

## Rollback Process

```
Problem Detected
       │
       ▼
Delete Release (GitHub UI)
       │
       ▼
Delete Tag
├── git push --delete origin vX.Y.Z
└── git tag -d vX.Y.Z
       │
       ▼
Fix Issue
       │
       ▼
Create New Release
```
