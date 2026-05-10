import streamlit as st
from streamlit_option_menu import option_menu

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="CPBA Analytics Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

/* =========================
HIDE STREAMLIT DEFAULT UI
========================= */

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none;
}

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
GOOGLE FONT
========================= */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* =========================
MAIN APP
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
    padding-left: 3rem;
    padding-right: 3rem;
    padding-bottom: 2rem;

    max-width: 100%;
}

/* =========================
NAVBAR
========================= */

ul {
    gap: 12px !important;
}

.nav-link {

    min-width: 180px !important;

    background: rgba(15,23,42,0.78) !important;

    border: 1px solid rgba(255,255,255,0.05);

    border-radius: 16px !important;

    transition: 0.35s ease !important;
}

.nav-link:hover {

    transform: translateY(-4px);

    border: 1px solid rgba(255,255,255,0.12);

    box-shadow:
        0 0 25px rgba(139,92,246,0.20);
}

/* =========================
HERO TITLE
========================= */

.hero-title {

    text-align: center;

    font-size: 92px;

    font-weight: 800;

    line-height: 1.05;

    margin-top: 55px;

    color: white;

    animation: fadeUp 1s ease;

    text-shadow:
        0 0 25px rgba(139,92,246,0.20),
        0 0 60px rgba(6,182,212,0.10);
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

.hero-subtitle {

    text-align: center;

    font-size: 25px;

    color: #cbd5e1;

    margin-top: 20px;

    margin-bottom: 70px;

    animation: fadeUp 1.2s ease;
}

/* =========================
ANIMATION
========================= */

@keyframes fadeUp {

    from {

        opacity: 0;
        transform: translateY(30px);
    }

    to {

        opacity: 1;
        transform: translateY(0px);
    }
}

/* =========================
CARDS
========================= */

.card {

    background: rgba(15,23,42,0.70);

    border: 1px solid rgba(255,255,255,0.06);

    border-radius: 28px;

    padding: 40px;

    min-height: 260px;

    margin-bottom: 30px;

    backdrop-filter: blur(18px);

    transition: all 0.4s ease;

    overflow: hidden;

    position: relative;
}

/* =========================
CARD HOVER
========================= */

.card:hover {

    transform: translateY(-10px);

    border: 1px solid rgba(255,255,255,0.12);

    box-shadow:
        0 0 40px rgba(139,92,246,0.18),
        0 0 80px rgba(6,182,212,0.08);
}

/* =========================
CARD SHINE EFFECT
========================= */

.card::before {

    content: "";

    position: absolute;

    top: -50%;
    left: -50%;

    width: 200%;
    height: 200%;

    background:
    linear-gradient(
        45deg,
        transparent,
        rgba(255,255,255,0.03),
        transparent
    );

    transform: rotate(25deg);

    transition: 0.9s;
}

.card:hover::before {

    left: 100%;
}

/* =========================
CARD TITLE
========================= */

.card-title {

    font-size: 34px;

    font-weight: 700;

    color: white;

    margin-bottom: 22px;
}

/* =========================
CARD TEXT
========================= */

.card-text {

    color: #cbd5e1;

    font-size: 19px;

    line-height: 1.9;
}

/* =========================
FOOTER
========================= */

.footer {

    text-align: center;

    color: #94a3b8;

    margin-top: 30px;

    padding-bottom: 20px;

    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# NAVIGATION BAR
# =====================================

selected = option_menu(

    menu_title=None,

    options=[
        "Home",
        "Dashboard",
        "Segmentation",
        "Predictions",
        "Insights",
        "About"
    ],

    icons=[
        "house",
        "bar-chart",
        "diagram-3",
        "cpu",
        "lightbulb",
        "person-circle"
    ],

    orientation="horizontal",

    default_index=0,

    styles={

        "container": {

            "padding": "0!important",

            "background-color": "transparent",

            "border": "none",

            "margin-bottom": "25px"
        },

        "icon": {

            "color": "#8b5cf6",

            "font-size": "20px"
        },

        "nav-link": {

            "font-size": "20px",

            "font-weight": "600",

            "text-align": "center",

            "padding": "18px 22px",

            "color": "#e2e8f0"
        },

        "nav-link-selected": {

            "background":
            "linear-gradient(90deg,#8b5cf6,#06b6d4)",

            "color": "white",

            "box-shadow":
            "0 0 30px rgba(139,92,246,0.35)"
        }
    }
)

# =====================================
# PAGE ROUTING
# =====================================

if selected == "Dashboard":
    st.switch_page("pages/1_Dashboard.py")

elif selected == "Segmentation":
    st.switch_page("pages/2_Customer_Segmentation.py")

elif selected == "Predictions":
    st.switch_page("pages/3_Predictions.py")

elif selected == "Insights":
    st.switch_page("pages/4_Insights.py")
elif selected == "About":
    st.switch_page("pages/5_About.py")

# =====================================
# HERO SECTION
# =====================================

st.html("""
<div class="hero-title">
    Customer Purchase
    <span class="gradient">Behavior Analyzer</span>
</div>
""")

st.html("""
<div class="hero-subtitle">
    AI-Powered Interactive Customer Analytics Platform
</div>
""")

# =====================================
# FIRST ROW
# =====================================

col1, col2 = st.columns(2)

with col1:

    st.html("""
    <div class="card">

        <div class="card-title">
            📈 Advanced Analytics
        </div>

        <div class="card-text">
            Analyze customer purchasing behavior,
            revenue growth, sales trends,
            and product performance
            using interactive dashboards.
        </div>

    </div>
    """)

with col2:

    st.html("""
    <div class="card">

        <div class="card-title">
            🧠 Machine Learning
        </div>

        <div class="card-text">
            Perform customer segmentation
            using K-Means clustering,
            RFM analysis,
            and predictive analytics.
        </div>

    </div>
    """)

# =====================================
# SECOND ROW
# =====================================

col3, col4 = st.columns(2)

with col3:

    st.html("""
    <div class="card">

        <div class="card-title">
            📊 Interactive Dashboard
        </div>

        <div class="card-text">
            Dynamic KPI cards,
            filters,
            downloadable reports,
            and advanced visualizations.
        </div>

    </div>
    """)

with col4:

    st.html("""
    <div class="card">

        <div class="card-title">
            🚀 Business Intelligence
        </div>

        <div class="card-text">
            Generate strategic insights,
            customer intelligence,
            and AI-driven business recommendations.
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