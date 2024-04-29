import random
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

def generate_random_items(num_items):
    return [random.randint(1, 10) for _ in range(num_items)]

def experiment(num_items_list, bin_capacity_list):
    for num_items in num_items_list:
        for bin_capacity in bin_capacity_list:
            items = generate_random_items(num_items)
            packed_bins = bin_packing(items, bin_capacity)
            total_bins = len(packed_bins)
            total_items_packed = sum(len(bin_items) for bin_items in packed_bins)
            print(f"Number of items: {num_items}, Bin capacity: {bin_capacity}")
            print(f"Worst solution: {total_bins} bins, Best solution: 1 bin")
            print(f"Total items packed: {total_items_packed}\n")
            print("Items packed into bins:")
            for bin_items in packed_bins:
                print(bin_items)
            print("\n")

# Example usage
num_items_list = [10, 20, 30, 40, 50, 60]
bin_capacity_list = [40, 80, 90, 100, 150]
experiment(num_items_list, bin_capacity_list)

# # Example usage
# items = [3, 5, 2, 7, 1, 4, 6]
# bin_capacity = 10
# packed_bins = bin_packing(items, bin_capacity)
# print("Items packed into bins:")
# for bin_items in packed_bins:
#     print(bin_items)