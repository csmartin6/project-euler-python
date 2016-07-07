import sys
import numpy as np
cache = {}


def count_routes(i, j):
    if i == 0 or j == 0:
        return 1
    else:
        if (i, j) in cache:
            return cache[(i, j)]
        else:
            cache[(i, j)] = count_routes(i - 1, j) + count_routes(i, j - 1)
            return cache[(i, j)]


def problem_015():
    n = 20

    num_paths = np.zeros((n + 1, n + 1), dtype=int)

    num_paths[0, :] = 1
    num_paths[:, 0] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            from_left = num_paths[i, j - 1]
            from_above = num_paths[i - 1, j]
            num_paths[i, j] = from_left + from_above

    return count_routes(20, 20)


def main():
    print "Problem 15"
    print "Answer: " + str(problem_015())


if __name__ == '__main__':
    sys.exit(main())
