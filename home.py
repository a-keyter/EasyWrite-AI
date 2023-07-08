import os
import streamlit as st
from supabase import create_client, Client

# API Key Codes - Replace w. Streamlit Secrets
from apikeys import supabase_url, supabase_key, openaikey

# Session User
userEmail = st.experimental_user.email

# Declare User Object
userObject = ""
supabase: Client = create_client(supabase_url, supabase_key)

# Streamlit logic

st.title("Jamie's demo AI Tools")

st.subheader("Hey Jamie, Alex here - Welcome to Streamlit!")

st.write("Basically, I'm going to throw some of my projects in here for you to have a go with. Any feedback or ideas are massively appreciated!")


st.write("""You can access the following tools using the menu to your left:

- ✉️ **Email Assist**

""")