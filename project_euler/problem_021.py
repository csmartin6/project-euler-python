import sys
import utils


def problem_021():
    n = 10001
    proper_divisor_sums = {}
    amicable_pairs = set()
    amicable_numbers = set()

    for num in xrange(n):
        proper_divisor_sum = sum(utils.proper_divisors(num))
        proper_divisor_sums[num] = proper_divisor_sum

        if proper_divisor_sum in proper_divisor_sums:
            c_divisor_sum = proper_divisor_sums[proper_divisor_sum]
        else:
            c_divisor_sum = sum(utils.proper_divisors(proper_divisor_sum))
            proper_divisor_sums[proper_divisor_sum] = c_divisor_sum

        if (num == c_divisor_sum) and num != proper_divisor_sum:
            amicable_pair = (num, proper_divisor_sum) if num < proper_divisor_sum else (proper_divisor_sum, num)
            amicable_pairs.add(amicable_pair)

            amicable_numbers.add(num)
            amicable_numbers.add(proper_divisor_sum)

    return sum(amicable_numbers)


def main():
    print "Problem 21"
    print "Answer: " + str(problem_021())


if __name__ == '__main__':
    sys.exit(main())
