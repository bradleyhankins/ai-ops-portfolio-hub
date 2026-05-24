import streamlit as st

from ai_helpers import generate_ai_text

st.set_page_config(page_title="Practical AI Ops Toolkit - AI Tool Router", page_icon="🧠", layout="wide")

TOOLS = """
ClientOps Intake AI: Diagnoses workflow bottlenecks, maturity level, automation opportunities, and 30-day improvement roadmaps.
OpsPilot AI: KPI reporting, operations intelligence, rep performance, lead source analysis, manager briefs, and sales meeting prep.
FollowUpPilot AI: Sales follow-up messages, next-best actions, lead temperature, deal risk, CRM notes, voicemail scripts, and follow-up timelines.
RecruitPilot AI: Responsible ATS Lite workflow for resume review organization, human-review packets, missing information, interview questions, and candidate tracker exports.
SOPPilot AI: SOPs, checklists, process documentation, readiness scoring, version control, training plans, quality control, and implementation plans.
"""

st.title("AI Tool Router")
st.caption("Optional AI enhancement for routing a natural-language business problem to the right portfolio app.")

st.info(
    "This page is optional. The main Portfolio Hub dropdown router still works without AI. "
    "Set OPENAI_TOKEN in the deployment environment to enable AI output."
)

business_problem = st.text_area(
    "Describe the business problem in plain English",
    height=220,
    placeholder="Example: We have leads coming in, but I do not know which reps are following up, our CRM notes are messy, and manager meetings are hard to prepare for.",
)

if st.button("Route Me to the Right Tool", use_container_width=True):
    prompt = f"""
You are a practical AI operations advisor.
Route the user's business problem to the best starting tool from the portfolio.
Be concise and specific. Recommend one primary tool and one secondary tool if helpful.

Available tools:
{TOOLS}

User's business problem:
{business_problem}

Return:
1. Best starting tool
2. Why this tool fits
3. Secondary tool if useful
4. Suggested first action
5. What output the user should download or review
"""
    with st.spinner("Routing to the best tool..."):
        st.markdown(generate_ai_text(prompt))

st.divider()
st.markdown(
    "**AI positioning:** This page adds a natural-language routing layer on top of the Portfolio Hub's structured tool selector."
)
