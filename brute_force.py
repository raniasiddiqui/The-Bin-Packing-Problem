
class Bin:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def put(self, item):
        if sum(self.items) + item <= self.capacity:
            self.items.append(item)
            return True
        return False

    def remove(self, item):
        self.items.remove(item)

    def __str__(self):
        return f"Bin({self.items})"

def brute_force(items, bins, current_position=0, best_solution=None):
    if current_position >= len(items):
        # Calculate the number of filled bins
        filled_bins = sum(1 for bin in bins if bin.items)
        if best_solution is None or filled_bins < best_solution['filled_bins']:
            best_solution = {'filled_bins': filled_bins, 'configuration': [bin.items[:] for bin in bins]}
        return best_solution

    current_item = items[current_position]
    for bin in bins:
        if bin.put(current_item):
            result = brute_force(items, bins, current_position + 1, best_solution)
            if best_solution is None or result['filled_bins'] < best_solution['filled_bins']:
                best_solution = result
            bin.remove(current_item)

    return best_solution

# Example of usage
if __name__ == "__main__":
    items = [1,2,3]
    bins = [Bin(10), Bin(10), Bin(10)]
    best_solution = brute_force(items, bins)
    print("Best solution found:", best_solution)

