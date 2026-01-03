# Copilot Instructions for IRHV24 Repository

## Mandatory Code Review Policy

**RULE: Code reviews are mandatory before ending any session.**

Before completing or ending any work session, Copilot MUST:

1. **Run the code review tool** (`code_review`) on all changes made during the session
2. **Address all review comments** that are actionable and relevant
3. **Continue running code reviews** until no new issues are found
4. **Only then** may the session be considered complete

### Code Review Workflow

```
1. Make changes to address the issue/request
2. Run code_review tool
3. If comments are found:
   a. Address each actionable comment
   b. Run code_review again
   c. Repeat until no new comments
4. Run codeql_checker for security analysis
5. Report progress and commit changes
6. Session may now end
```

### Rationale

This ensures:
- All code changes are reviewed for quality before merging
- Security vulnerabilities are caught early
- Best practices are consistently followed
- The codebase maintains high quality standards

## Additional Guidelines

### For Computational Notebooks

- Ensure all notebooks have one-to-one correlation with theory equations
- Verify output directories exist before saving files
- Use arbitrary precision arithmetic (mpmath) for theoretical calculations
- Include validation against experimental values where applicable

### For GitHub Actions Workflows

- Pin third-party actions to commit SHAs for supply chain security
- Use least-privilege permissions (prefer `contents: read` over `contents: write`)
- Include artifact upload for preserving outputs
- Add timeout limits to prevent runaway jobs

### For Documentation

- Keep README in sync with actual implemented features
- Clearly distinguish between implemented and planned features
- Include usage examples and quick start guides
