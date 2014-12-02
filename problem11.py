import numpy as np
from projectEulerUtils import product

arr = []
max_length = 4
with open('problem11_input.txt', 'r') as file:
	for line in file:
		current_line = line.rstrip('\n').split(' ')
		arr.append([int(x) for x in current_line])

N = len(arr)
max_product = 0
nums = np.array(arr)
max_product_list = []
# Check Rows

def maxProductInRow(arr):
	max_product = 0
	for row in arr: 
		products = [product(row[j:(j+max_length)]) for j in range(len(row)-max_length+1)]
		row_max  = max(products)
		if row_max > max_product:
			max_product = row_max
	return max_product

def maxProductOnDiagonal(arr):
	m,n = arr.shape
	max_product = 0;
	for k in range(-m+max_length,n-max_length):
		diag = np.diagonal(arr,k)
		products = [product(diag[j:(j+max_length)]) for j in range(len(diag)-max_length+1)]
		diag_max  = max(products)
		if diag_max > max_product:
			max_product = diag_max

	return max_product

maxInRow = maxProductInRow(nums)
maxInCol = maxProductInRow(nums.T)
maxInDiag = maxProductOnDiagonal(nums)
maxInDiagRot = maxProductOnDiagonal(np.rot90(nums))
max_product = max([maxInRow,maxInCol,maxInDiag,maxInDiagRot])


print max_product


