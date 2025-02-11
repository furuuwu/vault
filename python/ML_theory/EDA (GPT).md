# EDA (GPT)

## QUESTION: overview of EDA

**Exploratory Data Analysis (EDA)** is the process of analyzing and summarizing datasets to uncover patterns, spot anomalies, test hypotheses, and check assumptions. It often involves using visualizations and statistical techniques to gain insights into the data. EDA helps prepare data for modeling by identifying missing values, understanding distributions, and finding correlations.

### Steps in EDA

1. **Data Inspection**: Understand the structure and basic properties of the data.
2. **Data Cleaning**: Handle missing or incorrect data.
3. **Data Visualization**: Create plots and charts to visualize distributions and relationships.
4. **Feature Engineering**: Identify important features and create new ones if needed.
5. **Statistical Analysis**: Perform basic statistical checks like correlation, variance, etc.

---

### Python Code Examples for EDA

Below is a step-by-step approach to EDA with examples using Python.

---

#### 1. **Loading Data**

```python
import pandas as pd

# Load a sample dataset (e.g., Titanic dataset from seaborn)
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Display the first few rows
print(df.head())
```

---

#### 2. **Data Inspection**

```python
# Check the shape of the dataset
print("Shape of the dataset:", df.shape)

# View data types of columns
print(df.dtypes)

# Check for missing values
print(df.isnull().sum())

# Summary statistics
print(df.describe(include='all'))
```

---

#### 3. **Data Cleaning**

Handle missing values and incorrect data.

```python
# Fill missing Age with the median value
df['Age'].fillna(df['Age'].median(), inplace=True)

# Drop rows with missing Embarked values
df.dropna(subset=['Embarked'], inplace=True)

# Replace incorrect values (example)
df['Fare'] = df['Fare'].apply(lambda x: 0 if x < 0 else x)
```

---

#### 4. **Data Visualization**

Using Matplotlib and Seaborn to create visualizations.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Distribution of Age
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=20, kde=True, color='blue')
plt.title('Age Distribution')
plt.show()

# Survival count
sns.countplot(x='Survived', data=df, palette='Set2')
plt.title('Survival Count')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
```

---

#### 5. **Feature Engineering**

Create new features from existing ones.

```python
# Create a new feature 'FamilySize' from 'SibSp' and 'Parch'
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Bin ages into categories
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 60, 100], labels=['Child', 'Teen', 'Adult', 'Senior'])
```

---

#### 6. **Statistical Analysis**

```python
# Correlation of numeric features with Survival
print(df.corr()['Survived'].sort_values())

# Grouped statistics
print(df.groupby('Pclass')['Fare'].mean())

# Chi-Square test for categorical variables
from scipy.stats import chi2_contingency

contingency_table = pd.crosstab(df['Pclass'], df['Survived'])
chi2, p, dof, expected = chi2_contingency(contingency_table)
print("Chi-square test statistic:", chi2)
print("p-value:", p)
```

---

### Tips for EDA

1. **Focus on the Target Variable**: Understand the distribution and relationships involving the dependent variable (e.g., `Survived` in Titanic).
2. **Iterate and Experiment**: Try different visualizations and transformations to explore the data.
3. **Handle Outliers**: Use boxplots or statistical methods to detect and treat outliers.
4. **Document Insights**: Note patterns, anomalies, or potential issues for further investigation.

## QUESTION: distribution of the variables

The distribution of features and target values provides insight into the nature of the data. It helps identify patterns, detect outliers, and understand the relationships between variables. For the target variable, analyzing its distribution is essential to determine whether it's balanced or imbalanced, which can influence model selection and evaluation metrics.

### **Why is Distribution Analysis Important?**

1. **Feature Understanding**: Helps understand whether features are categorical, continuous, or ordinal.
2. **Data Cleaning**: Detects missing values, outliers, or anomalies in the data.
3. **Model Selection**: Certain machine learning models assume specific distributions of data.
4. **Imbalanced Data**: A heavily imbalanced target variable can lead to biased models.
5. **Feature Transformation**: Suggests transformations (e.g., log, standardization) for skewed features.

---

### **Visualizing Feature Distributions**

Here’s how you can visualize distributions using Python.

#### **1. Histogram for Continuous Features**

```python
import matplotlib.pyplot as plt

# Visualize the distribution of 'Age'
plt.figure(figsize=(8, 5))
df['Age'].hist(bins=20, color='blue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
```

#### **2. Count Plot for Categorical Features**

```python
import seaborn as sns

# Count plot for 'Pclass' (Passenger Class)
sns.countplot(x='Pclass', data=df, palette='Set2')
plt.title('Pclass Distribution')
plt.xlabel('Pclass')
plt.ylabel('Count')
plt.show()
```

#### **3. Boxplot for Outliers**

```python
# Boxplot for 'Fare'
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Fare'], color='lightblue')
plt.title('Fare Distribution with Outliers')
plt.show()
```

---

### **Analyzing Target Variable Distribution**

Understanding the target variable helps in identifying class imbalance and guides model evaluation.

#### **1. Distribution of the Target Variable**

```python
# Count plot for 'Survived'
sns.countplot(x='Survived', data=df, palette='Set1')
plt.title('Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.show()
```

#### **2. Checking Class Balance**

```python
# Class proportions
target_counts = df['Survived'].value_counts(normalize=True)
print(target_counts)

# Check imbalance
if target_counts[0] / target_counts[1] > 1.5:
    print("Target variable is imbalanced.")
else:
    print("Target variable is relatively balanced.")
```

---

### **Relevance of Analyzing Distributions**

#### **1. Detecting Skewness**

Skewed data can mislead models. For instance, in regression problems, skewed features may require a log or Box-Cox transformation to normalize distributions.

#### **2. Identifying Outliers**

Outliers can distort models, especially those sensitive to scales (e.g., linear regression, k-means). Boxplots and histograms help detect them.

#### **3. Handling Missing Values**

Understanding distributions helps in deciding how to impute missing values. For example, use the median for skewed data and the mean for normally distributed data.

#### **4. Target Variable Insights**

- **Binary Classification**: Class imbalance affects metrics like accuracy. Use techniques like SMOTE or stratified sampling for balancing.
- **Regression**: Analyze the spread of the target variable for homoscedasticity (constant variance).

---

### Example: Combined Analysis of Features and Target

You can analyze how features interact with the target variable.

#### Distribution of Age for Survival

```python
sns.histplot(data=df, x='Age', hue='Survived', multiple='stack', bins=20, kde=True, palette='Set2')
plt.title('Age Distribution by Survival')
plt.show()
```

#### Boxplot of Fare by Survival

```python
sns.boxplot(x='Survived', y='Fare', data=df, palette='coolwarm')
plt.title('Fare Distribution by Survival')
plt.show()
```
