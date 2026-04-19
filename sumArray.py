def sumArray(arr, n):
	total = 0
	for i in range(n):
		total += arr[i]
	return total

# Example usage:
arr = [6, 2, 3, 4, 5]
n = len(arr)
result = sumArray(arr, n)
print(result)
   