# File: my_numpy_example.py

import numpy as np

# Create a numpy array of 10 random floats between 0 and 1
random_floats = np.random.rand(10)

# Calculate mean, median, and standard deviation
mean_value = np.mean(random_floats)
median_value = np.median(random_floats)
std_deviation = np.std(random_floats)

# Print the results
print(f"Random Floats: {random_floats}")
print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")


# I used the chat GPT to learn about the mean, medain and st method of the numpy. 