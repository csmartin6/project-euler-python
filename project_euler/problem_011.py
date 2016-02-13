import sys
import numpy as np
import utils
import os


def max_contigous_product(arr, length):
    products = [utils.product(arr[j:(j + length)]) for j in xrange(len(arr) - length + 1)]
    return max(products)


def max_product_in_row(arr, max_length):
    max_ = 0
    for row in arr:
        row_max = max_contigous_product(row, max_length)
        max_ = row_max if row_max > max_ else max_
    return max_


def max_product_on_diagonal(arr, max_length):
    m, n = arr.shape
    max_ = 0
    for k in xrange(-m + max_length, n - max_length):
        diag = np.diagonal(arr, k)
        diag_max = max_contigous_product(diag, max_length)
        max_ = diag_max if diag_max > max_ else max_
    return max_


def problem_011():
    arr = []
    max_length = 4

    filename = os.path.join(os.path.dirname(__file__), '../data/problem_011_input.txt')

    with open(filename, 'r') as f:
        for line in f:
            current_line = line.rstrip('\n').split(' ')
            arr.append([int(x) for x in current_line])

    nums = np.array(arr)
    max_in_row = max_product_in_row(nums, max_length)
    max_in_col = max_product_in_row(nums.T, max_length)
    max_in_diag = max_product_on_diagonal(nums, max_length)
    max_in_diag_t = max_product_on_diagonal(np.rot90(nums), max_length)
    max_product = max([max_in_row, max_in_col, max_in_diag, max_in_diag_t])

    return max_product


def main():
    print "Problem 11"
    print "Answer: " + str(problem_011())


if __name__ == '__main__':
    sys.exit(main())
