import sys


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def next_number(n):
    return n + int(str(n)[::-1])


def problem_055():
    lychel_numbers = []
    for n in range(1, 10000):
        y = n
        lychel = True
        for i in range(50):
            y = next_number(y)
            if is_palindrome(y):
                lychel = False
                break
        if lychel:
            lychel_numbers.append(n)

    return len(lychel_numbers)


def main():
    print("Problem 55")
    print(("Answer: " + str(problem_055())))


if __name__ == '__main__':
    sys.exit(main())
