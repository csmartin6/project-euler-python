import sys


def problem_001():
    return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])


def main():
    print problem_001()

if __name__ == '__main__':
    sys.exit(main())
