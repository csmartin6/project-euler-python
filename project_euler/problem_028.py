import sys


def problem_028():
    n = 1001
    s = 1
    for a in range(3, n + 1, 2):
        corners = list(range(a * a, (a - 2) * (a - 2), -a + 1))
        s += sum(corners)

    return s


def main():
    print("Problem 28")
    print("Answer: " + str(problem_028()))


if __name__ == '__main__':
    sys.exit(main())
