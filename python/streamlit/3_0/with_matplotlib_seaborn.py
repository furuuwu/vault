import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

"""
# Using Matplotlib and Seaborn
"""

trees_df = pd.read_csv("trees.csv")
st.dataframe(trees_df)
diff_df: pd.Timestamp = pd.to_datetime("today") - pd.to_datetime(trees_df["date"])
trees_df["age"] = diff_df.dt.days
st.write(trees_df["age"])

st.markdown("## default histograms")

"Seaborn"
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df["age"])
plt.xlabel("Age (Days)")
st.pyplot(fig_sb)

"Matploblib"
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df["age"])
plt.xlabel("Age (Days)")
st.pyplot(fig_mpl)

"""
## explicit number of bins
"""

code = """
# Specify the number of bins
num_bins = 20  # Adjust this value as needed

"Seaborn"
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df["age"], bins=num_bins)  # Explicitly set bins
plt.xlabel("Age (Days)")
st.pyplot(fig_sb)

"Matplotlib"
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(
    trees_df["age"], bins=num_bins, edgecolor="black"
)  # Explicitly set bins
plt.xlabel("Age (Days)")
st.pyplot(fig_mpl)
"""

# Specify the number of bins
num_bins = 20  # Adjust this value as needed

"Seaborn"
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df["age"], bins=num_bins)  # Explicitly set bins
plt.xlabel("Age (Days)")
st.pyplot(fig_sb)

"Matplotlib"
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(
    trees_df["age"], bins=num_bins, edgecolor="black"
)  # Explicitly set bins
plt.xlabel("Age (Days)")
st.pyplot(fig_mpl)
