from collections import Counter

from  ..projectEulerUtils import utils as utils

N = 21;
requiredPrimeFactors = {}

for i in range(N):
	i_factors = Counter(utils.primeFactors(i))
	for factor,count in i_factors.iteritems():
		if factor not in requiredPrimeFactors:
			requiredPrimeFactors[factor]=count
		else:
			requiredPrimeFactors[factor]=max(requiredPrimeFactors[factor],count)

result = 1;
for factor,count in requiredPrimeFactors.iteritems():
	result *= (factor**count)

print result
		
