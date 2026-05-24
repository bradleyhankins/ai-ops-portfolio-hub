# Project Structure

This repository is organized to keep the deployed Streamlit app simple while documenting the intended engineering structure.

```text
.
├── app.py                  # Streamlit application entrypoint
├── README.md               # Project overview, case study, and test flow
├── ARCHITECTURE.md         # Application architecture and design decisions
├── PROJECT_STRUCTURE.md    # Repository structure reference
├── DEVELOPMENT_NOTES.md    # Implementation notes and future refactor plan
├── requirements.txt        # Python dependencies
└── screenshots/            # README screenshots
```

## File Responsibilities

### `app.py`

Contains the deployed Streamlit application.

Responsibilities:

- Page configuration
- Project metadata
- UI helper functions
- Page layout
- Link routing to deployed apps and GitHub repos

### `README.md`

Primary public-facing documentation.

Includes:

- Live demo link
- Portfolio summary
- Included projects
- Suggested test flow
- Tech stack
- Public demo note

### `ARCHITECTURE.md`

Explains how the app is structured conceptually and why the current version uses a simple Streamlit deployment model.

### `DEVELOPMENT_NOTES.md`

Documents future improvements and engineering decisions.

## Future Production Layout

A larger production version would likely use:

```text
app.py
src/
  config.py
  components.py
  content.py
  styles.css
  utils.py
tests/
  test_tool_selector.py
```

For the current portfolio version, the priority is clarity, deployability, and fast inspection by recruiters or technical reviewers.
