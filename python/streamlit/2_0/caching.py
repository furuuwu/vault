"""
# Caching

The way Streamlit caching works more specifically is by storing the results 
of a function in our app, and if that function is called with the same 
parameters by another user (or by us if we rerun the app), Streamlit does
not run the same function but instead loads the result of the function
from memory.

There are two Streamlit caching functions, one for data (`st.cache_data`) 
and one for resources like database connections or machine learning models
(`st.cache_resource`)

in this script:
* create a function `load_file` for our data upload part of the app
* use the `time` library to artificially make the function take much longer
than it would normally
* add a cache decorator `@st.cache_data()` on top of the `load_file` function 
and see it makes the app faster
"""

import streamlit as st
import pandas as pd
import altair as alt
import time

"""
## Palmer's Penguins
Use this Streamlit app to make your own scatterplot about penguins!
"""

penguin_file = st.file_uploader("Select Your Local Penguins CSV (default provided)")


@st.cache_data()
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv("penguins.csv")
    return df


penguins_df = load_file(penguin_file)

code = """
penguin_file = st.file_uploader("Select Your Local Penguins CSV (default provided)")

@st.cache_data()
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv("penguins.csv")
    return df


penguins_df = load_file(penguin_file)
"""
st.code(code, language="python")

selected_x_var = st.selectbox(
    "What do you want the x variable to be?",
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
)
selected_y_var = st.selectbox(
    "What about the y?",
    ["bill_depth_mm", "bill_length_mm", "flipper_length_mm", "body_mass_g"],
)
selected_gender = st.selectbox(
    "What gender do you want to filter for?",
    ["all penguins", "male penguins", "female penguins"],
)
if selected_gender == "male penguins":
    penguins_df = penguins_df[penguins_df["sex"] == "male"]
elif selected_gender == "female penguins":
    penguins_df = penguins_df[penguins_df["sex"] == "female"]
else:
    pass

alt_chart = (
    alt.Chart(penguins_df, title="Scatterplot of Palmer's Penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color="species",
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)
