# module 1

* Explore and analyze data with Python

  * Explore data with NumPy and Pandas
  * Visualize data
  * Examine real world data

  * nbs
    * `1_1-numpy-and-pandas.ipynb`
    * `1_2-visualize-data.ipynb`
    * `1_3-real-world-data.ipynb`
    * `01 - Flights Challenge.ipynb`

## NumPy, Pandas, Jupyter

NumPy is a Python library that provides functionality comparable to mathematical tools such as MATLAB and R. While NumPy significantly simplifies the user experience, it also offers comprehensive mathematical functions.

Pandas is an extremely popular Python library for data analysis and manipulation. Pandas is like a spreadsheet application for Python, providing easy-to-use functionality for data tables.

Jupyter notebooks are a popular way of running basic scripts using your web browser. Typically, these notebooks are a single webpage, broken up into text sections and code sections that are executed on the server rather than your local machine.

## Visualization

Graphing is done to provide a fast qualitative assessment of our data, which can be useful for understanding results, finding outlier values, examining how numbers are distributed, and so on.

While sometimes we know ahead of time what kind of graph will be most useful, other times we use graphs in an exploratory way

* 2D scatter plots
* proportions (pie charts and stacked bar graphs)
* how the data are spread (histograms and box-and-whisker plots)

## Real world data

Data presented in educational material is often remarkably perfect, designed to show students how to find clear relationships between variables.

Real-world data can contain many different issues that can affect the utility of the data and our interpretation of the results.

It's important to realize that most real-world data are influenced by factors that weren't recorded at the time. For example, we might have a table of race-car track times alongside engine sizes; but various other factors that weren't written down, such as the weather, probably also played a role. If problematic, we can often reduce the influence of these factors by increasing the size of the dataset.

In other situations, data points that are clearly outside of what's expected—also known as "outliers"—can sometimes be safely removed from analyses, although we must take care to not remove data points that provide real insights.

Another common issue in real-world data is bias. Bias refers to a tendency to select certain types of values more frequently than others in a way that misrepresents the underlying population, or "real world". Bias can sometimes be identified by exploring data while keeping in mind basic knowledge about where the data came from.

## Types of ML

* Predictive
  * Supervised machine learning in which the model is trained using data that includes known label values (so an algorithm uses the existing data to establish a relationship between x and y, resulting in a function that can be applied to x to calculate y).
  * Unsupervised machine learning in which the model is trained using only feature (x) values, and groups (or clusters) observations with similar features.
* Generative
* Reinforcement

---

Types of Supervised ML

* Regression algorithms

  in which the label is a numeric value, such as a price, temperature, amount, or other value that can be measured. Regression algorithms produce models in which the function (f) operates on the features (x) to calculate the numeric value of the label (y).

  For example, a regression algorithm could be used to train a model that predicts the expected number of ice creams sold by a kiosk in a park on a given day based on features like the month of the year, the day of the week, the temperature, the humidity, and so on.

* Classification algorithms

  in which the label is a discrete category (or class). Classification algorithms produce models in which the function (f) operates on the features (x) to calculate a probability value for each possible class, and returns the label (y) for the class with the highest probability.

  For example, a classification algorithm could be used to train a model that predicts whether or not a patient has diabetes based on features like blood-insulin level, weight, height, age and so on. A classification model that identifies one of two possible classes (such as true or false) is an example of binary classification. Algorithms that predict probability for more than two classes (for example, differentiating between patients without diabetes, type 1 diabetes, or type 2 diabetes) are used for multiclass classification.
