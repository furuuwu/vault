import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier
from numpy.typing import NDArray
import pandas as pd

"# Using a pretrained model"

"## Load the trained model and mappings"
code = """
with open("models/model_pickle.pkl", "rb") as f:
    model: RandomForestClassifier = pickle.load(f)

with open("models/class_mapping_pickle.pkl", "rb") as f:
    mappings: NDArray = pickle.load(f)
"""
st.code(code, language="python")

with open("models/model_pickle.pkl", "rb") as f:
    model: RandomForestClassifier = pickle.load(f)

with open("models/class_mapping_pickle.pkl", "rb") as f:
    mappings: NDArray = pickle.load(f)

st.write("model: ", model)
st.write("mappings: ", mappings)

"## Get new penguin from user's input"

"We need the island, bill length, bill depth, flipper length, \
    body mass, and sex to predict the penguin species"

code = """
island = st.selectbox("Penguin Island", options=["Biscoe", "Dream", "Torgerson"])
sex = st.selectbox("Sex", options=["Female", "Male"])
bill_length = st.number_input("Bill Length (mm)", min_value=0)
bill_depth = st.number_input("Bill Depth (mm)", min_value=0)
flipper_length = st.number_input("Flipper Length (mm)", min_value=0)
body_mass = st.number_input("Body Mass (g)", min_value=0)
user_inputs = [island, sex, bill_length, bill_depth, flipper_length, body_mass]
"""
st.code(code, language="python")

island = st.selectbox(
    "Penguin Island",
    options=["Biscoe", "Dream", "Torgerson"],
    index=0,  # Default to first option ("Biscoe")
)
sex = st.selectbox("Sex", options=["Female", "Male"], index=0)
bill_length = st.number_input(
    "Bill Length (mm)", min_value=0, value=44  # Default value
)
bill_depth = st.number_input("Bill Depth (mm)", min_value=0, value=15)
flipper_length = st.number_input("Flipper Length (mm)", min_value=0, value=200)
body_mass = st.number_input("Body Mass (g)", min_value=0, value=4500)
user_inputs = [island, sex, bill_length, bill_depth, flipper_length, body_mass]
st.write(f"""the user inputs are {user_inputs}""".format())

"## Apply the same pre-processing"

"our model does not have one variable called \
sex but instead has two variables called sex_female and sex_male"

code = """
# One way of doing it would be...
island_biscoe, island_dream, island_torgerson = 0, 0, 0
if island == "Biscoe":
    island_biscoe = 1
elif island == "Dream":
    island_dream = 1
elif island == "Torgerson":
    island_torgerson = 1

sex_female, sex_male = 0, 0
if sex == "Female":
    sex_female = 1
elif sex == "Male":
    sex_male = 1

new_prediction = model.predict(
    [
        [
            bill_length,
            bill_depth,
            flipper_length,
            body_mass,
            island_biscoe,
            island_dream,
            island_torgerson,
            sex_female,
            sex_male,
        ]
    ]
)
prediction_species = mappings[new_prediction][0]
"""
st.code(code, language="python")

code = """
# A better way
# Collect inputs into a DataFrame for easy preprocessing
user_inputs = pd.DataFrame(
    [[island, sex, bill_length, bill_depth, flipper_length, body_mass]],
    columns=[
        "island",
        "sex",
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
    ],
)

# Apply the same preprocessing as during model training
# Convert categorical variables into dummy variables
user_inputs_dummies = pd.get_dummies(user_inputs, columns=["island", "sex"])

# Ensure the correct order of columns (same as the training data)
required_columns = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
    "island_Biscoe",
    "island_Dream",
    "island_Torgersen",
    "sex_female",
    "sex_male",
]

# Add missing columns with default value 0 if needed
for col in required_columns:
    if col not in user_inputs_dummies.columns:
        user_inputs_dummies[col] = 0

# Reorder columns to match the model's input format
user_inputs_dummies = user_inputs_dummies[required_columns]
"""
st.code(code, language="python")

# Collect inputs into a DataFrame for easy preprocessing
user_inputs = pd.DataFrame(
    [[island, sex, bill_length, bill_depth, flipper_length, body_mass]],
    columns=[
        "island",
        "sex",
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
    ],
)

# Apply the same preprocessing as during model training
# Convert categorical variables into dummy variables
user_inputs_dummies = pd.get_dummies(user_inputs, columns=["island", "sex"])

# Ensure the correct order of columns (same as the training data)
required_columns = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
    "island_Biscoe",
    "island_Dream",
    "island_Torgersen",
    "sex_female",
    "sex_male",
]

# Add missing columns with default value 0 if needed
for col in required_columns:
    if col not in user_inputs_dummies.columns:
        user_inputs_dummies[col] = 0

# Reorder columns to match the model's input format
user_inputs_dummies = user_inputs_dummies[required_columns]

"## Make the prediction"

code = """
new_prediction = model.predict(user_inputs_dummies)
prediction_species = mappings[new_prediction][0]
st.write(f"We predict your penguin is of the {prediction_species} species")
"""
st.code(code, language="python")

new_prediction = model.predict(user_inputs_dummies)
prediction_species = mappings[new_prediction][0]
st.write(f"We predict your penguin is of the {prediction_species} species")

"## Model explanation"
st.write(
    """We used a machine learning (Random Forest)
model to predict the species, the features
used in this prediction are ranked by
relative importance below."""
)
st.image("models/feature_importance.png")

st.write(
    """Below are the histograms for each
continuous variable separated by penguin
species. The vertical line represents
your the inputted value."""
)
import matplotlib.pyplot as plt
import seaborn as sns

penguin_df = pd.read_csv("penguins.csv")
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["bill_length_mm"], hue=penguin_df["species"])
plt.axvline(bill_length)
plt.title("Bill Length by Species")
st.pyplot(ax)
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["bill_depth_mm"], hue=penguin_df["species"])
plt.axvline(bill_depth)
plt.title("Bill Depth by Species")
st.pyplot(ax)
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["flipper_length_mm"], hue=penguin_df["species"])
plt.axvline(flipper_length)
plt.title("Flipper Length by Species")
st.pyplot(ax)
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["body_mass_g"], hue=penguin_df["species"])
plt.axvline(body_mass)
plt.title("Body Mass by Species")
st.pyplot(ax)
