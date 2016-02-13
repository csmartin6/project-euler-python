import sys
import os


def problem_022():
    ascii_offset = 96
    filename = os.path.join(os.path.dirname(__file__), '../data/p022_names.txt')
    names = []
    with open(filename, 'r') as f:
        for line in f:
            names = line.strip().lower().replace("\"", "").split(',')

    names.sort()
    result = 0

    for index, name in enumerate(names):
        letter_scores = [(ord(letter) - ascii_offset) for letter in name]
        name_score = sum(letter_scores)
        result += name_score * (index + 1)

    return result


def main():
    print "Problem 22"
    print "Answer: " + str(problem_022())


if __name__ == '__main__':
    sys.exit(main())
