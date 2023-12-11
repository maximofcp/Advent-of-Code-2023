import re

numbers_pattern = re.compile(r'\d+')
special_chars_pattern = re.compile(r'[^A-Za-z0-9.]')
star_pattern = re.compile(r'[*]')
three_letter_word_pattern = re.compile(r'[A-Z]{3}')


def read_input(filename: str):
    with open(f'data/input/{filename}.txt') as file:
        return [line.replace('\n', '') for line in file.readlines()]
