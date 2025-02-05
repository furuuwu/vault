"""
This is the same thing as `penguins.py` but uses 
`altair` for the graphics (instead of matplotlib)
"""

import streamlit as st
import pandas as pd
import altair as alt

st.title("Palmer's Penguins")

"""* Load data"""
penguins_df = pd.read_csv("penguins.csv")
st.write(penguins_df.head())
code = """
penguins_df = pd.read_csv("penguins.csv")
st.write(penguins_df.head())
"""
st.code(code, language="python")

st.markdown(
    "Use this Streamlit app to make your own \
            scatterplot about penguins!"
)

"""* Filter data"""
selected_species = st.selectbox(
    "What species would you like to visualize?", ["Adelie", "Gentoo", "Chinstrap"]
)
selected_x_var = st.selectbox(
    "What do you want the x variable to be?",
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
)
selected_y_var = st.selectbox(
    "What about the y?",
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
)
filtered_penguins_df = penguins_df[penguins_df["species"] == selected_species]
code = """
selected_species = st.selectbox(
    "What species would you like to visualize?", ["Adelie", "Gentoo", "Chinstrap"]
)
selected_x_var = st.selectbox(
    "What do you want the x variable to be?",
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
)
selected_y_var = st.selectbox(
    "What about the y?",
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
)
filtered_penguins_df = penguins_df[penguins_df["species"] == selected_species]
"""
st.code(code, language="python")

"""
* Plots
"""

alt_chart = (
    alt.Chart(filtered_penguins_df, title=f"Scatterplot of {selected_species} penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
    )
)
st.altair_chart(alt_chart)

code = """
alt_chart = (
    alt.Chart(filtered_penguins_df, title=f"Scatterplot of {selected_species} penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
    )
)
st.altair_chart(alt_chart)
"""
st.code(code, language="python")

"""
Right now we can't zoom into our chart, so most of the graph is blank. 
We can change this by either using Altair to edit the axes, or we can 
make the Altair chart interactive so that the user can zoom in
wherever they'd like on the graph. The following code makes the Altair 
chart zoomable and extends the graph to fit the entire screen with 
the use_container_width parameter:
"""
alt_chart = (
    alt.Chart(filtered_penguins_df, title=f"Scatterplot of {selected_species} penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)

code = """
alt_chart = (
    alt.Chart(penguins_df, title=f"Scatterplot of {selected_species} penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)
"""
st.code(code, language="python")

"""
* Show all species, using the species (categorical variable) as a color label
"""

alt_chart = (
    alt.Chart(penguins_df, title="Scatterplot of all penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color="species",
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)

code = """
alt_chart = (
    alt.Chart(penguins_df, title="Scatterplot of all penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color="species",
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)
"""
st.code(code, language="python")
