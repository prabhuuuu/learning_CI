import streamlit as st

# streamlit ui
st.title("power caluclator")
st.write("ener a number to calcuate its square")

# get the input
ip = st.number_input("enter a number")

# calculate the square
sq = ip ** 2
cb= ip ** 3
fifth= ip ** 5

# display the results
st.write(f"The square of {ip} is {sq}")
st.write(f"The cube of {ip} is {cb}")
st.write(f"The fifth power of {ip} is {fifth}")