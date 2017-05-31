import sys
import utils



def problem_070():
    n = 10000000
    totients = {i: int(utils.totient(i)) for i in range(2, n+1)}
    perms = [k for k, v in totients.items() if sorted(str(k)) == sorted(str(v))]
    min_ratio = float("inf")
    min_ratio_n = 0
    for p in perms:
        if 1.0*p/totients[p] < min_ratio:
            min_ratio = 1.0*p/totients[p]
            min_ratio_n = p

    return min_ratio_n


def main():
    print("Problem 70")
    print(("Answer: " + str(problem_070())))


if __name__ == '__main__':
    sys.exit(main())
