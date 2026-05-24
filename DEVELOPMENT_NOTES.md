# Development Notes

## Build Philosophy

This project is intentionally built as a lightweight Streamlit app rather than a heavy full-stack application.

The purpose is to demonstrate practical AI operations workflow thinking through a working deployed tool.

## Engineering Priorities

1. Clear user workflow
2. Fast browser-based demo
3. Easy GitHub review
4. Minimal dependency overhead
5. Public-safe sample content
6. Consistent visual language across portfolio apps

## Current Tradeoffs

The current version keeps the app in a single Streamlit entrypoint so the deployment is simple and easy to inspect.

This creates some tradeoffs:

- Faster to review and deploy
- Easier for non-technical visitors to understand
- Less modular than a larger production codebase
- Future refactors should split presentation, configuration, and components

## Recommended Future Refactor

A future production-oriented version should move toward:

```text
src/config.py       # Project metadata and links
src/components.py   # Reusable Streamlit/HTML components
src/styles.css      # Styling
src/content.py      # Portfolio copy and static content
app.py              # Main app flow only
```

## Quality Notes

The current version uses:

- Python type hints for helper functions
- Data-driven rendering from project dictionaries
- Reusable card and section helpers
- Public-safe project copy
- Consistent width, spacing, and color system across the app family

## Future Tooling

Potential future developer tooling:

- Ruff for linting and formatting
- Pytest for utility tests
- Pre-commit hooks
- GitHub Actions smoke checks
- Snapshot-based visual QA checklist
