import os
from os.path import exists
import streamlit as st


########### Database ###########

from supabase import create_client, Client
# API Key Codes - Replace w. Streamlit Secrets
from apikeys import supabase_url, supabase_key
supabase: Client = create_client(supabase_url, supabase_key)


# Langchain and OPENAI

#LLM
from apikeys import openaikey
from langchain.llms import OpenAI

#Langchain Features
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

os.environ['OPENAI_API_KEY'] = openaikey

llm = OpenAI(temperature=0.4)

run_chain = False
all_deets = 0

#_______________________________________
#AI STUFF ABOVE

st.header("Message Writer")
st.subheader("Fill in the form to draft your message:")

format = st.selectbox("What format would you like the message?", ["email", "short text", "letter"])
sender = st.text_input("Your name?")
recipient = st.text_input("Who do you want to send an email / letter to?")
goal = st.text_input("What do you want from them?")
reason = st.text_input("Why do you want it?")
offer = st.text_input("Why should they do it / What do they get? (Optional)")
phone_number = st.text_input("Your mobile number? (Optional)")
submit = st.button("Draft")


if submit:
    form = [sender, recipient, goal, reason, ]

    for detail in form:
        if detail in form == "":
            st.error("Please fill in all required fields")
        else:
            all_deets += 1
    
    if offer == "":
        offer = "nothing"

    if phone_number == "":
        phone_number = "not to be included"

    if all_deets == len(form):
        run_chain = True

if run_chain == True:
    all_deets == False
    email_draft_template = PromptTemplate(
        input_variables = ["format", "sender", "recipient", "goal", "reason", "offer", "phone_number",],
        
        template ='''
        My name is {sender}. I want to write a {format} to {recipient}. The aim of the message is for the recipient to: {goal}. The reason I want to achieve this outcome is because {reason}. I can offer the following if they agree: {offer}. My phone number is {phone_number}

        Help me to write this message in a friendly and polite tone. 

        '''
    )

    email_draft_chain = LLMChain(llm=llm, prompt = email_draft_template, verbose = False, output_key='summary')

    #Organisational Summaries
    with st.spinner('Drafting your email (DO NOT REFRESH)'):
        #Problem Solving
        email_draft = email_draft_chain.run({"format": format, "sender": sender, "recipient": recipient, "goal": goal, "reason": reason, "offer": offer, "phone_number": phone_number})


    st.subheader("Here's a draft email for you:")
    st.write(email_draft)