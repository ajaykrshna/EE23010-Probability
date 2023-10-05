import numpy as np

# Define the number of random samples to generate
num_samples = 100000

# Generate random samples from the PDF of X using inverse transform sampling
samples_x = np.random.uniform(1, np.exp(2), num_samples)  # Generate samples between 1 and e^2
samples_y = np.log(samples_x)  # Calculate corresponding samples for Y

# Calculate the conditional probability P(Y < 1 | Y < 2) by counting the samples that satisfy the condition
count_y_lt_1 = np.sum(samples_y < 1)
count_y_lt_2 = np.sum(samples_y < 2)

conditional_prob = count_y_lt_1 / count_y_lt_2

print("Simulated Conditional Probability P(Y < 1 | Y < 2) =", conditional_prob)
