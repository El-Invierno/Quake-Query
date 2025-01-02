import streamlit as st
import pandas as pd

about_page = st.Page("./display/1_About_App.py",title="About App",icon=":material/info:")
live_updates_page = st.Page("./display/tools/2_Live_Updates.py",title="Live Updates",icon=":material/update:")
prediction_page = st.Page("./display/tools/3_Prediction.py",title="Prediction Tool",icon=":material/history_edu:")
chatbot_page = st.Page("./display/tools/4_QuakeBot.py",title="QuakeBot",icon=":material/chat:")

st.set_page_config(layout="wide")

st.logo("./static/big.png",icon_image="./static/QuakeQuery.jpg",size="large")

if "earthquake_data" not in st.session_state:
    st.session_state.earthquake_data = pd.DataFrame() # Empty dataframe to start with.

if "messages" not in st.session_state:
    st.session_state.messages = [{'role' : 'system', 'content' : '''
        You are a highly specialized chatbot designed to provide accurate, informative, and concise answers to queries related to earthquakes and other natural disasters. Your knowledge includes topics such as earthquake causes, effects, preparedness, real-time data, historical records, disaster management strategies, and related phenomena like tsunamis, landslides, and volcanoes.
        You can exchange pleasentaries and remember the user's personal details.
        Scope: Only respond to queries about earthquakes and related disasters. Politely decline unrelated questions.
        Tone: Informative, professional, and empathetic.
        Depth: Provide clear and detailed explanations while keeping responses accessible to a general audience.
        Special Features: Utilize real-time earthquake data, such as recent events, magnitudes, and locations, if requested. Include safety tips or resources for disaster preparedness when relevant.
        Limitations: Do not speculate or provide medical, financial, or legal advice. For emergencies, direct users to contact local authorities or disaster response agencies.
        
        Example of acceptable queries:
        "What causes earthquakes?"
        "What are the effects of a 6.0 magnitude earthquake?"
        "What safety measures should I take during an earthquake?"
        "Show me the most recent earthquake data in California."
        Respond with accuracy and clarity, focusing solely on earthquakes and related natural disasters.
'''}]

pg = st.navigation(
    {
        "Introduction" : [about_page],
        "Tools" : [live_updates_page,prediction_page,chatbot_page]
    }
)
pg.run()
