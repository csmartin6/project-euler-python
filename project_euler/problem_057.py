import sys
import utils


def root_2_series(n):
    i = 0
    a = 1
    b = 1
    yield a,b
    while i <= n:
        a,b = (2*b+a), (b+a)
        i += 1
        yield a,b



def problem_057():

    count = 0
    for a,b in root_2_series(1000):
        if len(str(a)) > len(str(b)):
            count += 1

    return count



def main():
    print("Problem 57")
    print(("Answer: " + str(problem_057())))


if __name__ == '__main__':
    sys.exit(main())