import sys


def ways_to_make_change(total, coins):
    if total == 0:
        return 0

    result = 0
    for i, c in enumerate(coins):
        if c == total:
            result += 1
        elif c <= total:
            result += ways_to_make_change(total - c, coins[i:])

    return result


def problem_031():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    change = 200
    return ways_to_make_change(change, coins)


def main():
    print("Problem 31")
    print("Answer: " + str(problem_031()))


if __name__ == '__main__':
    sys.exit(main())
