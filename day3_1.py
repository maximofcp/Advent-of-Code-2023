import re
from itertools import chain

from common import read_input, special_chars_pattern, numbers_pattern


def find_number_intervals_indexes(engine_line: str) -> list[tuple[int, int]]:
    return [(m.start(0), m.end(0)) for m in re.finditer(numbers_pattern, engine_line)]


def find_special_characters_indexes(engine_line: str) -> list[int]:
    return [m.start(0) for m in re.finditer(special_chars_pattern, engine_line)]


def number_belongs_to_engine(number_indexes: tuple[int, int], engine_lines: list[str]) -> bool:
    all_line_indexes = list(chain.from_iterable([find_special_characters_indexes(line) for line in engine_lines]))

    return any(number_indexes[0] - 1 <= i <= number_indexes[1] for i in all_line_indexes)


if __name__ == '__main__':
    engine_schematics: list[str] = read_input('day3_1')
    total_sum_of_engine_parts: int = 0
    saved_numbers: list[str] = []

    for line_index, line in enumerate(engine_schematics):
        for start, end in find_number_intervals_indexes(line):
            number_key = f'{line_index}-{start}-{end}'
            if number_key in saved_numbers:
                continue

            saved_numbers.append(number_key)
            surrounding_engine_lines = engine_schematics[max(line_index-1, 0):min(line_index+2, len(engine_schematics))]
            if number_belongs_to_engine((start, end), surrounding_engine_lines):
                total_sum_of_engine_parts += int(line[start:end])

    print(total_sum_of_engine_parts)
