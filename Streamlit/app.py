import numpy as np
import pandas as pd
import streamlit as st

# title of app
st.title("Hello World")

# text
st.text("First Streamlit App")

# adding a dataframe
df = pd.DataFrame({
    'name': ['John', 'Mary', 'Peter'],
    'age': [25, 30, 35]
})

# display dataframe
st.write("added a dataframe")
st.write(df)

# create a simple line chart
line_df = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randn(10)
})

# display line chart
st.write("added a line chart")
st.line_chart(line_df)