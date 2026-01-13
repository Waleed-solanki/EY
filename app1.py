import streamlit as st

st.title("Some basic user interface")

a = st.text_input("Enter your name:")
if st.button("submit"):
    st.write("Hello",a)

    