import sys
from collections import deque
from timeit import default_timer as timer


def problem_073():
    lower = (1, 3)
    upper = (1, 2)
    max_denominator = 12000

    between = 0
    pairs = deque()
    pairs.append((lower, upper))

    while pairs:
        lower, upper = pairs.popleft()
        if lower[1] + upper[1] <= max_denominator:
            mediant = (lower[0] + upper[0],
                       lower[1] + upper[1])
            between += 1
            pairs.append((lower, mediant))
            pairs.append((mediant, upper))

    return between


def main():
    print("Problem 73")
    start = timer()
    print("Answer: {}".format(problem_073()))
    print("Elapsed time: {}".format(timer() - start))


if __name__ == '__main__':
    sys.exit(main())
