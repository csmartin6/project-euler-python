import sys


def problem_062():

    cube_digits = {}
    x = 1
    while True:
        cube = x * x * x
        digits = ''.join(sorted(str(cube)))

        if digits not in cube_digits:
            cube_digits[digits] = []

        cube_digits[digits].append(cube)

        if len(cube_digits[digits]) == 5:
            return min(cube_digits[digits])
        x += 1


def main():
    print("Problem 62")
    print(("Answer: " + str(problem_062())))


if __name__ == '__main__':
    sys.exit(main())
