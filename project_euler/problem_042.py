import sys
import os



def is_triangular(word,triangular_nums):
    ascii_offset = 96
    letter_scores = [(ord(letter) - ascii_offset) for letter in word]
    word_score = sum(letter_scores)
    return word_score in triangular_nums


def problem_042():
    triangular_nums = set([n * (n + 1) / 2 for n in range(1, 100)])
    filename = os.path.join(os.path.dirname(__file__), '../data/p042_words.txt')
    words = []
    with open(filename, 'r') as f:
        for line in f:
            words = line.strip().lower().replace("\"", "").split(',')
    triangular_words = [w for w in words if is_triangular(w,triangular_nums)]

    return len(triangular_words)

def main():
    print("Problem 42")
    print("Answer: " + str(problem_042()))



if __name__ == '__main__':
    sys.exit(main())
