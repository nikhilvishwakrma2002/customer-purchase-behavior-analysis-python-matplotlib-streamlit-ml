import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🧠",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

rfm = pd.read_csv(
    "../Dataset/rfm_customer_segments.csv"
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

    font-size: 60px;

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

    margin-bottom: 35px;
}

/* =========================
FILTER PANEL
========================= */

.filter-panel {

    background:
    rgba(15,23,42,0.72);

    padding: 25px;

    border-radius: 24px;

    border:
    1px solid rgba(255,255,255,0.06);

    backdrop-filter: blur(18px);

    margin-bottom: 30px;
}

/* =========================
FILTER INPUTS
========================= */

.stMultiSelect {

    background:
    rgba(15,23,42,0.82);

    border-radius: 16px;

    padding: 8px;

    border:
    1px solid rgba(255,255,255,0.06);
}

label {

    color: #cbd5e1 !important;

    font-weight: 600 !important;
}

div[data-baseweb="select"] {

    background:
    rgba(15,23,42,0.82);

    border-radius: 14px;
}

/* =========================
KPI CARD
========================= */

.kpi-card {

    background:
    rgba(15,23,42,0.75);

    border:
    1px solid rgba(255,255,255,0.06);

    border-radius: 24px;

    padding: 28px;

    backdrop-filter: blur(18px);

    transition: 0.35s ease;

    text-align: center;
}

.kpi-card:hover {

    transform: translateY(-6px);

    box-shadow:
    0 0 35px rgba(139,92,246,0.18);
}

.kpi-title {

    color: #94a3b8;

    font-size: 16px;

    margin-bottom: 10px;
}

.kpi-value {

    color: white;

    font-size: 36px;

    font-weight: 700;
}

/* =========================
CHART CARD
========================= */

.chart-card {

    background:
    rgba(15,23,42,0.72);

    border:
    1px solid rgba(255,255,255,0.06);

    border-radius: 28px;

    padding: 20px;

    margin-top: 25px;

    backdrop-filter: blur(18px);
}

/* =========================
CHART TITLE
========================= */

.chart-title {

    font-size: 28px;

    font-weight: 700;

    color: white;

    margin-bottom: 18px;

    padding-left: 10px;
}

/* =========================
DATAFRAME
========================= */

[data-testid="stDataFrame"] {

    background:
    rgba(15,23,42,0.72);

    border-radius: 20px;

    padding: 10px;

    border:
    1px solid rgba(255,255,255,0.06);
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

st.markdown("""
<div class="page-title">
    Customer <span class="gradient">Segmentation</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-subtitle">
    AI-Powered Customer Intelligence & RFM Analytics
</div>
""", unsafe_allow_html=True)

# =====================================
# FILTER PANEL
# =====================================

st.markdown("""
<div class="filter-panel">
    <h3 style="color:white;">
        🔍 Cluster Filters
    </h3>
</div>
""", unsafe_allow_html=True)

cluster_filter = st.multiselect(
    "Select Customer Cluster",
    options=sorted(rfm['Cluster'].unique()),
    default=sorted(rfm['Cluster'].unique())
)

filtered_rfm = rfm[
    rfm['Cluster'].isin(cluster_filter)
]

# =====================================
# KPI SECTION
# =====================================

total_customers = filtered_rfm.shape[0]

average_monetary = filtered_rfm['Monetary'].mean()

average_frequency = filtered_rfm['Frequency'].mean()

average_recency = filtered_rfm['Recency'].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Customers</div>
        <div class="kpi-value">{total_customers:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Avg Monetary</div>
        <div class="kpi-value">₹{average_monetary:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Avg Frequency</div>
        <div class="kpi-value">{average_frequency:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Avg Recency</div>
        <div class="kpi-value">{average_recency:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================
# CLUSTER DISTRIBUTION
# =====================================

cluster_counts = (
    filtered_rfm['Cluster']
    .value_counts()
    .reset_index()
)

cluster_counts.columns = [
    'Cluster',
    'Customers'
]

fig1 = px.pie(
    cluster_counts,
    values='Customers',
    names='Cluster',
    hole=0.55,
    template='plotly_dark'
)

fig1.update_layout(
    title=None,
    height=450,
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white')
)

st.markdown("""
<div class="chart-card">
    <div class="chart-title">
        🥧 Customer Cluster Distribution
    </div>
</div>
""", unsafe_allow_html=True)

st.plotly_chart(fig1, use_container_width=True)

# =====================================
# SEGMENTATION SCATTER
# =====================================

fig2 = px.scatter(
    filtered_rfm,
    x='Frequency',
    y='Monetary',
    color=filtered_rfm['Cluster'].astype(str),
    size='Recency',
    hover_data=['Recency'],
    template='plotly_dark'
)

fig2.update_layout(
    title=None,
    height=650,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white')
)

st.markdown("""
<div class="chart-card">
    <div class="chart-title">
        🧠 Customer Segmentation Analysis
    </div>
</div>
""", unsafe_allow_html=True)

st.plotly_chart(fig2, use_container_width=True)

# =====================================
# CLUSTER MONETARY ANALYSIS
# =====================================

cluster_summary = (
    filtered_rfm.groupby('Cluster')[
        ['Recency', 'Frequency', 'Monetary']
    ]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    cluster_summary,
    x='Cluster',
    y='Monetary',
    color='Cluster',
    template='plotly_dark'
)

fig3.update_layout(
    title=None,
    height=450,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white')
)

st.markdown("""
<div class="chart-card">
    <div class="chart-title">
        📊 Average Monetary Value by Cluster
    </div>
</div>
""", unsafe_allow_html=True)

st.plotly_chart(fig3, use_container_width=True)

# =====================================
# RAW DATA
# =====================================

st.markdown("""
<div class="chart-card">
    <div class="chart-title">
        📋 Customer Segmentation Data
    </div>
</div>
""", unsafe_allow_html=True)

st.dataframe(
    filtered_rfm,
    use_container_width=True
)

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