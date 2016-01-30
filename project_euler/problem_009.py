import sys

def problem_009():
    n = 1000
    for i in xrange(n):
        for j in xrange(i+1,(n-i)/2):
            k = n-i-j
            if (i*i+j*j == k*k):
                result = i*j*k

    return result


def main():
    print problem_009()

if __name__ == '__main__':
    sys.exit(main())

