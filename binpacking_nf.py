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
weight = [2, 5, 4, 8, 1, 11, 3, 4]
capacity = 12
print("Number of bins required in Next Fit :",nextfit(weight, capacity))
 
# This code is contributed by code_freak
#Source reference: https://www.geeksforgeeks.org/bin-packing-problem-minimize-number-of-used-bins/
