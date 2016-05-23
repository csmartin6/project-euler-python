import sys
import utils


def is_pandigital(n):
    ns = str(n)
    ns_set = set(ns)
    for i in range(1,len(ns)+1):
        if str(i) not in ns_set:
            return False

    return True



def problem_041():
    for x in reversed([y for y in utils.prime_sieve(87654322)]):
        if is_pandigital(x):
            return x

    return 0

def main():
    print "Problem 41"
    print "Answer: " + str(problem_041())



if __name__ == '__main__':
    sys.exit(main())
