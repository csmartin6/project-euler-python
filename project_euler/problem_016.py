import sys
import utils


def problem_016():
    n = 1000
    digits= [1]

    for i in xrange(n):
        digits = utils.add_digit_array(digits, digits)

    return sum(digits)



def main():
    print "Problem 16"
    print "Answer: " + str(problem_016())


if __name__ == '__main__':
    sys.exit(main())