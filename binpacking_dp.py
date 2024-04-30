import time

def bin_packing(items, bin_capacity):
    n = len(items)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    last_item_packed = [-1] * (n + 1)

    for i in range(1, n + 1):
        space_left = bin_capacity
        for j in range(i, 0, -1):
            space_left -= items[j - 1]
            if space_left >= 0 and dp[j - 1] + 1 < dp[i]:
                dp[i] = dp[j - 1] + 1
                last_item_packed[i] = j - 1

    # Backtrack to find items packed into each bin
    bins = []
    i = n
    while i > 0:
        j = last_item_packed[i]
        bins.append(items[j:i])
        i = j
    bins.reverse()
    return bins



def read_item_sizes_from_file(file_name, n):
    with open(file_name, 'r') as file:
        items = [int(line.strip()) for line in file]
    return items[:n]

def experiment(n, bin_capacity):
    items = read_item_sizes_from_file(r"C:\Users\Lenovo\Downloads\bin_sizes.txt",n)
    start_time = time.time()
    packed_bins = bin_packing(items, bin_capacity)
    end_time = time.time()
    total_bins = len(packed_bins)
    print(f"Number of items: {n}, Bin capacity: {bin_capacity}")
    print(f"Total bins: {total_bins}")
    print(f"Execution time: {end_time - start_time:.6f} seconds\n")

# Example usage
n = 10000  # Specify the number of items you want to process
bin_capacity = 20  # Define the capacity of each bin
experiment(n, bin_capacity)