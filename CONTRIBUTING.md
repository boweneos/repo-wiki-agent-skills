# Contributing to Repo Wiki Agent Skills

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please check the [existing issues](https://github.com/agent-skills/repo-wiki-agent-skills/issues) to ensure it hasn't been reported.

When creating a bug report, include:
- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs **actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Relevant logs or error messages**
- **Screenshots** (if applicable)

### Suggesting Enhancements

Enhancement suggestions are tracked as [GitHub issues](https://github.com/agent-skills/repo-wiki-agent-skills/issues). When creating an enhancement suggestion:

- Use a clear and descriptive title
- Provide a detailed description of the proposed enhancement
- Explain why this enhancement would be useful
- List any alternatives you've considered
- Include examples or mockups if applicable

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/repo-wiki-agent-skills.git
   cd repo-wiki-agent-skills
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

3. **Make your changes**
   - Follow the code style (see below)
   - Add tests for new functionality
   - Update documentation as needed
   - Update CHANGELOG.md

4. **Test your changes**
   ```bash
   # Install development dependencies
   uv pip install -e ".[dev]"
   
   # Run linting
   ruff check .
   black --check .
   
   # Run tests
   pytest
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```
   
   Use conventional commit messages:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `style:` for formatting changes
   - `refactor:` for code refactoring
   - `test:` for adding tests
   - `chore:` for maintenance tasks

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Use a clear title and description
   - Reference any related issues
   - Wait for CI checks to pass
   - Address review feedback

## Development Setup

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- Git

### Installation

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/repo-wiki-agent-skills.git
cd repo-wiki-agent-skills

# Install in development mode
uv pip install -e ".[dev]"

# Or with pip
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=scripts --cov-report=html

# Run specific test file
pytest tests/test_specific.py
```

### Code Style

We use:
- **ruff** for linting
- **black** for code formatting

```bash
# Check code style
ruff check .
black --check .

# Auto-fix issues
ruff check --fix .
black .
```

### Project Structure

```
repo-wiki-agent-skills/
├── skills/              # Agent Skills definitions
│   └── repo-wiki/      # Main skill with scripts and templates
├── scripts/            # Python CLI scripts
├── .github/            # GitHub workflows and templates
├── tests/              # Test files (create if needed)
├── README.md           # Main documentation
├── CHANGELOG.md        # Version history
└── pyproject.toml      # Project configuration
```

## Adding New Skills

If you're adding a new Agent Skill:

1. Create a new directory in `skills/`
2. Add a `SKILL.md` file following the [Agent Skills specification](https://agentskills.io)
3. Include required frontmatter:
   ```yaml
   ---
   name: skill-name
   description: Brief description
   license: MIT
   compatibility:
     agents: ["claude", "gpt-4"]
   ---
   ```
4. Add step-by-step instructions
5. Update the main README.md to reference the new skill

## Adding Scripts

When adding Python scripts:

1. Place in appropriate directory (`scripts/` or `skills/repo-wiki/scripts/`)
2. Add type hints
3. Add docstrings
4. Follow PEP 8 style guide
5. Add tests if applicable

## Documentation

- Update README.md for user-facing changes
- Update CHANGELOG.md for all changes
- Add docstrings to new functions/classes
- Update skill documentation in SKILL.md files

## Testing Guidelines

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for good test coverage
- Use descriptive test names

## Commit Message Guidelines

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

Examples:
```
feat(scripts): add citation validation script
fix(workflow): correct release asset paths
docs(readme): update installation instructions
```

## Review Process

1. All PRs require at least one approval
2. CI checks must pass
3. Code must follow style guidelines
4. Documentation must be updated
5. Tests must pass

## Questions?

- Open a [GitHub Discussion](https://github.com/agent-skills/repo-wiki-agent-skills/discussions)
- Check existing [Issues](https://github.com/agent-skills/repo-wiki-agent-skills/issues)
- Review [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) for architecture details

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
