from enum import Enum
from collections import namedtuple, defaultdict


Point = namedtuple('Point', 'x y')


class MazeItem(Enum):
    ENTRANCE = '@'
    OPEN_PASSAGE = '.'
    STONE_WALL = '#'


def process_maze(template):
    keys = set()
    doors = set()
    entrance = None
    path = set()

    for y, row in enumerate(template):
        for x, item in enumerate(row):
            try:
                location = MazeItem(item)
            except ValueError:
                if item.isupper():
                    doors.add(Point(x, y))
                else:
                    keys.add(Point(x, y))

            if location == MazeItem.ENTRANCE:
                entrance = Point(x, y)
            elif location == MazeItem.OPEN_PASSAGE:
                path.add(Point(x, y))

    return keys, doors, entrance, path


def main(filename="input"):
    with open(filename) as input_file:
        grid_template = input_file.read().splitlines()

    process_maze(grid_template)


if __name__ == "__main__":
    main()
