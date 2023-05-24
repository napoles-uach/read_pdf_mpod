import streamlit as st
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from PyPDF2 import PdfReader

import os
os.environ["OPENAI_API_KEY"] =os.environ["gpt_key"]
#openai.api_key = os.environ["gptkey"]

st.title('Read PDF 4 MPOD')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  reader = PdfReader(uploaded_file)
  st.write(len(reader.pages))
  page = reader.pages
  full_text=[]
  # loop para leer todas las paginas
  for p in page:
    text = p.extract_text()
    full_text.append(text)
  # expander para ver el texto
  with st.expander("Texto extraido"):
    full_text
  # guarda el texto a archivo
  with open('readme.txt', 'w') as f:
    for p in full_text:
      f.write(p)
  
  from langchain.document_loaders import TextLoader
  loader = TextLoader("readme.txt")
   
  
llm = OpenAI(temperature=0)
