# Contributing to Scholarship Calculator Bot

First off, thank you for considering contributing to Scholarship Calculator Bot! It's people like you that make this project great.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** to trigger the issue
- **Describe the behavior you observed** and what you expected
- **Include screenshots** if applicable
- **Include your environment details** (OS, Python version, Docker version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a step-by-step description** of the suggested enhancement
- **Explain why this enhancement would be useful** to most users
- **List some examples** of how this enhancement would be used

### Pull Requests

- Fill in the required template
- Do not include issue numbers in the PR title
- Include screenshots and animated GIFs in your pull request whenever possible
- Follow the Python style guide
- Document new code
- Keep pull requests focused on a single feature or fix

## Development Setup

### Local Development

1. Fork the repo
2. Create a new branch from `main`:
   ```bash
   git checkout -b feature/my-feature
   ```

3. Set up your development environment:
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

4. Create `.env` file:
   ```bash
   cp .env.docker.example .env
   ```

5. Run the bot locally:
   ```bash
   python src/main.py
   ```

### Docker Development

1. Build and run with Docker:
   ```bash
   docker compose up --build
   ```

2. Make changes to the code and rebuild:
   ```bash
   docker compose down
   docker compose up --build
   ```

## Style Guidelines

### Python Code

- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints where possible
- Write docstrings for all functions, classes, and modules
- Keep functions focused and under 50 lines when possible
- Use meaningful variable and function names

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line
- Consider starting the commit message with an applicable emoji:
  - 🎨 `:art:` when improving the format/structure of the code
  - 🐎 `:racehorse:` when improving performance
  - 📝 `:memo:` when writing docs
  - 🐛 `:bug:` when fixing a bug
  - 🔥 `:fire:` when removing code or files
  - ✅ `:white_check_mark:` when adding tests
  - 🔒 `:lock:` when dealing with security

### Documentation

- Use Markdown for documentation
- Keep README.md up to date
- Document all public interfaces
- Include examples where helpful

## Additional Notes

### Issue and Pull Request Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project README

Thank you for contributing! 🎉
