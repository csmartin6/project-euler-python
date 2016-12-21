import sys

num2word = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
            6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
            11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
            19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
            50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}


def convert_number_to_words(num):
    if num in num2word:
        return num2word[num]

    if num >= 1000:
        return convert_number_to_words(num // 1000) + " thousand" + \
               (" and " + convert_number_to_words(num % 1000) if num % 1000 else "")
    elif num >= 100:
        return convert_number_to_words(num // 100) + " hundred" + \
               (" and " + convert_number_to_words(num % 100) if num % 100 else "")
    elif num > 20:
        return convert_number_to_words(num - num % 10) + \
               (" " + convert_number_to_words(num % 10) if num % 10 else "")
    else:
        raise RuntimeError("Something has gone wrong")


def letter_count(word):
    return len(word.replace(" ", ""))


def problem_017():
    letters = 0
    n = 1001
    for i in range(1, n):
        num_word = convert_number_to_words(i)
        letters += letter_count(num_word)

    return letters


def main():
    print("Problem 17")
    print("Answer: " + str(problem_017()))


if __name__ == '__main__':
    sys.exit(main())
