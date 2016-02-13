import sys
import utils


def problem_007():
    n = 10001
    i = 1
    prime_count = 1
    while prime_count < n:
        i += 2
        if utils.is_prime(i):
            prime_count += 1
    return i


def main():
    print "Problem 7"
    print "Answer: " + str(problem_007())


if __name__ == '__main__':
    sys.exit(main())
