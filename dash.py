import streamlit as st
import pandas as pd
import plotly.express as px
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="API Guardian", layout="wide")

# Sidebar Navigation
st.sidebar.title("API Guardian")
nav = st.sidebar.radio("Navigate", ["Dashboard", "Threats", "Traffic", "Settings"])

# Header Buttons
col1, col2, col3 = st.columns([6, 1, 1])
with col2:
    st.button("Settings")
with col3:
    st.button("Log Out")

st.title("Real-Time Threat Detection & Defense for APIs")

# Simulated Data
def get_threat_data():
    types = ['SQL Injection', 'XSS', 'CSRF', 'Broken Auth']
    severities = ['Low', 'Medium', 'High']
    return pd.DataFrame({
        'Time': [(datetime.now() - timedelta(minutes=i)).strftime("%H:%M:%S") for i in range(5)],
        'IP Address': [f"192.0.2.{random.randint(1, 10)}" for _ in range(5)],
        'Endpoint': ["/api/data", "/api/login", "/api/users", "/api/data", "/api/token"],
        'Threat Type': [random.choice(types) for _ in range(5)],
        'Severity': [random.choice(severities) for _ in range(5)],
    })

threat_data = get_threat_data()

# Main Dashboard Layout
if nav == "Dashboard":
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Live Threats")
        st.dataframe(threat_data)

        st.subheader("Request Stats")
        st.metric("Total Requests", "1,254")
        st.metric("Success Rate", "98.2%")
        st.metric("Error Rate", "1.6%")

        st.subheader("Latency")
        latency_data = pd.DataFrame({
            'Time': pd.date_range(start='10:00', periods=20, freq='min'),
            'Latency (ms)': [random.randint(50, 150) for _ in range(20)]
        })
        fig1 = px.line(latency_data, x='Time', y='Latency (ms)', title='Latency Over Time')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Threat Map")
        st.image("https://upload.wikimedia.org/wikipedia/commons/8/83/Equirectangular_projection_SW.jpg", caption="Threats Geo Map (Mockup)", use_column_width=True)

        st.subheader("Attack Timeline")
        attack_data = pd.DataFrame({
            'Time': pd.date_range(start='10:00', periods=20, freq='T'),
            'Attacks': [random.randint(0, 10) for _ in range(20)]
        })
        fig2 = px.line(attack_data, x='Time', y='Attacks', title='Attacks Over Time')
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Detected Threat Types")
        st.checkbox("SQL Injection", value=True)
        st.checkbox("XSS", value=True)
        st.checkbox("CSRF", value=False)
        st.checkbox("Other", value=True)

        st.subheader("Defense Actions")
        st.write("• Auto-blocked IPs: **12**")
        st.write("• Quarantined Requests: **4**")

elif nav == "Threats":
    st.subheader("Threat Log")
    st.dataframe(threat_data)

elif nav == "Traffic":
    st.subheader("Traffic Analysis (Coming Soon)")

elif nav == "Settings":
    st.subheader("Settings Panel (Coming Soon)")
