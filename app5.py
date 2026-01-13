import streamlit as st
import google.generativeai as genai

st.title("Welcome to generativeai with streamlit")

user_input = st.text_area("Ask me anything")
genai.configure(api_key="AIzaSyDADTc2AQhcjDNTjl5fXaWq7u1aFVs8E20")

models = genai.GenerativeModel('model/genai-2.5-flash')

if user_input and st.button("Get Response"):
    response = models.generate_content(user_input)
    st.write("Response from Generative AI:", response.text)