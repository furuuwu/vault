import streamlit as st
from transformers import pipeline

"""
# Hugging Face - sentiment analysis model
"""

"* Load the sentiment analysis model"
"This takes an awful long time btw... (as of jan 2025 it's 268MB)"
code = """
@st.cache_resource
def load_model(model_name: str):
    return pipeline(model_name)

model = load_model("sentiment-analysis")
"""
st.code(code, language="python")


@st.cache_resource
def load_model(model_name: str):
    return pipeline(model_name)


model = load_model("sentiment-analysis")

"* Ask for user's input text"
text = st.text_input("Enter text to analyze")

if text:
    result = model(text)
    st.write("Sentiment:", result[0]["label"])
    st.write("Confidence:", result[0]["score"])
