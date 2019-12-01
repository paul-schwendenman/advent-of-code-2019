import math


def calculate_fuel(module_mass):
    return max(math.floor(module_mass / 3) - 2, 0)


def main():
    lines = []
    with open('input') as file:
        lines = file.readlines()

    return sum(calculate_fuel(int(item)) for item in lines)


if __name__ == '__main__':
    print(main())
