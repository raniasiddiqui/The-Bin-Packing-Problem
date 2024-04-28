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

# Example usage
items = [3, 5, 2, 7, 1, 4, 6]
bin_capacity = 10
packed_bins = bin_packing(items, bin_capacity)
print("Items packed into bins:")
for bin_items in packed_bins:
    print(bin_items)