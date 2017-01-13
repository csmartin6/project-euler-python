import sys
import numpy as np
from fractions import Fraction

def min_quad_diophantine(d):
    x = 1
    y = 1

    while True:
        lhs = x * x - 1
        rhs = d * y * y
        if lhs == rhs:
            return x,y
        if lhs > rhs:
            y+=1
        else:
            x+=1


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

def eval_cont_fraction(a):
    val = 0
    for an in reversed(a[1:]):
        val = Fraction(1, an + val)
    return a[0] + val

def pell_quad_diophantine(d):

    a0, al, l = cont_frac_sqrt(d)

    if l % 2 == 0:
        c = eval_cont_fraction([a0]+al[:l])

    else:
        c = eval_cont_fraction([a0] + al+al[:l])
    return c.numerator, c.numerator



def problem_066():
    # x_max = max([min_quad_diophantine(d)[0] for d in range(2,12) if (int(np.sqrt(d)))**2 != d])
    x_max = 0
    d_max = 0
    for d in range(2, 1001):
        if (int(np.sqrt(d)))**2 != d:
            x,y = pell_quad_diophantine(d)
            if x >= x_max:
                x_max = x
                d_max = d
    return d_max


def main():
    print("Problem 66")
    print(("Answer: " + str(problem_066())))


if __name__ == '__main__':
    sys.exit(main())
