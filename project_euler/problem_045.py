import sys


def triangle_numbers(n):
    i = 0
    while i < n:
        i += 1
        yield i * (i + 1) / 2


def pentagonal_numbers(n):
    i = 0
    while i < n:
        i += 1
        yield i * (3 * i - 1) / 2


def hexagonal_numbers(n):
    i = 0
    while i < n:
        i += 1
        yield i * (2 * i - 1)


def problem_045():
    n = 10000000
    triangular = triangle_numbers(n)
    pentagonal = pentagonal_numbers(n)
    hexagonal = hexagonal_numbers(n)

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
