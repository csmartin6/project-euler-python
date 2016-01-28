from ..projectEulerUtils import utils as utils


def scalarMultiplyNumArray(arr,multiple):
	result = []
	carry = 0
	for digit in reversed(arr):
		x = digit * multiple + carry 
		result.append(x%10)
		carry = x/10 
	
	while carry >= 1:
		result.append(carry%10)
		carry/=10
	
	result.reverse()
	return result



def multiplyNumArray(arr1,arr2):
	csum = []	
	for index,digit in enumerate(reversed(arr2)):
		to_add = scalarMultiplyNumArray(arr1,digit)
		to_add.extend([0 for i in range(index)])
		if not csum:
			csum = scalarMultiplyNumArray(arr1,digit)
		else:
			csum = utils.addDigitArray(csum, to_add)
	return csum

N = 100

fact = [1]
for i in xrange(1,N+1):
	fact = scalarMultiplyNumArray(fact,i)

print fact
print sum(fact)
