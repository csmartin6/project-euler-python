import sys
import utils
import collections


def problem_052():
    for num_digits in range(2, 7):

        for n in range(10**num_digits, (10**(num_digits+1))//6):
            digits = collections.Counter(utils.as_digit_array(n))

            a = 2
            an = a * n
            an_digits = collections.Counter(utils.as_digit_array(an))
            while an_digits == digits and a < 6:
                a += 1
                an = a*n
                an_digits = collections.Counter(utils.as_digit_array(an))
            if digits == an_digits:
                return n

    return "not found"

def main():
    print("Problem 52")
    print("Answer: " + str(problem_052()))


if __name__ == '__main__':
    sys.exit(main())
