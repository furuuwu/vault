import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

"""
# The Central Limit Theorem

It says that if we take samples from some probability distribution enough times, the mean of those samples
would approximate a normal distribution.

From the [Wikipedia](https://en.wikipedia.org/wiki/Central_limit_theorem):
> In probability theory, the central limit theorem (CLT) states that, under appropriate conditions, 
the distribution of a normalized version of the sample mean converges to a standard normal distribution. 
This holds even if the original variables themselves are not normally distributed.

> In other words, suppose that a large sample of observations is obtained, each observation being randomly 
produced in a way that does not depend on the values of the other observations, and the average 
(arithmetic mean) of the observed values is computed. If this procedure is performed many times, 
resulting in a collection of observed averages, the central limit theorem says that if the sample size 
is large enough, the probability distribution of these averages will closely approximate a normal distribution.

> In statistics, the CLT can be stated as: let $X_1, X_2, \ldots, X_n$ denote a statistical sample of size $n$
from a population with expected value (average) $\mu$ and finite positive variance $\sigma^2$, and let $\\bar{X_n}$
denote the sample mean (which is itself a random variable). Then the limit as $n \\to 0$ of the distribution of
$(\\bar{X_n} - \mu)\sqrt{n}$ is a normal distribution with mean $0$ and variance $\sigma^2$.
"""

"""
## Eg. with a normal distribution

* Simulate 1,000 coin flips and stores those values in a list
"""

code = """
binom_dist = np.random.binomial(n=1, p=0.5, size=1000)
st.write(binom_dist)
"""
st.code(code, language="python")

binom_dist = np.random.binomial(n=1, p=0.5, size=1000)
st.write(binom_dist)

"""
n=1: The number of trials in each experiment (only one trial in this case).
p=0.5: The probability of success in each trial.
size=100: The number of independent experiments to run (generating an array of 100 samples).

When n=1, the binomial distribution essentially becomes a Bernoulli distribution, 
where each sample is either 0 (failure) or 1 (success) with probabilities 1-p and p, respectively.
"""

"""
(Optional) Plot the distribution
* with an histogram
* with a bar chart (more appropriate)
"""
fig, ax = plt.subplots()
ax = plt.hist(binom_dist)
st.pyplot(fig)

# Calculate the frequency of 0's and 1's
unique, counts = np.unique(binom_dist, return_counts=True)
# Create the bar chart
fig, ax = plt.subplots()
ax.bar(unique, counts, color="blue", edgecolor="black")
# Set x-axis ticks to show only 0 and 1
ax.set_xticks([0, 1])
# Add labels and title
ax.set_title("Binomial Distribution (n=1, p=0.5)")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
# Display the plot
st.pyplot(fig)

"""
* Sampling with replacement

Take 200 samples from the binomial distribution with replacement
"""
code = """np.random.choice(binom_dist, size=200, replace=True)"""
st.code(code, language="python")
st.write("the samples: ", np.random.choice(binom_dist, 200, replace=True))

"""
* Calculate their mean

Calculate the mean of the 200 samples.
This should be approximately equal to the probability p, which is 0.5 in this case.
"""

code = """np.mean(binom_dist)"""
st.code(code, language="python")
st.write("mean of the samples: ", np.mean(binom_dist))

"""
* Repeat for the sampling 1000 times

Run the sampling process 1000 times and calculate the mean of each sample.
"""
code = """
list_of_means = []
for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, size=200, replace=True).mean())
"""
st.code(code, language="python")
list_of_means = []
for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, size=200, replace=True).mean())

st.write("list of means: ", list_of_means)
st.write("mean of the means: ", np.mean(list_of_means))

"""
* Now plot the means

Plot the histogram of the means to visualize the distribution of the sample means.
"""
code = """
fig, ax = plt.subplots()
ax = plt.hist(list_of_means)
st.pyplot(fig)
"""
st.code(code, language="python")
fig, ax = plt.subplots()
ax = plt.hist(list_of_means)
st.pyplot(fig)

"""
The Central Limit Theorem guarantees that the distribution of the sample means will be approximately normal, regardless of the shape of the original distribution.
This is why we can use the mean and standard deviation of the sample means to make inferences about the original distribution.


Here's the final code in a single place:
"""
code = """
binom_dist = np.random.binomial(1, .5, 10000)
list_of_means = []
for i in range(0, 1000):
    samples = np.random.choice(binom_dist, 200, replace=True)
    list_of_means.append(samples.mean())
fig, ax = plt.subplots()
ax = plt.hist(list_of_means)
st.pyplot(fig)
"""
st.code(code, language="python")

binom_dist = np.random.binomial(1, 0.5, 10000)
list_of_means = []
for i in range(0, 1000):
    samples = np.random.choice(binom_dist, 200, replace=True)
    list_of_means.append(samples.mean())
fig, ax = plt.subplots()
ax = plt.hist(list_of_means)
st.pyplot(fig)

"""
## Eg. with a uniform distribution
"""

code = """
uniform_dist = np.random.uniform(low=0, high=50, size=1000)
list_of_means = []
for i in range(0, 1000):
    samples = np.random.choice(uniform_dist, 200, replace=True)
    list_of_means.append(samples.mean())
fig, ax = plt.subplots()
ax = plt.hist(list_of_means)
st.pyplot(fig)
"""
st.code(code, language="python")

uniform_dist = np.random.uniform(low=0, high=50, size=1000)

"""
(Optional) Plot the distribution
"""
fig, ax = plt.subplots()
ax = plt.hist(uniform_dist)
st.pyplot(fig)

"""
Plot the distribution of the means
"""
list_of_means = []
for i in range(0, 1000):
    samples = np.random.choice(uniform_dist, 200, replace=True)
    list_of_means.append(samples.mean())
fig, ax = plt.subplots()
ax = plt.hist(list_of_means)
st.pyplot(fig)

"""
The distribution of the means becomes normal in the limit, so increasing n should make it more evident. 
Also, ajust the number of bins 
"""
code = """
uniform_dist = np.random.uniform(low=0, high=50, size=10000)
list_of_means = []
for i in range(0, 10000):
    samples = np.random.choice(uniform_dist, 200, replace=True)
    list_of_means.append(samples.mean())
fig, ax = plt.subplots()
ax = plt.hist(x=list_of_means, bins=25)
st.pyplot(fig)
"""
st.code(code, language="python")

uniform_dist = np.random.uniform(low=0, high=50, size=10000)
fig, ax = plt.subplots()
ax = plt.hist(uniform_dist)
st.pyplot(fig)
list_of_means = []
for i in range(0, 10000):
    samples = np.random.choice(uniform_dist, 200, replace=True)
    list_of_means.append(samples.mean())
fig, ax = plt.subplots()
ax = plt.hist(x=list_of_means, bins=25)
st.pyplot(fig)

"""
## Eg. with a exponential distribution
"""

code = """
exponential_dist = np.random.exponential(scale=1, size=10000)
list_of_means = []
for i in range(0, 10000):
    samples = np.random.choice(exponential_dist, 200, replace=True)
    list_of_means.append(samples.mean())
fig, ax = plt.subplots()
ax = plt.hist(x=list_of_means, bins=25)
st.pyplot(fig)
"""
st.code(code, language="python")

exponential_dist = np.random.exponential(scale=1, size=10000)
fig, ax = plt.subplots()
ax = plt.hist(exponential_dist)
st.pyplot(fig)
list_of_means = []
for i in range(0, 10000):
    samples = np.random.choice(exponential_dist, 200, replace=True)
    list_of_means.append(samples.mean())
fig, ax = plt.subplots()
ax = plt.hist(x=list_of_means, bins=25)
st.pyplot(fig)

"""
This should be empirical evidence enough (for those who don't like math)!
"""
