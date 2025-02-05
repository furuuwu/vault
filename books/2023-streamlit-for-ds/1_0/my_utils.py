def show_function_code(func):
    import inspect
    import streamlit as st

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
