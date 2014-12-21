import projectEulerUtils

N = 10001
i = 1
prime_count = 1
while prime_count < N:
	i+=2
	if (projectEulerUtils.isPrime(i)):
		prime_count+=1


result = i
print result
