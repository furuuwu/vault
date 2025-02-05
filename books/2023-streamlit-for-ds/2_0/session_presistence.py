import streamlit as st

st.title("To-Do App")

"""
* Simplified state management

Streamlit avoids the complexity of manually updating individual UI 
elements by rerunning the entire script. 
This approach ensures that the app's state is always consistent with the 
latest inputs and interactions, eliminating bugs caused by partial updates 
or stale state.

* Declarative programming model

Streamlit uses a declarative model where the code describes what the UI
should look like based on the current state, rather than specifying how 
to update individual elements. By rerunning the script, Streamlit generates
the entire UI anew, reflecting the updated state seamlessly.

* Lightweight and Efficient

Although it may seem inefficient, Streamlit reruns are optimized. 
The framework caches computations, objects, and other elements where 
possible (e.g., using `@st.cache` or `st.session_state`), minimizing 
redundant work. 
Only elements directly affected by the user's interaction are updated on 
the frontend.


TLDR Streamlit automatically re-runs your script from top to bottom 
every time the user interacts with the UI (e.g., by clicking a button 
or entering text). 
This behavior ensures that the app remains responsive and updates dynamically.
"""

code = """
# All that talk means this won't work
my_todo_list = ["Buy groceries", "Learn Streamlit", "Learn Python"]

new_todo = st.text_input("What do you need to do?")
if st.button("Add the new To-Do item"):
    st.write("Adding a new item to the list")
    my_todo_list.append(new_todo)
st.write("Todos:", my_todo_list)
"""
st.code(code, language="python")

my_todo_list = ["Buy groceries", "Learn Streamlit", "Learn Python"]

new_todo = st.text_input("What do you need to do?")
if st.button("Add the new To-Do item"):
    st.write("Adding a new item to the list")
    my_todo_list.append(new_todo)
st.write("Todos:", my_todo_list)

"""
Notice you are unable to add multiple items to the list.

The issue with the current implementation: 
the `my_todo_list` is re-initialized every time the script runs, 
so your updates will not persist between interactions. 
To fix this, you can use Streamlit's `st.session_state` to persist the 
state of the to-do list across interactions.
"""
code = """
# Initialize the to-do list in session state if it doesn't already exist
if "my_todo_list2" not in st.session_state:
    st.session_state.my_todo_list2 = [
        "Buy groceries",
        "Learn Streamlit",
        "Learn Python",
    ]

new_todo = st.text_input("What do you need to do?", key="todo_input_2")
if st.button("Add the new To-Do item", key="add_button_2"):
    if new_todo:  # Only add if the input is not empty
        st.session_state.my_todo_list2.append(new_todo)
        st.success(f'Added "{new_todo}" to the list!')
    else:
        st.warning("Please enter a valid To-Do item.")

st.write("Todos:", st.session_state.my_todo_list2
"""
st.code(code, language="python")

# Initialize the to-do list in session state if it doesn't already exist
if "my_todo_list2" not in st.session_state:
    st.session_state.my_todo_list2 = [
        "Buy groceries",
        "Learn Streamlit",
        "Learn Python",
    ]

new_todo = st.text_input("What do you need to do?", key="todo_input_2")
if st.button("Add the new To-Do item", key="add_button_2"):
    if new_todo:  # Only add if the input is not empty
        st.session_state.my_todo_list2.append(new_todo)
        st.success(f'Added "{new_todo}" to the list!')
    else:
        st.warning("Please enter a valid To-Do item.")

st.write("Todos:", st.session_state.my_todo_list2)

"""
Also, notice I assigned a key to the buttons


When a element is created, Streamlit assigns it an internal ID based 
on the element type and provided parameters. 
Having duplicate IDs (e.g., identical labels without a unique key) 
causes conflicts - it will cause the error
> `streamlit.errors.StreamlitDuplicateElementId`: There are multiple
text_input elements with the same auto-generated ID
"""
