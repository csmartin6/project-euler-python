import sys
import os


import problem_018


def problem_067():
    triangle = []

    filename = os.path.join(os.path.dirname(__file__), '../data/p067_triangle.txt')
    with open(filename, 'r') as f:
        for line in f:
            current_line = line.rstrip('\n').split(' ')
            triangle.append([int(x) for x in current_line])

    return problem_018.max_path(triangle)


def main():
    print "Problem 67"
    print "Answer: " + str(problem_067())


if __name__ == '__main__':
    sys.exit(main())
