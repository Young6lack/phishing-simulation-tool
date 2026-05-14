# 🎣 Phishing Awareness Simulation Tool

A beginner cybersecurity project that demonstrates how phishing attacks work in a safe, controlled environment.

**Live Demo**: [Try the App Here](https://young6lack-phishing-simulation-tool-app-n0yxx1.streamlit.app/)  
**GitHub**: [View Source Code](https://github.com/Young6lack/phishing-simulation-tool)

---

## ✨ Project Overview

This tool simulates real-world phishing techniques to help users understand how attackers steal credentials. It is built for **educational and portfolio purposes only**.

### Key Features
- **📧 Fake Phishing Email Simulator** – Simulates sending targeted phishing emails
- **🌐 Realistic Fake Login Page** – Demonstrates credential harvesting (Microsoft-style design)
- **📊 Live Attack Dashboard** – Shows captured credentials in real-time
- **Educational Focus** – Explains the attack at every step

---

## 🛠️ Technologies Used
- **Python 3**
- **Streamlit** (for web interface)
- **Pandas** (for data tracking)
- Built on **Ubuntu VM**

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Young6lack/phishing-simulation-tool.git
cd phishing-simulation-tool

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
streamlit run app.py