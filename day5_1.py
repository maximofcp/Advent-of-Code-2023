import re

from common import read_input

numbers_pattern = re.compile(r'\d+')


def get_seeds(garden_map: list[str]) -> list[int]:
    return [int(number) for number in numbers_pattern.findall(garden_map[0])]


def get_map(source: str, destination: str, garden_map: list[str]) -> list[tuple[int, int, int]]:
    mapped: list[tuple[int, int, int]] = []
    read = False
    for line in garden_map:
        if read and not line:
            break
        if f'{source}-to-{destination}' in line:
            read = True
            continue
        if not read:
            continue

        line_split = line.split(' ')
        mapped.append((int(line_split[0]), int(line_split[1]), int(line_split[2])))

    return mapped


def find_mapped_value(number: int, map_: list[tuple[int, int, int]]) -> int:
    for destination_range, source_range, range_length in map_:
        if number < source_range or number > source_range + range_length:
            continue

        return destination_range + number - source_range

    return number


if __name__ == '__main__':
    garden_map: list[str] = read_input('day5_1')
    seeds = get_seeds(garden_map)
    seed_to_soil = get_map('seed', 'soil', garden_map)
    soil_to_fertilizer = get_map('soil', 'fertilizer', garden_map)
    fertilizer_to_water = get_map('fertilizer', 'water', garden_map)
    water_to_light = get_map('water', 'light', garden_map)
    light_to_temperature = get_map('light', 'temperature', garden_map)
    temperature_to_humidity = get_map('temperature', 'humidity', garden_map)
    humidity_to_location = get_map('humidity', 'location', garden_map)

    locations: list[int] = []

    for seed in seeds:
        soil_mapped_value = find_mapped_value(seed, seed_to_soil)
        fertilizer_mapped_value = find_mapped_value(soil_mapped_value, soil_to_fertilizer)
        water_mapped_value = find_mapped_value(fertilizer_mapped_value, fertilizer_to_water)
        light_mapped_value = find_mapped_value(water_mapped_value, water_to_light)
        temperature_mapped_value = find_mapped_value(light_mapped_value, light_to_temperature)
        humidity_mapped_value = find_mapped_value(temperature_mapped_value, temperature_to_humidity)
        location_mapped_value = find_mapped_value(humidity_mapped_value, humidity_to_location)

        locations.append(location_mapped_value)

    print(min(locations))
