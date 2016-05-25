import sys
import utils


def problem_049():
    primes = [p for p in utils.prime_sieve(10000) if p > 1000]
    primes_by_sorted_digits = {}
    for p in primes:
        s = ''.join(sorted(str(p)))
        if s not in primes_by_sorted_digits:
            primes_by_sorted_digits[s] = []
        primes_by_sorted_digits[s] += [p]

    for k, v in primes_by_sorted_digits.iteritems():
        if len(v) >= 3:
            arithmetic_seq = sorted(v)

            for i,a in enumerate(arithmetic_seq):
                for b in arithmetic_seq[(i+1):]:
                    c = (2*b - a)
                    if c in arithmetic_seq and c != 8147:
                        return ''.join([str(a),str(b),str(c)])

    return ''


def main():
    print "Problem 49"
    print "Answer: " + str(problem_049())


if __name__ == '__main__':
    sys.exit(main())
