from collections import Counter
import utils
import sys


def problem_005():
    n = 21
    prime_factors = {}

    for i in range(n):
        i_factors = Counter(utils.prime_factors(i))
        for factor, count in i_factors.iteritems():
            if factor not in prime_factors:
                prime_factors[factor] = count
            else:
                prime_factors[factor] = max(prime_factors[factor], count)

    result = 1
    for factor, count in prime_factors.iteritems():
        result *= (factor**count)

    return result


def main():
    print "Problem 5"
    print "Answer: " + str(problem_005())

if __name__ == '__main__':
    sys.exit(main())
