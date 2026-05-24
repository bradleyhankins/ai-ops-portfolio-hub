import streamlit as st

st.set_page_config(
    page_title="Practical AI Ops Toolkit",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------
# Project links
# -----------------------------

OPSPILOT_LIVE = "https://opspilot-ai.streamlit.app/"
OPSPILOT_GITHUB = "https://github.com/bradleyhankins/opspilot-ai"

FOLLOWUPPILOT_LIVE = "https://followuppilot-ai.streamlit.app/"
FOLLOWUPPILOT_GITHUB = "https://github.com/bradleyhankins/followuppilot-ai"

RECRUITPILOT_LIVE = "https://recruitpilot-ai.streamlit.app/"
RECRUITPILOT_GITHUB = "https://github.com/bradleyhankins/recruitpilot-ai"

SOPPILOT_LIVE = "https://soppilot-ai.streamlit.app/"
SOPPILOT_GITHUB = "https://github.com/bradleyhankins/soppilot-ai"

LINKEDIN_URL = "https://www.linkedin.com/in/bradleyhankins/"
GITHUB_PROFILE = "https://github.com/bradleyhankins"
RESUME_LINK = "PASTE_RESUME_LINK_HERE_OPTIONAL"


def safe_link_button(label, url):
    if isinstance(url, str) and url.startswith("http"):
        st.link_button(label, url)
    else:
        st.button(label + " Pending", disabled=True)


def project_card(title, category, status, problem, outcome, features, tech, live_url, github_url):
    with st.container(border=True):
        top_col1, top_col2 = st.columns([3, 1])
        with top_col1:
            st.subheader(title)
            st.caption(category)
        with top_col2:
            st.success(status)

        st.markdown(f"**Business problem:** {problem}")
        st.markdown(f"**Operational outcome:** {outcome}")

        st.markdown("**Core capabilities:**")
        for feature in features:
            st.markdown(f"- {feature}")

        st.markdown(f"**Tech stack:** {tech}")

        col1, col2 = st.columns(2)
        with col1:
            safe_link_button("Launch Live Demo", live_url)
        with col2:
            safe_link_button("View GitHub Repo", github_url)


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("Practical AI Ops Toolkit")
st.sidebar.caption("Portfolio v2")

st.sidebar.markdown("""
**Built by Bradley Hankins**

Operations & Revenue Leader focused on practical AI workflow automation, RevOps, process improvement, and manager decision support.
""")

st.sidebar.divider()

st.sidebar.markdown("### Toolkit Focus")
st.sidebar.markdown("""
- Operations visibility
- Sales execution
- Recruiting workflows
- SOP documentation
- Manager reporting
- Decision support
""")

st.sidebar.divider()

safe_link_button("GitHub Profile", GITHUB_PROFILE)
safe_link_button("LinkedIn Profile", LINKEDIN_URL)

if RESUME_LINK.startswith("http"):
    safe_link_button("View Resume", RESUME_LINK)

# -----------------------------
# Header
# -----------------------------

st.title("🧠 Practical AI Ops Toolkit")
st.subheader("A portfolio of AI-assisted workflow tools for operations, sales execution, hiring, and process documentation.")

st.markdown("""
I build practical AI-assisted tools that help small and mid-sized businesses turn scattered data, notes,
and daily workflows into clearer decisions, stronger execution, and repeatable operating systems.

This toolkit is designed around real operating problems: managers need visibility, sales teams need follow-up discipline,
hiring teams need consistent screening, and growing businesses need better documentation.
""")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
metric_col1.metric("Portfolio Projects", "4")
metric_col2.metric("Primary Stack", "Python + Streamlit")
metric_col3.metric("Output Type", "Dashboards + Reports")
metric_col4.metric("Focus", "AI Operations")

st.divider()

# -----------------------------
# Positioning
# -----------------------------

st.header("What This Portfolio Demonstrates")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Business / Operations

    - KPI reporting and manager visibility
    - Sales follow-up and CRM workflow discipline
    - Candidate screening and hiring process support
    - SOP, checklist, and training document generation
    - Process improvement and accountability systems
    """)

with col2:
    st.markdown("""
    ### AI / Technical

    - Python and Streamlit app development
    - Rules-based AI-style workflow logic
    - Data-driven decision support
    - Downloadable Markdown reporting
    - GitHub documentation and live deployments
    """)

st.info(
    "Portfolio note: All sample data, company names, customer names, candidate names, and scenarios are fictional and created for public demonstration."
)

st.divider()

# -----------------------------
# Portfolio Story
# -----------------------------

st.header("Portfolio Story")

st.markdown("""
The Practical AI Ops Toolkit was built around four connected business problems:

1. **Managers need better visibility into performance.**
2. **Sales teams need more consistent follow-up and CRM discipline.**
3. **Small businesses need a more structured way to evaluate candidates.**
4. **Teams need clearer process documentation, training, and quality standards.**

Together, these tools show how lightweight AI-assisted workflows can improve day-to-day operations without requiring enterprise software.
""")

st.divider()

# -----------------------------
# Projects
# -----------------------------

st.header("Projects")

project_card(
    title="OpsPilot AI",
    category="Operations Intelligence Dashboard",
    status="Live",
    problem="Field-sales and home-service managers often have activity data but lack a clear action plan.",
    outcome="Turns activity data into KPIs, manager briefs, coaching priorities, and downloadable reports.",
    features=[
        "KPI dashboard",
        "Rep performance analysis",
        "Lead source analysis",
        "AI-style operations diagnosis",
        "Manager brief and weekly meeting agenda",
        "Downloadable manager report"
    ],
    tech="Python, Streamlit, Pandas, CSV workflow, Markdown report export",
    live_url=OPSPILOT_LIVE,
    github_url=OPSPILOT_GITHUB
)

project_card(
    title="FollowUpPilot AI",
    category="Sales Follow-Up Workflow Tool",
    status="Live",
    problem="Sales opportunities are often lost because follow-up is slow, inconsistent, or poorly documented.",
    outcome="Standardizes customer follow-up, CRM notes, objection handling, and multi-touch follow-up plans.",
    features=[
        "Follow-up priority score",
        "Customer text and email generator",
        "CRM-ready note and call script",
        "Objection guidance",
        "Manager coaching note",
        "Multi-touch follow-up sequence",
        "Downloadable follow-up plan"
    ],
    tech="Python, Streamlit, rules-based workflow logic, Markdown report export",
    live_url=FOLLOWUPPILOT_LIVE,
    github_url=FOLLOWUPPILOT_GITHUB
)

project_card(
    title="RecruitPilot AI",
    category="Candidate Screening Workflow Tool",
    status="Live",
    problem="Small businesses often hire from scattered notes, informal interviews, and inconsistent evaluation processes.",
    outcome="Creates structured candidate reviews, fit scores, risk levels, interview questions, and onboarding plans.",
    features=[
        "Candidate fit score",
        "Risk level and hiring recommendation",
        "Role success profile",
        "Green flags and red flags",
        "Follow-up interview questions",
        "Interview scorecard",
        "Candidate email and onboarding plan",
        "Downloadable candidate report"
    ],
    tech="Python, Streamlit, rules-based screening logic, Markdown report export",
    live_url=RECRUITPILOT_LIVE,
    github_url=RECRUITPILOT_GITHUB
)

project_card(
    title="SOPPilot AI",
    category="SOP & Training Document Generator",
    status="Live",
    problem="Small businesses often rely on tribal knowledge, verbal instructions, and inconsistent process documentation.",
    outcome="Turns rough process notes into SOPs, checklists, risk diagnoses, training plans, and implementation guides.",
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

# -----------------------------
# Toolkit Roadmap
# -----------------------------

st.header("Toolkit Roadmap")

roadmap_col1, roadmap_col2 = st.columns(2)

with roadmap_col1:
    st.markdown("""
    ### Near-Term Upgrades

    - Improve dashboards and charts
    - Add adjustable goal targets
    - Add richer export formats
    - Add stronger role-specific templates
    - Add project screenshots and case study refinements
    """)

with roadmap_col2:
    st.markdown("""
    ### Future Direction

    - Optional OpenAI API integrations
    - PDF export capability
    - Multi-record upload workflows
    - Team-level reporting
    - ClientOps Intake AI diagnostic app
    - Lightweight consulting assessment workflow
    """)

st.divider()

# -----------------------------
# Career / Consulting Positioning
# -----------------------------

st.header("Career / Consulting Positioning")

st.markdown("""
This portfolio supports a focused direction in:

**AI Operations + Workflow Automation + RevOps + Process Improvement**

The projects demonstrate how I approach business problems:

1. Identify a repeated operational pain point.
2. Map the workflow and decision logic.
3. Build a simple working tool.
4. Generate manager-ready outputs.
5. Document the project with a live demo and GitHub case study.

The result is a portfolio that shows both business operations experience and hands-on AI workflow implementation.
""")

st.divider()

# -----------------------------
# Connect
# -----------------------------

st.header("Connect")

connect_col1, connect_col2, connect_col3 = st.columns(3)

with connect_col1:
    safe_link_button("LinkedIn Profile", LINKEDIN_URL)

with connect_col2:
    safe_link_button("GitHub Profile", GITHUB_PROFILE)

with connect_col3:
    if RESUME_LINK.startswith("http"):
        safe_link_button("Resume", RESUME_LINK)
    else:
        st.button("Resume Link Pending", disabled=True)

st.success("Practical AI tools built to solve real operational problems.")
