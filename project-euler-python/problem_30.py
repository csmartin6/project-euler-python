from ..projectEulerUtils import utils as utils

N = 100000

for i in xrange(N):if digits
	digits = utils.asDigitArray(i)

	sum_of_5th_powers = sum([x**5 for x in digits])	
	if sum_of_5th_powers == i:
		print i