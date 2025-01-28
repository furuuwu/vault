import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import inspect

"""
# Code blocks
"""


# Generalized function to display the source code of another function
def show_function_code(func):
    """
    Displays the source code of the provided function using st.code().
    Args:
        func (callable): The function whose code will be displayed.
    """
    try:
        code_text = inspect.getsource(func)  # Get the source code of the function
        st.code(code_text, language="python")
    except Exception as e:
        st.error(f"Could not retrieve code: {e}")


# Function containing the actual code logic
def scatter_plot_example():
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


st.write("Hellow, world! uwu")
"""
`Hellow, world! uwu`

```python
print("Hellow, world! uwu")
```
"""

code = """
one_to_ten = np.arange(1, 11)
st.write(one_to_ten)
"""

st.code(code, language="python")
one_to_ten = np.arange(1, 11)
st.write(one_to_ten)

# Display the code of the scatter_plot_example function
show_function_code(scatter_plot_example)

# Execute the scatter plot example
scatter_plot_example()
