import math

def smallestPrimeFactor(N):
	if N%2 == 0: 
		return 2
	for i in xrange(3,int(math.sqrt(N))+1,2):
		if N%i == 0:
			return i

	return N