import sys
import numpy as np
import utils


def is_pandigital(n):
    ns = str(n)
    ns_set = set(ns)
    for i in range(1,len(ns)+1):
        if str(i) not in ns_set:
            return False

    return True



def problem_041():
    max_prime = 0;
    for x in utils.prime_sieve(87654322):
        if is_pandigital(x):
            max_prime = x

    return max_prime

def main():
    print "Problem 41"
    print "Answer: " + str(problem_041())



if __name__ == '__main__':
    sys.exit(main())
