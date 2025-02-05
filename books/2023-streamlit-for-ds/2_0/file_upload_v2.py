import altair as alt
import pandas as pd
import streamlit as st

st.title("Palmer's Penguins")
st.markdown(
    "Use this Streamlit app to make your own scatterplot about \
            penguins!"
)
penguin_file = st.file_uploader(
    "Select Your Local Penguins CSV \
                                (default provided)"
)
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    st.stop()

code = """
penguin_file = st.file_uploader(
    "Select Your Local Penguins CSV (default provided)"
)
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    st.stop()
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

# filter based on gender
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
    .mark_point(size=100)  # Adjust size for better visibility
    .encode(
        x=alt.X(selected_x_var, title=selected_x_var),
        y=alt.Y(selected_y_var, title=selected_y_var),
        color="species",  # Map color to species
        shape="species",  # Automatically assign shapes to species
    )
    .interactive()
)

st.altair_chart(alt_chart, use_container_width=True)

# custom marker shapes...
shape_map = {"Adelie": "circle", "Gentoo": "square", "Chinstrap": "triangle"}

alt_chart = (
    alt.Chart(penguins_df, title="Scatterplot of Palmer's Penguins")
    .mark_point(size=100)  # Set the size of the points for better visibility
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color="species",
        shape=alt.Shape(
            "species",
            scale=alt.Scale(
                domain=list(shape_map.keys()), range=list(shape_map.values())
            ),
        ),
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)
