import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Water Purity Check", layout="wide")

# --- AESTHETIC GREEN THEME ---
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%); }
h1 { color: #1B5E20 !important; text-align: center; font-size: 42px !important; }
.main-card {
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}
.stButton > button {
    background: linear-gradient(90deg, #2E7D32, #66BB6A) !important;
    color: white !important;
    font-size: 20px !important;
    font-weight: bold !important;
    padding: 12px 50px !important;
    border-radius: 30px !important;
    border: none !important;
    display: block;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)

st.title("💧 Water Purity Check")
st.markdown("<p style='text-align:center; color:#388E3C; font-size:18px;'>Check if your water is safe to drink • Made by Anum</p>", unsafe_allow_html=True)
st.write("")

# Load Model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# --- ROW 1 - 5 in 1 row ---
st.markdown("<div class='main-card'>", unsafe_allow_html=True)
st.markdown("### 🧪  Water Chemistry")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    ph = st.slider("pH Level", 0.0, 14.0, 7.0)
with col2:
    hardness = st.slider("Hardness", 0.0, 350.0, 150.0)
with col3:
    solids = st.slider("Solids", 0.0, 60000.0, 20000.0)
with col4:
    chloramines = st.slider("Chloramines", 0.0, 15.0, 7.0)
with col5:
    sulfate = st.slider("Sulfate", 0.0, 500.0, 250.0)
st.markdown("</div>", unsafe_allow_html=True)

# --- ROW 2 - 3 in 1 row ---
st.markdown("<div class='main-card'>", unsafe_allow_html=True)
st.markdown("### ⚡  Water Quality")
col6, col7, col8 = st.columns(3)
with col6:
    conductivity = st.slider("Conductivity", 0.0, 800.0, 400.0)
with col7:
    organic_carbon = st.slider("Organic Carbon", 0.0, 30.0, 15.0)
with col8:
    trihalomethanes = st.slider("Trihalomethanes", 0.0, 130.0, 60.0)
st.markdown("</div>", unsafe_allow_html=True)

# --- ROW 3 - Last 1 ---
st.markdown("<div class='main-card'>", unsafe_allow_html=True)
st.markdown("### 👀  Clarity")
turbidity = st.slider("Turbidity", 0.0, 10.0, 4.0)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
if st.button("✨ Predict Purity"):
    data = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    result = model.predict(data)
    prob = model.predict_proba(data)[0][1] * 100
    st.markdown(f"<div class='main-card'><h2 style='text-align:center; color:#1B5E20;'>Purity Probability: {prob:.2f}%</h2></div>", unsafe_allow_html=True)
    if result[0] == 1:
        st.success("✅ Water is Drinkable - Safe to Drink!")
        st.balloons()
    else:
        st.error("❌ Water is Not Drinkable - Please Purify It!")