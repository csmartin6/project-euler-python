import sys


def problem_044():

    pentagonal = [n*(3*n-1)/2 for n in range(1, 10000)]
    pentagonal_set = set(pentagonal)
    candidates = {}

    for i, k in enumerate(pentagonal):
        for j in pentagonal[:i]:
            if (k+j) in pentagonal_set and (k-j) in pentagonal_set:
                candidates[(j, k)] = k - j

    return min(candidates.values())


def main():
    print "Problem 44"
    print "Answer: " + str(problem_044())


if __name__ == '__main__':
    sys.exit(main())
