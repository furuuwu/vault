import streamlit as st

"""
**Example 1: Customize your button type**
"""
code = """
st.button("Reset", type="primary")
"""
st.code(code, language="python")

st.button("Reset", type="primary")

code = """
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
"""
st.code(code, language="python")

if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

code = """
if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
"""
st.code(code, language="python")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")

"""
**Example 2: Add icons to your button**

Although you can add icons to your buttons through Markdown, 
the icon parameter is a convenient and consistent alternative.
"""
code = """
left, middle, right = st.columns(3)
if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", use_container_width=True):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")
"""
st.code(code, language="python")

left, middle, right = st.columns(3)
if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", use_container_width=True):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")
