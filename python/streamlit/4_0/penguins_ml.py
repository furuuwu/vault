"# modeling"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"## Loading the data"
penguin_df = pd.read_csv("penguins.csv")
print(penguin_df.head())
penguin_df.dropna(inplace=True)

"## Defining the output and feature variables"
# Encode the output labels
# output = penguin_df["species"]
output, uniques = pd.factorize(penguin_df["species"])
print("Class mapping (species to numeric):", list(enumerate(uniques)))

# Extract and preprocess features
features = penguin_df[
    [
        "island",
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
        "sex",
    ]
]
features = pd.get_dummies(features)
print("Here are our output variables")
print(output[:5])
print("Here are our feature variables")
print(features.head())

"## Classification using a random forest model"

"### Training the model"

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    features, output, test_size=0.2, random_state=42
)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

"### Making predictions"

predictions = clf.predict(X_test)
print("Predictions:")
print(predictions)
# Decode predictions to original species
decoded_predictions = uniques[predictions]
print("Decoded Predictions (Species):")
print(decoded_predictions)

"### Evaluating the model"

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

"### Saving and loading the model"
"* using `joblib`"

import joblib

# Save model and mappings
joblib.dump(clf, "models/model_joblib.joblib")
joblib.dump(uniques, "models/class_mapping_joblib.joblib")

# Load model and mappings
from numpy.typing import NDArray

loaded_model: RandomForestClassifier = joblib.load("models/model_joblib.joblib")
loaded_uniques: NDArray = joblib.load("models/class_mapping_joblib.joblib")


"* using `pickle`"

import pickle

# Save model and mappings
with open("models/model_pickle.pkl", "wb") as f:
    pickle.dump(clf, f)

with open("models/class_mapping_pickle.pkl", "wb") as f:
    pickle.dump(uniques, f)

# Load model and mappings
with open("models/model_pickle.pkl", "rb") as f:
    loaded_model: RandomForestClassifier = pickle.load(f)

with open("models/class_mapping_pickle.pkl", "rb") as f:
    loaded_uniques: NDArray = pickle.load(f)

# Test predictions with loaded model and mapping
loaded_predictions = loaded_model.predict(X_test)
loaded_decoded_predictions = loaded_uniques[loaded_predictions]
print("Decoded Predictions from Loaded Model:")
print(loaded_decoded_predictions)

"### Model explanation"
# Plot feature importance
fig, ax = plt.subplots()
ax = sns.barplot(x=clf.feature_importances_, y=features.columns)
plt.title("Which features are the most important for species prediction?")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.tight_layout()
fig.savefig("models/feature_importance.png")
