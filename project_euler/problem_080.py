import sys
from timeit import default_timer as timer
import utils


def squart_root_digits(number, num_digits=100):
    a = utils.as_digit_array(number)
    if len(a) % 2:
        a = [0] + a

    a = a + [0] * (2 * num_digits - len(a))

    digits = []
    c = 0
    p = 0
    for i in range(0, len(a), 2):
        c = 100 * c + utils.from_digit_array(a[i:i + 2])

        for x in range(1, 11):
            if x * (20 * p + x) > c:
                break
        x -= 1
        digits.append(x)
        y = x * (20 * p + x)
        p = 10 * p + x
        c -= y
        if c == 0:
            break

    return digits


def problem_080():
    sum_ = 0
    num_digits = 100
    for n in range(101):
        digits = squart_root_digits(n, num_digits=num_digits)
        if len(digits) == num_digits:
            sum_ += sum(digits)
    return sum_


def main():
    print("Problem 80")
    start = timer()
    print("Answer: {}".format(problem_080()))
    print("Elapsed time: {}".format(timer() - start))


if __name__ == '__main__':
    sys.exit(main())
