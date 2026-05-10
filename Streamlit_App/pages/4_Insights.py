import streamlit as st
import pandas as pd

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Business Insights",
    page_icon="📈",
    layout="wide"
)

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    "../Dataset/cleaned_customer_purchase_data.csv"
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

    margin-bottom: 40px;
}

/* =========================
INSIGHT CARD
========================= */

.insight-card {

    background:
    rgba(15,23,42,0.72);

    border:
    1px solid rgba(255,255,255,0.06);

    border-radius: 28px;

    padding: 30px;

    margin-bottom: 28px;

    backdrop-filter: blur(18px);

    transition: 0.35s ease;
}

.insight-card:hover {

    transform: translateY(-5px);

    box-shadow:
    0 0 35px rgba(139,92,246,0.18);
}

/* =========================
CARD TITLE
========================= */

.insight-title {

    font-size: 28px;

    font-weight: 700;

    color: white;

    margin-bottom: 18px;
}

/* =========================
CARD TEXT
========================= */

.insight-text {

    color: #cbd5e1;

    font-size: 18px;

    line-height: 1.9;
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
    Business <span class="gradient">Insights</span>
</div>
""")

st.html("""
<div class="page-subtitle">
    AI-Driven Strategic Customer Intelligence & Analytics
</div>
""")

# =====================================
# GENERATE INSIGHTS
# =====================================

top_category = (
    df.groupby('Product_Category')['Total_Amount']
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

top_brand = (
    df.groupby('Product_Brand')['Total_Amount']
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

top_country = (
    df.groupby('Country')['Total_Amount']
    .sum()
    .sort_values(ascending=False)
    .index[0]
)

average_rating = df['Ratings'].mean()

# =====================================
# PRODUCT INTELLIGENCE
# =====================================

st.html(f"""
<div class="insight-card">

    <div class="insight-title">
        🛍️ Product Intelligence
    </div>

    <div class="insight-text">

        The highest revenue-generating product category is
        <span class="gradient"><b>{top_category}</b></span>.

        <br><br>

        This indicates strong customer demand and purchasing
        behavior within this segment. Strategic inventory
        optimization and targeted marketing campaigns can
        further improve sales performance.

    </div>

</div>
""")

# =====================================
# BRAND PERFORMANCE
# =====================================

st.html(f"""
<div class="insight-card">

    <div class="insight-title">
        🏆 Brand Performance
    </div>

    <div class="insight-text">

        <span class="gradient"><b>{top_brand}</b></span>
        is currently the best-performing product brand
        based on total customer spending.

        <br><br>

        Expanding collaborations, promotions, and visibility
        for this brand could significantly improve
        overall revenue generation.

    </div>

</div>
""")

# =====================================
# GEOGRAPHIC ANALYSIS
# =====================================

st.html(f"""
<div class="insight-card">

    <div class="insight-title">
        🌍 Geographic Analysis
    </div>

    <div class="insight-text">

        Customers from
        <span class="gradient"><b>{top_country}</b></span>
        contribute the highest share of revenue.

        <br><br>

        This region represents a high-value customer market
        and should be prioritized for business expansion,
        retention campaigns, and targeted personalization.

    </div>

</div>
""")

# =====================================
# CUSTOMER SATISFACTION
# =====================================

st.html(f"""
<div class="insight-card">

    <div class="insight-title">
        ⭐ Customer Satisfaction
    </div>

    <div class="insight-text">

        The average customer rating is
        <span class="gradient"><b>{average_rating:.2f}</b></span>.

        <br><br>

        Improving customer experience, delivery efficiency,
        personalization, and after-sales service can further
        strengthen customer loyalty and retention.

    </div>

</div>
""")

# =====================================
# STRATEGIC RECOMMENDATIONS
# =====================================

st.html("""
<div class="insight-card">

    <div class="insight-title">
        🚀 Strategic Recommendations
    </div>

    <div class="insight-text">

        • Focus on high-performing customer segments

        <br><br>

        • Increase marketing investment for premium categories

        <br><br>

        • Implement AI-powered recommendation systems

        <br><br>

        • Improve customer retention strategies

        <br><br>

        • Expand operations in high-performing regions

        <br><br>

        • Optimize inventory using demand forecasting analytics

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