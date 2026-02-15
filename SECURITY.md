# Security Policy

## Supported Versions

We actively support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security vulnerability, please follow these steps:

### 1. **Do NOT** create a public GitHub issue

Security vulnerabilities should be reported privately to prevent exploitation.

### 2. Email Security Team

Send an email to: **security@agentskills.io** (or create a private security advisory on GitHub)

Include the following information:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if available)
- Your contact information

### 3. Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity

### 4. Disclosure Policy

- We will acknowledge receipt of your report
- We will keep you informed of the progress
- We will credit you in the security advisory (if desired)
- We will coordinate public disclosure after a fix is available

## Security Best Practices

### For Users

1. **Keep dependencies updated**
   ```bash
   pip install --upgrade repo-wiki-agent-skills
   ```

2. **Review generated documentation**
   - Check citations point to correct files
   - Verify no sensitive information is exposed
   - Validate markdown output

3. **Use managed blocks carefully**
   - Don't place secrets in managed sections
   - Review agent-generated content before committing

4. **Validate citations**
   ```bash
   python skills/repo-wiki/scripts/validate_citations.py
   ```

### For Contributors

1. **Never commit secrets**
   - Use environment variables
   - Add secrets to `.gitignore`
   - Use secret scanning tools

2. **Validate inputs**
   - Sanitize file paths
   - Check line ranges
   - Verify git operations

3. **Follow secure coding practices**
   - Use type hints
   - Add input validation
   - Handle errors gracefully

## Known Security Considerations

### File System Access

The tool reads and writes files. Ensure:
- Proper file permissions
- Path validation to prevent directory traversal
- Safe handling of symlinks

### Git Operations

The tool executes git commands. Ensure:
- Git repository is trusted
- No malicious hooks
- Safe diff operations

### LLM Integration

If using LLM features:
- Don't send secrets to LLM APIs
- Review generated content
- Validate citations independently

## Security Updates

Security updates will be:
- Released as patch versions (e.g., 1.0.1)
- Documented in CHANGELOG.md
- Tagged with security labels
- Announced via GitHub Releases

## Security Checklist

Before releasing:
- [ ] No hardcoded secrets
- [ ] Input validation in place
- [ ] Error handling implemented
- [ ] Dependencies up to date
- [ ] Security tests added
- [ ] Documentation updated

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [Git Security](https://git-scm.com/docs/git-config#_security)

## Contact

For security concerns:
- **Email**: security@agentskills.io
- **GitHub**: Create a [private security advisory](https://github.com/agent-skills/repo-wiki-agent-skills/security/advisories/new)

Thank you for helping keep this project secure! 🔒
