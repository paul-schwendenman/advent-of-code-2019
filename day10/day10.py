from collections import namedtuple, OrderedDict, defaultdict
import math
from enum import Enum


# class Space(Enum):
#     ASTERIOD = '#'
#     EMPTY = '.'


Point = namedtuple('Point', 'x y')


# def calc_slope(point_2, point_1):
#     top = (point_1.x - point_2.x)
#     bottom = (point_1.y - point_2.y)
#     try:
#         slope = top / bottom
#     except ZeroDivisionError:
#         slope = math.inf

#     return (top >= 0), (bottom >=0), slope

# def calc_magnitude(point_1, point_2):
#     return (point_1.x - point_2.x) ** 2 + (point_2.x - point_2.y) ** 2


# def stuff():
#     a = defaultdict(OrderedDict)


# def is_asteroid(asteroid):
#     # return Space(grid[point.x][point.y]) == Space.ASTERIOD
#     # return Space(asteroid) == Space.ASTERIOD
#     return asteroid == '#'


# def find_asteroids2(grid):
#     max_count = 0
#     max_point = None

#     asteroids = []
#     counts = defaultdict(lambda: defaultdict(lambda: '.'))
#     for y_pos, row in enumerate(grid):
#         for x_pos, asteroid in enumerate(row):
#             if asteroid == '#':
#                 asteroids.append(Point(x_pos, y_pos))

#     # print(asteroids)

#     for asteroid1 in asteroids:
#         paths = {}
#         c = defaultdict(lambda: 0)
#         l = defaultdict(list)
#         if asteroid1 != Point(13, 17):
#             continue
#         for asteroid2 in asteroids:
#             if asteroid1 == asteroid2:
#                 continue
#             slope = calc_slope(asteroid1, asteroid2)
#             magnitude = calc_magnitude(asteroid1, asteroid2)

#             # print(f'{asteroid1} {asteroid2} {slope} {magnitude}')

#             paths[slope] = magnitude
#             c[slope] += 1
#             l[slope].append((asteroid2, magnitude))

#         number_of_asteroids = len(paths.keys())
#         counts[asteroid1.y][asteroid1.x] = number_of_asteroids
#         # print(c.values())
#         # print(l)
#         k = sorted(l.keys())
#         quad_1 = [a for a in k if a[0]==True and a[1] == True]
#         # print(quad_1, len(quad_1))
#         quad_2 = [a for a in k if a[0]==True and a[1] == False]
#         # print(quad_2, len(quad_2))
#         quad_3 = [a for a in k if a[0]==False and a[1] == False]

#         # print(quad_3, len(quad_3))
#         index = 200 - (len(quad_1) + len(quad_2))
#         # print(f'index {index}')
#         quad_4 = [a for a in k if a[0]==False and a[1] == True]
#         # print(quad_4, len(quad_4))

#         # print((quad_1 + quad_2 + quad_3 + quad_4)[198:202])
#         slope = list((sorted(quad_3)))[index-1]
#         slope2 = list((sorted(quad_3)))[index]
#         # print(slope, l[slope])
#         # print(slope2, l[slope2])
#         # print(f'point {asteroid1} {number_of_asteroids} {paths}')
#         if number_of_asteroids > max_count:
#             max_count = number_of_asteroids
#             max_point = asteroid1

#     # for i in range(len(grid)):
#     #     for j in range(len(grid[0])):
#     #         print(counts[i][j], end='')
#     #     print('')

#     # for row in grid:
#     #     print(row)

#     return max_point, max_count

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


def find_asteroids3(grid):
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

        print(f'mag {magnitude} angle {angle}')
        mapper[angle].append((magnitude, asteroid))


    angles = sorted(set(calc_angle(center, asteroid) for asteroid in asteroids))
    angle_200 = angles[199]
    print(angle_200)
    print(mapper[angle_200])

    winner = sorted(mapper[angle_200])[0][1]

    print(winner)

    return combine_point(winner)


def main(filename="input"):
    with open(filename) as input_data:
        grid = input_data.read().splitlines()

    return find_asteroids3(grid)

    print(grid)


if __name__ == "__main__":
    print(main())
