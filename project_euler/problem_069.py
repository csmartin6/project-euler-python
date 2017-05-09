import sys
import utils
import numpy as np


def problem_069_sieve():
    n = 1000000
    rel_prime = np.zeros((n+1,))
    primes = set(utils.prime_sieve(n))

    for p in primes:

        for k, kp in enumerate(range(p, n+1, p)):
            rel_prime[kp] += k + 1
            if (k + 1) in primes and (k + 1) > p:
                rel_prime[kp] -= 1

    ratio = np.array([(i/(i-r) if r > 0 else 0) for i, r in enumerate(rel_prime)])
    return np.argmax(ratio)

def problem_069():
    n = 1000000
    x = 1
    primes = utils.prime_sieve(1000)
    p = next(primes)
    while x * p < n:
        x *= p
        p = next(primes)

    return x


def main():
    print("Problem 69")
    print(("Answer: " + str(problem_069_sieve())))


if __name__ == '__main__':
    sys.exit(main())
