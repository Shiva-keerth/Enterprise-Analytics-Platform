import streamlit as st
import matplotlib.pyplot as plt

def render_fraud_dashboard(df):
    st.markdown("## 🛡️ Enterprise Fraud Detection Engine")
    
    if df.empty:
        st.warning("No data available.")
        return

    # Top Level KPIs
    col1, col2, col3 = st.columns(3)
    total_txns = len(df)
    total_fraud = df['is_fraud'].sum() if 'is_fraud' in df.columns else 0
    fraud_rate = (total_fraud / total_txns * 100) if total_txns > 0 else 0
    
    with col1:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{total_txns:,}</div><div class="metric-label">Total Transactions</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card" style="border-left:4px solid #ff4b4b;"><div class="metric-value">{total_fraud:,}</div><div class="metric-label">Fraudulent Flags</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{fraud_rate:.2f}%</div><div class="metric-label">Fraud Rate</div></div>', unsafe_allow_html=True)

    st.markdown("### Risk Analysis")
    colA, colB = st.columns(2)
    
    with colA:
        st.markdown("**Fraud Distribution**")
        fig1, ax1 = plt.subplots(figsize=(6,4))
        ax1.set_facecolor('transparent')
        fig1.patch.set_facecolor('transparent')
        data = df['is_fraud'].value_counts()
        ax1.bar(["Legit", "Fraud"], data.values, color=['#00ffb4', '#ff4b4b'])
        ax1.tick_params(colors='white')
        st.pyplot(fig1)

    with colB:
        st.markdown("**Average Amount by Status**")
        fig2, ax2 = plt.subplots(figsize=(6,4))
        ax2.set_facecolor('transparent')
        fig2.patch.set_facecolor('transparent')
        data1 = df.groupby("is_fraud")["amount"].mean()
        ax2.bar(["Legit", "Fraud"], data1.values, color=['#0af', '#7b61ff'])
        ax2.tick_params(colors='white')
        st.pyplot(fig2)
