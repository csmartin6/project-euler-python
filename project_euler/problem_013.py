import sys
import utils
import os


def problem_013():
    arr = []
    filename = os.path.join(os.path.dirname(__file__), '../data/problem_013_input.txt')
    with open(filename, 'r') as f:
        for line in f:
            current_line = line.rstrip('\n')
            arr.append([int(x) for x in current_line])

    z = reduce(lambda b, c: utils.add_digit_array(b, c), arr)
    z = [str(a) for a in z]
    return int("".join(z[0:10]))


def main():
    print "Problem 13"
    print "Answer: " + str(problem_013())


if __name__ == '__main__':
    sys.exit(main())
