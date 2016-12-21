import sys
import utils


def problem_012():
    n = 500
    num = 1
    i = 1
    while utils.count_divisors(num) < n:
        i += 1
        num += i
    return num


def main():
    print("Problem 12")
    print("Answer: " + str(problem_012()))


if __name__ == '__main__':
    sys.exit(main())
