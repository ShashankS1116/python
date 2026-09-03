## creating application

import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")
name = st.text_input("Enter your name :")
if name:
    st.write(f"Hello, {name}") 

## creating a slider-----------------x

age = st.slider("Select your age:", 0, 100, 25)

st.write(f"Your age is {age}.")

## creating a selection box---------------x

options = ["python", "java", "c++", "javascript"]
choice = st.selectbox("choose your favourite language:", options)
st.write(f"you selected {choice}.")

## creating a database-----------x

data = {
    "Name" : ["John", "Jane", "Jake", "Jill"],
    "Age" : [28, 34, 35, 40],
    "City" : ["New York", "India", "Houston", "Russia"]
}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


##creating a upload button ----------------x

uploaded_file = st.file_uploader("choose a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

