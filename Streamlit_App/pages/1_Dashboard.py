import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    "../Dataset/cleaned_customer_purchase_data.csv"
)

df['Date'] = pd.to_datetime(df['Date'])

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

.dashboard-title {

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

.dashboard-subtitle {

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

.stDateInput,
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

    font-size: 38px;

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
DOWNLOAD BUTTON
========================= */

.stDownloadButton button {

    width: 100%;

    margin-top: 20px;

    background:
    linear-gradient(
        90deg,
        #8b5cf6,
        #06b6d4
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 14px;

    font-size: 16px;

    font-weight: 600;
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
<div class="dashboard-title">
    Executive <span class="gradient">Dashboard</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="dashboard-subtitle">
    AI-Powered Customer Purchase Analytics Platform
</div>
""", unsafe_allow_html=True)

# =====================================
# FILTER PANEL
# =====================================

st.markdown("""
<div class="filter-panel">
    <h3 style="color:white;">
        🔍 Analytics Filters
    </h3>
</div>
""", unsafe_allow_html=True)

f1, f2, f3, f4 = st.columns(4)

with f1:

    date_range = st.date_input(
        "Date Range",
        value=(
            df['Date'].min(),
            df['Date'].max()
        )
    )

with f2:

    country_filter = st.multiselect(
        "Country",
        options=sorted(df['Country'].unique()),
        default=sorted(df['Country'].unique())
    )

with f3:

    gender_filter = st.multiselect(
        "Gender",
        options=sorted(df['Gender'].unique()),
        default=sorted(df['Gender'].unique())
    )

with f4:

    category_filter = st.multiselect(
        "Category",
        options=sorted(df['Product_Category'].unique()),
        default=sorted(df['Product_Category'].unique())
    )

# =====================================
# FILTER DATA
# =====================================

filtered_df = df[
    (df['Country'].isin(country_filter)) &
    (df['Gender'].isin(gender_filter)) &
    (df['Product_Category'].isin(category_filter))
]

filtered_df = filtered_df[
    (filtered_df['Date'] >= pd.to_datetime(date_range[0])) &
    (filtered_df['Date'] <= pd.to_datetime(date_range[1]))
]

# =====================================
# KPI SECTION
# =====================================

total_revenue = filtered_df['Total_Amount'].sum()
total_customers = filtered_df['Customer_ID'].nunique()
total_orders = filtered_df['Transaction_ID'].nunique()
average_rating = filtered_df['Ratings'].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Revenue</div>
        <div class="kpi-value">₹{total_revenue:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Customers</div>
        <div class="kpi-value">{total_customers:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Orders</div>
        <div class="kpi-value">{total_orders:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Average Rating</div>
        <div class="kpi-value">{average_rating:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================
# MONTHLY SALES TREND
# =====================================

filtered_df['Month_Year'] = (
    filtered_df['Date']
    .dt.to_period('M')
    .astype(str)
)

monthly_sales = (
    filtered_df.groupby('Month_Year')['Total_Amount']
    .sum()
    .reset_index()
)

fig1 = px.line(
    monthly_sales,
    x='Month_Year',
    y='Total_Amount',
    markers=True,
    template='plotly_dark'
)

fig1.update_layout(
    title=None,
    height=450,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    margin=dict(l=20, r=20, t=20, b=20)
)

st.markdown("""
<div class="chart-card">
    <div class="chart-title">
        📈 Monthly Revenue Trend
    </div>
</div>
""", unsafe_allow_html=True)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# SECOND ROW
# =====================================

col5, col6 = st.columns(2)

# CATEGORY CHART

with col5:

    category_sales = (
        filtered_df.groupby('Product_Category')['Total_Amount']
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        category_sales,
        values='Total_Amount',
        names='Product_Category',
        hole=0.55,
        template='plotly_dark'
    )

    fig2.update_layout(
        title=None,
        height=450,
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )

    st.markdown("""
    <div class="chart-card">
    <div class="chart-title">
        📈 Monthly Revenue Trend
    </div>
        </div>
    """, unsafe_allow_html=True)

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# GENDER CHART

with col6:

    gender_sales = (
        filtered_df.groupby('Gender')['Total_Amount']
        .sum()
        .reset_index()
    )

    fig3 = px.bar(
        gender_sales,
        x='Gender',
        y='Total_Amount',
        color='Gender',
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
        📈 Monthly Revenue Trend
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# TOP BRANDS
# =====================================

top_brands = (
    filtered_df.groupby('Product_Brand')['Total_Amount']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig4 = px.bar(
    x=top_brands.values,
    y=top_brands.index,
    orientation='h',
    template='plotly_dark'
)

fig4.update_layout(
    title=None,
    height=500,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white')
)

st.markdown("""
<div class="chart-card">
    <div class="chart-title">
        📈 Monthly Revenue Trend
    </div>
</div>
""", unsafe_allow_html=True)

st.plotly_chart(fig4, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# DOWNLOAD BUTTON
# =====================================

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Report",
    data=csv,
    file_name="cpba_filtered_report.csv",
    mime="text/csv"
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