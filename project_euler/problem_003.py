import sys
import utils


def problem_003():
    n = 600851475143
    return max(utils.prime_factors(n))


def main():
    print problem_003()

if __name__ == '__main__':
    sys.exit(main())
