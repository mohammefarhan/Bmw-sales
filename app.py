import streamlit as st
import pandas as pd
import joblib

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="BMW Sales Predictor",
    page_icon="🚗",
    layout="wide"
)

# -------------------------
# LOAD MODEL + DATA
# -------------------------
model = joblib.load("bmw_sales_model.pkl")
model_columns = joblib.load("model_columns.pkl")

df = pd.read_csv("bmw_global_sales_dataset.csv")

country_list = sorted(df['country'].unique())
segment_list = sorted(df['segment'].unique())
engine_list = sorted(df['engine_type'].unique())

# -------------------------
# SIDEBAR
# -------------------------
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg", width=120)
    st.markdown("### BMW ML Dashboard")
    st.caption("Developed by Farhan")
    st.divider()
    st.success("Model R² Score: 0.747")

# -------------------------
# PREMIUM CSS
# -------------------------
st.markdown("""
<style>
.header-container {
    background: linear-gradient(135deg,#020617,#1e3a8a);
    padding:35px;
    border-radius:18px;
    text-align:center;
    color:white;
    margin-bottom:20px;
}
.glow-title {
    font-size:42px;
    font-weight:800;
}
.prediction-box {
    background:#020617;
    padding:28px;
    border-radius:14px;
    text-align:center;
    font-size:30px;
    color:white;
    box-shadow:0 0 20px rgba(59,130,246,0.3);
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown("""
<div class="header-container">
<img src="https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg" width="80">
<div class="glow-title">BMW Sales Prediction Dashboard</div>
<p>Machine Learning Powered Automotive Analytics</p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# INPUT SECTION
# -------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Vehicle Metrics")
    price = st.number_input("Price (USD)", value=50000)
    marketing = st.number_input("Marketing Spend", value=10000)
    dealership = st.number_input("Dealership Count", value=50)
    competition = st.number_input("Competition Index", value=5)

with col2:
    st.subheader("⚙️ Configuration")
    country = st.selectbox("Country", country_list)
    segment = st.selectbox("Segment", segment_list)
    engine = st.selectbox("Engine Type", engine_list)

    filtered_models = sorted(df[df["segment"] == segment]["model"].unique())
    model_name = st.selectbox("BMW Model", filtered_models)

st.divider()

# -------------------------
# CREATE INPUT DATA
# -------------------------
input_data = pd.DataFrame({
    "price_usd":[price],
    "marketing_spend_usd":[marketing],
    "dealership_count":[dealership],
    "competition_index":[competition],
    "country":[country],
    "segment":[segment],
    "engine_type":[engine],
    "model":[model_name]
})

input_data = pd.get_dummies(input_data)
input_data = input_data.reindex(columns=model_columns, fill_value=0)

# -------------------------
# PREDICTION
# -------------------------
if st.button("🚀 Predict Units Sold", use_container_width=True):

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
        <div class="prediction-box">
        📈 Predicted Units Sold <br><br>
        <b>{int(prediction)}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------
# FOOTER
# -------------------------
st.markdown(
"<center style='color:gray;margin-top:40px;'>Developed by Farhan | BMW ML Dashboard</center>",
unsafe_allow_html=True
)