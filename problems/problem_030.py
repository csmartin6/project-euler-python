from ..projectEulerUtils import projectEulerUtils as utils

N = 1000000

nums = []

for i in xrange(2,N):
	digits = utils.asDigitArray(i)

	sum_of_5th_powers = sum([x**5 for x in digits])	
	if sum_of_5th_powers == i:
		nums.append(i)

print nums
print sum(nums)