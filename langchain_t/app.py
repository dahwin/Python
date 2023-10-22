import os
from api import apikey
import streamlit as st
from langchain.llms import HuggingFaceEndpoint, OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SimpleSequentialChain

os.environ['dahwin'] = apikey

st.title('🦅🦅🦅 Dahwin mediag')
prompt = st.text_input('input your prompt')

titel_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'wrte me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title'],
    template = 'wrte me a youtube video scripts based on this title {title}'
)

llm = HuggingFaceEndpoint(temperature=0.9)

title_chain = LLMChain(llm=llm,prompt=titel_template,verbose=True)
script_chain = LLMChain(llm=llm,prompt=script_template,verbose=True)
sequential_chain = SimpleSequentialChain(chain=[title_chain,script_chain],verbose=True)

if prompt :
    response = sequential_chain.run(topic=prompt)
    st.write(response)