import streamlit as st
import joblib
import numpy as np

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Predictions",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# LOAD MODEL
# =====================================

model = joblib.load(
    "../Streamlit_App/models/spending_model.pkl"
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
PREDICTION CARD
========================= */

.prediction-card {

    background:
    rgba(15,23,42,0.72);

    border:
    1px solid rgba(255,255,255,0.06);

    border-radius: 28px;

    padding: 35px;

    backdrop-filter: blur(18px);

    margin-top: 20px;
}

/* =========================
INPUTS
========================= */

label {

    color: #cbd5e1 !important;

    font-weight: 600 !important;
}

/* =========================
SLIDER
========================= */

.stSlider {

    padding-top: 10px;
    padding-bottom: 10px;
}

/* =========================
BUTTON
========================= */

.stButton button {

    width: 100%;

    margin-top: 25px;

    background:
    linear-gradient(
        90deg,
        #8b5cf6,
        #06b6d4
    );

    color: white;

    border: none;

    border-radius: 16px;

    padding: 16px;

    font-size: 18px;

    font-weight: 600;

    transition: 0.35s ease;
}

.stButton button:hover {

    transform: translateY(-3px);

    box-shadow:
    0 0 30px rgba(139,92,246,0.30);
}

/* =========================
RESULT CARD
========================= */

.result-card {

    background:
    rgba(15,23,42,0.78);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius: 30px;

    padding: 40px;

    margin-top: 35px;

    text-align: center;

    backdrop-filter: blur(20px);

    animation: fadeUp 0.6s ease;
}

/* =========================
RESULT TITLE
========================= */

.result-title {

    font-size: 24px;

    color: #cbd5e1;

    margin-bottom: 20px;
}

/* =========================
RESULT VALUE
========================= */

.result-value {

    font-size: 58px;

    font-weight: 800;

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
ANIMATION
========================= */

@keyframes fadeUp {

    from {

        opacity: 0;
        transform: translateY(20px);
    }

    to {

        opacity: 1;
        transform: translateY(0px);
    }
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
    Customer <span class="gradient">Predictions</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-subtitle">
    AI-Powered Customer Spending Prediction System
</div>
""", unsafe_allow_html=True)

# =====================================
# PREDICTION SECTION
# =====================================


col1, col2, col3 = st.columns(3)

with col1:

    age = st.slider(
        "Customer Age",
        18,
        80,
        30
    )

with col2:

    purchases = st.slider(
        "Total Purchases",
        1,
        20,
        5
    )

with col3:

    rating = st.slider(
        "Customer Rating",
        1.0,
        5.0,
        3.5
    )

predict_button = st.button(
    "🚀 Predict Customer Spending"
)

st.markdown("""
</div>
""", unsafe_allow_html=True)

# =====================================
# PREDICTION
# =====================================

if predict_button:

    input_data = np.array([
        [age, purchases, rating]
    ])

    prediction = model.predict(input_data)[0]

    st.components.v1.html(f"""
    <div class="result-card">

        <div class="result-title">
            Predicted Customer Spending
        </div>

        <div class="result-value">
            ₹{prediction:,.2f}
        </div>
    </div>

<style>

.result-card {{

    background:
    rgba(15,23,42,0.78);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius: 30px;

    padding: 40px;

    margin-top: 35px;

    text-align: center;

    backdrop-filter: blur(20px);

    animation: fadeUp 0.6s ease;
}}

.result-title {{

    font-size: 24px;

    color: #cbd5e1;

    margin-bottom: 20px;

    font-family: Poppins;
}}

.result-value {{

    font-size: 58px;

    font-weight: 800;

    font-family: Poppins;

    background:
    linear-gradient(
        90deg,
        #06b6d4,
        #8b5cf6,
        #ec4899
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}}

body {{
    margin: 0;
    background: transparent;
}}

</style>
""", height=250)

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