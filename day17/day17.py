from intcode import open_program, IntCode
from collections import namedtuple


Point = namedtuple('Point', 'x y')


def get_neighboors(current_location: Point):
    yield Point(current_location.x - 1, current_location.y)
    yield Point(current_location.x + 1, current_location.y)
    yield Point(current_location.x, current_location.y - 1)
    yield Point(current_location.x, current_location.y + 1)


def print_grid(outputs):
    display_map = {
        46: '.',
        35: '#',
        10: '\n',
        60: '<',
        62: '>',
        94: '^',
        118: 'v'
    }
    for output in outputs:
        print(display_map[output], end='')


def convert_to_array(outputs):
    path = set()
    x = 0
    y = 0
    robot = None
    for output in outputs:
        if output == 10:
            y += 1
            x = 0
            continue
        elif output == 35:
            point = Point(x, y)
            path.add(point)
        elif output in {60, 62, 94, 118}:
            if not robot:
                robot = Point(x, y)
            else:
                raise Exception('Two robots')

        x += 1

    return path, robot


def part1(program):
    computer = IntCode(program, default_memory=8000)
    computer.run()

    outputs = list(computer._outputs)
    computer._outputs.clear()

    print_grid(outputs)
    scaffold, robot = convert_to_array(outputs)

    intersections = set()
    for location in scaffold:
        if all(map(lambda x: x in scaffold, get_neighboors(location))):
            intersections.add(location)

    return sum(intersection.x * intersection.y for intersection in list(intersections))


def main(filename='input'):
    program = open_program(filename)
    return part1(program)


if __name__ == "__main__":
    print(main())
