import streamlit as st

def render_social_dashboard(df):
    st.markdown("## 📱 Social Media Command Center")
    
    if df.empty:
        st.warning("No data available.")
        return

    # Top Level KPIs
    col1, col2, col3 = st.columns(3)
    total_posts = len(df)
    total_likes = df['likes'].sum() if 'likes' in df.columns else 0
    total_reach = df['reach'].sum() if 'reach' in df.columns else 0
    
    with col1:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{total_posts:,}</div><div class="metric-label">Total Posts</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{total_likes:,}</div><div class="metric-label">Total Engagement</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{total_reach:,}</div><div class="metric-label">Total Reach</div></div>', unsafe_allow_html=True)

    st.markdown("### Content Performance")
    colA, colB = st.columns(2)
    
    with colA:
        st.markdown("**Engagement by Media Type**")
        if 'media_type' in df.columns and 'likes' in df.columns:
            data = df.groupby("media_type")["likes"].mean()
            st.bar_chart(data)

    with colB:
        st.markdown("**Reach by Content Category**")
        if 'content_category' in df.columns and 'reach' in df.columns:
            data = df.groupby("content_category")["reach"].mean()
            st.bar_chart(data)
