def read_input(filename: str):
    with open(f'data/input/{filename}.txt') as file:
        return [line.replace('\n', '') for line in file.readlines()]
