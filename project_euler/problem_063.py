import sys
import numpy as np


def problem_063():
    n_digit_powers = 0
    n_max = np.log(10) / (np.log(10) - np.log(9))
    for n in range(1, int(np.ceil(n_max))):
        i = 0
        i_n = i ** n
        digit_count = len(str(i_n))
        while digit_count <= n:
            i += 1
            i_n = i ** n
            digit_count = len(str(i_n))
            if digit_count == n:
                # print("{} digits \t {} = {} ^ {}".format(n,i_n,i,n))
                n_digit_powers += 1

    return n_digit_powers


def problem_063_v2():
    return sum([int(np.log(10) / (np.log(10) - np.log(n))) for n in range(1,10)])

def main():
    print("Problem 63")
    print(("Answer: " + str(problem_063())))
    print(("Answer: " + str(problem_063_v2())))


if __name__ == '__main__':
    sys.exit(main())