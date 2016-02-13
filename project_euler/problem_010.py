import sys
import utils

# def problem_010():
#     n = 2000000
#
#     acc = 2
#     nums = xrange(3, n + 1, 2)
#     cur_prime = 3
#     while cur_prime <= np.sqrt(n):
#         cur_prime = nums[0]
#         acc += cur_prime
#         nums = [x for x in nums if x % cur_prime != 0]
#     return acc + sum(nums)


def problem_010():
    n = 2000000
    primes = list(utils.prime_sieve(n))
    return sum(primes)


def main():
    print "Problem 10"
    print "Answer: " + str(problem_010())


if __name__ == '__main__':
    sys.exit(main())
