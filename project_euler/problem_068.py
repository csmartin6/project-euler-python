import sys
import itertools


def check_ngon(kgon):
    sums = [sum(line) for line in kgon if all(line)]
    if len(sums) == 0:
        return True
    return min(sums) == max(sums)


def check_inner_outer(inner, outer, k):
    total_sum = sum(outer) + 2*sum(inner)
    return total_sum % k == 0


def build_ngon(inner, outer):

    for perm in itertools.permutations(inner):
        ngon = [[o, None, None] for o in outer]

        for i, p in enumerate(perm):
            ngon[i][1] = p
            ngon[i-1][2] = p

        if check_ngon(ngon):
            return ngon

    return None


def problem_068():
    k = 5
    n = 2*k

    max_ = 0
    # i = smallest outide number

    for i in range(1, n-k+2):
        for rem in itertools.permutations(range(i+1, n+1), k-1):
            outer = [i] + list(rem)
            inner = [x for x in range(1, n+1) if x not in outer]

            if check_inner_outer(inner, outer, k):
                ngon = build_ngon(inner, outer)

                if ngon:
                    ngon_str = ''.join([''.join([str(j) for j in n]) for n in ngon])
                    if len(ngon_str) < 17:
                        max_ = max(max_, int(ngon_str))

    return max_


def main():
    print("Problem 68")
    print(("Answer: " + str(problem_068())))


if __name__ == '__main__':
    sys.exit(main())
