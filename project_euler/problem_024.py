import math
import sys


def find_nth_ordering(n, digits, seq_length):
    num_orderings = math.factorial(seq_length - 1)
    if seq_length == 1:
        return [digits[n]]
    for index, digit in enumerate(digits):
        if (index + 1) * num_orderings > n:
            remaining_digits = digits[:index] + digits[(index + 1):]
            return [digit] + find_nth_ordering(n - (index * num_orderings), remaining_digits, seq_length - 1)
    raise RuntimeError("Something has gone wrong")


def problem_024():
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nth = 999999

    return int(''.join([str(x) for x in find_nth_ordering(nth, d, len(d))]))


def main():
    print("Problem 24")
    print("Answer: " + str(problem_024()))


if __name__ == '__main__':
    sys.exit(main())
