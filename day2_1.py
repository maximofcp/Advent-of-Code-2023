import re
from common import read_input


GAME_COLOR_LIMITS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

game_id_pattern = r'Game (?P<id>\d+)'
compiled_game_id_pattern = re.compile(game_id_pattern)


def is_game_total_color_possible(game: str, color: str) -> bool:
    pattern: str = f"\\d+ {color}"

    return all(int(color_total.split(' ')[0]) <= GAME_COLOR_LIMITS[color] for color_total in re.findall(pattern, game))


def get_game_id(game: str) -> int:
    return int(compiled_game_id_pattern.match(game).groupdict()['id'])


if __name__ == '__main__':
    games: list[str] = read_input('day2_1')
    sum_of_possible_game_ids = 0

    for game in games:
        possible_game: bool = True
        for color in GAME_COLOR_LIMITS.keys():
            possible_game = possible_game and is_game_total_color_possible(game, color)

        if possible_game:
            sum_of_possible_game_ids += get_game_id(game)

    print(sum_of_possible_game_ids)
