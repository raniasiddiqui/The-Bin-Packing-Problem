def can_fit_more(boxes, capacity):
    return any(box['size'] <= capacity and not box['taken'] for box in boxes)

def add_to_array(arr, value):
    arr.append(value)

def clear_last(arr):
    if arr:
        arr.pop()

def fit_to_boxes_rec(boxes, capacity, best, current_bin):
    if sum(current_bin) > sum(best[0]):
        best[0] = current_bin[:]

    if capacity == 0:
        return sum(current_bin)

    max_value = sum(best[0])
    for box in boxes:
        if box['size'] <= capacity and not box['taken']:
            box['taken'] = True
            current_bin.append(box['size'])
            max_value = max(max_value, fit_to_boxes_rec(boxes, capacity - box['size'], best, current_bin))
            current_bin.pop()
            box['taken'] = False

    return max_value

def fit_to_boxes(boxes, total_capacity):
    best = [[]]  # Only one 'best' array is needed as we're looking for any packing solution
    bins = 0

    while can_fit_more(boxes, total_capacity):
        current_bin = []
        value = fit_to_boxes_rec(boxes, total_capacity, best, current_bin)
        print(f"Bin {bins + 1}: {best[0]} with total size: {value}")
        for size in best[0]:
            for box in boxes:
                if box['size'] == size and not box['taken']:
                    box['taken'] = True
                    break
        best[0] = []  # Clear the best for the next round
        bins += 1

    return bins


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


def main():
    capacity = 20
    box_sizes = get_first_n_numbers_from_file(100)

    boxes = [{'size': size, 'taken': False} for size in box_sizes]

    print("Total bins used:", fit_to_boxes(boxes, capacity))

if __name__ == "__main__":
    main()
