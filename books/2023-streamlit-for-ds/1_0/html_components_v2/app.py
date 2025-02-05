import streamlit as st
import os

# Read the HTML, CSS, and JS files
html_path = "index.html"
# css_path = "styles.css"
# js_path = "script.js"


with open(html_path, "r") as f:
    html_content = f.read()

# with open(css_path, "r") as f:
#    css_content = f.read()

# with open(js_path, "r") as f:
#    js_content = f.read()

# Embed the HTML, CSS, and JS into the Streamlit app
st.components.v1.html(html_content, height=450)
