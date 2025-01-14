#

<https://developers.google.com/machine-learning/crash-course>

ML Models

* Linear Regression: `linear_regression_taxi.ipynb`

  * Explain a loss function and how it works.
  * Define and describe how gradient descent finds the optimal model parameters.
  * Describe how to tune hyperparameters to efficiently train a linear model.

* Logistic Regression: `binary_classification_rice.ipynb`

  * Identify use cases for performing logistic regression.
  * Explain how logistic regression models use the sigmoid function to calculate probability.
  * Compare linear regression and logistic regression.
  * Explain why logistic regression uses log loss instead of squared loss.
  * Explain the importance of regularization when training logistic regression models.

* Classification

  * Determine an appropriate threshold for a binary classification model.
  * Calculate and choose appropriate metrics to evaluate a binary classification model.
  * Interpret ROC and AUC.

Data

* Working with numerical data: `numerical_data_stats.ipynb`, `numerical_data_bad_values.ipynb`

  * Understand feature vectors.
  * Explore your dataset's potential features visually and mathematically.
  * Identify outliers.
  * Understand four different techniques to normalize numerical data.
  * Understand binning and develop strategies for binning numerical data.
  * Understand the characteristics of good continuous numerical features.
  * links
    * <https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html>
    * <https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html>

* Working with categorical data

  * Distinguish categorical data from numerical data.
  * Represent categorical data with one-hot vectors.
  * Address common issues with categorical data.
  * Create feature crosses.

* Datasets, generalization, and overfitting

  * Identify four different characteristics of data and datasets.
  * Identify at least four different causes of data unreliability.
  * Determine when to discard missing data and when to impute it.
  * Differentiate between direct and derived labels.
  * Identify two different ways to improve the quality of human-rated labels.
  * Explain why to subdivide a dataset into a training set, validation set, and test set; identify a potential problem in data splits.
  * Explain overfitting and identify three possible causes for it.
  * Explain the concept of regularization. In particular, explain the following:
  * Bias versus variance (adaptation to outliers…)
  * L2 regularization, including Lambda (regularization rate)
  * Early stopping
  * Interpret different kinds of loss curves; detect convergence and overfitting in loss curves.

Advanced ML methods

* Neural networks
  * Explain the motivation for building neural networks, and the use cases they address.
  * Define and explain the function of the key components of a deep neural network architecture: Nodes, Hidden layers, Activation functions
  * Develop intuition around how neural network predictions are made, by stepping through the inference process.
  * Build a high-level intuition of how neural networks are trained, using the backpropagation algorithm.
  * Explain how neural networks can be used to perform two types of multi-class classification: one-vs.-all and one-vs.-one.
  * links

    * <https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/>
* Embeddings

  * Visualize vector representations of word embeddings, such as word2vec.
  * Distinguish encoding from embedding.
  * Describe contextual embedding.
* Large Language Models
  * Define a few different types of language models and their components.
  * Describe how large language models are created and the importance of context and parameters.
  * Identify how large language models take advantage of self-attention.
  * Reveal three key problems with large language models.
  * Explain how fine-tuning and distillation can improve a model's predictions and efficiency.

Real-worlds ML

* Production ML systems

  * Appreciate the breadth of components in a production ML system.
  * Pick the ideal training paradigm (static versus dynamic).
  * Pick the ideal inference paradigm (static versus dynamic).
  * Test your machine learning deployment.
  * Ask the right questions about your production ML system.
  * Determine flaws in real-world ML models.
  * Monitor the components in a production ML system.
* Automated ML
  * Automate tasks in a machine learning workflow.
  * Determine the benefits and limitations of using AutoML with your machine learning model.
  * Enumerate the common AutoML patterns and apply them to your ML projects.
* Fairness
  * Become aware of common human biases that can inadvertently be reproduced by ML algorithms.
  * Proactively explore data to identify sources of bias before training a model.
  * Evaluate model predictions for bias.

my rating: 9/10
