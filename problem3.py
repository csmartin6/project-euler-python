def smallestPrimeFactor(N):
	
	for i in xrange(2,N):
		if N%i == 0:
			return i

	return N

def primeFactors(N):

	factors = []

	while (N>1):
		next_factor = smallestPrimeFactor(N)
		factors.append(next_factor)
		N /= next_factor

	return factors


N = 600851475143 

prime_factors = primeFactors(N)

print prime_factors
