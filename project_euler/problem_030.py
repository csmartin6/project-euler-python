import sys
import utils


def problem_030():
    n = 1000000

    nums = []

    for i in xrange(2, n):
        digits = utils.as_digit_array(i)

        sum_of_5th_powers = sum([x**5 for x in digits])
        if sum_of_5th_powers == i:
            nums.append(i)

    return sum(nums)


def main():
    print "Problem 30"
    print "Answer: " + str(problem_030())


if __name__ == '__main__':
    sys.exit(main())
