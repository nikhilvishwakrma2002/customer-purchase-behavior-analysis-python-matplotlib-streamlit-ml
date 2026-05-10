import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="About Project",
    page_icon="🚀",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

/* =========================
GOOGLE FONT
========================= */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* =========================
HIDE STREAMLIT UI
========================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* =========================
APP BACKGROUND
========================= */

.stApp {

    background:
    linear-gradient(
        135deg,
        #020617 0%,
        #071129 30%,
        #0f172a 60%,
        #1e1b4b 100%
    );

    color: white;
}

/* =========================
MAIN CONTAINER
========================= */

.block-container {

    padding-top: 1.5rem;
    padding-left: 2rem;
    padding-right: 2rem;
    padding-bottom: 2rem;

    max-width: 100%;
}

/* =========================
TITLE
========================= */

.page-title {

    font-size: 64px;

    font-weight: 800;

    color: white;

    margin-bottom: 10px;
}

/* =========================
GRADIENT TEXT
========================= */

.gradient {

    background:
    linear-gradient(
        90deg,
        #06b6d4,
        #8b5cf6,
        #ec4899
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

/* =========================
SUBTITLE
========================= */

.page-subtitle {

    color: #cbd5e1;

    font-size: 20px;

    margin-bottom: 45px;
}

/* =========================
SECTION CARD
========================= */

.section-card {

    background:
    rgba(15,23,42,0.72);

    border:
    1px solid rgba(255,255,255,0.06);

    border-radius: 28px;

    padding: 35px;

    margin-bottom: 30px;

    backdrop-filter: blur(18px);

    transition: 0.35s ease;
}

.section-card:hover {

    transform: translateY(-5px);

    box-shadow:
    0 0 35px rgba(139,92,246,0.18);
}

/* =========================
SECTION TITLE
========================= */

.section-title {

    font-size: 32px;

    font-weight: 700;

    color: white;

    margin-bottom: 20px;
}

/* =========================
SECTION TEXT
========================= */

.section-text {

    color: #cbd5e1;

    font-size: 18px;

    line-height: 2;
}

/* =========================
TECH GRID
========================= */

.tech-grid {

    display: grid;

    grid-template-columns:
    repeat(auto-fit, minmax(220px, 1fr));

    gap: 20px;

    margin-top: 25px;
}

.tech-card {

    background:
    rgba(255,255,255,0.04);

    border:
    1px solid rgba(255,255,255,0.06);

    border-radius: 22px;

    padding: 25px;

    text-align: center;
}

.tech-title {

    color: white;

    font-size: 22px;

    font-weight: 700;

    margin-top: 10px;
}

.tech-text {

    color: #cbd5e1;

    margin-top: 12px;

    font-size: 16px;

    line-height: 1.7;
}

/* =========================
FOOTER
========================= */

.footer {

    text-align: center;

    color: #94a3b8;

    margin-top: 60px;

    padding-bottom: 20px;

    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# PAGE TITLE
# =====================================

st.html("""
<div class="page-title">
    About <span class="gradient">CPBA Project</span>
</div>
""")

st.html("""
<div class="page-subtitle">
    Customer Purchase Behavior Analyzer • AI-Powered Analytics Platform
</div>
""")

# =====================================
# PROJECT OVERVIEW
# =====================================

st.html("""
<div class="section-card">

    <div class="section-title">
        🚀 Project Overview
    </div>

    <div class="section-text">

        Customer Purchase Behavior Analyzer (CPBA)
        is an advanced AI-powered analytics platform
        developed to analyze customer purchasing patterns,
        business trends, customer intelligence,
        and predictive analytics.

        <br><br>

        The platform transforms raw customer transaction
        data into meaningful business insights using
        interactive dashboards and machine learning.

        <br><br>

        It provides customer segmentation,
        executive dashboards, spending predictions,
        AI-driven recommendations,
        and business intelligence analytics.

    </div>

</div>
""")

# =====================================
# MY JOURNEY
# =====================================

st.html("""
<div class="section-card">

    <div class="section-title">
        🌟 My Journey Through This Project
    </div>

    <div class="section-text">

        This project started with a vision to create
        a professional enterprise-level analytics system
        combining Data Analytics, Machine Learning,
        Interactive Visualization, and Modern UI Design.

        <br><br>

        During development, multiple challenges were faced,
        including dashboard optimization,
        machine learning integration,
        UI engineering, visualization handling,
        and real-time analytics design.

        <br><br>

        The project evolved from a simple dashboard
        into a complete AI-powered analytics ecosystem.

        <br><br>

        Every page was carefully designed
        to provide a seamless analytics experience
        with modern glassmorphism aesthetics.

        <br><br>

        This project significantly improved skills in:

        <br><br>

        • Data Analytics
        <br>
        • Data Visualization
        <br>
        • Machine Learning
        <br>
        • Business Intelligence
        <br>
        • Dashboard Engineering
        <br>
        • Streamlit Development
        <br>
        • UI/UX Design
        <br>
        • Problem Solving

    </div>

</div>
""")

# =====================================
# FEATURES
# =====================================

st.html("""
<div class="section-card">

    <div class="section-title">
        ⚡ Core Features
    </div>

    <div class="section-text">

        • Executive Analytics Dashboard

        <br><br>

        • Revenue Trend Analysis

        <br><br>

        • Interactive KPI Monitoring

        <br><br>

        • Customer Segmentation Analytics

        <br><br>

        • RFM Intelligence System

        <br><br>

        • Spending Prediction System

        <br><br>

        • AI-Driven Business Insights

        <br><br>

        • Downloadable Reports

        <br><br>

        • Modern Interactive UI

    </div>

</div>
""")

# =====================================
# TECH STACK
# =====================================

st.html("""
<div class="section-card">

    <div class="section-title">
        🛠️ Technology Stack
    </div>

    <div class="tech-grid">

        <div class="tech-card">
            <div class="tech-title">🐍 Python</div>
            <div class="tech-text">
                Core backend programming language.
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-title">📊 Pandas</div>
            <div class="tech-text">
                Data cleaning and analysis.
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-title">📈 Plotly</div>
            <div class="tech-text">
                Interactive visualizations.
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-title">🤖 Scikit-Learn</div>
            <div class="tech-text">
                Machine learning models.
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-title">⚡ Streamlit</div>
            <div class="tech-text">
                Dashboard framework.
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-title">🎨 CSS</div>
            <div class="tech-text">
                Custom modern UI styling.
            </div>
        </div>

    </div>

</div>
""")

# =====================================
# OBJECTIVE
# =====================================

st.html("""
<div class="section-card">

    <div class="section-title">
        🎯 Project Objective
    </div>

    <div class="section-text">

        The primary objective of CPBA
        is to help businesses understand
        customer purchasing behavior
        using analytics and artificial intelligence.

        <br><br>

        By analyzing customer data,
        businesses can:

        <br><br>

        • Improve customer targeting
        <br>
        • Increase revenue growth
        <br>
        • Improve customer retention
        <br>
        • Optimize inventory
        <br>
        • Predict future spending
        <br>
        • Enhance business decisions

    </div>

</div>
""")

# =====================================
# DEVELOPER
# =====================================

st.html("""
<div class="section-card">

    <div class="section-title">
        👨‍💻 Developer Information
    </div>

    <div class="section-text">

        Developed By:
        <span class="gradient">
            <b>Nikhil Kumar Vishwakrma</b>
        </span>

        <br><br>

        BCA (Data Science & AI)

        <br><br>

        Passionate about
        Artificial Intelligence,
        Data Analytics,
        Machine Learning,
        and Interactive Dashboard Development.

        <br><br>

        This project reflects
        enterprise-level analytics engineering
        combined with modern UI development.

    </div>

</div>
""")

# =====================================
# FOOTER
# =====================================

st.html("""
<div class="footer">

    Built with Streamlit • Plotly • Machine Learning

    <br><br>

    Developed By
    <span class="gradient">
        Nikhil Kumar Vishwakrma
        <br>
        <a href="mailto:nikhilvishwakrma2002@gmail.com">Email</a>
    </span>

</div>
""")