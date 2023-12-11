import itertools

from common import read_input
from day8_1 import parse_stations_map
import sys

sys.setrecursionlimit(1000000)


def find_collective_paths(instructions: str, stations: dict[str, tuple[str, str]], start_nodes, iterations: int = 0) -> int:
    _from = start_nodes

    while i := next(itertools.cycle(instructions)):
    #for i in itertools.cycle(instructions):
        end_nodes = [stations[node][0 if i == 'L' else 1] for node in _from]
        if all(node.endswith('Z') for node in end_nodes):
            return iterations

        _from = end_nodes

    # return find_collective_paths(instructions, stations, _from, iterations)


def find_starting_nodes(stations: dict[str, tuple[str, str]]):
    return [k for k in stations.keys() if k.endswith('A')]


if __name__ == '__main__':
    path_map: list[str] = read_input('day8_1')
    instructions: str = path_map[0]
    stations: dict[str, tuple[str, str]] = parse_stations_map(path_map[2:])
    start_nodes = find_starting_nodes(stations)
    iterations: int = find_collective_paths(instructions, stations, start_nodes)

    print(iterations)
