import numpy as np
import matplotlib.pyplot as plt


def generate_histogram():
    # Generate random data
    data = np.random.randn(1000)  # 1000 random numbers from a normal distribution

    # Create the histogram
    plt.hist(data, bins=30, alpha=0.7, color="blue", edgecolor="black")
    plt.title("Histogram of Random Data")
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    # Save the histogram to a file
    plt.savefig("histogram.png")
    print("Histogram saved as 'histogram.png'")


if __name__ == "__main__":
    generate_histogram()
