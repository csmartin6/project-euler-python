import sys
import utils


def concat(a, b):
    return int(str(a) + str(b)), int(str(b) + str(a))


def problem_060():
    prime_gen = utils.erat3()
    primes = set()
    one_prime_sets = set()
    two_prime_sets = set()
    three_prime_sets = set()
    four_prime_sets = set()
    max_prime = 0

    def is_prime(n):
        nonlocal primes, prime_gen, max_prime
        while max_prime <= n:
            np = prime_gen.__next__()
            primes.add(np)
            max_prime = np

        return n in primes

    def add_to_prime_pair_set(orig_set, pr):

        for prime in orig_set:
            for cp in concat(pr, prime):
                if not is_prime(cp):
                    return False
        return True

    for p in utils.erat3():

        for s in four_prime_sets:
            if add_to_prime_pair_set(s, p):
                return sum(s) + p

        for s in three_prime_sets:
            if add_to_prime_pair_set(s, p):
                four_prime_sets.add(s + (p,))

        for s in two_prime_sets:
            if add_to_prime_pair_set(s, p):
                three_prime_sets.add(s + (p,))

        for s in one_prime_sets:
            if add_to_prime_pair_set(s, p):
                two_prime_sets.add(s + (p,))

        one_prime_sets.add((p,))

    return "Something went wrong"


def main():
    print("Problem 60")
    print(("Answer: " + str(problem_060())))


if __name__ == '__main__':
    sys.exit(main())
