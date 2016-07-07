import sys
import utils


def problem_010():
    n = 2000000
    primes = list(utils.prime_sieve(n))
    return sum(primes)


def main():
    print "Problem 10"
    print "Answer: " + str(problem_010())


if __name__ == '__main__':
    sys.exit(main())
