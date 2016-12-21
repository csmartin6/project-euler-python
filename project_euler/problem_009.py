import sys


def problem_009():
    n = 1000
    result = None

    for i in range(n):
        for j in range(i+1, (n-i)//2):
            k = n-i-j
            if i * i + j * j == k * k:
                result = i*j*k

    return result


def main():
    print("Problem 9")
    print("Answer: " + str(problem_009()))

if __name__ == '__main__':
    sys.exit(main())
