import re
from functools import cache

from common import read_input
from day4_1 import get_winning_numbers, get_bet_numbers

card_number_pattern = re.compile(r'Card *(?P<number>\d+):')


def get_card_number(card: str) -> int:
    return int(card_number_pattern.match(card).groupdict()['number'])


@cache
def calculate_card_copies(card: str) -> int:
    copies = 0
    winning_numbers = get_winning_numbers(card)
    bet_numbers = get_bet_numbers(card)

    for bet in bet_numbers:
        if bet in winning_numbers:
            copies += 1

    return copies


def calculate_scratchcards(cards: list[str], start_range: int, end_range: int) -> int:
    cards_to_count = cards[start_range:end_range]
    nr_cards = len(cards_to_count)

    for card in cards_to_count:
        card_number = get_card_number(card)
        copies = calculate_card_copies(card)
        nr_cards += calculate_scratchcards(cards, card_number, card_number + copies)

    return nr_cards


if __name__ == '__main__':
    scratchcards: list[str] = read_input('day4_1')
    print(calculate_scratchcards(scratchcards, 0, len(scratchcards)))
