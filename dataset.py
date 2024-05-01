import random

# Number of bins
num_bins = 10000

# Generate random weights for each bin
weights = [random.randint(1, 20) for _ in range(num_bins)]

# Write the data to a text file
with open("bin_sizes.txt", "w") as file:
    for weight in weights:
        file.write(str(weight) + "\n")

print("Data generation complete. Saved to bin_sizes.txt")
