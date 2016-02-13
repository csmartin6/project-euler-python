import sys


def problem_004():
    palindromes = [x*y for x in xrange(900, 1000) for y in xrange(900, 1000) if str(x*y) == str(x*y)[::-1]]
    return max(palindromes)


def main():
    print "Problem 4"
    print "Answer: " + str(problem_004())

if __name__ == '__main__':
    sys.exit(main())
