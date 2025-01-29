import streamlit as st
import pandas as pd
import plotly.express as px

"""
# Using Plotly

Streamlit allows us to call plotly graphs from within Streamlit apps using the
`st.plotly_chart()` function, which makes it a breeze to port 
any Plotly or Dash dashboards.
"""

code = """
trees_df = pd.read_csv("trees.csv")
fig = px.histogram(trees_df["dbh"])
st.plotly_chart(fig)
"""
st.code(code, language="python")

trees_df = pd.read_csv("trees.csv")
fig = px.histogram(trees_df["dbh"])
st.plotly_chart(fig)
