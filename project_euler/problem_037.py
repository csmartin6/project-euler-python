import sys
from . import utils


def problem_037():
    n = 1000000
    truncateable_primes = []
    primes = set([x for x in utils.prime_sieve(n)])
    for x in primes:
        prime = str(x)
        truncateable = True
        for i in range(len(prime)):
            if i < len(prime):
                left = int(prime[i:])
                if left not in primes:
                    truncateable = False
                    break
            if i > 0:
                right = int(prime[:i])
                if right not in primes:
                    truncateable = False
                    break
        if truncateable and x > 10:
            truncateable_primes.append(x)
    return sum(truncateable_primes)


def main():
    print("Problem 37")
    print("Answer: " + str(problem_037()))


if __name__ == '__main__':
    sys.exit(main())
