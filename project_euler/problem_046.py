import sys
from . import utils


def problem_046():

    n = 100
    squares = [i*i for i in range(n)]
    primes = [i for i in utils.prime_sieve(n*n)]
    prime_set = set(primes)

    prime_plus_square = set()
    for s in squares:
        for p in primes:
            prime_plus_square.add(2*s + p)

    for i in range(3, n*n, 2):
        if i not in prime_set and i not in prime_plus_square:
            return i

    return -1


def main():
    print("Problem 46")
    print("Answer: " + str(problem_046()))


if __name__ == '__main__':
    sys.exit(main())
