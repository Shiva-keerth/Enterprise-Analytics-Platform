import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    """
    Applies Isolation Forest to detect anomalous transaction patterns.
    This acts as the Machine Learning precursor to the rule-based Fraud Engine.
    """
    if df.empty or 'amount' not in df.columns or 'device_risk_score' not in df.columns:
        return df
        
    # Select features for anomaly detection
    features = ['amount', 'device_risk_score', 'hour']
    X = df[features].fillna(0)
    
    # Initialize and fit the Isolation Forest model
    model = IsolationForest(contamination=0.05, random_state=42)
    df['anomaly_score'] = model.fit_predict(X)
    
    # Map scores: -1 is anomalous, 1 is normal
    df['is_anomaly'] = df['anomaly_score'].apply(lambda x: True if x == -1 else False)
    
    return df
