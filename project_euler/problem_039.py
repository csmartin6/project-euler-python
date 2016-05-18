import sys
import numpy as np




def problem_039():
    # generate triples using brute force
    triples = set()
    sum_count = [0]*1000
    for a in xrange(2,333):
        for b in xrange(a,500):
            c = int(np.sqrt(a*a + b*b))
            if a*a + b*b == c*c and a + b +c < 1000:
                sum_count[a+b+c] += 1
                triples.add((a,b,c))


    return np.argmax(sum_count)

def main():
    print "Problem 39"
    print "Answer: " + str(problem_039())


if __name__ == '__main__':
    sys.exit(main())
