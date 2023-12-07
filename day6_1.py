from common import read_input, numbers_pattern


def parse_races(races: list[str]) -> list[tuple[int, int]]:
    times = numbers_pattern.findall(races[0])
    distances = numbers_pattern.findall(races[1])

    return [(int(time), int(distance)) for time, distance in zip(times, distances)]


def calculate_possible_wins(time: int, distance: int) -> int:
    win_count = 0
    for t in range(0, time):
        score = t * (time - t)
        if score > distance:
            win_count += 1

    return win_count


if __name__ == '__main__':
    races_input: list[str] = read_input('day6_1')
    races: list[tuple[int, int]] = parse_races(races_input)

    record_beats = 1

    for time, distance in races:
        record_beats *= calculate_possible_wins(time, distance)

    print(record_beats)
