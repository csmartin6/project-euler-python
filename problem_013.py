from itertools import izip_longest

def addNumArray(arr1,arr2):
	arr = izip_longest(reversed(arr1),reversed(arr2), fillvalue=0)
	result = []
	carry = 0
	for x,y in arr:
		z = x + y + carry 
		result.append(z%10)
		carry = 1 if z >= 10 else 0
	if carry == 1:
		result.append(carry)
	result.reverse()
	return result

arr = []
max_length = 4
with open('problem_013_input.txt', 'r') as file:
	for line in file:
		current_line = line.rstrip('\n')
		arr.append([int(x) for x in current_line])


z = reduce(lambda x,y: addNumArray(x,y),arr)

print z[0:10]

