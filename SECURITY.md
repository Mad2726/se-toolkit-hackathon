# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Reporting a Vulnerability

We take the security of Scholarship Calculator Bot seriously. If you believe you have found a security vulnerability, please report it to us as soon as possible.

### How to Report

**DO NOT** create a public GitHub issue for security vulnerabilities.

Instead, please:

1. **Email us** at: [YOUR_EMAIL]
2. **Include in your report**:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact assessment
   - Any suggested fixes (if available)

### What to Expect

- **Initial response**: We will acknowledge receipt of your report within 48 hours
- **Assessment**: We will assess the vulnerability and determine its impact
- **Fix timeline**: We aim to address critical vulnerabilities within 7 days
- **Disclosure**: We will coordinate with you on responsible disclosure timing

### Security Best Practices for Users

1. **Protect your BOT_TOKEN**
   - Never commit `.env` file to git
   - Rotate token if you suspect it's compromised
   - Use environment variables in production

2. **Restrict admin access**
   - Only add trusted user IDs to `ADMIN_USER_IDS`
   - Regularly review admin access

3. **Keep dependencies updated**
   - Regularly update Python packages
   - Monitor for security advisories

4. **Secure your server**
   - Use firewall rules to restrict access
   - Keep Ubuntu and Docker updated
   - Use SSH keys instead of passwords

5. **Database security**
   - Backup database regularly
   - Restrict file permissions on database files
   - Don't expose database files publicly

### Security Features

Current security measures in the project:

- ✅ Environment variables for sensitive data
- ✅ `.env` excluded from version control
- ✅ Non-root user in Docker container
- ✅ No hardcoded secrets in source code
- ✅ Input validation for user data
- ✅ SQLite with parameterized queries (prevents SQL injection)

### Known Limitations

- ⚠️ Telegram bot tokens are transmitted in plain text to the bot
- ⚠️ SQLite doesn't have built-in encryption (consider PostgreSQL for production with sensitive data)
- ⚠️ No rate limiting implemented (potential for abuse)

### Responsible Disclosure

We follow responsible disclosure practices:
- We will not share your personal information
- We will credit reporters in release notes (with permission)
- We will coordinate public disclosure timing

---

**Thank you for helping keep Scholarship Calculator Bot secure! 🙏**
