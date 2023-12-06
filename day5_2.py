import asyncio

from common import read_input
from day5_1 import get_map, get_seeds


def get_seed_ranges(garden_map: list[str]) -> list[tuple[int, int]]:
    values = get_seeds(garden_map)

    return [(values[index], values[index + 1]) for index in range(0, len(values), 2)]


async def find_mapped_value(number: int, map_: list[tuple[int, int, int]]) -> int:
    for destination_range, source_range, range_length in map_:
        if number < source_range or number > source_range + range_length:
            continue

        return destination_range + number - source_range

    return number


async def find_location(seed: int, maps: list[list[tuple[int, int, int]]]) -> int:
    value = seed
    for task in maps:
        value = await find_mapped_value(value, task)

    return value


async def find_lowest_location(seed: int, length: int, maps: list[list[tuple[int, int, int]]]) -> int:
    lowest = None
    for number in range(seed, seed + length):
        location = await find_location(number, maps)
        if lowest is None:
            lowest = location
            continue

        if location < lowest:
            lowest = location

    return lowest


async def main():
    garden_map: list[str] = read_input('day5_1')
    seed_ranges = get_seed_ranges(garden_map)
    seed_to_soil = get_map('seed', 'soil', garden_map)
    soil_to_fertilizer = get_map('soil', 'fertilizer', garden_map)
    fertilizer_to_water = get_map('fertilizer', 'water', garden_map)
    water_to_light = get_map('water', 'light', garden_map)
    light_to_temperature = get_map('light', 'temperature', garden_map)
    temperature_to_humidity = get_map('temperature', 'humidity', garden_map)
    humidity_to_location = get_map('humidity', 'location', garden_map)

    maps: list = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature,
                  temperature_to_humidity, humidity_to_location]

    lowest = None
    tasks: list = [find_lowest_location(start, length, maps) for start, length in seed_ranges]

    results = await asyncio.gather(*tasks)
    for result in results:
        if lowest is None:
            lowest = result
            continue
        if result < lowest:
            lowest = result

    print(lowest)


if __name__ == '__main__':
    asyncio.run(main())
