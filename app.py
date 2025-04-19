import streamlit as st

st.title("power calculator")
st.write("calculate its square, cube and fifth power")

n = st.number_input("enter a number", value = 1, step = 1)

s = n ** 2
c = n ** 3
f = n ** 5

st.write(f"the square of {n}  is  {s}")
st.write(f"the cube of {n} is {c}")
st.write(f"the fifth power of {n} is {f}")
