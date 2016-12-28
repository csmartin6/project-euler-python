import sys
import utils
import collections
import itertools


def problem_051():
    num_in_seq = 8
    n = 6
    primes = utils.erat3()
    next_prime = next(primes)
    while next_prime < 10**(n-1):
        next_prime = next(primes)

    for n in range(6, 8):

        # find all n digit primes
        n_digit_primes = set()
        while next_prime < 10**n:
            n_digit_primes.add(next_prime)
            next_prime = next(primes)

        for d in [3]: #range(1, n + 1):
            for digit_values in itertools.product(list(range(10)), repeat=n-d):

                if sum(digit_values) % 3 != 0:
                    for digit_pos in itertools.combinations(list(range(n-1)), n-d-1):
                        digit_pos_ = digit_pos+(n-1,)
                        prime_seq = []
                        for i in range(10):
                            test_prime = [i]*n

                            for p, v in zip(digit_pos_,digit_values):
                                test_prime[p] = v

                            test_prime = utils.from_digit_array(test_prime)

                            if test_prime in n_digit_primes:
                                prime_seq.append(test_prime)
                            if len(prime_seq) + (10-i) < num_in_seq:
                                break

                        if len(prime_seq) >= num_in_seq:
                            # print("prime_seq: {}".format(prime_seq))
                            return min(prime_seq)


def problem_051_c():
    num_in_seq = 8
    n = 6
    primes = utils.erat3()
    next_prime = next(primes)
    min_in_seq = float("inf")
    while next_prime < 10**(n-1):
        next_prime = next(primes)

    for n in range(6, 8):
        # find all n digit primes
        n_digit_primes = set()
        while next_prime < 10**n:
            n_digit_primes.add(next_prime)
            next_prime = next(primes)



        num_digits = 3
        digit_map = {}
        for p in  n_digit_primes:
            digits = utils.as_digit_array(p)
            c = collections.Counter(digits)
            for digit, count in c.items():
                if count >= num_digits:
                    s = str(p)
                    digit_pos = [pos for pos, char in enumerate(s) if char == str(digit)]
                    for c in itertools.combinations(digit_pos,num_digits):
                        x_digits = [str(d) for d in digits]
                        for pos in c:
                            x_digits[pos] = 'x'

                        sp = ''.join(x_digits)
                        if sp in digit_map :
                            digit_map[sp] += [p]
                        else:
                            digit_map[sp] = [p]

        for k,v in digit_map.items():
            if len(v) >= num_in_seq:
                min_in_seq = min(min(v) ,min_in_seq)

        if min_in_seq != float("inf"):
            return min_in_seq


def main():
    print("Problem 51")
    print("Answer: " + str(problem_051()))


if __name__ == '__main__':
    sys.exit(main())
