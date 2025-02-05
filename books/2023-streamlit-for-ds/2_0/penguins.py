import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Palmer's Penguins")

""" 
* Load the dataset (Palmer's penguins)
"""

penguins_df = pd.read_csv("penguins.csv")
st.write(penguins_df.head())

st.markdown(
    "Use this Streamlit app to make your own \
            scatterplot about penguins!"
)

""" 
* Get user's input (a specific penguin species and 2 features)
"""
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

""" 
* Filter the dataset
"""

filtered_penguins_df = penguins_df[penguins_df["species"] == selected_species]

""" 
* Generate the scatterplot (using matplotlib)
"""
fig, ax = plt.subplots()
ax.scatter(
    x=filtered_penguins_df[selected_x_var],
    y=filtered_penguins_df[selected_y_var],
    c="blue",
    alpha=0.5,
)
ax.set_title(f"Scatter Plot of {selected_y_var} x {selected_x_var}")
ax.set_xlabel(f"{selected_x_var}")
ax.set_ylabel(f"{selected_y_var}")

st.pyplot(fig)

st.markdown(
    "This scatterplot shows the relationship between \
            {} and {} for penguins of the {} species.".format(
        selected_x_var, selected_y_var, selected_species
    )
)

st.markdown(
    "For more information about Palmer's penguins, visit \
            [this link](https://allisonhorst.github.io/palmerpenguins/)."
)
