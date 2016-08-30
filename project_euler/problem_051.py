import sys
import utils
import collections
import itertools

def problem_051():

    # n 4 to 10
    #   find all n digit primes
    #   decompose all primes into bag of digits
    #   remove all primes that don't have 3 of the same digit
    #   check_map {digit_pos: {digits value: prime}},
    #   for each remaining prime.
    #       for every set of three digit positions
    #           insert into check_map

    #   loop over map
    #       find any digit pos value pairs that have a size > threshold

    num_in_seq = 7
    n = 2
    found = False
    primes = utils.erat3()
    next_prime = primes.next()
    while next_prime < 10**(n-1):
        next_prime = primes.next()

    for n in range(2,8):

        # find all n digit primes
        n_digit_primes = set()
        while next_prime < 10**n:
            n_digit_primes.add(next_prime)
            next_prime = primes.next()
            #print next_prime

        for d in range(1, n + 1):

            for digit_values in itertools.product(range(10), repeat=n-d):
                for digit_pos in itertools.combinations(range(n), n-d):
                    prime_seq = []
                    for i in range(10):
                        test_prime = [i]*n
                        for p, v in zip(digit_pos,digit_values):
                            test_prime[p] = v

                        test_prime = utils.from_digit_array(test_prime)

                        if test_prime in n_digit_primes:
                            prime_seq.append(test_prime)
                        if len(prime_seq) + (10-i) < num_in_seq:
                            break

                    if len(prime_seq) >= num_in_seq:
                        print "prime_seq: {}".format(prime_seq)
                        return min(prime_seq)




def main():
    print "Problem 51"
    print "Answer: " + str(problem_051())


if __name__ == '__main__':
    sys.exit(main())
