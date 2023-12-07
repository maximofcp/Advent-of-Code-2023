from common import read_input, numbers_pattern


def get_winning_numbers(card: str) -> list[int]:
    return numbers_pattern.findall(card)[1:11]


def get_bet_numbers(card: str) -> list[int]:
    return numbers_pattern.findall(card)[11:]


def calculate_card_points(card: str) -> int:
    points = 0
    winning_numbers = get_winning_numbers(card)
    bet_numbers = get_bet_numbers(card)

    for bet in bet_numbers:
        if bet in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2

    return points


if __name__ == '__main__':
    scratchcards: list[str] = read_input('day4_1')
    points = 0

    for card in scratchcards:
        points += calculate_card_points(card)

    print(points)
