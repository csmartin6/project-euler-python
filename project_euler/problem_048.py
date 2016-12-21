import sys
from . import utils


def problem_048():
    n = 1000
    last_ten_digits = []

    for i in range(1, n+1):
        digits = utils.as_digit_array(i)
        product = utils.truncated_power_num_array(digits, i, num_digits=10)
        last_ten_digits = utils.add_digit_array(last_ten_digits, product[-10:])[-10:]

    return utils.from_digit_array(last_ten_digits)


def main():
    print("Problem 48")
    print("Answer: " + str(problem_048()))


if __name__ == '__main__':
    sys.exit(main())
