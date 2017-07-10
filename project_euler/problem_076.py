import sys
from timeit import default_timer as timer
from functools import lru_cache

def distinct_sum(n):
    return distinct_sum_inner(n, n-1)

@lru_cache(maxsize=10000)
def distinct_sum_inner(n, k):
    if k == 0 or n == 0:
        return 0
    elif k == n:
        return 1 + distinct_sum_inner(n, k-1)
    else:
        return sum([distinct_sum_inner(n - i, min(i, k, n-i)) for i in range(1, min(k, n) + 1)])


def problem_076():
    n = 100
    return distinct_sum(n)


def main():
    print("Problem 76")
    start = timer()
    print("Answer: {}".format(problem_076()))
    print("Elapsed time: {}".format(timer() - start))


if __name__ == '__main__':
    sys.exit(main())
