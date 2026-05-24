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

PROJECTS = {
    "OpsPilot AI": {
        "category": "Operations Intelligence Dashboard",
        "problem": "Managers often have activity data but lack a clear action plan.",
        "outcome": "Turns sales activity into KPIs, coaching priorities, manager briefs, and downloadable reports.",
        "features": [
            "KPI dashboard",
            "Rep and lead source analysis",
            "AI-style operations diagnosis",
            "Manager brief and meeting agenda",
            "Downloadable manager report"
        ],
        "tech": "Python • Streamlit • Pandas • CSV workflow",
        "live": OPSPILOT_LIVE,
        "github": OPSPILOT_GITHUB,
        "best_for": "Operations, RevOps, performance visibility, manager reporting"
    },
    "FollowUpPilot AI": {
        "category": "Sales Follow-Up Workflow Tool",
        "problem": "Sales opportunities are lost when follow-up is slow or poorly documented.",
        "outcome": "Standardizes customer communication, CRM notes, objection handling, and follow-up sequences.",
        "features": [
            "Priority score",
            "Text and email generator",
            "CRM note and call script",
            "Objection guidance",
            "Multi-touch follow-up plan"
        ],
        "tech": "Python • Streamlit • Workflow logic • Markdown export",
        "live": FOLLOWUPPILOT_LIVE,
        "github": FOLLOWUPPILOT_GITHUB,
        "best_for": "Sales execution, CRM discipline, follow-up workflows"
    },
    "RecruitPilot AI": {
        "category": "Candidate Screening Workflow Tool",
        "problem": "Small businesses often hire from scattered notes and inconsistent interviews.",
        "outcome": "Creates structured candidate reviews, fit scores, risk levels, scorecards, and onboarding plans.",
        "features": [
            "Candidate fit score",
            "Risk level and recommendation",
            "Green and red flags",
            "Interview questions and scorecard",
            "Downloadable candidate report"
        ],
        "tech": "Python • Streamlit • Screening logic • Markdown export",
        "live": RECRUITPILOT_LIVE,
        "github": RECRUITPILOT_GITHUB,
        "best_for": "Hiring consistency, interview structure, onboarding preparation"
    },
    "SOPPilot AI": {
        "category": "SOP & Training Document Generator",
        "problem": "Teams rely on tribal knowledge, verbal instructions, and inconsistent documentation.",
        "outcome": "Turns rough process notes into SOPs, checklists, training plans, quality guides, and rollout plans.",
        "features": [
            "Complexity score",
            "Risk diagnosis",
            "Missing-info check",
            "SOP, checklist, and training plan",
            "Downloadable SOP package"
        ],
        "tech": "Python • Streamlit • Process logic • Markdown export",
        "live": SOPPILOT_LIVE,
        "github": SOPPILOT_GITHUB,
        "best_for": "Process documentation, training consistency, quality control"
    }
}

# -----------------------------
# Styling
# -----------------------------

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.35rem;
        padding-bottom: 3rem;
        max-width: 1120px;
    }

    [data-testid="stSidebar"] { background: #111827; }
    [data-testid="stSidebar"] * { color: #f9fafb !important; }

    .hero {
        padding: 2rem 2rem 1.8rem 2rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #111827 0%, #1f2937 52%, #334155 100%);
        color: #ffffff;
        box-shadow: 0 18px 36px rgba(17, 24, 39, 0.20);
        margin-bottom: 1rem;
        border: 1px solid rgba(255,255,255,.08);
    }

    .eyebrow {
        text-transform: uppercase;
        letter-spacing: .13em;
        font-size: .75rem;
        font-weight: 800;
        color: #93c5fd;
        margin-bottom: .65rem;
    }

    .hero-title {
        font-size: 2.35rem;
        line-height: 1.08;
        font-weight: 850;
        margin-bottom: .75rem;
        max-width: 850px;
    }

    .hero-subtitle {
        font-size: 1.02rem;
        line-height: 1.62;
        color: #e5e7eb;
        max-width: 900px;
        margin-bottom: 1rem;
    }

    .hero-pills span {
        display: inline-block;
        padding: .35rem .65rem;
        margin: .18rem .28rem .18rem 0;
        border-radius: 999px;
        background: rgba(255,255,255,.10);
        border: 1px solid rgba(255,255,255,.16);
        font-weight: 700;
        font-size: .78rem;
        color: #f8fafc;
    }

    .stat-card {
        padding: 1rem 1rem .95rem 1rem;
        border-radius: 16px;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        box-shadow: 0 7px 18px rgba(15, 23, 42, .06);
        min-height: 112px;
        margin-bottom: .75rem;
    }

    .stat-label {
        color: #6b7280;
        font-size: .82rem;
        font-weight: 750;
        text-transform: uppercase;
        letter-spacing: .05em;
        margin-bottom: .45rem;
    }

    .stat-value {
        color: #111827;
        font-size: 1.55rem;
        line-height: 1.18;
        font-weight: 850;
        white-space: normal;
        overflow-wrap: break-word;
    }

    .section-title {
        margin-top: 1.3rem;
        margin-bottom: .55rem;
        font-size: 1.45rem;
        font-weight: 850;
        color: #111827;
    }

    .section-lede {
        color: #4b5563;
        font-size: .98rem;
        line-height: 1.62;
        margin-bottom: 1rem;
        max-width: 950px;
    }

    .info-card, .roadmap-card, .spotlight-card, .link-card {
        padding: 1.2rem;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        background: #ffffff;
        box-shadow: 0 8px 20px rgba(15,23,42,.055);
    }

    .info-card { min-height: 215px; }
    .roadmap-card { min-height: 235px; }
    .spotlight-card { margin-bottom: .75rem; border-left: 5px solid #1d4ed8; }
    .link-card { min-height: 180px; border-top: 4px solid #111827; }

    .info-card h3, .roadmap-card h3, .spotlight-card h3, .link-card h3 {
        font-size: 1.05rem;
        font-weight: 850;
        color: #111827;
        margin-bottom: .5rem;
    }

    .info-card li, .roadmap-card li, .spotlight-card li {
        color: #4b5563;
        line-height: 1.48;
        font-size: .92rem;
        margin-bottom: .18rem;
    }

    .link-card p, .spotlight-card p {
        color: #4b5563;
        line-height: 1.55;
        font-size: .93rem;
    }

    .project-card {
        padding: 1.25rem;
        border: 1px solid #e5e7eb;
        border-radius: 20px;
        background: #ffffff;
        box-shadow: 0 10px 26px rgba(15,23,42,.07);
        min-height: 468px;
        margin-bottom: .65rem;
    }

    .project-topline {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: .75rem;
        margin-bottom: .45rem;
    }

    .project-title {
        font-size: 1.22rem;
        font-weight: 900;
        color: #111827;
        margin: 0;
    }

    .project-category {
        font-size: .8rem;
        color: #1d4ed8;
        font-weight: 800;
        margin-bottom: .65rem;
    }

    .status-pill {
        padding: .22rem .55rem;
        border-radius: 999px;
        font-size: .72rem;
        font-weight: 850;
        color: #065f46;
        background: #d1fae5;
        border: 1px solid #a7f3d0;
        white-space: nowrap;
    }

    .card-label {
        font-size: .7rem;
        text-transform: uppercase;
        letter-spacing: .08em;
        font-weight: 850;
        color: #6b7280;
        margin-top: .75rem;
        margin-bottom: .22rem;
    }

    .card-copy {
        color: #374151;
        line-height: 1.48;
        font-size: .9rem;
    }

    .feature-list {
        margin: .2rem 0 0 0;
        padding-left: 1.02rem;
        color: #374151;
        line-height: 1.42;
        font-size: .88rem;
    }

    .tech-line {
        margin-top: .8rem;
        padding: .62rem .72rem;
        border-radius: 12px;
        background: #f3f4f6;
        color: #1f2937;
        font-size: .82rem;
        font-weight: 760;
    }

    .note-box {
        padding: .9rem 1rem;
        border-radius: 14px;
        background: #f8fafc;
        color: #334155;
        border: 1px solid #e2e8f0;
        font-weight: 650;
        margin: .95rem 0;
        font-size: .92rem;
    }

    .final-cta {
        padding: 1.4rem;
        border-radius: 20px;
        background: #111827;
        color: white;
        margin-top: 1.25rem;
        text-align: center;
    }

    .final-cta h2 {
        color: white;
        margin-bottom: .3rem;
        font-size: 1.35rem;
    }

    .final-cta p {
        color: #d1d5db;
        margin-bottom: 0;
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


def stat_card(label, value):
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-label">{label}</div>
            <div class="stat-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


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


def practical_link_card(title, body, primary_label, primary_url):
    st.markdown(
        f"""
        <div class="link-card">
            <h3>{title}</h3>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    safe_link_button(primary_label, primary_url)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("Practical AI Ops Toolkit")
st.sidebar.caption("Executive Portfolio v2.3")
st.sidebar.markdown("""
**Bradley Hankins**  
Operations & Revenue Leader  
AI Workflow Automation  
RevOps & Process Improvement
""")
st.sidebar.divider()
st.sidebar.markdown("### Best starting points")
safe_link_button("View GitHub Profile", GITHUB_PROFILE)
safe_link_button("Connect on LinkedIn", LINKEDIN_URL)
if RESUME_LINK.startswith("http"):
    safe_link_button("View Resume", RESUME_LINK)
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

# -----------------------------
# Hero
# -----------------------------

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">AI Operations Portfolio</div>
        <div class="hero-title">Practical AI tools for operational execution.</div>
        <div class="hero-subtitle">
            A focused portfolio of AI-assisted workflow tools built to improve visibility, follow-up discipline,
            candidate screening, process documentation, manager reporting, and decision support for growing teams.
        </div>
        <div class="hero-pills">
            <span>Operations</span>
            <span>RevOps</span>
            <span>Workflow Automation</span>
            <span>Python</span>
            <span>Streamlit</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
with stat_col1:
    stat_card("Portfolio Projects", "4")
with stat_col2:
    stat_card("Primary Stack", "Python + Streamlit")
with stat_col3:
    stat_card("Outputs", "Dashboards + Reports")
with stat_col4:
    stat_card("Focus", "AI Operations")

# -----------------------------
# Practical next steps
# -----------------------------

st.markdown('<div class="section-title">Start here</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-lede">For hiring managers, recruiters, or consulting prospects, these are the fastest ways to evaluate the work.</div>',
    unsafe_allow_html=True
)

link_col1, link_col2, link_col3 = st.columns(3)
with link_col1:
    practical_link_card(
        "Review the full code portfolio",
        "See the repositories, README files, case studies, and project structure behind each deployed app.",
        "Open GitHub Profile",
        GITHUB_PROFILE
    )
with link_col2:
    practical_link_card(
        "Connect professionally",
        "View background, current positioning, and reach out regarding operations, AI workflow, or RevOps opportunities.",
        "Open LinkedIn Profile",
        LINKEDIN_URL
    )
with link_col3:
    practical_link_card(
        "Use the live tools",
        "Open any project below to test the working Streamlit applications directly in the browser.",
        "Jump to OpsPilot AI",
        OPSPILOT_LIVE
    )

# -----------------------------
# Overview
# -----------------------------

st.markdown('<div class="section-title">Executive summary</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-lede">This toolkit connects business operations experience with hands-on AI workflow implementation. Each project starts with a repeated operational pain point, maps the decision logic, and produces manager-ready outputs that can be used in the field.</div>',
    unsafe_allow_html=True
)

biz_col, tech_col = st.columns(2)
with biz_col:
    st.markdown(
        """
        <div class="info-card">
            <h3>Business Operations</h3>
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
            <h3>AI Workflow Implementation</h3>
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
    '<div class="note-box">Public demo note: all sample data, names, companies, and scenarios are fictional and created for portfolio demonstration.</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Project spotlight
# -----------------------------

st.markdown('<div class="section-title">Project spotlight</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-lede">Rather than using rotating cards that hide information, this selector lets visitors quickly focus on the project most relevant to them.</div>',
    unsafe_allow_html=True
)

selected_project = st.selectbox(
    "Choose a project to spotlight",
    list(PROJECTS.keys()),
    index=0
)
spotlight = PROJECTS[selected_project]
spotlight_features = "".join([f"<li>{feature}</li>" for feature in spotlight["features"]])
st.markdown(
    f"""
    <div class="spotlight-card">
        <h3>{selected_project}</h3>
        <p><strong>{spotlight['category']}</strong></p>
        <p><strong>Best for:</strong> {spotlight['best_for']}</p>
        <p><strong>Problem:</strong> {spotlight['problem']}</p>
        <p><strong>Outcome:</strong> {spotlight['outcome']}</p>
        <ul>{spotlight_features}</ul>
        <p><strong>Tech:</strong> {spotlight['tech']}</p>
    </div>
    """,
    unsafe_allow_html=True
)
spot_col1, spot_col2 = st.columns(2)
with spot_col1:
    safe_link_button(f"Launch {selected_project}", spotlight["live"])
with spot_col2:
    safe_link_button(f"View {selected_project} on GitHub", spotlight["github"])

# -----------------------------
# Story
# -----------------------------

st.markdown('<div class="section-title">Portfolio story</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-lede">
        The toolkit was built around four connected business problems: managers need performance visibility, sales teams need follow-up discipline,
        hiring teams need consistent screening, and growing teams need clearer process documentation. Together, the projects demonstrate a practical AI Ops approach without relying on enterprise software.
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Projects
# -----------------------------

st.markdown('<div class="section-title">Project portfolio</div>', unsafe_allow_html=True)

project_col1, project_col2 = st.columns(2)

with project_col1:
    p = PROJECTS["OpsPilot AI"]
    project_card("OpsPilot AI", p["category"], p["problem"], p["outcome"], p["features"], p["tech"], p["live"], p["github"])

with project_col2:
    p = PROJECTS["FollowUpPilot AI"]
    project_card("FollowUpPilot AI", p["category"], p["problem"], p["outcome"], p["features"], p["tech"], p["live"], p["github"])

project_col3, project_col4 = st.columns(2)

with project_col3:
    p = PROJECTS["RecruitPilot AI"]
    project_card("RecruitPilot AI", p["category"], p["problem"], p["outcome"], p["features"], p["tech"], p["live"], p["github"])

with project_col4:
    p = PROJECTS["SOPPilot AI"]
    project_card("SOPPilot AI", p["category"], p["problem"], p["outcome"], p["features"], p["tech"], p["live"], p["github"])

# -----------------------------
# Roadmap
# -----------------------------

st.markdown('<div class="section-title">Toolkit roadmap</div>', unsafe_allow_html=True)
roadmap_col1, roadmap_col2 = st.columns(2)

with roadmap_col1:
    st.markdown(
        """
        <div class="roadmap-card">
            <h3>Near-Term Upgrades</h3>
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
            <h3>Future Direction</h3>
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
        The projects show a repeatable approach: identify an operational pain point, map the workflow, build a working tool,
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
