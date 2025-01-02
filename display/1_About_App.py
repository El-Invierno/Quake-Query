import streamlit as st

st.markdown("# About App")
st.divider()
with st.container(border=True):
    st.markdown(
        """
# Quake Query

**Welcome to Quake Query**, your one-stop platform for everything related to earthquake prediction, preparedness, and response. Leveraging cutting-edge technology and live data, we aim to keep you informed and prepared to deal with seismic activities.

---

## 🌍 **Features**

### 1. **Prediction System**
- Powered by advanced **Machine Learning (ML) models**, Quake Query analyzes seismic data to provide:
  - **Probability of future earthquakes**.
  - **Predicted magnitudes and affected regions**.
  - **Early warnings and risk assessments**.

### 2. **Interactive Chatbot**
- Learn how to **prevent, mitigate, and respond** to earthquakes with our intelligent chatbot.
- Key functionalities include:
  - Step-by-step **earthquake preparedness guides**.
  - **Mitigation strategies** for reducing risks.
  - Advice for **emergency responses** during and after an earthquake.
  - Access to **FAQs and expert tips** on staying safe.

### 3. **Live Earthquake Updates**
- Stay updated with **real-time earthquake data** from across the globe.
- Features:
  - **Interactive maps** showing recent seismic activities.
  - **Details about location, magnitude, depth, and time** of earthquakes.
  - **Push notifications** for major seismic events.

---

## 🚀 **Getting Started**
1. Visit our homepage to access the main functionalities.
2. Choose a feature:
   - Use the **Prediction System** to analyze potential seismic risks.
   - Chat with our **Earthquake Response Bot** for guidance.
   - Check the **Live Updates** section for the latest information.
3. Take proactive steps and share your learnings to help others.

---

## 📊 **Technology Stack**
- **Frontend**: Streamlit for an interactive and user-friendly interface.
- **Backend**: Python for robust logic and ML model integration.
- **Data Sources**: Live seismic data feeds for accurate updates.
- **Machine Learning**: State-of-the-art models for earthquake prediction.

---

## 🌟 **Why Quake Query?**
- **Reliable Predictions**: Leverage ML for accurate insights.
- **Actionable Knowledge**: Learn best practices to ensure safety.
- **Real-Time Awareness**: Access live earthquake data anytime.

---

## 📞 **Contact Us**
Have questions or feedback? Reach out to us at **yashtawde9@gmail.com**.

---

## ✍️ **Author**
**Yash Tawde**

---

Stay informed. Stay safe.

**Quake Query - Empowering Earthquake Preparedness.**
        """
    )
