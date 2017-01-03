import sys
import itertools


def triangle(n):
    i = 1
    x = 1
    while x < n:
        yield x
        i += 1
        x = i * (i+1) // 2


def square(n):
    i = 1
    x = 1
    while x < n:
        yield x
        i += 1
        x = i * i


def pentagonal(n):
    i = 1
    x = 1
    while x < n:
        yield x
        i += 1
        x = i * (3*i - 1) // 2


def hexagonal(n):
    i = 1
    x = 1
    while x < n:
        yield x
        i += 1
        x = i * (2*i - 1)


def heptagonal(n):
    i = 1
    x = 1
    while x < n:
        yield x
        i += 1
        x = i * (5*i - 3) // 2


def octagonal(n):
    i = 1
    x = 1
    while x < n:
        yield x
        i += 1
        x = i * (3*i - 2)


def next_cycle(cycle, prefix, figurate):

    if not figurate:
        if prefix != int(str(cycle[0])[:2]):
            return None
        else:
            return cycle

    for i in range(len(figurate)):
        if prefix in figurate[i]:
            for num in figurate[i][prefix]:
                rem_figurate = figurate[:i] + figurate[i+1:]
                next_prefix = int(str(num)[2:])
                rest_of_cycle = next_cycle(cycle + [num], next_prefix, rem_figurate)
                if rest_of_cycle is not None:
                    return rest_of_cycle
        else:
            return None


def problem_061():
    n_min = 1000
    n_max = 10000
    figurate = [[n for n in triangle(n_max) if n > n_min],
                [n for n in square(n_max) if n > n_min],
                [n for n in pentagonal(n_max) if n > n_min],
                [n for n in hexagonal(n_max) if n > n_min],
                [n for n in heptagonal(n_max) if n > n_min],
                [n for n in octagonal(n_max) if n > n_min]]

    figurate_split = []
    for f in figurate:
        groups = {}
        data = sorted(f, key=lambda y: int(str(y)[:2]))
        for k, g in itertools.groupby(data, key=lambda y: int(str(y)[:2])):
            groups[k] = list(g)
        figurate_split.append(groups)

    for f in figurate[0]:
        next_prefix = int(str(f)[2:])
        cycle = next_cycle([f], next_prefix, figurate_split[1:])
        if cycle is not None:
            print("cycle: {}".format(cycle))
            return sum(cycle)

    return "No cycle found"


def main():
    print("Problem 61")
    print(("Answer: " + str(problem_061())))


if __name__ == '__main__':
    sys.exit(main())
