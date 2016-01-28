from ..projectEulerUtils import utils as utils

N = 28124
abundant_numbers = [x for x in range(N) if sum(utils.properDivisors(x)) > x]

nums = [0 for x in xrange(N)]
for i,numberA in enumerate(abundant_numbers):
	for numberB in abundant_numbers[i:]:
		if numberA+numberB < N:
			nums[numberA+numberB]=1

non_abundant = [number for number,sum_of_abundant in enumerate(nums) if not sum_of_abundant]

print sum(non_abundant)


