import math
from collections import Counter
from itertools import izip_longest


def is_prime(N):
    if N % 2 == 0:
        False
    for i in xrange(3, int(math.sqrt(N)) + 1, 2):
        if N % i == 0:
            return False
    return True


def primeSieve(N):
    pos_primes = [True] * N
    pos_primes[0] = pos_primes[1] = False
    for (i, isprime) in enumerate(pos_primes):
        if isprime:
            yield i
            for n in xrange(i * i, N, i):
                pos_primes[n] = False


def smallest_prime_factor(N):
    if N % 2 == 0:
        return 2
    for i in xrange(3, int(math.sqrt(N)) + 1, 2):
        if N % i == 0:
            return i

    return N


def prime_factors(n):
    if n == 1: return [1]
    factors = []

    while (n > 1):
        next_factor = smallest_prime_factor(n)
        factors.append(next_factor)
        n /= next_factor

    return factors


def product(arr):
    return reduce(lambda x, y: x * y, arr)


def findDivisors(N):
    factorPairs = [(x, N / x) for x in range(1, int(math.sqrt(N)) + 1) if N % x == 0]
    factors = [factor for pair in factorPairs for factor in pair]
    unique_factors = list(set(factors))
    return unique_factors


def countDivisors(N):
    prime_factors = Counter(prime_factors(N))
    possible_factors = [count + 1 for factor, count in prime_factors.iteritems()]
    return product(possible_factors)


def properDivisors(x):
    divisors = findDivisors(x)
    proper_divisors = sorted(divisors)[:-1]
    return proper_divisors


def asDigitArray(x, base=10):
    arr = []

    while x > 0:
        arr.append(x % base)
        x /= base

    arr.reverse()
    return arr


def addDigitArray(arr1, arr2):
    arr = izip_longest(reversed(arr1), reversed(arr2), fillvalue=0)
    result = []
    carry = 0
    for x, y in arr:
        z = x + y + carry
        result.append(z % 10)
        carry = 1 if z >= 10 else 0
    if carry == 1:
        result.append(carry)
    result.reverse()
    return result
