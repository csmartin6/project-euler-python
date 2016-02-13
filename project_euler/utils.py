import math
from collections import Counter
from itertools import izip_longest


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_sieve(n):
    pos_primes = [True] * n
    pos_primes[0] = pos_primes[1] = False
    for (i, isprime) in enumerate(pos_primes):
        if isprime:
            yield i
            for z in xrange(i * i, n, i):
                pos_primes[z] = False


def smallest_prime_factor(n):
    if n % 2 == 0:
        return 2
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i

    return n


def prime_factors(n):
    if n == 1:
        return [1]
    factors = []

    while n > 1:
        next_factor = smallest_prime_factor(n)
        factors.append(next_factor)
        n /= next_factor

    return factors


def product(arr):
    return reduce(lambda x, y: x * y, arr)


def find_divisors(n):
    factor_pairs = [(x, n / x) for x in range(1, int(math.sqrt(n)) + 1) if n % x == 0]
    factors = [factor for pair in factor_pairs for factor in pair]
    unique_factors = list(set(factors))
    return unique_factors


def count_divisors(n):
    factors = Counter(prime_factors(n))
    possible_factors = [count + 1 for factor, count in factors.iteritems()]
    return product(possible_factors)


def proper_divisors(x):
    divisors = find_divisors(x)
    return sorted(divisors)[:-1]


def as_digit_array(x, base=10):
    arr = []

    while x > 0:
        arr.append(x % base)
        x /= base

    arr.reverse()
    return arr


def add_digit_array(arr1, arr2):
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


def scalar_multiply_num_array(arr, multiple):
    result = []
    carry = 0
    for digit in reversed(arr):
        x = digit * multiple + carry
        result.append(x % 10)
        carry = x / 10

    while carry >= 1:
        result.append(carry % 10)
        carry /= 10

    result.reverse()
    return result


def multiply_num_array(arr1, arr2):
    csum = []
    for index, digit in enumerate(reversed(arr2)):
        to_add = scalar_multiply_num_array(arr1, digit)
        to_add.extend([0]*index)
        if not csum:
            csum = scalar_multiply_num_array(arr1, digit)
        else:
            csum = add_digit_array(csum, to_add)
    return csum
