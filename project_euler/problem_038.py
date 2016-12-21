import sys


def problem_038():
    for i in range(9876, 9123, -1):
        concat_product = str(i) + str(i * 2)
        if len(set(concat_product)) == 9 and '0' not in concat_product:
            return int(concat_product)
    return 0


def main():
    print("Problem 38")
    print("Answer: " + str(problem_038()))


if __name__ == '__main__':
    sys.exit(main())
