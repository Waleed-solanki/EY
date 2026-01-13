import streamlit as st

st.title("Welcome to home page")
name = st.text_input("Enter name:")
age = st.slider("Enter your age:", 1 , 100)
city = st.selectbox ("choose your city",["Delhi","Pune","Goa","Haryana"])

st.markdown("## subheading")

if st.button("Show details"):
    st.write("Name",name)
    st.write("Age",age)
    st.write("City",city)
