# Architecture

Practical AI Ops Toolkit is a Streamlit portfolio hub built as a lightweight product-style application.

## Current Architecture

The application currently uses a single Streamlit entrypoint for straightforward deployment on Streamlit Community Cloud.

```text
app.py
README.md
requirements.txt
screenshots/
```

## Application Layers

Although the deployed version is contained in `app.py`, the code is organized conceptually into clear layers:

```text
Configuration
- Project links
- Project metadata
- Tool recommendation mapping

Presentation
- Custom CSS
- Hero sections
- Cards
- Sidebar links
- Project spotlight sections

UI Components
- Link buttons
- Stat cards
- Project cards
- Use-case cards

Page Flow
- Hero
- Tool selector
- Start-here section
- Project use cases
- Portfolio story
- Project cards
- Roadmap
- Positioning
```

## Design Choices

This app intentionally keeps deployment simple while demonstrating:

- Streamlit page composition
- Reusable UI helper functions
- Project metadata-driven rendering
- Consistent portfolio-wide visual language
- Clear public-demo positioning

## Why Single-File for This Version

The current single-file structure keeps the live deployment easy to inspect and reduces dependency complexity for a portfolio project.

A future production version would likely split the app into:

```text
app.py
config.py
components.py
styles.css
content.py
```

## Future Refactor Plan

Planned code organization improvements:

1. Move CSS into `styles.css`
2. Move project metadata into `config.py`
3. Move card rendering helpers into `components.py`
4. Add automated linting with Ruff
5. Add lightweight tests for project selector mapping
