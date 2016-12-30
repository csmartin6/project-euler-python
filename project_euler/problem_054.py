import sys
import os
from collections import Counter

card_to_value = {'2': 2,
                 '3': 3,
                 '4': 4,
                 '5': 5,
                 '6': 6,
                 '7': 7,
                 '8': 8,
                 '9': 9,
                 'T': 10,
                 'J': 11,
                 'Q': 12,
                 'K': 13,
                 'A': 14
                 }


def is_flush(cards):
    suit = cards[0][1]
    for c in cards[1:]:
        if c[1] != suit:
            return False
    return True


def is_straight(cards):
    values = [c[0] for c in cards]
    # no repeats
    count = Counter(values)
    return (count.most_common(1)[0][1] == 1) and (max(values) - min(values) == len(values) - 1)


def x_of_a_kind(cards):
    values = [c[0] for c in cards]
    count = Counter(values)
    pairs = Counter({k: v for k, v in count.items() if v >= 2})
    rem = sorted([k for k, v in count.items() if v == 1], reverse=True)
    return pairs, rem


def poker(hand_a, hand_b):
    a_flush = is_flush(hand_a)
    b_flush = is_flush(hand_b)
    a_straight = is_straight(hand_a)
    b_straight = is_straight(hand_b)

    # straight flushes
    a_straight_flush = a_flush and a_straight
    b_straight_flush = b_flush and b_straight

    if a_straight_flush and b_straight_flush:
        return "a" if hand_a[0][0] >= hand_b[0][0] else "b"

    if a_straight_flush:
        return "a"

    if b_straight_flush:
        return "a"

    a_pairs, a_rem = x_of_a_kind(hand_a)
    b_pairs, b_rem = x_of_a_kind(hand_b)

    # four of kind
    a_4_of_a_kind = a_pairs.most_common(1)[0][1] if a_pairs and (a_pairs.most_common(1)[0][1] == 4) else 0
    b_4_of_a_kind = b_pairs.most_common(1)[0][1] if b_pairs and (b_pairs.most_common(1)[0][1] == 4) else 0

    if a_4_of_a_kind and b_4_of_a_kind:
        return "a" if a_4_of_a_kind >= b_4_of_a_kind else "b"

    if a_4_of_a_kind:
        return "a"

    if b_4_of_a_kind:
        return "b"

    # Full House
    a_full_house = 0
    b_full_house = 0

    if a_pairs:
        two_most_common = a_pairs.most_common(2)
        if (len(two_most_common) == 2) and (two_most_common[0][1] == 3) and (two_most_common[1][1] == 2):
            a_full_house = two_most_common[0][0]

    if b_pairs:
        two_most_common = b_pairs.most_common(2)
        if (len(two_most_common) == 2) and (two_most_common[0][1] == 3) and (two_most_common[1][1] == 2):
            b_full_house = two_most_common[0][0]

    if a_full_house and b_full_house:
        return "a" if a_full_house >= b_full_house else "b"

    if a_full_house:
        return "a"

    if b_full_house:
        return "b"

    # Flush
    if a_flush and b_flush:
        return "a" if hand_a[0][0] >= hand_b[0][0] else "b"

    if a_flush:
        return "a"

    if b_flush:
        return "b"

    # Straight
    if a_straight and b_straight:
        return "a" if hand_a[0][0] >= hand_b[0][0] else "b"

    if a_straight:
        return "a"

    if b_straight:
        return "b"

    # Three of a kind
    a_3_of_a_kind = a_pairs.most_common(1)[0][1] if a_pairs and (a_pairs.most_common(1)[0][1] == 3) else 0
    b_3_of_a_kind = b_pairs.most_common(1)[0][1] if b_pairs and (b_pairs.most_common(1)[0][1] == 3) else 0

    if a_3_of_a_kind and b_3_of_a_kind:
        return "a" if a_3_of_a_kind >= b_3_of_a_kind else "b"

    if a_3_of_a_kind:
        return "a"

    if b_3_of_a_kind:
        return "b"

    # Two pair
    if len(a_pairs) == 2 and len(b_pairs) == 2:

        if max(a_pairs.values()) == max(b_pairs.values()):
            if min(a_pairs.values()) == min(b_pairs.values()):
                return "a" if a_rem[0] >= b_rem[0] else "b"
            else:
                return "a" if min(a_pairs.values()) >= min(b_pairs.values()) else "b"

    if len(a_pairs) == 2:
        return "a"

    if len(b_pairs) == 2:
        return "b"

    # One pair

    if a_pairs and b_pairs:
        if max(a_pairs.keys()) == max(b_pairs.keys()):
            return "a" if a_rem[0] >= b_rem[0] else "b"
        else:
            return "a" if a_pairs.most_common(1)[0][0] >= b_pairs.most_common(1)[0][0] else "b"

    if a_pairs:
        return "a"
    if b_pairs:
        return "b"

    # High Card

    return "a" if hand_a[0][0] >= hand_b[0][0] else "b"


def problem_054():
    filename = os.path.join(os.path.dirname(__file__), '../data/p054_poker.txt')
    winners = Counter()
    with open(filename, 'r') as f:
        for line in f:
            cards = [(card_to_value[c[0]], c[1]) for c in line.rstrip('\n').split(' ')]
            hand_a = sorted(cards[:5], reverse=True)
            hand_b = sorted(cards[5:], reverse=True)
            winner = poker(hand_a, hand_b)
            winners[winner] += 1

    return winners['a']


def main():
    print("Problem 54")
    print(("Answer: " + str(problem_054())))


if __name__ == '__main__':
    sys.exit(main())
