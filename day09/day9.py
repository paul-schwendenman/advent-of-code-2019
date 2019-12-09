import sys
from enum import Enum
import itertools


class InvalidParameterMode(Exception):
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


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def parse_program(program):
    return (int(item) for item in program.split(','))


def split_instruction(instruction):
    opcode = Opcode(instruction % 100)
    instruction = list(str(instruction))
    parameter_modes = (["0"] * 5 + instruction)[-3:-6:-1]

    return opcode, parameter_modes


def lookup_value(memory, mode, position, relative_base):
    try:
        if mode == '0':
            return memory[position]
        elif mode == '1':
            return position
        elif mode == '2':
            eprint('help')
            return relative_base + memory[position]
        else:
            raise InvalidParameterMode

    except IndexError:
        pass


def lookup_values(memory, parameter_modes, cursor, relative_base):
    param_1 = lookup_value(memory, parameter_modes[0], cursor + 1, relative_base)
    param_2 = lookup_value(memory, parameter_modes[1], cursor + 2, relative_base)
    param_3 = lookup_value(memory, parameter_modes[2], cursor + 3, relative_base)

    return param_1, param_2, param_3


class IntCode():
    def __init__(self, program):
        self.program = program[:] + [0] * 1000
        self.cursor = 0
        self.inputs = []
        self.outputs = []
        self.relative_base = 0

    def run(self):

        while True:
            opcode, parameter_modes = split_instruction(self.program[self.cursor])

            params = lookup_values(self.program, parameter_modes, self.cursor, self.relative_base)
            eprint(f'{opcode} {params} {parameter_modes}')

            if opcode is Opcode.HALT:
                return True
            elif opcode is Opcode.ADD:
                self.program[params[2]] = self.program[params[0]] + self.program[params[1]]

                self.cursor += 4
            elif opcode is Opcode.MULTIPY:
                self.program[params[2]] = self.program[params[0]] * self.program[params[1]]

                self.cursor += 4
            elif opcode is Opcode.INPUT:
                if self.inputs:
                    self.program[params[0]] = self.inputs.pop(0)
                else:
                    return False

                self.cursor += 2
            elif opcode is Opcode.OUTPUT:
                self.outputs.append(self.program[params[0]])

                self.cursor += 2
            elif opcode is Opcode.JUMP_IF:
                if self.program[params[0]]:
                    self.cursor = self.program[params[1]]
                else:
                    self.cursor += 3
            elif opcode is Opcode.JUMP_NOT_IF:
                if not self.program[params[0]]:
                    self.cursor = self.program[params[1]]
                else:
                    self.cursor += 3
            elif opcode is Opcode.LESS_THAN:
                self.program[params[2]] = 1 if self.program[params[0]] < self.program[params[1]] else 0

                self.cursor += 4
            elif opcode is Opcode.EQUAL_TO:
                self.program[params[2]] = 1 if self.program[params[0]] == self.program[params[1]] else 0

                self.cursor += 4
            elif opcode is Opcode.ADJUST_RELATIVE_BASE:
                self.relative_base += self.program[params[0]]

                self.cursor += 2
            else:
                print(f"missing opcode: {opcode}")
                raise MissingOpcode


def run_program(program_string):
    program = list(parse_program(program_string))
    computer = IntCode(program)
    computer.run()

    return computer.outputs


def main():
    with open('../day09/input') as input:
        program_string = input.readlines()[0]

    return run_program(program_string)



if __name__ == "__main__":
    print(main())
