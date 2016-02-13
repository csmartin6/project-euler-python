import utils
import sys


def consecutive_primes(a, b, primes):
    n = 0
    while n * n + a * n + b in primes:
        n += 1
    return n


def problem_027():
    n = 100000
    max_a = 1000
    max_b = 1000
    primes = set([p for p in utils.prime_sieve(n)])

    # b must be prime and positive
    pos_b = [b for b in utils.prime_sieve(max_b)]

    max_consecutive_primes = 0

    pair = (0, 0)
    for b in pos_b:
        for a in range(-max_a + 1, max_a):
            n = consecutive_primes(a, b, primes)
            if n > max_consecutive_primes:
                max_consecutive_primes = n
                pair = (a, b)

    return pair[0] * pair[1]


def main():
    print "Problem 27"
    print "Answer: " + str(problem_027())


if __name__ == '__main__':
    sys.exit(main())
