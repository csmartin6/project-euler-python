import sys
import numpy as np
import os


def max_path(triangle):
    max_sum = []
    for index, row in enumerate(triangle):
        if not max_sum:
            max_sum.append(row)
        else:
            row_max = np.zeros_like(row)
            for pos, value in enumerate(row):
                row_max[pos] = value + max(max_sum[index - 1][max(pos - 1, 0)],
                                           max_sum[index - 1][min(pos, index - 1)])
            max_sum.append(row_max)

    return max(max_sum[-1])


def problem_018():
    triangle = []

    filename = os.path.join(os.path.dirname(__file__), '../data/problem_018_input.txt')
    with open(filename, 'r') as f:
        for line in f:
            current_line = line.rstrip('\n').split(' ')
            triangle.append([int(x) for x in current_line])

    return max_path(triangle)


def main():
    print "Problem 18"
    print "Answer: " + str(problem_018())


if __name__ == '__main__':
    sys.exit(main())
