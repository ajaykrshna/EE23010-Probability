import numpy as np

# Define the number of random samples to generate
num_samples = 1000

# Generate random samples of X
uniform_samples = np.random.uniform(0, 1, num_samples)
samples_x = 1 / (1 - uniform_samples)

# Calculate Y = ln(X) for the samples
samples_y = np.log(samples_x)

# Count the number of samples where Y < 1, Y < 2, and both conditions
count_y_lt_1 = np.sum(samples_y < 1)
count_y_lt_2 = np.sum(samples_y < 2)

# Calculate the conditional probability P(Y < 1 | Y < 2)
conditional_prob = count_y_lt_1 / count_y_lt_2

print("Conditional Probability P(Y < 1 | Y < 2) =", conditional_prob)
