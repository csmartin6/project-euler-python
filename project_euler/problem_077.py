import sys
from timeit import default_timer as timer
from functools import lru_cache
import utils


def distinct_sum_prime(n):
    return distinct_sum_prime_inner(n, tuple(list(utils.prime_sieve(n))[::-1]))


@lru_cache(maxsize=10000)
def distinct_sum_prime_inner(n, ks):
    if len(ks) == 0 or n == 0:
        return 0
    elif ks[0] > n:
        return distinct_sum_prime_inner(n, ks[1:])
    elif ks[0] == n:
        return 1 + distinct_sum_prime_inner(n, ks[1:])
    else:
        return sum([distinct_sum_prime_inner(n - ks[i], ks[i:]) for i in range(len(ks))])


def problem_077():
    count = 0
    num = 1
    while count < 5000:
        num += 1
        count = distinct_sum_prime(num)
    return num


def main():
    print("Problem 77")
    start = timer()
    print("Answer: {}".format(problem_077()))
    print("Elapsed time: {}".format(timer() - start))


if __name__ == '__main__':
    sys.exit(main())
