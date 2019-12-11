import sys
from enum import Enum, IntEnum
from collections import defaultdict, namedtuple
from typing import Tuple


Point = namedtuple('Point', 'x y')


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def rotate(self, direction):
        return Direction((self + direction) % 4)


class MissingParameterMode(Exception):
    pass


class MissingOpcode(Exception):
    pass


class Opcode(Enum):
    ADD = 1
    MULTIPY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF = 5
    JUMP_NOT_IF = 6
    LESS_THAN = 7
    EQUAL_TO = 8
    ADJUST_RELATIVE_BASE = 9
    HALT = 99


class ParameterMode(Enum):
    POSITION = '0'
    IMMEDIATE = '1'
    RELATIVE = '2'


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def parse_program(program):
    return (int(item) for item in program.split(','))


def split_instruction(instruction):
    opcode = Opcode(instruction % 100)
    instruction = list(str(instruction))
    parameter_modes = [ParameterMode(mode) for mode in (["0"] * 5 + instruction)[-3:-6:-1]]

    return opcode, parameter_modes


def lookup_value(memory, mode, position, relative_base):
    try:
        if mode == ParameterMode.POSITION:
            return memory[position]
        elif mode == ParameterMode.IMMEDIATE:
            return position
        elif mode == ParameterMode.RELATIVE:
            return relative_base + memory[position]
        else:
            raise MissingParameterMode

    except IndexError:
        pass


def lookup_values(memory, parameter_modes, cursor, relative_base):
    param_1 = lookup_value(memory, parameter_modes[0], cursor + 1, relative_base)
    param_2 = lookup_value(memory, parameter_modes[1], cursor + 2, relative_base)
    param_3 = lookup_value(memory, parameter_modes[2], cursor + 3, relative_base)

    return param_1, param_2, param_3


class IntCode():
    def __init__(self, program=None, default_memory=2000):
        self._memory = [0] * default_memory
        self._cursor = 0
        self._relative_base = 0

        if program:
            self.load_program(program)

        self.inputs = []
        self.outputs = []

    def load_program(self, program):
        self._memory[:len(program)] = program

    def run(self):
        while True:
            opcode, parameter_modes = split_instruction(self._memory[self._cursor])

            params = lookup_values(self._memory, parameter_modes, self._cursor, self._relative_base)
            # eprint(f'{opcode} {params} {parameter_modes}')

            if opcode is Opcode.HALT:
                return True
            elif opcode is Opcode.ADD:
                self._memory[params[2]] = self._memory[params[0]] + self._memory[params[1]]

                self._cursor += 4
            elif opcode is Opcode.MULTIPY:
                self._memory[params[2]] = self._memory[params[0]] * self._memory[params[1]]

                self._cursor += 4
            elif opcode is Opcode.INPUT:
                if self.inputs:
                    self._memory[params[0]] = self.inputs.pop(0)
                else:
                    return False

                self._cursor += 2
            elif opcode is Opcode.OUTPUT:
                self.outputs.append(self._memory[params[0]])

                self._cursor += 2
            elif opcode is Opcode.JUMP_IF:
                if self._memory[params[0]]:
                    self._cursor = self._memory[params[1]]
                else:
                    self._cursor += 3
            elif opcode is Opcode.JUMP_NOT_IF:
                if not self._memory[params[0]]:
                    self._cursor = self._memory[params[1]]
                else:
                    self._cursor += 3
            elif opcode is Opcode.LESS_THAN:
                self._memory[params[2]] = 1 if self._memory[params[0]] < self._memory[params[1]] else 0

                self._cursor += 4
            elif opcode is Opcode.EQUAL_TO:
                self._memory[params[2]] = 1 if self._memory[params[0]] == self._memory[params[1]] else 0

                self._cursor += 4
            elif opcode is Opcode.ADJUST_RELATIVE_BASE:
                self._relative_base += self._memory[params[0]]

                self._cursor += 2
            else:
                print(f"missing opcode: {opcode}")
                raise MissingOpcode


def run_program(program_string, input_value=0):
    computer.inputs.append(input_value)
    halted = computer.run()

    return halted, computer.outputs


class PaintingRobot():
    def __init__(self):
        pass


def move_robot(location: Point, facing: Direction, clockwise: int) -> Tuple[Point, Direction]:
    facing = facing.rotate(1 if clockwise else -1)

    if facing == Direction.UP:
        location = Point(location.x, location.y - 1)
    elif facing == Direction.RIGHT:
        location = Point(location.x + 1, location.y)
    elif facing == Direction.DOWN:
        location = Point(location.x, location.y + 1)
    elif facing == Direction.LEFT:
        location = Point(location.x - 1, location.y)

    return location, facing


def main():
    with open('../day11/input') as input:
        program_string = input.readlines()[0]

    program = list(parse_program(program_string))
    computer = IntCode(program)

    # return run_program(program_string, input_value=input_value)
    halted = False
    grid = defaultdict(lambda: 0)
    location = Point(0, 0)
    facing = Direction.UP
    while not halted:
        computer.inputs.append(grid[location])
        halted = computer.run()

        color = computer.outputs.pop(0)
        direction = computer.outputs.pop(0)

        grid[location] = color
        location, facing = move_robot(location, facing, direction)

    return len(grid.keys())




if __name__ == "__main__":
    print(main())
