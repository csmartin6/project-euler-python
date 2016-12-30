import sys
import utils


def problem_058():
    prime_count = 0
    diagonal_count = 1
    prime_ratio = 1
    i = 1
    side = 1

    while prime_ratio >= 0.1:
        side = 2*i+1
        new_diags = range((side-2)**2, side**2, side-1)
        primes = [k for k in new_diags[1:] if utils.is_prime(k)]
        prime_count += len(primes)
        diagonal_count += 4
        prime_ratio = prime_count/diagonal_count
        i += 1

    return side


def main():
    print("Problem 58")
    print(("Answer: " + str(problem_058())))


if __name__ == '__main__':
    sys.exit(main())
