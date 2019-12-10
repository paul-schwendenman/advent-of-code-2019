from collections import namedtuple, OrderedDict, defaultdict
import math
from enum import Enum


class Space(Enum):
    ASTERIOD = '#'
    EMPTY = '.'


Point = namedtuple('Point', 'x y')


def calc_slope(point_1, point_2):
    top = (point_1.x - point_2.x)
    bottom = (point_1.y - point_2.y)
    try:
        slope = top / bottom
    except ZeroDivisionError:
        slope = math.inf

    return (top >= 0), (bottom >=0), slope

def calc_magnitude(point_1, point_2):
    return (point_1.x - point_2.x) ** 2 + (point_2.x - point_2.y) ** 2


def stuff():
    a = defaultdict(OrderedDict)


def is_asteroid(asteroid):
    # return Space(grid[point.x][point.y]) == Space.ASTERIOD
    # return Space(asteroid) == Space.ASTERIOD
    return asteroid == '#'


def find_asteroids2(grid):
    max_count = 0
    max_point = None

    asteroids = []
    counts = defaultdict(lambda: defaultdict(lambda: '.'))
    for y_pos, row in enumerate(grid):
        for x_pos, asteroid in enumerate(row):
            if asteroid == '#':
                asteroids.append(Point(x_pos, y_pos))

    print(asteroids)

    for asteroid1 in asteroids:
        paths = {}
        for asteroid2 in asteroids:
            if asteroid1 == asteroid2:
                continue
            slope = calc_slope(asteroid1, asteroid2)
            magnitude = calc_magnitude(asteroid1, asteroid2)

            # print(f'{asteroid1} {asteroid2} {slope} {magnitude}')

            paths[slope] = magnitude

        number_of_asteroids = len(paths.keys())
        counts[asteroid1.y][asteroid1.x] = number_of_asteroids
        # print(f'point {asteroid1} {number_of_asteroids} {paths}')
        if number_of_asteroids > max_count:
            max_count = number_of_asteroids
            max_point = asteroid1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(counts[i][j], end='')
        print('')

    for row in grid:
        print(row)

    return max_point, max_count


def main(filename="input"):
    with open(filename) as input_data:
        grid = input_data.read().splitlines()

    return find_asteroids2(grid)

    print(grid)


if __name__ == "__main__":
    print(main())
