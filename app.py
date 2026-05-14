import streamlit as st
import pandas as pd
from datetime import datetime
import time

st.set_page_config(page_title="Phishing Awareness Simulator", page_icon="🎣", layout="wide")

st.title("🎣 Phishing Awareness Simulation Tool")
st.markdown("Demonstrates how phishing attacks work")

tab1, tab2, tab3 = st.tabs(["📧 Send Fake Phishing Email", "🌐 Fake Login Page", "📊 Attack Dashboard"])

with tab1:
    st.subheader("Send Simulated Phishing Email")
    email = st.text_input("Target Email", "employee@company.com")
    subject = st.text_input("Email Subject", "Urgent: Update Your Account Password")
    
    if st.button("Send Phishing Email", type="primary"):
        with st.spinner("Sending email..."):
            time.sleep(1.5)
        st.success(f"✅ Phishing email sent to {email}!")
        st.info("In a real attack, this email would contain a malicious link.")

with tab2:
    st.subheader("Fake Login Page (Demo)")
    st.markdown("**This is what a victim would see**")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/512px-Microsoft_logo.svg.png", width=150)
    
    username = st.text_input("Email or Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign In", type="primary"):
        if username and password:
            # Save to "database"
            new_entry = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Username": username,
                "Password": password[:2] + "*****",
                "IP": "192.168.1.105"
            }
            
            try:
                df = pd.read_csv("phished_data.csv")
                df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
            except:
                df = pd.DataFrame([new_entry])
            
            df.to_csv("phished_data.csv", index=False)
            
            st.error("❌ Login Failed - Credentials Captured!")
            st.balloons()
            st.success("This is how easy it is for attackers to steal credentials.")
        else:
            st.warning("Enter credentials")

with tab3:
    st.subheader("📊 Attack Dashboard")
    try:
        df = pd.read_csv("phished_data.csv")
        st.dataframe(df, use_container_width=True)
        st.metric("Total Credentials Captured", len(df))
    except:
        st.info("No data yet. Try the fake login page above.")

st.caption("Educational tool only.")