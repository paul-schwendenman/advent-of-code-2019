from collections import namedtuple, OrderedDict, defaultdict
import math
from enum import Enum


Point = namedtuple('Point', 'x y')


def calc_angle(point_1: Point, point_2: Point):
    dx = point_2.x - point_1.x
    dy = point_2.y - point_1.y
    return math.degrees(math.atan2(dx, -dy)) % 360


def calc_magnitude(point_1: Point, point_2: Point):
    dx = point_2.x - point_1.x
    dy = point_2.y - point_1.y

    return math.hypot(dx, dy)


def combine_point(point: Point):
    return point.x * 100 + point.y


def part2(grid):
    asteroids = []
    for y_pos, row in enumerate(grid):
        for x_pos, asteroid in enumerate(row):
            if asteroid == '#':
                asteroids.append(Point(x_pos, y_pos))

    center = Point(13, 17)
    asteroids.remove(center)

    mapper = defaultdict(list)

    for asteroid in asteroids:
        magnitude = calc_magnitude(center, asteroid)
        angle = calc_angle(center, asteroid)

        mapper[angle].append((magnitude, asteroid))

    angles = sorted(set(calc_angle(center, asteroid) for asteroid in asteroids))
    angle_200 = angles[199]

    winner = sorted(mapper[angle_200])[0][1]

    return combine_point(winner)


def main(filename="input"):
    with open(filename) as input_data:
        grid = input_data.read().splitlines()

    return part2(grid)

    print(grid)


if __name__ == "__main__":
    print(main())
