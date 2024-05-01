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
def nextfit(weight, capacity):
    result = 0
    rem = capacity
    for _ in range(len(weight)):
        if rem >= weight[_]:
            rem = rem - weight[_]
        else:
            result += 1
            rem = capacity - weight[_]
    return result
 
# Driver Code
weight = item_sizes
capacity = 20
print("Number of bins required in Next Fit :",nextfit(weight, capacity))
 
# This code is contributed by code_freak
#Source reference: https://www.geeksforgeeks.org/bin-packing-problem-minimize-number-of-used-bins/
