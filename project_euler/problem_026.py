import fractions
import numpy as np
import sys


def multiplicative_order(a, n):
    if fractions.gcd(a, n) != 1:
        return 0
    max_k = 1e6
    k = 0
    ak = a
    while ak % n != 1:
        k += 1
        ak *= a
        if k > max_k:
            raise RuntimeError("k greater than "+str(max_k))
    return k


def problem_026():
    n = 1000
    repetend_lengths = [multiplicative_order(10, p) for p in range(2, n)]
    return np.argmax(repetend_lengths)+2


def main():
    print "Problem 26"
    print "Answer: " + str(problem_026())


if __name__ == '__main__':
    sys.exit(main())
