import streamlit as st
from utils.data_pipeline import load_fraud_data, load_social_data
from modules.fraud_engine import render_fraud_dashboard
from modules.social_engine import render_social_dashboard

st.set_page_config(page_title="Enterprise Analytics", layout="wide", page_icon="📈")

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0a1128 0%, #162244 100%); color: #e0e6f0; }
    .metric-card {
        background: rgba(20, 30, 60, 0.6);
        border: 1px solid rgba(0, 255, 180, 0.2);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    .metric-value { font-size: 28px; font-weight: 800; color: #00ffb4; }
    .metric-label { font-size: 14px; color: #9aa8c0; text-transform: uppercase; letter-spacing: 1px; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🏢 Navigation")
selection = st.sidebar.radio("Go to", ["Fraud Detection Engine", "Social Media Analytics"])

st.sidebar.info("Enterprise Unified Analytics Platform - v1.0")

if selection == "Fraud Detection Engine":
    df_fraud = load_fraud_data()
    render_fraud_dashboard(df_fraud)
else:
    df_social = load_social_data()
    render_social_dashboard(df_social)
