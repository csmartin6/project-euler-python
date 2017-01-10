import sys
from fractions import Fraction
import utils


def eval_cont_fraction(a):
    val = 0
    for an in reversed(a[1:]):
        val = Fraction(1, an + val)
    return a[0] + val


def problem_065():
    e_ns = [2] + [1]*99
    k = 1
    for i in range(2, len(e_ns), 3):
        e_ns[i] = 2*k
        k += 1
    nth_convergent = eval_cont_fraction(e_ns).numerator

    return sum(utils.as_digit_array(nth_convergent))


def main():
    print("Problem 65")
    print(("Answer: " + str(problem_065())))


if __name__ == '__main__':
    sys.exit(main())
