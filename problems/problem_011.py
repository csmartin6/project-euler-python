import numpy as np
from ..projectEulerUtils import projectEulerUtils as utils


arr = []
max_length = 4
#with open('input_data/problem_011_input.txt', 'r') as file:
with open('projecteuler/input_data/problem_011_input.txt', 'r') as file:
	for line in file:
		current_line = line.rstrip('\n').split(' ')
		arr.append([int(x) for x in current_line])

N = len(arr)
max_product = 0
nums = np.array(arr)
max_product_list = []
# Check Rows

def maxContigousProduct(arr,length):
	products = [utils.product(arr[j:(j+length)]) for j in range(len(arr)-length+1)]
	return max(products)

def maxProductInRow(arr):
	max_product = 0
	for row in arr: 
		row_max  = maxContigousProduct(row,max_length)
		max_product  = max(row_max,max_product)
	return max_product

def maxProductOnDiagonal(arr):
	m,n = arr.shape
	max_product = 0;
	for k in range(-m+max_length,n-max_length):
		diag = np.diagonal(arr,k)
		diag_max = maxContigousProduct(diag,max_length)
		max_product  = max(diag_max,max_product)

	return max_product

maxInRow = maxProductInRow(nums)
maxInCol = maxProductInRow(nums.T)
maxInDiag = maxProductOnDiagonal(nums)
maxInDiagRot = maxProductOnDiagonal(np.rot90(nums))
max_product = max([maxInRow,maxInCol,maxInDiag,maxInDiagRot])

print max_product


