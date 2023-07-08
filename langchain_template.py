#Install deps
import os
import streamlit as st

#LLM
from langchain.llms import OpenAI

#Langchain Features
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

#Import API keys
from apikeys import openaikey

#Set API keys
os.environ['OPENAI_API_KEY'] = openaikey

#Set OpenAI as llm
llm = OpenAI(temperature=0.9)

#Prompt Engine
#Prompt Templates
generic_template = PromptTemplate(
    input_variables = ['input'],
    template= 'Based on: {input}, do XYZ'
)

#LLM Chain
generic_chain_a = LLMChain(llm=llm, prompt = generic_template, verbose = True, output_key='output')
generic_chain_b = LLMChain(llm=llm, prompt = generic_template, verbose = True, output_key='output')
generic_chain_c = LLMChain(llm=llm, prompt = generic_template, verbose = True, output_key='output')

sequential_chain = SequentialChain(chains=[generic_chain_a, generic_chain_b, generic_chain_c ], input_variables=['response'], output_variables=['x','y','z'], verbose=True)

#App framework

st.title('Streamlit App Template')
st.header('Welcome!') 
st.write('This is a template for making your basic streamlit apps')
st.divider()

