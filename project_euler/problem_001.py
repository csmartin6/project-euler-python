import sys


def problem_001():
    return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])


def main():
    print "Problem 1"
    print "Answer: " + str(problem_001())

if __name__ == '__main__':
    sys.exit(main())
