# Practical AI Ops Toolkit

Practical AI Ops Toolkit is a portfolio hub for AI-enhanced workflow tools built by Bradley Hankins.

The portfolio demonstrates practical AI applications for:

- Client workflow diagnostics
- Operations visibility
- Sales follow-up execution
- CRM workflow discipline
- ATS Lite resume review workflows
- Human-review applicant documentation
- SOP and training documentation
- Manager reporting and decision support

## Live Demo

[Launch Practical AI Ops Toolkit](https://ai-ops-portfolio-hub.streamlit.app/)

## Current Version

The toolkit uses an embedded AI pattern across the portfolio.

Each output-heavy app works in two layers:

1. **Rules-based workflow core:** provides reliable scoring, routing, diagnostics, structure, calculations, and fallback output.
2. **Embedded AI enhancement layer:** when an OpenAI token is available, the app improves summaries, recommendations, reports, and communication outputs.

If the AI call fails or an API key is unavailable, the apps fall back to the rules-based outputs. The user experience stays the same.

## Portfolio Architecture

The portfolio now uses a consistent project pattern across the apps:

```text
app.py                 # Streamlit UI and orchestration
ai_helpers.py          # AI guardrails, API access, fallback, cache keys
pdf_helpers.py         # PDF export helpers where applicable
core/                  # Business logic, diagnostics, prompts, report builders
data/                  # Sample data, dropdown options, public demo notes
.github/workflows/     # CI checks where enabled
```

## Projects Included

### ClientOps Intake AI

Client diagnostic intake assistant that identifies workflow bottlenecks, scores operational maturity, recommends automation opportunities, routes users to the right toolkit app, and generates a 30-day improvement roadmap.

- Live app: https://clientops-intake-ai.streamlit.app/
- Repository: https://github.com/bradleyhankins/clientops-intake-ai
- Output: PDF diagnostic report

### OpsPilot AI

Operations intelligence dashboard that converts field-sales activity into KPI visibility, rep performance insights, lead source analysis, operations diagnosis, manager briefs, weekly sales meeting agendas, and downloadable manager reports.

- Live app: https://opspilot-ai.streamlit.app/
- Repository: https://github.com/bradleyhankins/opspilot-ai
- Output: PDF manager report and filtered CSV export

### FollowUpPilot AI

Sales follow-up workflow assistant that turns customer context into next-best actions, lead temperature, deal risk scoring, customer text messages, emails, voicemail scripts, CRM notes, call scripts, objection guidance, manager coaching notes, follow-up sequences, and downloadable follow-up plans.

- Live app: https://followuppilot-ai.streamlit.app/
- Repository: https://github.com/bradleyhankins/followuppilot-ai
- Output: PDF follow-up plan

### RecruitPilot AI

Responsible ATS Lite resume review assistant that organizes job descriptions and PDF/DOCX resume uploads into review priorities, resume match signals, missing or unclear information, follow-up interview questions, manager summaries, candidate emails, PDF review packets, and candidate tracker CSV rows for human review.

- Live app: https://recruitpilot-ai.streamlit.app/
- Repository: https://github.com/bradleyhankins/recruitpilot-ai
- Output: PDF review packet and CSV tracker row

### SOPPilot AI

Process documentation workflow assistant that turns rough process notes into SOPs, process checklists, missing-information checks, risk diagnoses, rollout readiness guidance, manager summaries, training plans, quality control guides, implementation plans, and downloadable SOP packages.

- Live app: https://soppilot-ai.streamlit.app/
- Repository: https://github.com/bradleyhankins/soppilot-ai
- Output: PDF SOP package

## Suggested Test Flow

1. Launch the live portfolio hub.
2. Review the hero section and project summary cards.
3. Use the “Which tool should I use?” section to choose a workflow.
4. Review the embedded AI-enhanced recommendation language.
5. Open each live app and generate a sample output.
6. Download a PDF report/package from each output-heavy app.

## Screenshots

Screenshots will be refreshed after the final UI pass across the portfolio.

## Export Strategy

Current exports across the output-heavy apps:

- PDF reports/packages for manager-ready deliverables
- CSV exports where structured data is useful

## Portfolio Purpose

This portfolio was created to show how lightweight AI-enhanced tools can help small and mid-sized businesses improve operations without needing complex enterprise software.

The focus is practical execution:

- Better workflow diagnosis
- Better visibility
- Better follow-up
- Better applicant review organization
- Better process documentation
- Better training consistency
- Better manager documentation
- Better decision support

## Tech Stack

- Python
- Streamlit
- OpenAI API integration
- Rules-based workflow logic
- Silent AI fallback pattern
- Modular app architecture
- Deterministic AI cache keys
- Pandas
- PDF report exports
- CSV-based workflows
- GitHub
- GitHub Actions checks
- Streamlit Community Cloud

## Run Locally

```bash
py -m pip install -r requirements.txt
py -m streamlit run app.py
```

## Environment Variables

To enable embedded AI output:

```bash
OPENAI_TOKEN=your_api_key_here
```

The apps still work without this token by using rules-based fallback outputs.

## Public Demo Note

All sample data, names, companies, and scenarios used in these projects are fictional and created for public portfolio demonstration purposes.

## Responsible AI Note

These tools use deterministic rules as the source of truth. AI is used to polish, summarize, or organize outputs without replacing human review or business judgment.

RecruitPilot AI is designed to organize applicant information for human review. It should not be used as the sole basis for selection, rejection, compensation, or employment decisions.

## Built By

Bradley Hankins  
Operations & Revenue Leader | AI Workflow Automation | RevOps & Process Improvement
