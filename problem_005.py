from collections import Counter
import projectEulerUtils

N = 21;
requiredPrimeFactors = {}

for i in range(N):
	i_factors = Counter(projectEulerUtils.primeFactors(i))
	for factor,count in i_factors.iteritems():
		if factor not in requiredPrimeFactors:
			requiredPrimeFactors[factor]=count
		else:
			requiredPrimeFactors[factor]=max(requiredPrimeFactors[factor],count)

result = 1;
for factor,count in requiredPrimeFactors.iteritems():
	result *= (factor**count)

print result
		
