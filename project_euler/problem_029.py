import sys


def problem_029():
    n = 100
    powers = set()
    for a in xrange(2, n+1):
        cur = a
        for i in xrange(n-1):
            cur *= a
            powers.add(cur)

    return len(powers)


def main():
    print "Problem 29"
    print "Answer: " + str(problem_029())


if __name__ == '__main__':
    sys.exit(main())
