from __future__ import annotations
from typing import Dict, List, Iterator
from collections import namedtuple


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def get_neighboors(self) -> Iterator[Point]:
        for offset in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            yield self + offset

    def __add__(self, other) -> Point:
        return Point(self.x + other[0], self.y + other[1])


def parse_maze(maze_template):
    maze: Dict[Point, str] = {}
    portals: Dict[str, List[Point]] = {}
    return maze, portals


def main(filename='input'):
    with open(filename) as input_file:
        maze_template = input_file.read().splitlines()

    return parse_maze(maze_template)


if __name__ == "__main__":
    print(main('example1.input'))
