import sys
import utils


def problem_032():
    # 2 possible multipulcation setups
    # 2 * 3 * 4
    # 1 * 4 * 4

    # 2 * 3

    pandigital = set()

    for a in range(12, 99):
        a_digits = set(utils.as_digit_array(a))
        if len(a_digits) == 2:
            for b in range(123, 988):
                digits = set(a_digits)
                digits.update(utils.as_digit_array(b))
                if len(digits) == 5:
                    m = a * b
                    digits.update(utils.as_digit_array(m))
                    if 0 not in digits and len(digits) == 9 and m < 10000:
                        pandigital.add(m)

    for a in range(1, 10):
        a_digits = set(utils.as_digit_array(a))
        for b in range(1234, 9877):
            digits = set(a_digits)
            digits.update(utils.as_digit_array(b))
            if len(digits) == 5:
                m = a * b
                digits.update(utils.as_digit_array(m))
                if 0 not in digits and len(digits) == 9 and m < 10000:
                    pandigital.add(m)

    return sum(pandigital)


def main():
    print "Problem 32"
    print "Answer: " + str(problem_032())


if __name__ == '__main__':
    sys.exit(main())
