import sys
import utils


def problem_072():

    n = 1000000
    totients = [utils.totient(i) for i in range(2, n+1)]
    return sum(totients)


def main():
    print("Problem 72")
    print(("Answer: " + str(problem_072())))

if __name__ == '__main__':
    sys.exit(main())
