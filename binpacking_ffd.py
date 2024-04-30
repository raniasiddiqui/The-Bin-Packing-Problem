def firstFit(weight, n, capacity):
	
	# Initialize result (Count of bins)
	result = 0
	# Create an array to store remaining space in bins as there can be at most n bins
	bin_rem = [0]*n
	
	# Place items one by one
	for i in range(n):
	
		# Find the first bin that can accommodate
		j = 0
		while( j < result):
			if (bin_rem[j] >= weight[i]):
				bin_rem[j] = bin_rem[j] - weight[i]
				break
			j+=1
			
		# If no bin could accommodate weight[i]
		if (j == result):
			bin_rem[result] = capacity - weight[i]
			result = result+1
	return result
	
# Returns number of bins required using first fit
def firstFitDec(weight, n, capacity):

	# First sort all weights in decreasing order
	weight.sort(reverse = True)

	# Now call first fit for sorted items
	return firstFit(weight, n, capacity)

# Driver program
weight = [ 2, 5, 4, 7, 1, 3, 8, 12, 14, 20]
c = 3
n = len(weight)
print("Number of bins required in First Fit Decreasing : ",str(firstFitDec(weight, n, c)))

# This code is contributed by shinjanpatra
#Source reference: https://www.geeksforgeeks.org/bin-packing-problem-minimize-number-of-used-bins/
