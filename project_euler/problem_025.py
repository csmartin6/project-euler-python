import math
import sys

def problem_025():
    n = 1000
    fib = [1, 1]
    i = 1
    digits = 1

    while digits < n:
        fib.append(fib[i] + fib[i - 1])
        i += 1
        digits = int(math.log10(fib[i])) + 1

    return (i + 1)


def main():
    print "Problem 25"
    print "Answer: " + str(problem_025())


if __name__ == '__main__':
    sys.exit(main())

