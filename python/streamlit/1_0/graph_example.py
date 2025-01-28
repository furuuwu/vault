import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Numeric input: slider for controlling the number of data points
num_points = st.slider(
    "Select the number of data points:", min_value=10, max_value=1000, value=100
)

# Generate random data based on the slider input
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Create a scatter plot
fig, ax = plt.subplots()
ax.scatter(x, y, c="blue", alpha=0.5)
ax.set_title(f"Scatter Plot with {num_points} Points")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Display the plot
st.pyplot(fig)


st.title("Illustrating the Central Limit Theorem with Streamlit")
st.subheader("An App by Tyler Richards")
st.write(
    "This app simulates a thousand coin flips using the chance of heads input below, and then samples with replacement\
          from that population and plots the histogram of the means of the samples in order to illustrate the central limit theorem!"
)
perc_heads = st.number_input(
    label="Chance of Coins Landing on Heads", min_value=0.0, max_value=1.0, value=0.5
)
binom_dist = np.random.binomial(1, perc_heads, 1000)
list_of_means = []
for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())
fig, ax = plt.subplots()
ax = plt.hist(list_of_means)
st.pyplot(fig)

"""
As you probably noticed, every time that we changed the input of our script, Streamlit re-ran the
entire application.
We change this default behaviour in different way, such as adding caching or forms
"""
