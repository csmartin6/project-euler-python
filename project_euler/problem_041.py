import sys
import numpy as np
import utils


def is_pandigital(n):
    ns = str(n)
    print ns
    ns_set = set(ns[:])
    print ns_set
    for i in range(1,len(ns)+1):
        if i not in ns_set:
            return False

    return True



def problem_041():
    max_prime = 0;
    for x in utils.prime_sieve(654321):
        if is_pandigital(x):
            max_prime = x

    return max_prime

def main():
    print is_pandigital(4321)
    #print "Problem 41"
    #print "Answer: " + str(problem_041())



if __name__ == '__main__':
    sys.exit(main())
