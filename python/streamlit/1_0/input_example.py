import streamlit as st

# Text input
user_input = st.text_input("Enter a message:", "Hello, Streamlit!")

# Number input
number_input = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)

# Slider input
slider_input = st.slider(
    "Select a range of values:", min_value=0, max_value=100, value=(25, 75)
)

# Checkbox input
checkbox_input = st.checkbox("Check this box if you agree")

# Select box input
select_input = st.selectbox("Choose a fruit:", ["Apple", "Banana", "Cherry"])

# Display the inputs
st.write("You entered the message:", user_input)
st.write("You entered the number:", number_input)
st.write("You selected the range:", slider_input)
st.write("Checkbox status:", "Checked" if checkbox_input else "Unchecked")
st.write("You chose the fruit:", select_input)
