from common import read_input


def get_line_number(line: str) -> int:
    first_digit = None
    last_digit = None

    for line_item in line:
        try:
            first_digit = int(line_item)
            break
        except ValueError:
            ...

    for line_item in reversed(line):
        try:
            last_digit = int(line_item)
            break
        except ValueError:
            ...

    return int(f'{first_digit}{last_digit}')


if __name__ == '__main__':
    calibration_document: list[str] = read_input('day1_1')
    sum_all_calibration_values: int = 0

    for calibration_line in calibration_document:
        sum_all_calibration_values += get_line_number(calibration_line)

    print(sum_all_calibration_values)
