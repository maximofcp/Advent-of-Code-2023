import re

from common import read_input
from day2_1 import GAME_COLOR_LIMITS


def max_total_game_color(game: str, color: str) -> int:
    pattern: str = f"\\d+ {color}"

    return max(int(color_total.split(' ')[0]) for color_total in re.findall(pattern, game))


if __name__ == '__main__':
    games: list[str] = read_input('day2_1')
    sum_of_game_powers: int = 0

    for game in games:
        power: int = 1
        for color in GAME_COLOR_LIMITS.keys():
            power *= max_total_game_color(game, color)

        sum_of_game_powers += power

    print(sum_of_game_powers)
