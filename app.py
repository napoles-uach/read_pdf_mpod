import streamlit as st
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from PyPDF2 import PdfReader

import os
os.environ["OPENAI_API_KEY"] =gpt_key
st.title('Read PDF 4 MPOD')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  reader = PdfReader(uploaded_file)
  st.write(len(reader.pages))
  
llm = OpenAI(temperature=0)
