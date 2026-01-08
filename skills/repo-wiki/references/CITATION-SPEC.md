# Citation Specification

## Overview

Every technical claim in the documentation must be backed by a citation to the source code.

## Citation Format

### Footnote Style (Preferred)

```markdown
The service starts an HTTP server on the configured port[^1].

[^1]: `src/server.ts` L12–L48 (commit abc1234)
```

### Inline Style

```markdown
The service starts an HTTP server on the configured port.
Source: `src/server.ts` L12–L48
```

## Required Components

1. **File path** - Relative to repository root
2. **Start line** - Line number where referenced code begins
3. **End line** - Line number where referenced code ends
4. **Commit SHA** (optional) - For stable references

## What Requires Citations

- Default values and configuration
- Error behavior and exceptions
- Performance characteristics
- Control flow descriptions
- API contracts

## Citation Coverage Rule

Pages should maintain **≥80% citation coverage** for technical claims.
