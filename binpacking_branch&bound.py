class Bin:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def remaining_capacity(self):
        return self.capacity - sum(self.items)

    def pack(self, item):
        self.items.append(item)

    def unpack(self, item):
        self.items.remove(item)

def branch_and_bound_bin_packing(items, bin_capacity):
    items.sort(reverse=True)
    best_solution = float('inf')
    current_solution = []

    best_solution = branch_and_bound(items, bin_capacity, 0, current_solution, best_solution)

    return best_solution

def branch_and_bound(items, bin_capacity, index, current_solution, best_solution):
    if index >= len(items):
        if len(current_solution) < best_solution:
            return len(current_solution)

    if index >= len(items):
        return best_solution

    for bin in current_solution:
        if bin.remaining_capacity() >= items[index]:
            bin.pack(items[index])
            updated_best_solution = branch_and_bound(items, bin_capacity, index + 1, current_solution, best_solution)
            if updated_best_solution < best_solution:
                best_solution = updated_best_solution
            bin.unpack(items[index])

    if len(current_solution) < best_solution:
        new_bin = Bin(bin_capacity)
        new_bin.pack(items[index])
        updated_best_solution = branch_and_bound(items, bin_capacity, index + 1, current_solution + [new_bin], best_solution)
        if updated_best_solution < best_solution:
            best_solution = updated_best_solution

    return best_solution

# Example usage
if __name__ == "__main__":
    items = [8, 7, 5, 4, 6, 2]
    bin_capacity = 20
    min_bins = branch_and_bound_bin_packing(items, bin_capacity)
    print("Minimum number of bins required:", min_bins)
