import sys

import utils


def problem_023():
    n = 28124
    abundant_numbers = [x for x in range(n) if sum(utils.proper_divisors(x)) > x]
    nums = [0]*n
    for i, numberA in enumerate(abundant_numbers):
        for numberB in abundant_numbers[i:]:
            if numberA + numberB < n:
                nums[numberA + numberB] = 1

    non_abundant = [number for number, sum_of_abundant in enumerate(nums) if not sum_of_abundant]

    return sum(non_abundant)


def main():
    print "Problem 23"
    print "Answer: " + str(problem_023())


if __name__ == '__main__':
    sys.exit(main())
