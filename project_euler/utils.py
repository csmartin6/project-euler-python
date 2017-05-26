import math
from collections import Counter
from itertools import zip_longest
import itertools
from functools import reduce


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_sieve(n):
    pos_primes = [True] * n
    pos_primes[0] = pos_primes[1] = False
    for (i, isprime) in enumerate(pos_primes):
        if isprime:
            yield i
            for z in range(i * i, n, i):
                pos_primes[z] = False


def smallest_prime_factor(n):
    if n % 2 == 0:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i

    return n


def prime_factors(n):
    if n == 1:
        return [1]
    factors = []

    while n > 1:
        next_factor = int(smallest_prime_factor(n))
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
    possible_factors = [count + 1 for factor, count in factors.items()]
    return product(possible_factors)


def proper_divisors(x):
    divisors = find_divisors(x)
    return sorted(divisors)[:-1]


def as_digit_array(x, base=10):
    arr = []

    while x > 0:
        arr.append(x % base)
        x //= base

    arr.reverse()
    return arr


def from_digit_array(arr, base=10):
    num = 0
    place_value = 1
    for d in reversed(arr):
        num += d * place_value
        place_value *= base
    return num


def add_digit_array(arr1, arr2):
    arr = zip_longest(reversed(arr1), reversed(arr2), fillvalue=0)
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
        carry = x // 10

    while carry >= 1:
        result.append(carry % 10)
        carry //= 10

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


def power_num_array(arr, pow):

    csum = [1]
    curr = arr
    binary_exponent= bin(pow)[2:]
    for b in reversed(binary_exponent):
        if b == '1':
            csum = multiply_num_array(csum, curr)
        curr = multiply_num_array(curr, curr)

    return csum


def truncated_power_num_array(arr, pow, num_digits=10):

    csum = [1]
    curr = arr[-num_digits:]
    binary_exponent= bin(pow)[2:]
    for b in reversed(binary_exponent):
        if b == '1':
            csum = multiply_num_array(csum, curr)[-num_digits:]
        curr = multiply_num_array(curr, curr)[-num_digits:]

    return csum


# from stack overflow
# https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python
def erat3():
    d = {9: 3, 25: 5}
    yield 2
    yield 3
    yield 5
    mask = 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    modulos = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

    for q in itertools.compress(
            itertools.islice(itertools.count(7), 0, None, 2),
            itertools.cycle(mask)):
        p = d.pop(q, None)
        if p is None:
            d[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in d or (x % 30) not in modulos:
                x += 2*p
            d[x] = p


def factorials():
    yield 1
    yield 1

    f = 1
    n = 2
    while True:
        f = n * f
        yield f
        n += 1