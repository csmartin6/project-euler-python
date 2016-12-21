import sys
import marisa_trie

def add_next_digit(current_number, candidates):
    possible = []
    for c in candidates.items(current_number[-2:]):
        if len(c[0]) == 3:
            d = current_number + c[0][-1]
            if len(set(d)) == len(d):
                possible.append(d)
    return possible



def problem_043():

    digit_tries = []
    digits_234 = (marisa_trie.Trie(['{0:03d}'.format(i) for i in range(0,1000,2) if len(set(str(i))) == len(str(i))]))
    digits_345 = marisa_trie.Trie(['{0:03d}'.format(i) for i in range(0, 1000, 3) if len(set(str(i))) == len(str(i))])
    digits_456 = marisa_trie.Trie(['{0:03d}'.format(i) for i in range(0, 1000, 5) if len(set(str(i))) == len(str(i))])
    digits_567 = marisa_trie.Trie(['{0:03d}'.format(i) for i in range(0, 1000, 7) if len(set(str(i))) == len(str(i))])
    digits_678 = marisa_trie.Trie(['{0:03d}'.format(i) for i in range(0, 1000, 11) if len(set(str(i))) == len(str(i))])
    digits_789 = marisa_trie.Trie(['{0:03d}'.format(i) for i in range(0, 1000, 13) if len(set(str(i))) == len(str(i))])
    digits_8910 = marisa_trie.Trie(
        ['{0:03d}'.format(i) for i in range(0, 1000, 17) if len(set('{0:03d}'.format(i))) == 3])

    digit_tries.append(digits_345)
    digit_tries.append(digits_456)
    digit_tries.append(digits_567)
    digit_tries.append(digits_678)
    digit_tries.append(digits_789)
    digit_tries.append(digits_8910)

    possible_pandigitals = set([c[0] for c in list(digits_234.items()) if len(c[0]) == 3])
    for digit_trie in digit_tries:
        possible_pandigitals = [add_next_digit(current_number, digit_trie) for current_number in possible_pandigitals]
        possible_pandigitals = set([x for p in possible_pandigitals for x in p])

    pandigitals = []

    # add first number
    for p in possible_pandigitals:
        for i in range(10):
            if str(i) not in p:
                pandigitals.append(int(str(i)+p))
                break
    return sum(pandigitals)



def main():
    print("Problem 43")
    print("Answer: " + str(problem_043()))



if __name__ == '__main__':
    sys.exit(main())
