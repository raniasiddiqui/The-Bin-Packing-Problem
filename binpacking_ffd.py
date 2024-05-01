# # This code is contributed by shinjanpatra
# #Source reference: https://www.geeksforgeeks.org/bin-packing-problem-minimize-number-of-used-bins/
def get_first_n_numbers_from_file(n, filename='bins_data.txt'):
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

item_sizes = get_first_n_numbers_from_file(10000)
# print(item_sizes)
def firstFit(weight, n, capacity):
    # Initialize result (Count of bins)
    result = 0
    # Create an array to store remaining space in bins as there can be at most n bins
    bin_rem = [0]*n

    # Place items one by one
    for i in range(n):
        # Find the first bin that can accommodate
        j = 0
        while j < result:
            if bin_rem[j] >= weight[i]:
                bin_rem[j] -= weight[i]
                break
            j += 1

        # If no bin could accommodate weight[i]
        if j == result:
            bin_rem[result] = capacity - weight[i]
            result += 1
    return result

# Returns number of bins required using first fit
def firstFitDec(weight, n, capacity):
    # First sort all weights in decreasing order
    weight.sort(reverse=True)
    # Now call first fit for sorted items
    return firstFit(weight, n, capacity)


# File name containing the weights

# Set capacity
c = 20

# Read weights from file
weight = item_sizes
n = len(weight)

# Calculate the number of bins required using First Fit Decreasing
print("Number of bins required in First Fit Decreasing:", firstFitDec(weight, n, c))
