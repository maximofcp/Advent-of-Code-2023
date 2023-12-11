from common import read_input, three_letter_word_pattern


def find_path(instructions: str, stations: dict[str, tuple[str, str]], start: str, stop: str, iterations: int = 0) -> int:
    _from = start
    _to = stop

    for i in instructions:
        _to = stations[_from][0 if i == 'L' else 1]
        iterations += 1

        if _to == stop:
            return iterations

        _from = _to

    return find_path(instructions, stations, _from, stop, iterations)


def parse_stations_map(paths: list[str]) -> dict[str, tuple[str, str]]:
    stations_map: dict[str, tuple[str, str]] = {}
    for path in paths:
        sts = three_letter_word_pattern.findall(path)
        stations_map[sts[0]] = (sts[1], sts[2])

    return stations_map


if __name__ == '__main__':
    path_map: list[str] = read_input('day8_1')
    instructions: str = path_map[0]
    stations: dict[str, tuple[str, str]] = parse_stations_map(path_map[2:])

    iterations: int = find_path(instructions, stations, 'AAA', 'ZZZ')

    print(iterations)
