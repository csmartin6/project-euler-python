import math

def isPrime(N):
	if N<=1:
		return False
	
	if N%2 == 0: 
		False
	
	for i in xrange(3,int(math.sqrt(N))+1,2):
		if N%i == 0:
			return False
	
	return True