import streamlit as st
import pandas as pd
from datetime import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Page Configuration
st.set_page_config(
    page_title="Phishing Awareness Simulator",
    page_icon="🎣",
    layout="wide"
)

st.title("🎣 Phishing Awareness Simulation Tool")
st.markdown("**Cybersecurity Portfolio Project #2** | Educational Tool Only")

tab1, tab2, tab3 = st.tabs(["📧 Send Real Phishing Email", "🌐 Fake Login Page", "📊 Attack Dashboard"])

# ===================== TAB 1: SEND REAL EMAIL =====================
with tab1:
    st.subheader("📧 Send Real Phishing Email (Educational Demo)")
    st.warning("for testing. Never use for malicious purposes!")

    col1, col2 = st.columns(2)
    with col1:
        sender_email = st.text_input("Your Gmail Address", "your.email@gmail.com")
        app_password = st.text_input("Gmail App Password", type="password")
    
    with col2:
        target_email = st.text_input("Target (Victim) Email", "test@example.com")
        subject = st.text_input("Email Subject", "Urgent: Account Security Alert - Action Required")

    message_body = st.text_area("Phishing Email Body", 
        """Dear Valued Employee,

Our security team has detected unusual activity on your company account. 
To prevent account suspension, please verify your credentials immediately:

👉 [VERIFY YOUR ACCOUNT NOW](http://localhost:8501)

Failure to verify within 24 hours may result in account lockout.

Best regards,
IT Security Department
Company Name""", height=250)

    if st.button("🚀 Send Real Email", type="primary"):
        if sender_email and app_password and target_email and message_body:
            try:
                with st.spinner("Sending email..."):
                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = target_email
                    msg['Subject'] = subject
                    msg.attach(MIMEText(message_body, 'plain'))

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender_email, app_password)
                    server.sendmail(sender_email, target_email, msg.as_string())
                    server.quit()

                st.success(f"✅ Email successfully sent to **{target_email}**!")
                st.balloons()
            except Exception as e:
                st.error(f"❌ Failed to send email: {str(e)}")
                st.info("💡 Make sure you are using a **Gmail App Password** (not your regular password)")
        else:
            st.warning("Please fill in all required fields.")

# ===================== TAB 2: FAKE LOGIN PAGE =====================
with tab2:
    st.subheader("🌐 Fake Login Page (What the Victim Sees)")
    st.markdown("**This is how a realistic phishing page looks**")

    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/512px-Microsoft_logo.svg.png", width=180)

    username = st.text_input("Email or Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In", type="primary"):
        if username and password:
            # Save captured credentials
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
            
            st.error("❌ Invalid credentials. Please try again.")
            st.success("✅ Credentials captured for demonstration!")
            st.balloons()
        else:
            st.warning("Please enter username and password.")

# ===================== TAB 3: DASHBOARD =====================
with tab3:
    st.subheader("📊 Attack Dashboard - Captured Credentials")
    
    try:
        df = pd.read_csv("phished_data.csv")
        st.dataframe(df, use_container_width=True)
        
        total = len(df)
        st.metric("Total Credentials Captured", total)
        
        if total > 0:
            st.success(f"🎯 {total} successful phishing attempts!")
    except FileNotFoundError:
        st.info("No credentials captured yet. Try the Fake Login Page.")

st.caption("⚠️ This is an **educational tool only**. Use responsibly for awareness training.")
