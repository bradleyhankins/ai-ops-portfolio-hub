# Engineering Roadmap

This roadmap tracks the next phase of hardening for the Practical AI Ops Toolkit.

The apps are currently functional, deployed, and portfolio-ready. The next goal is to make the codebase and AI architecture look and behave more like production-quality software.

## Guiding Principle

Rules decide. AI improves wording. Fallback protects the app.

The deterministic rules engine should remain the source of truth for scoring, recommendations, calculations, risk labels, and workflow routing. The AI layer should only improve clarity, structure, tone, and documentation quality.

---

## Phase 1: AI Reliability and Guardrails

### Goals

- Standardize AI helper behavior across all apps.
- Prevent unstable cache behavior.
- Limit prompt size for cost and reliability.
- Keep AI output bounded to the app's purpose.
- Make failure safe and invisible to the user.

### Tasks

- [ ] Confirm every app imports `stable_cache_key` from `ai_helpers.py`.
- [ ] Replace any remaining Python `hash()` cache keys with `stable_cache_key()`.
- [ ] Confirm every AI prompt is wrapped with the shared guardrail prefix.
- [ ] Add app-specific guardrail notes where needed.
- [ ] Add stronger RecruitPilot hiring guardrails.
- [ ] Confirm all AI failures silently fall back to rules-based output.
- [ ] Add input length limits for file uploads and long text areas.

### App-Specific Guardrails

#### ClientOps Intake AI

AI may improve the diagnostic summary, but it must not invent business facts, guarantees, ROI claims, or recommendations that conflict with the rules-based bottleneck or selected toolkit app.

#### FollowUpPilot AI

AI may improve message quality, but it must not invent discounts, deadlines, warranties, financing terms, customer promises, or urgency that was not provided.

#### OpsPilot AI

AI may improve manager brief wording, but it must not change KPI calculations, invent causes, fabricate performance numbers, or override the rules-based bottleneck.

#### SOPPilot AI

AI may improve documentation clarity, but it must not invent legal requirements, compliance standards, company policies, pricing, or procedures that were not provided.

#### RecruitPilot AI

AI may support human review preparation only. It must not rank candidates, recommend hiring or rejection, infer protected characteristics, or make employment decisions.

#### Portfolio Hub

AI may improve recommendation language, but it must not invent app features or route users to an app outside the defined toolkit mapping.

---

## Phase 2: PDF Report Polish

### Goals

Make exported PDFs feel like business deliverables rather than basic converted markdown.

### Tasks

- [ ] Add app-specific report headers.
- [ ] Add generated date.
- [ ] Add page numbers if practical.
- [ ] Add section dividers.
- [ ] Improve bullet and numbered-list formatting.
- [ ] Improve long text wrapping.
- [ ] Add footer note identifying the app.
- [ ] Standardize file naming across apps.

---

## Phase 3: Code Architecture Cleanup

### Goals

Make the GitHub repos look engineered instead of single-file prototypes.

### Target Structure

```text
app.py
core/
  scoring.py
  rules.py
  report_builder.py
  prompts.py
  validators.py
utils/
  ai_helpers.py
  pdf_helpers.py
  formatting.py
data/
  sample_data.py
tests/
  test_scoring.py
  test_reports.py
```

### Tasks

- [ ] Refactor one app first as the model repo.
- [ ] Move sample data out of `app.py`.
- [ ] Move scoring/rules into `core/`.
- [ ] Move AI prompts into `core/prompts.py`.
- [ ] Move report generation into `core/report_builder.py`.
- [ ] Keep `app.py` focused on UI orchestration.

Recommended first refactor candidate: ClientOps Intake AI, because it has the cleanest workflow.

---

## Phase 4: Tests and CI

### Goals

Add professional software quality signals.

### Tasks

- [ ] Add unit tests for scoring functions.
- [ ] Add unit tests for report builder functions.
- [ ] Add basic GitHub Actions workflow.
- [ ] Add dependency checks.
- [ ] Add README architecture section.
- [ ] Add screenshots after the final UI pass.

---

## Phase 5: UX and Privacy Polish

### Goals

Make the apps safer and clearer for public use.

### Tasks

- [ ] Add clear privacy note explaining that user input may be processed by the AI provider when AI is enabled.
- [ ] Add warnings not to upload sensitive, confidential, or regulated information.
- [ ] Add upload file size limits where applicable.
- [ ] Add text length limits for resume/job description/process fields.
- [ ] Add friendlier validation messages.

---

## Current Priority

Start with Phase 1, then move into PDF polish.

Phase 1 is the highest-leverage improvement because it improves safety, reliability, cost control, and professional architecture across the full toolkit.
