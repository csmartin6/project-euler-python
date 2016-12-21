import sys
import numpy as np
from functools import reduce


def problem_040():
    magnitude_changes = np.cumsum([i * 9 * 10 ** (i - 1) for i in range(1, 7)])
    magnitude_changes = np.append([0],magnitude_changes)
    digits = [] #['1']
    ns = [10**i for i in range(7)]
    for n in ns:

        magnitude_idx = np.searchsorted(magnitude_changes, n) -1
        base_number = 10 ** (magnitude_idx)
        digits_past_base = n - magnitude_changes[magnitude_idx]
        numbers_past_base, digit_in_number = divmod(digits_past_base, magnitude_idx + 1)

        if digit_in_number == 0: # digit is actuall in previous number
            nth_digit = str(base_number + numbers_past_base -1)[-1]
        else:
            nth_digit = str(base_number + numbers_past_base)[digit_in_number-1]
        digits.append(nth_digit)
    return reduce(lambda a, b: a * int(b), digits, 1)


def problem_040_brute_force():
    champernowne = ""

    for i in range(1000000):
        champernowne += str(i)

    digits = []

    for i in range(7):
        n = 10 ** i
        nth_digit = champernowne[n]
        digits.append(nth_digit)

    return reduce(lambda a, b: a * int(b), digits, 1)


def main():
    print("Problem 40")
    print("Answer: " + str(problem_040()))

    print("Problem 40 b")
    print("Answer: " + str(problem_040_brute_force()))


if __name__ == '__main__':
    sys.exit(main())
