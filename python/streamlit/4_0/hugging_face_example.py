import streamlit as st
from transformers import pipeline

"""
# Hugging Face - sentiment analysis model

use its pipeline function, which lets us ask for a model by name.
"""

"* Load the sentiment analysis model"
"This takes an awful long time btw... (as of jan 2025 it's 268MB)"

code = """
model = pipeline("sentiment-analysis")
"""
st.code(code, language="python")

model = pipeline("sentiment-analysis")

"* Ask for user's input text"
code = """
text = st.text_input("Enter text to analyze")

if text:
    result = model(text)
    st.write("Sentiment:", result[0]["label"])
    st.write("Confidence:", result[0]["score"])
"""
st.code(code, language="python")

text = st.text_input("Enter text to analyze")

if text:
    result = model(text)
    st.write("Sentiment:", result[0]["label"])
    st.write("Confidence:", result[0]["score"])

"""
When you use the pipeline function from the Hugging Face transformers 
library, it automatically downloads the model the first time it's used. 
After that, the model is cached locally in a directory 
(usually `~/.cache/huggingface/transformers`) and reused for subsequent runs.

So, when you run your app again, the model will not be downloaded again; 
instead, it will be loaded from the local cache.

`st.cache_resource` is a caching mechanism provided by Streamlit to allow 
you to cache heavy resources, like machine learning models, and avoid 
reloading them every time. In your case, since the model is already 
cached locally by Hugging Face's transformers library, you don't 
necessarily need to cache it again with st.cache_resource. 
However, you can explicitly use st.cache_resource to ensure that 
your model is only loaded once and reused in subsequent runs.

see `hugging_face_example_v2.py`
"""
