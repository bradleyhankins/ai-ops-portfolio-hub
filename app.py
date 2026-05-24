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

# -----------------------------
# Styling
# -----------------------------

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1180px;
    }

    [data-testid="stSidebar"] {
        background: #0f172a;
    }

    [data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }

    .hero {
        padding: 2.25rem 2rem;
        border-radius: 28px;
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 52%, #2563eb 100%);
        color: white;
        box-shadow: 0 22px 48px rgba(15, 23, 42, 0.22);
        margin-bottom: 1.5rem;
    }

    .eyebrow {
        text-transform: uppercase;
        letter-spacing: .12em;
        font-size: .78rem;
        font-weight: 800;
        color: #bfdbfe;
        margin-bottom: .75rem;
    }

    .hero-title {
        font-size: 3.15rem;
        line-height: 1.03;
        font-weight: 900;
        margin-bottom: .8rem;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        line-height: 1.65;
        color: #e0f2fe;
        max-width: 920px;
        margin-bottom: 1.2rem;
    }

    .hero-pills span {
        display: inline-block;
        padding: .45rem .75rem;
        margin: .2rem .35rem .2rem 0;
        border-radius: 999px;
        background: rgba(255,255,255,.14);
        border: 1px solid rgba(255,255,255,.23);
        font-weight: 700;
        font-size: .88rem;
    }

    .section-title {
        margin-top: 1.25rem;
        margin-bottom: .65rem;
        font-size: 1.65rem;
        font-weight: 850;
        color: #0f172a;
    }

    .section-lede {
        color: #475569;
        font-size: 1.02rem;
        line-height: 1.6;
        margin-bottom: 1.15rem;
    }

    .info-card {
        padding: 1.35rem;
        border: 1px solid #e2e8f0;
        border-radius: 22px;
        background: #ffffff;
        box-shadow: 0 10px 24px rgba(15,23,42,.07);
        min-height: 220px;
    }

    .info-card h3 {
        font-size: 1.15rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: .55rem;
    }

    .info-card p, .info-card li {
        color: #475569;
        line-height: 1.5;
        font-size: .96rem;
    }

    .project-card {
        padding: 1.35rem;
        border: 1px solid #dbeafe;
        border-radius: 24px;
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        box-shadow: 0 12px 30px rgba(15,23,42,.08);
        min-height: 520px;
        margin-bottom: .85rem;
    }

    .project-topline {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        margin-bottom: .6rem;
    }

    .project-title {
        font-size: 1.35rem;
        font-weight: 900;
        color: #0f172a;
        margin: 0;
    }

    .project-category {
        font-size: .86rem;
        color: #2563eb;
        font-weight: 800;
        margin-bottom: .75rem;
    }

    .status-pill {
        padding: .25rem .6rem;
        border-radius: 999px;
        font-size: .78rem;
        font-weight: 850;
        color: #065f46;
        background: #d1fae5;
        border: 1px solid #a7f3d0;
        white-space: nowrap;
    }

    .card-label {
        font-size: .75rem;
        text-transform: uppercase;
        letter-spacing: .08em;
        font-weight: 850;
        color: #64748b;
        margin-top: .85rem;
        margin-bottom: .25rem;
    }

    .card-copy {
        color: #334155;
        line-height: 1.5;
        font-size: .95rem;
    }

    .feature-list {
        margin: .2rem 0 0 0;
        padding-left: 1.05rem;
        color: #334155;
        line-height: 1.45;
        font-size: .92rem;
    }

    .tech-line {
        margin-top: .9rem;
        padding: .7rem .8rem;
        border-radius: 14px;
        background: #eff6ff;
        color: #1e3a8a;
        font-size: .88rem;
        font-weight: 700;
    }

    .roadmap-card {
        padding: 1.2rem;
        border-radius: 20px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        min-height: 260px;
    }

    .note-box {
        padding: 1rem 1.1rem;
        border-radius: 18px;
        background: #ecfeff;
        color: #164e63;
        border: 1px solid #a5f3fc;
        font-weight: 650;
        margin: 1rem 0;
    }

    .final-cta {
        padding: 1.7rem;
        border-radius: 26px;
        background: #0f172a;
        color: white;
        margin-top: 1.4rem;
        text-align: center;
    }

    .final-cta h2 {
        color: white;
        margin-bottom: .35rem;
    }

    .final-cta p {
        color: #cbd5e1;
        margin-bottom: 0;
    }

    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 1rem;
        border-radius: 18px;
        box-shadow: 0 8px 18px rgba(15,23,42,.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Helpers
# -----------------------------

def safe_link_button(label, url):
    if isinstance(url, str) and url.startswith("http"):
        st.link_button(label, url, use_container_width=True)
    else:
        st.button(label + " Pending", disabled=True, use_container_width=True)


def project_card(title, category, problem, outcome, features, tech, live_url, github_url):
    feature_html = "".join([f"<li>{feature}</li>" for feature in features])
    st.markdown(
        f"""
        <div class="project-card">
            <div class="project-topline">
                <h3 class="project-title">{title}</h3>
                <span class="status-pill">Live</span>
            </div>
            <div class="project-category">{category}</div>
            <div class="card-label">Business Problem</div>
            <div class="card-copy">{problem}</div>
            <div class="card-label">Operational Outcome</div>
            <div class="card-copy">{outcome}</div>
            <div class="card-label">Core Capabilities</div>
            <ul class="feature-list">{feature_html}</ul>
            <div class="tech-line">{tech}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)
    with col1:
        safe_link_button("Live Demo", live_url)
    with col2:
        safe_link_button("GitHub", github_url)


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("Practical AI Ops Toolkit")
st.sidebar.caption("Portfolio v2.1")
st.sidebar.markdown("""
**Bradley Hankins**  
Operations & Revenue Leader  
AI Workflow Automation  
RevOps & Process Improvement
""")
st.sidebar.divider()
st.sidebar.markdown("### Toolkit Focus")
st.sidebar.markdown("""
- Operations visibility
- Sales execution
- Recruiting workflows
- Process documentation
- Manager reporting
- Decision support
""")
st.sidebar.divider()
safe_link_button("GitHub Profile", GITHUB_PROFILE)
safe_link_button("LinkedIn Profile", LINKEDIN_URL)
if RESUME_LINK.startswith("http"):
    safe_link_button("Resume", RESUME_LINK)

# -----------------------------
# Hero
# -----------------------------

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">AI Operations Portfolio</div>
        <div class="hero-title">Practical AI tools for real business operations.</div>
        <div class="hero-subtitle">
            A connected portfolio of AI-assisted workflow tools built to improve operations visibility,
            sales follow-up, candidate screening, SOP documentation, manager reporting, and decision support
            for small and mid-sized businesses.
        </div>
        <div class="hero-pills">
            <span>Python</span>
            <span>Streamlit</span>
            <span>Workflow Automation</span>
            <span>RevOps</span>
            <span>Manager Reporting</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
metric_col1.metric("Portfolio Projects", "4")
metric_col2.metric("Primary Stack", "Python + Streamlit")
metric_col3.metric("Outputs", "Dashboards + Reports")
metric_col4.metric("Focus", "AI Operations")

# -----------------------------
# Overview
# -----------------------------

st.markdown('<div class="section-title">What this portfolio demonstrates</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-lede">This toolkit connects business operations experience with hands-on AI workflow implementation. Each app starts with a real operational pain point, maps the decision logic, and produces manager-ready outputs.</div>',
    unsafe_allow_html=True
)

biz_col, tech_col = st.columns(2)
with biz_col:
    st.markdown(
        """
        <div class="info-card">
            <h3>Business / Operations</h3>
            <ul>
                <li>KPI reporting and manager visibility</li>
                <li>Sales follow-up and CRM discipline</li>
                <li>Candidate screening and hiring support</li>
                <li>SOP, checklist, and training generation</li>
                <li>Process improvement and accountability systems</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
with tech_col:
    st.markdown(
        """
        <div class="info-card">
            <h3>AI / Technical</h3>
            <ul>
                <li>Python and Streamlit app development</li>
                <li>Rules-based AI-style workflow logic</li>
                <li>Data-driven decision support</li>
                <li>Downloadable Markdown reporting</li>
                <li>GitHub documentation and live deployments</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="note-box">All sample data, names, companies, and scenarios are fictional and created for public portfolio demonstration.</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Story
# -----------------------------

st.markdown('<div class="section-title">Portfolio story</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-lede">
        The toolkit was built around four connected business problems: managers need visibility, sales teams need follow-up discipline,
        hiring teams need consistent screening, and growing teams need clearer process documentation. Together, these projects show
        how lightweight AI-assisted workflows can improve day-to-day operations without enterprise software.
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Projects
# -----------------------------

st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

project_col1, project_col2 = st.columns(2)

with project_col1:
    project_card(
        title="OpsPilot AI",
        category="Operations Intelligence Dashboard",
        problem="Managers often have activity data but lack a clear action plan.",
        outcome="Turns sales activity into KPIs, coaching priorities, manager briefs, and downloadable reports.",
        features=[
            "KPI dashboard",
            "Rep and lead source analysis",
            "AI-style operations diagnosis",
            "Manager brief and meeting agenda",
            "Downloadable manager report"
        ],
        tech="Python • Streamlit • Pandas • CSV workflow",
        live_url=OPSPILOT_LIVE,
        github_url=OPSPILOT_GITHUB
    )

with project_col2:
    project_card(
        title="FollowUpPilot AI",
        category="Sales Follow-Up Workflow Tool",
        problem="Sales opportunities are lost when follow-up is slow or poorly documented.",
        outcome="Standardizes customer communication, CRM notes, objection handling, and follow-up sequences.",
        features=[
            "Priority score",
            "Text and email generator",
            "CRM note and call script",
            "Objection guidance",
            "Multi-touch follow-up plan"
        ],
        tech="Python • Streamlit • Workflow logic • Markdown export",
        live_url=FOLLOWUPPILOT_LIVE,
        github_url=FOLLOWUPPILOT_GITHUB
    )

project_col3, project_col4 = st.columns(2)

with project_col3:
    project_card(
        title="RecruitPilot AI",
        category="Candidate Screening Workflow Tool",
        problem="Small businesses often hire from scattered notes and inconsistent interviews.",
        outcome="Creates structured candidate reviews, fit scores, risk levels, scorecards, and onboarding plans.",
        features=[
            "Candidate fit score",
            "Risk level and recommendation",
            "Green and red flags",
            "Interview questions and scorecard",
            "Downloadable candidate report"
        ],
        tech="Python • Streamlit • Screening logic • Markdown export",
        live_url=RECRUITPILOT_LIVE,
        github_url=RECRUITPILOT_GITHUB
    )

with project_col4:
    project_card(
        title="SOPPilot AI",
        category="SOP & Training Document Generator",
        problem="Teams rely on tribal knowledge, verbal instructions, and inconsistent documentation.",
        outcome="Turns rough process notes into SOPs, checklists, training plans, quality guides, and rollout plans.",
        features=[
            "Complexity score",
            "Risk diagnosis",
            "Missing-info check",
            "SOP, checklist, and training plan",
            "Downloadable SOP package"
        ],
        tech="Python • Streamlit • Process logic • Markdown export",
        live_url=SOPPILOT_LIVE,
        github_url=SOPPILOT_GITHUB
    )

# -----------------------------
# Roadmap
# -----------------------------

st.markdown('<div class="section-title">Toolkit roadmap</div>', unsafe_allow_html=True)
roadmap_col1, roadmap_col2 = st.columns(2)

with roadmap_col1:
    st.markdown(
        """
        <div class="roadmap-card">
            <h3>Near-term upgrades</h3>
            <ul>
                <li>Improve dashboards and charts</li>
                <li>Add adjustable goal targets</li>
                <li>Add richer export formats</li>
                <li>Add stronger role-specific templates</li>
                <li>Refine screenshots and case studies</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with roadmap_col2:
    st.markdown(
        """
        <div class="roadmap-card">
            <h3>Future direction</h3>
            <ul>
                <li>Optional OpenAI API integrations</li>
                <li>PDF export capability</li>
                <li>Multi-record upload workflows</li>
                <li>Team-level reporting</li>
                <li>ClientOps Intake AI diagnostic app</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Positioning + Connect
# -----------------------------

st.markdown('<div class="section-title">Career / consulting positioning</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-lede">
        This portfolio supports a focused direction in <strong>AI Operations, Workflow Automation, RevOps, and Process Improvement</strong>.
        The projects show a repeatable approach: identify an operational pain point, map the workflow, build a simple tool,
        generate manager-ready outputs, and document the work through live demos and GitHub case studies.
    </div>
    """,
    unsafe_allow_html=True
)

connect_col1, connect_col2, connect_col3 = st.columns(3)
with connect_col1:
    safe_link_button("LinkedIn Profile", LINKEDIN_URL)
with connect_col2:
    safe_link_button("GitHub Profile", GITHUB_PROFILE)
with connect_col3:
    if RESUME_LINK.startswith("http"):
        safe_link_button("Resume", RESUME_LINK)
    else:
        st.button("Resume Link Pending", disabled=True, use_container_width=True)

st.markdown(
    """
    <div class="final-cta">
        <h2>Practical AI tools built to solve real operational problems.</h2>
        <p>Operations visibility. Sales execution. Hiring consistency. Process documentation.</p>
    </div>
    """,
    unsafe_allow_html=True
)
