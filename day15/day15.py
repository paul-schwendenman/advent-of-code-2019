from intcode import IntCode, parse_program
from collections import defaultdict, namedtuple
from enum import IntEnum
from copy import deepcopy
import sys


sys.setrecursionlimit(5500000)


Point = namedtuple('Point', 'x y')


class Direction(IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class StatusCode(IntEnum):
    WALL = 0
    MOVED = 1
    FOUND = 2


class GridSpace(IntEnum):
    UNKNOWN = 0
    EMPTY = 1
    WALL = 2
    DROID = 3
    OXYGEN_SYSTEM = 4


def get_neighboors(grid, location):
    x_pos, y_pos = location
    return (
        (x_pos-1, y_pos),
        (x_pos+1, y_pos),
        (x_pos, y_pos-1),
        (x_pos, y_pos+1),
    )


def get_move(grid, location):
    neighboors = [grid[neighboor] for neighboor in get_neighboors(grid, location)]
    # print(neighboors)

    if grid[get_next_square(location, Direction.WEST)] is GridSpace.UNKNOWN:
        return Direction.WEST
    elif grid[get_next_square(location, Direction.NORTH)] is GridSpace.UNKNOWN:
        return Direction.NORTH
    elif grid[get_next_square(location, Direction.EAST)] is GridSpace.UNKNOWN:
        return Direction.EAST
    elif grid[get_next_square(location, Direction.SOUTH)] is GridSpace.UNKNOWN:
        return Direction.SOUTH
    # if grid[get_next_square(location, Direction.WEST)] is not GridSpace.WALL:
    #     return Direction.WEST
    # elif grid[get_next_square(location, Direction.NORTH)] is not GridSpace.WALL:
    #     return Direction.NORTH
    # elif grid[get_next_square(location, Direction.EAST)] is not GridSpace.WALL:
    #     return Direction.EAST
    # elif grid[get_next_square(location, Direction.SOUTH)] is not GridSpace.WALL:
    #     return Direction.SOUTH


def get_next_square(current_location: Point, direction: Direction):
    if direction == Direction.NORTH:
        return Point(current_location.x - 1, current_location.y)
    elif direction == Direction.SOUTH:
        return Point(current_location.x + 1, current_location.y)
    elif direction == Direction.EAST:
        return Point(current_location.x, current_location.y - 1)
    elif direction == Direction.WEST:
        return Point(current_location.x, current_location.y + 1)


def run_move(computer, move, grid, location, depth):
    oxygen_found = 1e15
    next_location = get_next_square(location, move)
    if next_location in grid:
        return grid, oxygen_found
    computer = deepcopy(computer)
    computer.inputs.append(move)
    halted = computer.run()
    output = computer.outputs.pop(0)

    if output == StatusCode.WALL:
        grid[next_location] = GridSpace.WALL
    elif output == StatusCode.MOVED:
        # grid[location] = GridSpace.EMPTY
        grid[next_location] = GridSpace.EMPTY
        location = next_location
        grid, oxygen_found = run_moves(computer, grid, next_location, depth+1)
    elif output == StatusCode.FOUND:
        grid[next_location] = GridSpace.OXYGEN_SYSTEM
        oxygen_found = depth
        print(f'found OXY at {next_location}')
    return grid, oxygen_found


def run_moves(computer, grid, location, depth=1):
    counts = []
    for direction in [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST]:
        grid, oxygen_found = run_move(computer, direction, grid, location, depth)
        # if oxygen_found:
        #     break
        counts.append(oxygen_found)
    return grid, min(counts)


def escape_helper(grid, location, direction, depth, history):
    next_location = get_next_square(location, direction)
    if next_location in history:
        return 0
    output = grid[next_location]

    if output == GridSpace.WALL:
        return depth
    else:
        return escape(grid, next_location, depth+1)


def escape(grid, location, depth=1, history=set()):
    history.add(location)
    # print(location)
    counts = []
    for direction in [Direction.NORTH, Direction.SOUTH, Direction.EAST, Direction.WEST]:
        count = escape_helper(grid, location, direction, depth, history)
        counts.append(count)

    return max(counts)


def main():
    with open('../day15/input') as input:
        program_string = input.readlines()[0]

    program = list(parse_program(program_string))
    computer = IntCode(program, default_memory=8000)

    halted = False
    location = Point(0, 0)
    grid = defaultdict(lambda: 0)
    grid[location] = GridSpace.DROID

    count = 0
    while not halted:
        # sleep(2)
        grid, _oxy = run_moves(computer, grid, location)

        # print_grid(grid)
        halted = True
        count += 1

    print_grid(grid)
    print(_oxy)

    print(escape(grid, Point(-16, 14)))


def print_grid(grid):
    display = {
        GridSpace.UNKNOWN: ' ',
        GridSpace.WALL: '#',
        GridSpace.EMPTY: '.',
        GridSpace.DROID: 'D',
        GridSpace.OXYGEN_SYSTEM: '*',
    }
    grid = grid.copy()
    min_x = min(point.x for point in grid.keys())
    max_x = max(point.x for point in grid.keys())
    min_y = min(point.y for point in grid.keys())
    max_y = max(point.y for point in grid.keys())

    for pos_y in range(min_y, max_y + 1):
        for pos_x in range(min_x, max_x + 1):
            # print('#' if grid[Point(pos_x, pos_y)] else ' ', end='')
            print(display[grid[Point(pos_x, pos_y)]], end='')
        print('')

    print('-----------------')


if __name__ == "__main__":
    main()
