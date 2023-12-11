from collections import Counter
from enum import Enum
from operator import itemgetter

from common import read_input


class Hand(Enum):
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    '1': 1,
}


def parse_hands(hands_input: list[str]) -> list[tuple[str, int]]:
    hands: list[tuple[str, int]] = []
    for hand in hands_input:
        cards, value = hand.split(' ')
        hands.append((cards, int(value)))

    return hands


def match_five_of_a_kind(counter: Counter) -> int:
    return 5 * 1000000 if 5 in counter.values() else 0


def match_four_of_a_kind(counter: Counter) -> int:
    return 4 * 1000000 if 4 in counter.values() else 0


def match_three_of_a_kind(counter: Counter) -> int:
    return 3 * 1000000 if 3 in counter.values() else 0


def match_two_pairs(counter: Counter) -> int:
    return 2 * 1000000 if Counter(counter.values())[2] == 2 else 0


def match_one_pair(counter: Counter) -> int:
    return 1 * 1000000 if Counter(counter.values())[2] == 1 else 0


def match_highest_card(counter: Counter, hand: str) -> int:
    return sum(card_values[c] * counter[c] * v * 1000 for c, v in zip(hand, (5, 4, 3, 2, 1)))


def get_hand_value(hand: str) -> int:
    matches = (
        match_five_of_a_kind,
        match_four_of_a_kind,
        match_three_of_a_kind,
        match_two_pairs,
        match_one_pair)
    value = 0
    c = Counter(hand)

    for match in matches:
        v = match(c)
        value += v

        if v != 0:
            break

    return value + match_highest_card(c, hand)


if __name__ == '__main__':
    hands_input: list[str] = read_input('day7_1')
    hands = parse_hands(hands_input)
    hands_with_ranks: list[tuple[str, int, int]] = []

    for hand, bid in hands:
        value = get_hand_value(hand)
        hands_with_ranks.append((hand, bid, value))

    total_winnings = sum([b * (r + 1) for r, (_, b, _) in enumerate(sorted(hands_with_ranks, key=itemgetter(2)))])

    print(total_winnings)

# correto: 248569531
