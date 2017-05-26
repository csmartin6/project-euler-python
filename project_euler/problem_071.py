import sys
from fractions import Fraction
from math import gcd

# TODO: use Farey's neighbours
# medieands
# 2+3k / 5+7k


def problem_071():
    n = 1000000
    target = Fraction(3,7)
    closest = Fraction(0,1)
    for denom in range(2,n):
        if denom != target.denominator:

            numer = int(denom*target)

            if gcd(numer, denom) == 1:
                cand = Fraction(numer, denom)
                if cand > closest:
                    closest = cand

    return cand.numerator


def main():
    print("Problem 71")
    print(("Answer: " + str(problem_071())))


if __name__ == '__main__':
    sys.exit(main())
