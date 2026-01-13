import streamlit as st

st.title("Calculator app")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

op = st.selectbox("choose operatioin",["add","sub","mul","div"])

if st.button("calculate"):
    if op == "add":
        result = num1 + num2
    elif op == "sub":
        result = num1 - num2
    elif op == "mul":
        result = num1 * num2
    elif op == "div":
        if num2 !=0:
            result = num1 / num2
        else :
            result = "Error: Divisible by zero"     
st.write(f"The result is", {result})                   