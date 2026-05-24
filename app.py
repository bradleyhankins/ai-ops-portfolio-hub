import streamlit as st

st.set_page_config(page_title="Practical AI Ops Toolkit", page_icon="🧠", layout="wide")

# Replace these placeholders with your actual links before deploying.
OPSPILOT_LIVE = "https://opspilot-ai.streamlit.app/"
OPSPILOT_GITHUB = "https://github.com/bradleyhankins/opspilot-ai"

FOLLOWUPPILOT_LIVE = "https://followuppilot-ai.streamlit.app/"
FOLLOWUPPILOT_GITHUB = "https://github.com/bradleyhankins/followuppilot-ai"

RECRUITPILOT_LIVE = "https://recruitpilot-ai.streamlit.app/"
RECRUITPILOT_GITHUB = "https://github.com/bradleyhankins/recruitpilot-ai"

LINKEDIN_URL = "https://www.linkedin.com/in/bradleyhankins"
GITHUB_PROFILE = "https://github.com/bradleyhankins"

SOPPILOT_LIVE = "https://soppilot-ai.streamlit.app/"
SOPPILOT_GITHUB = "https://github.com/bradleyhankins/soppilot-ai"

def safe_link_button(label, url):
    if url.startswith("http"):
        st.link_button(label, url)
    else:
        st.button(label + " Pending", disabled=True)


def project_card(title, subtitle, problem, features, tech, live_url, github_url):
    st.subheader(title)
    st.caption(subtitle)
    st.markdown(f"**Problem solved:** {problem}")
    st.markdown("**Core features:**")
    for feature in features:
        st.markdown(f"- {feature}")
    st.markdown(f"**Tech stack:** {tech}")
    col1, col2 = st.columns(2)
    with col1:
        safe_link_button("Launch Live Demo", live_url)
    with col2:
        safe_link_button("View GitHub Repo", github_url)


st.title("🧠 Practical AI Ops Toolkit")
st.subheader("AI-assisted workflow tools for operations, sales execution, and hiring.")

st.markdown("""
Built by **Bradley Hankins**, this portfolio demonstrates practical AI-assisted tools designed for small and
mid-sized businesses that need better visibility, workflow discipline, and decision support without complex
enterprise software.

The focus is not AI for novelty. The focus is AI for operational execution.
""")

col1, col2, col3 = st.columns(3)
col1.metric("Portfolio Projects", "4")
col2.metric("Primary Stack", "Python + Streamlit")
col3.metric("Focus Area", "AI Operations")

st.divider()

st.header("Portfolio Story")

st.markdown("""
This toolkit was built around three practical business problems:

1. **Managers need better visibility into performance.**
2. **Sales teams need more consistent follow-up and CRM discipline.**
3. **Small businesses need a more structured way to evaluate candidates.**
4. **Teams need clearer process documentation, training, and quality standards.**            

Together, these projects show how lightweight AI-assisted workflows can improve day-to-day operations across
performance management, sales execution, and recruiting.
""")

st.divider()

st.header("Projects")

project_card(
    title="OpsPilot AI",
    subtitle="AI-assisted operations intelligence dashboard",
    problem="Field-sales and home-service managers often have activity data but lack a clear action plan.",
    features=[
        "KPI dashboard",
        "Rep performance analysis",
        "Lead source analysis",
        "AI-style operations diagnosis",
        "Manager brief",
        "Weekly sales meeting agenda",
        "Downloadable manager report"
    ],
    tech="Python, Streamlit, Pandas, CSV workflow, Markdown report export",
    live_url=OPSPILOT_LIVE,
    github_url=OPSPILOT_GITHUB
)

st.divider()

project_card(
    title="FollowUpPilot AI",
    subtitle="AI-assisted sales follow-up workflow tool",
    problem="Sales opportunities are often lost because follow-up is slow, inconsistent, or poorly documented.",
    features=[
        "Follow-up priority score",
        "Customer text and email generator",
        "CRM-ready note",
        "Call script",
        "Objection guidance",
        "Manager coaching note",
        "Multi-touch follow-up sequence",
        "Downloadable follow-up plan"
    ],
    tech="Python, Streamlit, rules-based workflow logic, Markdown report export",
    live_url=FOLLOWUPPILOT_LIVE,
    github_url=FOLLOWUPPILOT_GITHUB
)

st.divider()

project_card(
    title="RecruitPilot AI",
    subtitle="AI-assisted candidate screening workflow tool",
    problem="Small businesses often hire from scattered notes, informal interviews, and inconsistent evaluation processes.",
    features=[
        "Candidate fit score",
        "Risk level",
        "Hiring recommendation",
        "Role success profile",
        "Green flags and red flags",
        "Follow-up interview questions",
        "Interview scorecard",
        "Candidate email",
        "Recommended onboarding plan",
        "Downloadable candidate report"
    ],
    tech="Python, Streamlit, rules-based screening logic, Markdown report export",
    live_url=RECRUITPILOT_LIVE,
    github_url=RECRUITPILOT_GITHUB
)

st.divider()

project_card(
    title="SOPPilot AI",
    subtitle="AI-assisted SOP, checklist, and training document generator",
    problem="Small businesses often rely on tribal knowledge, verbal instructions, and inconsistent process documentation.",
    features=[
        "Process complexity score",
        "Risk diagnosis",
        "Missing-information check",
        "Improvement recommendations",
        "Standard Operating Procedure",
        "Process checklist",
        "Training plan",
        "Quality control guide",
        "Implementation plan",
        "Downloadable SOP package"
    ],
    tech="Python, Streamlit, rules-based workflow logic, Markdown report export",
    live_url=SOPPILOT_LIVE,
    github_url=SOPPILOT_GITHUB
)

st.divider()

st.header("Skills Demonstrated")

skill_col1, skill_col2, skill_col3 = st.columns(3)

with skill_col1:
    st.markdown("""
    **Operations**
    - KPI reporting
    - Revenue operations
    - Process improvement
    - Manager workflows
    - Performance visibility
    """)

with skill_col2:
    st.markdown("""
    **AI Workflow Design**
    - Rules-based AI logic
    - Prompt-style output design
    - Decision support tools
    - Workflow automation
    - Report generation
    """)

with skill_col3:
    st.markdown("""
    **Technical**
    - Python
    - Streamlit
    - Pandas
    - GitHub
    - Streamlit Community Cloud
    - Markdown exports
    """)

st.divider()

st.header("Consulting / Career Positioning")

st.markdown("""
These projects support a focused professional direction:

**AI Operations + Workflow Automation for small and mid-sized businesses.**

The goal is to help businesses use practical AI tools to:

- Improve operational visibility
- Standardize follow-up processes
- Strengthen CRM discipline
- Support manager coaching
- Improve hiring consistency
- Turn scattered data into action-ready outputs
- Reduce repetitive administrative work
""")

st.divider()

st.header("Connect")

col1, col2 = st.columns(2)
with col1:
    safe_link_button("LinkedIn Profile", LINKEDIN_URL)
with col2:
    safe_link_button("GitHub Profile", GITHUB_PROFILE)

st.info("Portfolio note: All sample data, names, companies, and scenarios used in these projects are fictional and created for public demonstration purposes.")
