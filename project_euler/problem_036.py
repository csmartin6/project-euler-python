import sys


def problem_036():
    n = 1000000
    palindromes = []
    for x in xrange(n):
        base_10 = str(x)
        base_2 = bin(x)[2:]
        if base_10 == base_10[::-1] and base_2 == base_2[::-1]:
            palindromes.append(x)

    return sum(palindromes)


def main():
    print "Problem 36"
    print "Answer: " + str(problem_036())


if __name__ == '__main__':
    sys.exit(main())
