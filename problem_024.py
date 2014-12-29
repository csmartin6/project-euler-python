import math 
d = [0,1,2,3,4,5,6,7,8,9]


Nth = 999999


def findNthOrdering(N, digits,seq_length):
	num_orderings = math.factorial(seq_length-1)
	if seq_length == 1:
		return [digits[N]]
	for index, digit in enumerate(digits):
		if (index+1)*num_orderings > N:
			remaining_digits = digits[:index]+digits[(index+1):]
			return [digit]+findNthOrdering(N-(index*num_orderings), remaining_digits,seq_length-1)
	raise RuntimeError("Something has gone wrong")

print findNthOrdering(Nth,d,len(d))



