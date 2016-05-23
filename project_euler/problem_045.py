import sys


def triangle_numbers():
    n = 0
    while True:
        n += 1
        yield n * (n + 1) / 2


def pentagonal_numbers():
    n = 0
    while True:
        n += 1
        yield n * (3 * n - 1) / 2


def hexagonal_numbers():
    n = 0
    while True:
        n += 1
        yield n * (2 * n - 1)


def problem_045():

    triangular = triangle_numbers()
    pentagonal = pentagonal_numbers()
    hexagonal = hexagonal_numbers()

    p = 40756
    t = 40756

    for h in hexagonal:

        while p < h:
            p = pentagonal.next()

        while t < h:
            t = triangular.next()

        if p == h and t == h:
            break

    return h


def main():
    print "Problem 45"
    print "Answer: " + str(problem_045())


if __name__ == '__main__':
    sys.exit(main())
