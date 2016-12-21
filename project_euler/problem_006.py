import sys


def problem_006():
    n = 100
    sum_of_squares = 0
    for i in range(n+1):
        sum_of_squares += i * i

    squared_sum = (n*(n+1)/2)**2
    return squared_sum-sum_of_squares


def main():
    print("Problem 6")
    print("Answer: " + str(problem_006()))

if __name__ == '__main__':
    sys.exit(main())
