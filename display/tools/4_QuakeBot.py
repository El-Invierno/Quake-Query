import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser

st.title("QuakeBot")
st.divider()

os.environ['OPENAI_API_KEY'] = st.secrets.openai.OPENAI_API_KEY

if "openai_model" not in st.session_state:
    st.session_state.openai_model = "gpt-4o-mini"

model = ChatOpenAI(model=st.session_state.openai_model)
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
url = st.secrets.qdrant.url
api_key = st.secrets.qdrant.api_key
qdrant = QdrantVectorStore.from_existing_collection(
embedding=embeddings,
collection_name="earthquake_data",
url=url,
api_key=api_key
)
retriever = qdrant.as_retriever(search_type="mmr", search_kwargs={"k": 20})

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
    
def call_chain(messages):
    chain = model | StrOutputParser()
    response = chain.invoke(messages)
    return response

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt := st.chat_input("Enter your query regarding earthquakes"):
    st.session_state.messages.append({'role' : 'user', 'content' : prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message('ai'):
        result = call_chain(st.session_state.messages)
        st.markdown(result)
    st.session_state.messages.append({'role' : 'ai', 'content' : result})
