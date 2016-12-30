import sys
import os
from operator import xor
from itertools import cycle,product

def problem_059():
    filename = os.path.join(os.path.dirname(__file__), '../data/p059_cipher.txt')
    with open(filename, 'r') as f:

        coded = [int(x) for x in f.read().split(',')]


    for password in product(range(97,122), repeat=3):
        decoded = []
        for c, p in zip(coded, cycle(password)):
            decoded.append(chr(xor(c, p)))

        decoded = ''.join(decoded)
        if " the " in decoded:
            return sum([ord(c) for c in decoded])
    return "No match found"



def main():
    print("Problem 59")
    print(("Answer: " + str(problem_059())))


if __name__ == '__main__':
    sys.exit(main())
