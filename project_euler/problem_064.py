import sys
import numpy as np
from fractions import Fraction


def cont_frac_sqrt(n):
    sqrt_n = np.sqrt(n)
    a = []
    numer, rem = 1, int(sqrt_n)
    init_state = (numer, rem)
    while True:
        x = Fraction(numer, n - rem * rem)
        whole = int((sqrt_n + rem)/x.denominator)
        a.append(whole)
        rem = whole * x.denominator - rem
        numer = x.denominator
        if (numer, rem) == init_state:
            return int(sqrt_n), a, len(a)


def problem_064():
    odd_period = 0
    for i in range(2, 10001):
        if int(np.sqrt(i))*int(np.sqrt(i)) != i:
            whole, rep, period = cont_frac_sqrt(i)
            if period % 2:
                odd_period += 1

    return odd_period


def main():
    print("Problem 64")
    print(("Answer: " + str(problem_064())))


if __name__ == '__main__':
    sys.exit(main())
