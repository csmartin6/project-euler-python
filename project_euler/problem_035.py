import sys
from . import utils

def problem_035():
    n = 1000000

    primes = set([p for p in utils.prime_sieve(n)])
    circular_primes = []
    for prime in primes:
        digits = utils.as_digit_array(prime)
        prime_count = 0
        for i in range(len(digits)):
            test_prime = utils.from_digit_array(digits[i:] + digits[:i])
            if test_prime not in primes:
                break
            else:
                prime_count += 1
        if prime_count == len(digits):
            circular_primes.append(prime)

    return len(circular_primes)

def main():
    print("Problem 35")
    print("Answer: " + str(problem_035()))


if __name__ == '__main__':
    sys.exit(main())
