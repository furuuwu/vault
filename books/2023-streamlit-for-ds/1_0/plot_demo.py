"""
* create a line chart that starts at a random number sampled from a normal
distribution with mean 0 and variance 1. 
* run a for loop that keeps sampling new random numbers in bunches of 5
and adding that to the sum we had before while waiting for a
twentieth of a second so we can see the graph change, simulating an animation
"""

import streamlit as st
import time
import numpy as np

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(50, 1).cumsum(
        axis=0
    )  # above 100 gets slow on my machine.
    status_text.text(f"{i}% complete")
    # status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Rerun")
