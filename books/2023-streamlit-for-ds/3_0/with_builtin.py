import streamlit as st
import pandas as pd
import numpy as np
import io

st.title("Visualization - using Streamlit's builtin functions")
st.write("""This app analyzes the San Francisco trees dataset""")
trees_df = pd.read_csv("trees.csv")
st.write(trees_df.head())

"""
Info
"""

code = """
# this doesn't work
# st.write(trees_df.info())

buffer = io.StringIO()  # Create an in-memory buffer
trees_df.info(buf=buffer)  # Redirect the output of info() to the buffer
info_str = buffer.getvalue()  # Get the string from the buffer
st.text(info_str)  # Display the information as plain text
"""
st.code(code, language="python")

buffer = io.StringIO()  # Create an in-memory buffer
trees_df.info(buf=buffer)  # Redirect the output of info() to the buffer
info_str = buffer.getvalue()  # Get the string from the buffer
st.text(info_str)  # Display the information as plain text

st.write("Another option is converting to html")
code = """
# Extract info-like details
info_data = {
    "Column": trees_df.columns,
    "Non-Null Count": trees_df.notnull().sum(),
    "Dtype": trees_df.dtypes
}

# Create a DataFrame for the info data
info_df = pd.DataFrame(info_data)

# Convert to HTML
html_table = info_df.to_html(index=False, escape=False)

# Display in Streamlit
st.markdown(html_table, unsafe_allow_html=True)
"""
st.code(code, language="python")

# Extract info-like details
info_data = {
    "Column": trees_df.columns,
    "Non-Null Count": trees_df.notnull().sum(),
    "Dtype": trees_df.dtypes,
}

# Create a DataFrame for the info data
info_df = pd.DataFrame(info_data)

# Convert to HTML
html_table = info_df.to_html(index=False, escape=False)

# Display in Streamlit
st.markdown(html_table, unsafe_allow_html=True)

"""
dbh - Diameter at Breast Height (width of the tree at chest height). Unique vaues:
"""
st.write(trees_df["dbh"].unique())

"""
* `st.line_chart()`
* `st.bar_chart()`
* `st.area_chart()`
* `st.map()`
"""

"""
* Group the trees by width, count the unique trees of each width
"""
code = """
# Group the DataFrame by the "dbh" column and count occurrences for each group
grouped = trees_df.groupby(["dbh"]).count()

# Select the "tree_id" column from the grouped result
tree_id_counts = grouped["tree_id"]

# Convert the resulting Series into a new DataFrame
df_dbh_grouped = pd.DataFrame(tree_id_counts)

# Rename the column "tree_id" to "tree_count" in the new DataFrame
df_dbh_grouped.columns = ["tree_count"]

---

# another way to do this
df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"])
df_dbh_grouped.columns = ["tree_count"]
"""
st.code(code, language="python")

# Group the DataFrame by the "dbh" column and count occurrences for each group
grouped = trees_df.groupby(["dbh"]).count()

# Select the "tree_id" column from the grouped result
tree_id_counts = grouped["tree_id"]

# Convert the resulting Series into a new DataFrame
df_dbh_grouped = pd.DataFrame(tree_id_counts)

# Rename the column "tree_id" to "tree_count" in the new DataFrame
df_dbh_grouped.columns = ["tree_count"]

st.write(df_dbh_grouped.head())

"""
* Plots
"""
code = """
# make a line, bar, and area chart of each
st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)
"""
st.code(code, language="python")

st.line_chart(df_dbh_grouped)
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

"""
if the dataset has more columns, it plots them all
"""
code = """
df_dbh_grouped["new_col"] = np.random.randn(len(df_dbh_grouped)) * 500
st.line_chart(df_dbh_grouped)
"""
st.code(code, language="python")

df_dbh_grouped["new_col"] = np.random.randn(len(df_dbh_grouped)) * 500
st.line_chart(df_dbh_grouped)

"""
explicitly tell Streamlit the variables that we want to plot 
on the x and y axes
"""
code = """
# Group by 'dbh' and count the number of trees for each 'dbh'
df_dbh_grouped = trees_df.groupby("dbh").size().reset_index(name="tree_count")

# plot
st.line_chart(df_dbh_grouped, x="dbh", y="tree_count")

---

# another way
df_dbh_grouped = pd.DataFrame(
    trees_df.groupby(["dbh"]).count()["tree_id"]
).reset_index()
df_dbh_grouped.columns = ["dbh", "tree_count"]
st.line_chart(df_dbh_grouped, x="dbh", y="tree_count")
"""
st.code(code, language="python")

# Group by 'dbh' and count the number of trees for each 'dbh'
df_dbh_grouped = trees_df.groupby("dbh").size().reset_index(name="tree_count")

# Plot using Streamlit's line chart
st.line_chart(df_dbh_grouped, x="dbh", y="tree_count")

code = """
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n = 1000)
st.map(trees_df)
"""
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.sample(n=1000)
st.map(trees_df)

"""
As with other functions, we don't have many options for customization here 
other than an optional zoom parameter, but this works very well for 
quick visualization.
"""
