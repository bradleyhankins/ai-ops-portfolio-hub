import streamlit as st

st.set_page_config(page_title="Practical AI Ops Toolkit", page_icon="🧠", layout="wide")

LINKEDIN_URL = "https://www.linkedin.com/in/bradleyhankins/"
GITHUB_PROFILE = "https://github.com/bradleyhankins"

PROJECTS = {
    "OpsPilot AI": {
        "category": "Operations Intelligence",
        "summary": "KPI visibility, rep insights, lead source analysis, manager briefs, meeting agendas, and downloadable reports.",
        "features": ["KPI Dashboard", "Rep Analysis", "Lead Sources", "Manager Brief", "Reports"],
        "tech": "Python • Streamlit • Pandas • CSV workflow",
        "live": "https://opspilot-ai.streamlit.app/",
        "github": "https://github.com/bradleyhankins/opspilot-ai",
        "best_for": "Operations, RevOps, performance visibility, manager reporting",
    },
    "FollowUpPilot AI": {
        "category": "Sales Follow-Up Workflow",
        "summary": "Next-best actions, lead temperature, deal risk, text/email/voicemail scripts, CRM notes, and follow-up plans.",
        "features": ["Next Best Action", "Lead Temperature", "Deal Risk", "Voicemail", "Follow-Up Plan"],
        "tech": "Python • Streamlit • Workflow logic • Markdown export",
        "live": "https://followuppilot-ai.streamlit.app/",
        "github": "https://github.com/bradleyhankins/followuppilot-ai",
        "best_for": "Sales execution, CRM discipline, follow-up workflows",
    },
    "RecruitPilot AI": {
        "category": "ATS Lite Resume Review",
        "summary": "Human-review resume organization with review priorities, match signals, missing information, questions, and packets.",
        "features": ["Resume Input", "Review Priority", "Match Signals", "Questions", "Review Packet"],
        "tech": "Python • Streamlit • Keyword logic • Markdown export",
        "live": "https://recruitpilot-ai.streamlit.app/",
        "github": "https://github.com/bradleyhankins/recruitpilot-ai",
        "best_for": "ATS Lite workflows, resume review organization, interview preparation",
    },
    "SOPPilot AI": {
        "category": "Process Documentation",
        "summary": "SOPs, checklists, training plans, risk checks, quality controls, rollout guidance, and documentation packages.",
        "features": ["SOP Builder", "Checklists", "Training", "Risk Checks", "SOP Package"],
        "tech": "Python • Streamlit • Process logic • Markdown export",
        "live": "https://soppilot-ai.streamlit.app/",
        "github": "https://github.com/bradleyhankins/soppilot-ai",
        "best_for": "Process documentation, training consistency, quality control",
    },
}

CSS = """
<style>
.block-container{max-width:1180px;padding-top:1.35rem;padding-bottom:3rem}
[data-testid="stSidebar"]{background:#111827}
[data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3,[data-testid="stSidebar"] p,[data-testid="stSidebar"] li,[data-testid="stSidebar"] span,[data-testid="stSidebar"] label{color:#f9fafb!important}
[data-testid="stSidebar"] li::marker{color:#93c5fd!important}
.sidebar-link{display:block;width:100%;margin:.45rem 0;padding:.78rem .95rem;border-radius:12px;background:#f9fafb;color:#111827!important;border:1px solid #e5e7eb;font-weight:850;text-align:center;text-decoration:none!important;box-shadow:0 6px 16px rgba(0,0,0,.18);transition:all .15s ease-in-out}
.sidebar-link:hover{background:#dbeafe;border-color:#93c5fd;color:#0f172a!important;transform:translateY(-1px)}
.hero{padding:2rem 2rem 1.8rem;border-radius:20px;background:linear-gradient(135deg,#111827 0%,#1f2937 52%,#334155 100%);color:#fff;box-shadow:0 18px 36px rgba(17,24,39,.20);margin-bottom:1rem;border:1px solid rgba(255,255,255,.08)}
.eyebrow{text-transform:uppercase;letter-spacing:.13em;font-size:.75rem;font-weight:800;color:#93c5fd;margin-bottom:.65rem}
.hero-title{font-size:2.35rem;line-height:1.08;font-weight:850;margin-bottom:.75rem;max-width:850px}
.hero-subtitle{font-size:1.02rem;line-height:1.62;color:#e5e7eb;max-width:900px;margin-bottom:1rem}
.hero-pills span{display:inline-block;padding:.35rem .65rem;margin:.18rem .28rem .18rem 0;border-radius:999px;background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.16);font-weight:700;font-size:.78rem;color:#f8fafc}
.stat-card,.info-card,.roadmap-card,.spotlight-card,.link-card,.usecase-card,.available-card,.project-card{background:#fff;border:1px solid #e5e7eb;box-shadow:0 8px 20px rgba(15,23,42,.055)}
.stat-card{height:142px;padding:1rem;border-radius:16px;margin-bottom:.75rem}.stat-label{color:#6b7280;font-size:.82rem;font-weight:750;text-transform:uppercase;letter-spacing:.05em;margin-bottom:.6rem}.stat-value{color:#111827;font-size:1.48rem;line-height:1.18;font-weight:850;overflow-wrap:break-word}
.section-title{margin-top:1.3rem;margin-bottom:.55rem;font-size:1.45rem;font-weight:850;color:#111827}.section-lede{color:#4b5563;font-size:.98rem;line-height:1.62;margin-bottom:1rem;max-width:950px}
.info-card,.roadmap-card,.spotlight-card,.link-card,.usecase-card,.available-card{padding:1.2rem;border-radius:18px}.info-card{min-height:215px}.roadmap-card{min-height:235px}.spotlight-card{margin-bottom:.75rem;border-left:5px solid #1d4ed8}.link-card{min-height:180px;border-top:4px solid #111827}.usecase-card{min-height:150px;border-left:4px solid #1d4ed8;margin-bottom:.75rem}.available-card{border-top:4px solid #111827}
.info-card h3,.roadmap-card h3,.spotlight-card h3,.link-card h3,.usecase-card h3,.available-card h3{font-size:1.05rem;font-weight:850;color:#111827;margin-bottom:.5rem}.info-card li,.roadmap-card li,.spotlight-card li,.available-card li{color:#4b5563;line-height:1.48;font-size:.92rem;margin-bottom:.18rem}.link-card p,.spotlight-card p,.usecase-card p{color:#4b5563;line-height:1.55;font-size:.93rem}.usecase-card strong{color:#111827}
.project-card{height:315px;margin-bottom:.65rem;padding:1.2rem;border-radius:20px;box-shadow:0 10px 26px rgba(15,23,42,.07);display:flex;flex-direction:column}
.project-topline{display:flex;align-items:flex-start;justify-content:space-between;gap:.75rem;margin-bottom:.35rem}.project-title{font-size:1.34rem;font-weight:900;color:#111827;margin:0}.project-category{font-size:.82rem;color:#1d4ed8;font-weight:850;margin-bottom:.8rem}.status-pill{padding:.22rem .55rem;border-radius:999px;font-size:.72rem;font-weight:850;color:#065f46;background:#d1fae5;border:1px solid #a7f3d0;white-space:nowrap}
.card-copy{color:#374151;line-height:1.48;font-size:.94rem;margin-bottom:.75rem}.feature-wrap{margin-top:.1rem}.feature-chip{display:inline-block;padding:.28rem .52rem;margin:.16rem .16rem .16rem 0;border-radius:999px;background:#f1f5f9;color:#1f2937;border:1px solid #e2e8f0;font-size:.74rem;font-weight:750}.tech-line{margin-top:auto;padding:.62rem .72rem;border-radius:12px;background:#f3f4f6;color:#1f2937;font-size:.82rem;font-weight:760}
.note-box{padding:.9rem 1rem;border-radius:14px;background:#f8fafc;color:#334155;border:1px solid #e2e8f0;font-weight:650;margin:.95rem 0;font-size:.92rem}.final-cta{padding:1.4rem;border-radius:20px;background:#111827;color:white;margin-top:1.25rem;text-align:center}.final-cta h2{color:white;margin-bottom:.3rem;font-size:1.35rem}.final-cta p{color:#d1d5db;margin-bottom:0}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def link_button(label: str, url: str) -> None:
    st.link_button(label, url, use_container_width=True)


def sidebar_link(label: str, url: str) -> None:
    st.markdown(f'<a class="sidebar-link" href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>', unsafe_allow_html=True)


def stat_card(label: str, value: str) -> None:
    st.markdown(f'<div class="stat-card"><div class="stat-label">{label}</div><div class="stat-value">{value}</div></div>', unsafe_allow_html=True)


def project_card(name: str, project: dict) -> None:
    feature_html = "".join(f"<span class='feature-chip'>{feature}</span>" for feature in project["features"])
    st.markdown(
        f"""
        <div class="project-card">
            <div class="project-topline"><h3 class="project-title">{name}</h3><span class="status-pill">Live</span></div>
            <div class="project-category">{project['category']}</div>
            <div class="card-copy">{project['summary']}</div>
            <div class="feature-wrap">{feature_html}</div>
            <div class="tech-line">{project['tech']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        link_button("Live Demo", project["live"])
    with col2:
        link_button("GitHub", project["github"])


def card(title: str, body: str, css_class: str = "link-card") -> None:
    st.markdown(f'<div class="{css_class}"><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)


def usecase_card(need: str, project: str, result: str) -> None:
    st.markdown(f'<div class="usecase-card"><h3>{need}</h3><p><strong>{project}</strong></p><p>{result}</p></div>', unsafe_allow_html=True)


with st.sidebar:
    st.title("Practical AI Ops Toolkit")
    st.caption("Executive Portfolio")
    st.markdown("""**Bradley Hankins**  
Operations & Revenue Leader  
AI Workflow Automation  
RevOps & Process Improvement""")
    st.divider()
    st.markdown("### Toolkit Focus")
    st.markdown("- Operations visibility\n- Sales execution\n- ATS Lite workflows\n- Process documentation\n- Manager reporting\n- Decision support")
    st.divider()
    st.markdown("### Connect")
    sidebar_link("GitHub Profile", GITHUB_PROFILE)
    sidebar_link("LinkedIn Profile", LINKEDIN_URL)

st.markdown("""
<div class="hero">
    <div class="eyebrow">AI Operations Portfolio</div>
    <div class="hero-title">Practical AI tools for operational execution.</div>
    <div class="hero-subtitle">A focused portfolio of AI-assisted workflow tools built to improve visibility, follow-up discipline, applicant review organization, process documentation, manager reporting, and decision support for growing teams.</div>
    <div class="hero-pills"><span>Operations</span><span>RevOps</span><span>Workflow Automation</span><span>Python</span><span>Streamlit</span></div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1: stat_card("Portfolio Projects", "4")
with c2: stat_card("Primary Stack", "Python + Streamlit")
with c3: stat_card("Outputs", "Dashboards + Reports")
with c4: stat_card("Focus", "AI Operations")

st.markdown('<div class="section-title">Start here</div>', unsafe_allow_html=True)
st.markdown('<div class="section-lede">For hiring managers, recruiters, or consulting prospects, these are the fastest ways to evaluate the work.</div>', unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)
with s1:
    card("Review the full code portfolio", "See the repositories, README files, case studies, and project structure behind each deployed app.")
    link_button("Open GitHub Profile", GITHUB_PROFILE)
with s2:
    card("Connect professionally", "View background, current positioning, and reach out regarding operations, AI workflow, or RevOps opportunities.")
    link_button("Open LinkedIn Profile", LINKEDIN_URL)
with s3:
    card("Use the live tools", "Test the working Streamlit apps directly in the browser. Start with the project most relevant to your business problem.")
    link_button("Open OpsPilot AI", PROJECTS["OpsPilot AI"]["live"])

st.markdown('<div class="section-title">Best project by use case</div>', unsafe_allow_html=True)
st.markdown('<div class="section-lede">Each tool solves a different operating problem. This section helps visitors quickly find the most relevant project.</div>', unsafe_allow_html=True)

u1, u2 = st.columns(2)
with u1:
    usecase_card("Need performance visibility?", "OpsPilot AI", "Review KPIs, rep performance, lead source quality, and manager action items.")
    usecase_card("Need applicant review organization?", "RecruitPilot AI", "Organize job descriptions and resume text into review priorities, match signals, and follow-up questions for human review.")
with u2:
    usecase_card("Need stronger follow-up?", "FollowUpPilot AI", "Generate next-best actions, customer communication, CRM notes, deal-risk context, and multi-touch follow-up plans.")
    usecase_card("Need process documentation?", "SOPPilot AI", "Convert rough process notes into SOPs, checklists, training plans, quality controls, and rollout guidance.")

st.markdown('<div class="section-title">Executive summary</div>', unsafe_allow_html=True)
st.markdown('<div class="section-lede">This toolkit connects business operations experience with hands-on AI workflow implementation. Each project starts with a repeated operational pain point, maps the workflow, and produces manager-ready outputs that can be used in the field.</div>', unsafe_allow_html=True)

x1, x2 = st.columns(2)
with x1:
    st.markdown('<div class="info-card"><h3>Business Operations</h3><ul><li>KPI reporting and manager visibility</li><li>Sales follow-up and CRM discipline</li><li>ATS Lite applicant review organization</li><li>SOP, checklist, and training generation</li><li>Process improvement and accountability systems</li></ul></div>', unsafe_allow_html=True)
with x2:
    st.markdown('<div class="info-card"><h3>AI Workflow Implementation</h3><ul><li>Python and Streamlit app development</li><li>Rules-based AI-style workflow logic</li><li>Data-driven decision support</li><li>Downloadable Markdown reporting</li><li>GitHub documentation and live deployments</li></ul></div>', unsafe_allow_html=True)

st.markdown('<div class="note-box">Public demo note: all sample data, names, companies, and scenarios are fictional and created for portfolio demonstration.</div>', unsafe_allow_html=True)
st.markdown('<div class="note-box">Responsible AI note: RecruitPilot AI is designed to organize applicant information for human review. It should not be used as the sole basis for selection, rejection, compensation, or employment decisions.</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Project spotlight</div>', unsafe_allow_html=True)
st.markdown('<div class="section-lede">This selector lets visitors quickly focus on the project most relevant to them.</div>', unsafe_allow_html=True)
selected_project = st.selectbox("Choose a project to spotlight", list(PROJECTS.keys()), index=0)
spotlight = PROJECTS[selected_project]
spotlight_features = "".join(f"<li>{feature}</li>" for feature in spotlight["features"])
st.markdown(f"""
<div class="spotlight-card">
    <h3>{selected_project}</h3>
    <p><strong>{spotlight['category']}</strong></p>
    <p><strong>Best for:</strong> {spotlight['best_for']}</p>
    <p><strong>Summary:</strong> {spotlight['summary']}</p>
    <ul>{spotlight_features}</ul>
    <p><strong>Tech:</strong> {spotlight['tech']}</p>
</div>
""", unsafe_allow_html=True)
sp1, sp2 = st.columns(2)
with sp1: link_button(f"Launch {selected_project}", spotlight["live"])
with sp2: link_button(f"View {selected_project} on GitHub", spotlight["github"])

st.markdown('<div class="section-title">Portfolio story</div>', unsafe_allow_html=True)
st.markdown('<div class="section-lede">The toolkit was built around four connected business problems: managers need performance visibility, sales teams need follow-up discipline, growing teams need structured applicant review, and organizations need clearer process documentation.</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Project portfolio</div>', unsafe_allow_html=True)
p1, p2 = st.columns(2)
with p1: project_card("OpsPilot AI", PROJECTS["OpsPilot AI"])
with p2: project_card("FollowUpPilot AI", PROJECTS["FollowUpPilot AI"])
p3, p4 = st.columns(2)
with p3: project_card("RecruitPilot AI", PROJECTS["RecruitPilot AI"])
with p4: project_card("SOPPilot AI", PROJECTS["SOPPilot AI"])

st.markdown('<div class="section-title">Toolkit roadmap</div>', unsafe_allow_html=True)
r1, r2 = st.columns(2)
with r1:
    st.markdown('<div class="roadmap-card"><h3>Near-Term Upgrades</h3><ul><li>Refresh screenshots across all repos</li><li>Add richer export formats</li><li>Add stronger role-specific templates</li><li>Refine case studies</li><li>Explore PDF export options</li></ul></div>', unsafe_allow_html=True)
with r2:
    st.markdown('<div class="roadmap-card"><h3>Future Direction</h3><ul><li>Optional OpenAI API integrations</li><li>Multi-record upload workflows</li><li>Team-level reporting</li><li>ClientOps Intake AI diagnostic app</li><li>Packaged small-business workflow toolkit</li></ul></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Career / consulting positioning</div>', unsafe_allow_html=True)
st.markdown('<div class="section-lede">This portfolio supports a focused direction in <strong>AI Operations, Workflow Automation, RevOps, and Process Improvement</strong>. The projects show a repeatable approach: identify an operational pain point, map the workflow, build a working tool, generate manager-ready outputs, and document the work through live demos and GitHub case studies.</div>', unsafe_allow_html=True)
st.markdown('<div class="available-card"><h3>Available for</h3><ul><li>Operations leadership roles</li><li>Revenue operations roles</li><li>AI workflow automation roles</li><li>Process improvement roles</li><li>Small-business AI consulting projects</li></ul></div>', unsafe_allow_html=True)

ct1, ct2 = st.columns(2)
with ct1: link_button("LinkedIn Profile", LINKEDIN_URL)
with ct2: link_button("GitHub Profile", GITHUB_PROFILE)

st.markdown('<div class="final-cta"><h2>Practical AI tools built to solve real operational problems.</h2><p>Operations visibility. Sales execution. Applicant review organization. Process documentation.</p></div>', unsafe_allow_html=True)
