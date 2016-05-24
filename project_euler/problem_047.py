import sys
import utils


def problem_047():
    k = 4
    consecutive = []
    for n in xrange(2,1000000):
        distinct_prime_factors = set(utils.prime_factors(n))
        if len(distinct_prime_factors) == k:
            consecutive.append(n)
            if len(consecutive) == k:
                return consecutive[0]
        else:
            consecutive = []

    return []


def main():
    print "Problem 47"
    print "Answer: " + str(problem_047())


if __name__ == '__main__':
    sys.exit(main())
