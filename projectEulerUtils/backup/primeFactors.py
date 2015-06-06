import smallestPrimeFactor

def primeFactors(N):
	if N==1: return [1]
	factors = []

	while (N>1):
		next_factor = smallestPrimeFactor(N)
		factors.append(next_factor)
		N /= next_factor

	return factors
