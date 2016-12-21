import sys
from . import utils
import fractions
from functools import reduce

def problem_033():
    tol = 1e-7
    digit_cancelling_fractions = []
    for i in range(10,100):
        for j in range(i+1,100):
            value = fractions.Fraction(i,j)

            numerator = utils.as_digit_array(i)
            denominator = utils.as_digit_array(j)
            for d in numerator:
                if d != 0 and d in denominator:
                    new_numerator = list(numerator)
                    new_numerator.remove(d)
                    new_denominator = list(denominator)
                    new_denominator.remove(d)
                    if new_denominator[0] != 0:
                        new_value = fractions.Fraction(new_numerator[0],new_denominator[0])
                        if new_value == value :
                            digit_cancelling_fractions.append(value)
                            #print "i: {}, j: {}".format(i,j)

    #print digit_cancelling_fractions
    return reduce(lambda x,y: x*y, digit_cancelling_fractions).denominator


def main():
    print("Problem 33")
    print(("Answer: " + str(problem_033())))


if __name__ == '__main__':
    sys.exit(main())
