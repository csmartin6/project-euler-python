import sys
import utils


def problem_050():
    n = 1000000
    primes = [p for p in utils.prime_sieve(n)]
    prime_set = set(primes)

    max_sum = 0
    prime_seq = []

    max_seq_len = 0
    for i, p in enumerate(primes):
        cum = sum(primes[i:(i+max_seq_len)])

        if cum > n:
            break

        seq_len = 0
        for j,q in enumerate(primes[(i+max_seq_len):]):
            cum += q

            if cum > n:
                if seq_len > max_seq_len:
                    max_seq_len = seq_len
                break

            if cum in prime_set:
                seq_len = max_seq_len+j
                max_sum = cum
                prime_seq = primes[i:(i+max_seq_len+j+1)]

    return max_sum


def main():
    print "Problem 50"
    print "Answer: " + str(problem_050())


if __name__ == '__main__':
    sys.exit(main())
