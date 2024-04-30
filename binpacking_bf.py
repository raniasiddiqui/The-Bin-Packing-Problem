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
    weight = [ 11, 5, 4, 14, 1, 3, 8 ]
    c = 2
    n = len(weight)
    print("Number of bins required in First Fit : ", bestFit(weight, n, c))
     
# This code is contributed by Rajput-Ji
#Source reference: https://www.geeksforgeeks.org/bin-packing-problem-minimize-number-of-used-bins/
