from intcode import IntCode, parse_program
from collections import defaultdict, namedtuple


Point = namedtuple('Point', 'x y')


def main(initial_color=0):
    with open('../day13/input') as input:
        program_string = input.readlines()[0]

    program = list(parse_program(program_string))
    computer = IntCode(program, default_memory=8000)

    halted = False
    grid = defaultdict(lambda: 0)
    while not halted:
        # computer.inputs.append(grid[location])
        halted = computer.run()

    while len(computer.outputs) > 0:
        x_pos = computer.outputs.pop(0)
        y_pos = computer.outputs.pop(0)
        tile_id = computer.outputs.pop(0)

        grid[Point(x_pos, y_pos)] = tile_id

    print(grid)

    print_grid(grid)

    return len([item for item in grid.values() if item == 2])


def main2(initial_color=0):
    with open('../day13/input') as input_file:
        program_string = input_file.readlines()[0]

    user_inputs = []


    program = list(parse_program(program_string))
    program[0] = 2
    computer = IntCode(program, default_memory=8000)

    computer.inputs.extend([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, -1, -1, 0, 1, -1, -1, -1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    halted = False
    grid = defaultdict(lambda: 0)
    while not halted:
        # computer.inputs.append(grid[location])
        halted = computer.run()

        while len(computer.outputs) > 0:
            x_pos = computer.outputs.pop(0)
            y_pos = computer.outputs.pop(0)
            tile_id = computer.outputs.pop(0)

            grid[Point(x_pos, y_pos)] = tile_id

        print_grid(grid)

        user_input = get_user_input(user_inputs)
        user_inputs.append(user_input)

        computer.inputs.append(user_input)

    print(user_inputs)

    return grid[Point(-1, 0)]


def get_user_input(user_inputs):
    user_input = None
    while user_input not in (-1, 0, 1):
        try:
            user_input = int(input("? "))
        except ValueError:
            pass
        except KeyboardInterrupt:
            print(user_inputs)
    return user_input


def print_grid(grid):
    display = {
        0: ' ',
        1: '#',
        2: '.',
        3: '^',
        4: '*',
    }
    grid = grid.copy()
    min_x = 0  # min(point.x for point in grid.keys())
    max_x = max(point.x for point in grid.keys())
    min_y = 0  # min(point.y for point in grid.keys())
    max_y = max(point.y for point in grid.keys())

    for pos_y in range(min_y, max_y + 1):
        for pos_x in range(min_x, max_x + 1):
            # print('#' if grid[Point(pos_x, pos_y)] else ' ', end='')
            print(display[grid[Point(pos_x, pos_y)]], end='')
        print('')


if __name__ == "__main__":
    print(main2())
