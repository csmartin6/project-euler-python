import sys
from . import utils
import math
from functools import reduce

def problem_034():
    digit_factorials = []
    factorials = [math.factorial(x) for x in range(10)]
    for x in range(10,2540160):
        digits = utils.as_digit_array(x)
        sum_factorial = reduce(lambda a,b: a + factorials[b], digits, 0)
        if sum_factorial == x:
            digit_factorials.append(x)

    return sum(digit_factorials)

def main():
    print("Problem 34")
    print("Answer: " + str(problem_034()))


if __name__ == '__main__':
    sys.exit(main())
