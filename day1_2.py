from common import read_input
from day1_1 import get_line_number

SPELLED_NUMBERS_MAP = {
    'twone': '21',
    'oneight': '18',
    'eightwo': '82',
    'eighthree': '83',
    'threeight': '38',
    'fiveight': '58',
    'nineight': '98',
    'sevenine': '79',
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def translate_spelled_numbers_into_real_numbers(line: str) -> str:
    for spelled, number in SPELLED_NUMBERS_MAP.items():
        line = line.replace(spelled, number, -1)

    return line


if __name__ == '__main__':
    calibration_document: list[str] = read_input('day1_1')
    sum_all_calibration_values: int = 0

    for calibration_line in calibration_document:
        translated_line = translate_spelled_numbers_into_real_numbers(calibration_line)
        line_number = get_line_number(translated_line)
        sum_all_calibration_values += line_number

    print(sum_all_calibration_values)
