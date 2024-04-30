import random
from numpy.random import choice
import numpy as np
import time

def GenerateSE(T, k, p, w_i, bin_capacity):
    SE = [[] for _ in range(p)]
    bin_current_weights = [[] for _ in range(p)]  # Dynamic list of bin weights

    for n in range(p):
        for i in range(k):
            b = len(bin_current_weights[n])  # Current number of bins
            probabilities = np.zeros(b + 1)  # Extra space for potentially new bin
            for j in range(b):
                if bin_current_weights[n][j] + w_i[i] <= bin_capacity:
                    if j >= len(T):
                        T.append([random.random()])  # Ensure pheromone trail exists for new bin
                    probabilities[j] = T[j][0]  # Use existing pheromone trail
            probabilities[-1] = 1  # Base probability for opening a new bin

            probabilities /= probabilities.sum()  # Normalize probabilities
            chosen_bin = choice(range(len(probabilities)), p=probabilities)
            if chosen_bin == b:  # New bin
                bin_current_weights[n].append(w_i[i])
                SE[n].append(chosen_bin)
                T.append([random.random()])  # Initialize pheromone for new bin
            else:
                bin_current_weights[n][chosen_bin] += w_i[i]
                SE[n].append(chosen_bin)

    return SE, T

def Fitness(SE, p, bin_capacity):
    d = []
    for solution in SE:
        if None in solution:
            d.append(float('inf'))
        else:
            d.append(len(set(solution)))  # Fitness is the number of unique bins used
    return d

def ACO_BPP(p, e, item_sizes, bin_capacity):
    iteration = int(60 / p)  # Adjust iteration based on the number of ants
    k = len(item_sizes)
    w_i = item_sizes

    T = [[1.0]]  # Start with an initial pheromone matrix for one bin

    for itr in range(iteration):
        SE, T = GenerateSE(T, k, p, w_i, bin_capacity)
        d = Fitness(SE, p, bin_capacity)
        best_idx = d.index(min(d))

        # Update pheromones for better paths
        for i, bin_idx in enumerate(SE[best_idx]):
            if bin_idx >= len(T):
                T.append([1.0])  # Ensure pheromone list is long enough
            T[bin_idx][0] += 100 / (d[best_idx] + 1)  # Increase pheromone

        # Pheromone evaporation
        for i in range(len(T)):
            T[i][0] *= e

        if itr == 0 or itr == iteration - 1:
            print(f"Iteration {itr+1}, Best fitness: {min(d)}, Configuration: {SE[best_idx]}")
            print(f"Number of bins used: {len(set(SE[best_idx]))}")

    return None

# Example usage
def get_first_n_numbers_from_file(n, filename='bin_sizes.txt'):
    """
    Reads the first n numbers from a specified file.

    Parameters:
        n (int): The number of numbers to return.
        filename (str): The path to the file containing numbers.

    Returns:
        list: A list containing the first n numbers from the file, or fewer if the file contains fewer numbers.
    """
    try:
        with open(filename, 'r') as file:
            # Read lines, convert to integers where possible, and filter out non-digit lines
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist in the current directory.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    # Return the first n numbers, or all numbers if there are less than n
    return numbers[:n]




item_sizes = get_first_n_numbers_from_file(8000)
bin_capacity = 25
start_time = time.time()
ACO_BPP(30, 0.4, item_sizes, bin_capacity)
end_time = time.time()

runtime = end_time - start_time

print("Runtime:", runtime, "seconds")


