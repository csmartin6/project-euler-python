import sys
from timeit import default_timer as timer
from functools import lru_cache


@lru_cache(maxsize=100000)
def partition_count(n, modulus=1000000):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        m = 1
        penta = m*(3*m-1)//2
        part = 0
        while penta <= n:
            part += ((-1) ** (abs(m)-1)) * partition_count(n-penta, modulus)
            m = - m + 1 if m < 0 else -m
            penta = m * (3 * m - 1) // 2

        return part % modulus


def problem_078():
    part = -1
    num = 1
    modulus = 1000000
    while part != 0:
        num += 1
        part = partition_count(num, modulus)
    return num


def main():
    print("Problem 78")
    start = timer()
    print("Answer: {}".format(problem_078()))
    print("Elapsed time: {}".format(timer() - start))


if __name__ == '__main__':
    sys.exit(main())
