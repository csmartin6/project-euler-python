import sys


def problem_002():
    fib = [1, 1]
    while fib[-2] + fib[-1] < 4000000:
        fib.append(fib[-2] + fib[-1])

    return sum([x for x in fib if x % 2 == 0])


def main():
    print problem_002()

if __name__ == '__main__':
    sys.exit(main())
