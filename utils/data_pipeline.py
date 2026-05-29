import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_fraud_data():
    """Simulates ETL extraction and transformation for fraud data."""
    try:
        df = pd.read_csv("data/synthetic_fraud_dataset.csv")
        # Ensure timestamp/hour columns are correctly typed
        if 'hour' in df.columns:
            df['hour'] = df['hour'].astype(int)
        return df
    except FileNotFoundError:
        st.error("Fraud dataset not found. Please place 'synthetic_fraud_dataset.csv' in the 'data' folder.")
        return pd.DataFrame()

@st.cache_data
def load_social_data():
    """Simulates ETL extraction and transformation for social media data."""
    try:
        df = pd.read_csv("data/Instagram_Analytics.csv")
        # Clean basic NaN values
        df.fillna(0, inplace=True)
        return df
    except FileNotFoundError:
        st.error("Instagram dataset not found. Please place 'Instagram_Analytics.csv' in the 'data' folder.")
        return pd.DataFrame()
