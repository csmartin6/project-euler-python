import sys
import utils
import collections



def problem_053():

    count = 0
    max_n = 100
    for n in range(23, max_n + 1):
        r = 1
        ncr = n
        while ncr < 1e6 and r < max_n/2:
            r += 1
            ncr *= n-r+1
            ncr /= r

        count += n - 2*r + 1

    return count

def main():
    print "Problem 53"
    print "Answer: " + str(problem_053())


if __name__ == '__main__':
    sys.exit(main())
