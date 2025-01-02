import streamlit as st
import pandas as pd
import time
import keyboard
import os
import psutil

about_page = st.Page("./display/1_About_App.py",title="About App",icon=":material/info:")
live_updates_page = st.Page("./display/tools/2_Live_Updates.py",title="Live Updates",icon=":material/update:")
prediction_page = st.Page("./display/tools/3_Prediction.py",title="Prediction Tool",icon=":material/history_edu:")
chatbot_page = st.Page("./display/tools/4_QuakeBot.py",title="QuakeBot",icon=":material/chat:")

st.set_page_config(layout="wide")

st.logo("./static/big.png",icon_image="./static/QuakeQuery.jpg",size="large")

if "earthquake_data" not in st.session_state:
    st.session_state.earthquake_data = pd.DataFrame() # Empty dataframe to start with.

if "messages" not in st.session_state:
    st.session_state.messages = []

pg = st.navigation(
    {
        "Introduction" : [about_page],
        "Tools" : [live_updates_page,prediction_page,chatbot_page]
    }
)
pg.run()
