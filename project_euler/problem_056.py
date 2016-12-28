import sys
import utils


def problem_056():
    max_sum = 0
    for i in range(2, 100):
        n = utils.as_digit_array(i)
        for _ in range(100):
            digital_sum = sum(n)
            if digital_sum > max_sum:
                max_sum = digital_sum
            n = utils.scalar_multiply_num_array(n,i)
    return max_sum


def main():
    print("Problem 56")
    print(("Answer: " + str(problem_056())))


if __name__ == '__main__':
    sys.exit(main())