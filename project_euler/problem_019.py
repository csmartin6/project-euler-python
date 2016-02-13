import datetime
from collections import Counter
import sys


def problem_019_a():
    # using datetime
    day_of_week = [datetime.date(year, month, 1).weekday() for year in range(1901, 2001) for month in range(1, 13)]
    c = Counter(day_of_week)

    return c[6]


def problem_019_b():
    # without datatime

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    sundays = 0
    day_of_week = 1  # Jan 1 1901 was a Tuesday

    for year in range(1901, 2001):
        for month in range(12):
            if day_of_week == 6:
                sundays += 1

            day_of_week = (day_of_week + month_lengths[month]) % 7
            if month == 1 and ((year % 4 == 0 and not year % 100 == 0) or year % 400 == 0):
                day_of_week = (day_of_week + 1) % 7

    return sundays


def main():
    print "Problem 19"
    print "with datetime"
    print "Answer: " + str(problem_019_a())
    print "without datetime"
    print "Answer: " + str(problem_019_b())


if __name__ == '__main__':
    sys.exit(main())
