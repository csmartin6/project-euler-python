import math
from collections import Counter
from itertools import izip_longest

def isPrime(N):
	if N%2 == 0: 
		False
	for i in xrange(3,int(math.sqrt(N))+1,2):
		if N%i == 0:
			return False

	return True

def smallestPrimeFactor(N):
	if N%2 == 0: 
		return 2
	for i in xrange(3,int(math.sqrt(N))+1,2):
		if N%i == 0:
			return i

	return N

def primeFactors(N):
	if N==1: return [1]
	factors = []

	while (N>1):
		next_factor = smallestPrimeFactor(N)
		factors.append(next_factor)
		N /= next_factor

	return factors


def product(arr):
	return reduce(lambda x,y:x*y,arr)


def findDivisors(N):
	factorPairs  = [(x, N/x) for x in range(1,int(math.sqrt(N))+1) if N % x == 0]
	return [factor for pair in factorPairs for factor in pair]

def countDivisors(N):
	prime_factors = Counter(primeFactors(N))
	possible_factors = [count+1 for factor, count in prime_factors.iteritems()]
	return product(possible_factors)


def addDigitArray(arr1,arr2):
	arr = izip_longest(reversed(arr1),reversed(arr2), fillvalue=0)
	result = []
	carry = 0
	for x,y in arr:
		z = x + y + carry 
		result.append(z%10)
		carry = 1 if z >= 10 else 0
	if carry == 1:
		result.append(carry)
	result.reverse()
	return result