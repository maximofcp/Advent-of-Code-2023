import re
from itertools import chain

from common import read_input, star_pattern
from day3_1 import find_special_characters_indexes, numbers_pattern


def find_star_indexes(engine_line: str) -> list[int]:
    return [m.start(0) for m in re.finditer(star_pattern, engine_line)]


def find_number_intervals_indexes(engine_line: str, line_index: int) -> list[tuple[int, int, int]]:
    return [(m.start(0), m.end(0), line_index) for m in re.finditer(numbers_pattern, engine_line)]


def find_star_gear_ratios(star_indexes: list[int], engine_lines: list[str]) -> int:
    all_numbers_for_engine_lines = list(chain.from_iterable(
        [find_number_intervals_indexes(line, i) for i, line in enumerate(engine_lines)]))

    ratio_powers: list[int] = []

    for star_index in star_indexes:
        ratio = 1
        ratio_count = 0
        for number_start, number_end, line_index in all_numbers_for_engine_lines:
            intersects = number_start >= star_index - 1 and number_start <= star_index + 1 or number_end > star_index -1 and number_end <= star_index + 1
            if intersects:
                ratio *= int(engine_lines[line_index][number_start:number_end])
                ratio_count += 1

        if ratio_count == 2:
            ratio_powers.append(ratio)

    return sum(ratio_powers)


def number_belongs_to_engine(number_indexes: tuple[int, int], engine_lines: list[str]) -> bool:
    all_line_indexes = list(chain.from_iterable([find_special_characters_indexes(line) for line in engine_lines]))

    return any(number_indexes[0] - 1 <= i <= number_indexes[1] for i in all_line_indexes)


if __name__ == '__main__':
    engine_schematics: list[str] = read_input('day3_1')
    total_sum_of_engine_parts: int = 0

    for line_index, line in enumerate(engine_schematics):
        star_indexes = find_star_indexes(line)
        if not star_indexes:
            continue

        surrounding_engine_lines = engine_schematics[max(line_index - 1, 0):min(line_index + 2, len(engine_schematics))]
        total_sum_of_engine_parts += find_star_gear_ratios(star_indexes, surrounding_engine_lines)

    print(total_sum_of_engine_parts)
