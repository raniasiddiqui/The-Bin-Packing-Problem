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

item_sizes = get_first_n_numbers_from_file(120)
def bestFit(weight, n, c):
     
    # Initialize result (Count of bins)
    result = 0
    # Create an array to store remaining space in bins as there can be at most n bins
    bin_rem = [0]*n
 
    # Place items one by one
    for i in range(n):
        j = 0
         
        # Initialize minimum space left and index of best bin
        min = c + 1
        bi = 0
        for j in range(result):
            if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min):
                bi = j
                min = bin_rem[j] - weight[i]
             
        # If no bin could accommodate weight[i], create a new bin
        if (min == c + 1):
            bin_rem[result] = c - weight[i]
            result += 1
        else: # Assign the item to best bin
            bin_rem[bi] -= weight[i]
    return result
 
# Driver code
if __name__ == '__main__':
    weight = item_sizes
    c = 20
    n = len(weight)
    print("Number of bins required in First Fit : ", bestFit(weight, n, c))
     
# This code is contributed by Rajput-Ji
#Source reference: https://www.geeksforgeeks.org/bin-packing-problem-minimize-number-of-used-bins/
