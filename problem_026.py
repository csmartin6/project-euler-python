import fractions
import numpy as np
def multiplicativeOrder(a,n):
	if fractions.gcd(a,n)!=1:
		return 0
	max_k=1e6
	k=0
	ak=a
	while (ak%n!=1):
		k+=1
		ak*=a
		if k > max_k:
			raise RuntimeError("k greater than 1000")
	return k

N=1000
repetend_lengths = [multiplicativeOrder(10,p) for p in range(2,N)]


print np.argmax(repetend_lengths)+2


