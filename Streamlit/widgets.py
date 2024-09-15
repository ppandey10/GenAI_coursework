import numpy as np
import pandas as pd
import streamlit as st

# title
st.title('Streamlit Testing')

# input name
name = st.text_input("Enter your name")

# input age as slider
age = st.slider("Enter your age", 0, 100, 25)

# display name and age
st.write(f"Hello, {name}! You are {age} years old.")

# add file uploader
upload_file = st.file_uploader("Upload a file", type=["csv", "txt"])

# display uploaded file
if upload_file is not None:
    st.write(f"You uploaded a file: {upload_file.name}")