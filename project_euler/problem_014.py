import sys
from collections import Counter


def next_num(n):
    next_number = n / 2 if n % 2 == 0 else 3 * n + 1
    return next_number


def problem_014_a():
    n = 1000001
    seq_lengths = {1: 1}

    for i in range(2, n):
        current_number = i
        count = 0
        while current_number not in seq_lengths:
            current_number = next_num(current_number)
            count += 1

        seq_lengths[i] = count + seq_lengths[current_number]

    return max(seq_lengths, key=lambda k: seq_lengths[k])


def collatz(n):
    yield n
    while n != 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        yield n


def problem_014_b():
    n = 1000001
    seq_lengths = Counter()

    for i in range(1, n):
        for x in collatz(i):
            if x in seq_lengths:
                seq_lengths[i] += seq_lengths[x]
                break
            else:
                seq_lengths[i] += 1

    return max(seq_lengths, key=lambda k: seq_lengths[k])


def main():
    print("Problem 14")
    print("Method A: " + str(problem_014_a()))
    print("Method B: " + str(problem_014_b()))


if __name__ == '__main__':
    sys.exit(main())
