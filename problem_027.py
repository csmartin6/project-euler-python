from projectEulerUtils import primeSieve

# primes less than 100000
N=100000
max_a = 1000
max_b = 1000
primes = set([p for p in primeSieve(N)])


# b must be prime and positive
pos_b = [b for b in primeSieve(max_b)]

def consecutive_primes(a,b):
	n = 0
	while(n*n+a*n+b in primes):
		n+=1
	return n


max_consecutive_primes = 0

for b in pos_b:
	for a in range(-max_a+1,max_a):
		n = consecutive_primes(a,b)
		if n > max_consecutive_primes:
			max_consecutive_primes = n
			pair = (a,b)
print pair
print "Consecutive Primes: "+str(max_consecutive_primes)
print "product: "+str(pair[0]*pair[1])

