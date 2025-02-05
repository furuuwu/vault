import streamlit as st

"""
# $\LaTeX$
"""

"""
## using the `st.latex()` function - displays as Block
"""
code = """
# Display a LaTeX equation
st.latex(
    r\"""
    E = mc^2
\"""
)

# Display more complex LaTeX
st.latex(
    r\"""
    f(x) = \int_{-\infty}^{\infty} e^{-x^2} dx
\"""
)
"""
st.code(code, language="python")

# Display a LaTeX equation
st.latex(
    r"""
    E = mc^2
"""
)

# Display more complex LaTeX
st.latex(
    r"""
    f(x) = \int_{-\infty}^{\infty} e^{-x^2} dx
"""
)

"""
## using `st.markdown()` - displays Inline
"""
code = """
st.markdown(r"Here is an inline equation: $f(x) = x^2 + 3x + 2$")
"""
st.code(code, language="python")
st.markdown(r"Here is an inline equation: $f(x) = x^2 + 3x + 2$")

"""
## inside markdown implicitly
"""

code = """
\"""
$f(x) = x^2 + 3x + 2$
\"""
"""
st.code(code, language="python")
"""
this is inline: $f(x) = x^2 + 3x + 2$
"""
