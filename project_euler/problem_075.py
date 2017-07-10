import sys
from timeit import default_timer as timer
import numpy as np


def problem_075():
    L = 1500000
    perimeters = {}
    n_max = L//3

    for n in range(1, n_max):
        m_max = (- (2*n) + np.sqrt(4*(n**2) + 8 * L))/4
        for m in range(n+1, int(m_max)+1):
            a_0 = (m * m - n * n)
            b_0 = 2 * m * n
            a_0, b_0 = min(a_0, b_0), max(a_0, b_0)
            c_0 = (m * m + n * n)
            if a_0 + b_0 + c_0 > L:
                break
            for k in range(1, n_max):
                a = k * a_0
                b = k * b_0
                c = k * c_0
                per = a + b + c
                if per > L:
                    break
                else:
                    if per not in perimeters:
                        perimeters[per] = set()

                    perimeters[per].add((a, b, c))
    return len([k for k, v in perimeters.items() if len(v) == 1])


def main():
    print("Problem 75")
    start = timer()
    print("Answer: {}".format(problem_075()))
    print("Elapsed time: {}".format(timer() - start))


if __name__ == '__main__':
    sys.exit(main())
