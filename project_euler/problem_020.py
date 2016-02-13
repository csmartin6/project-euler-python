import sys
import utils


def problem_020():
    n = 100
    fact = [1]
    for i in xrange(1, n + 1):
        fact = utils.scalar_multiply_num_array(fact, i)

    return sum(fact)


def main():
    print "Problem 20"
    print "Answer: " + str(problem_020())


if __name__ == '__main__':
    sys.exit(main())
