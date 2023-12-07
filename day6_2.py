from common import read_input
from day5_1 import numbers_pattern
from day6_1 import calculate_possible_wins


def parse_race(races: list[str]) -> tuple[int, int]:
    return int(''.join(numbers_pattern.findall(races[0]))), int(''.join(numbers_pattern.findall(races[1])))


if __name__ == '__main__':
    races_input: list[str] = read_input('day6_1')
    time, distance = parse_race(races_input)

    print(calculate_possible_wins(time, distance))
