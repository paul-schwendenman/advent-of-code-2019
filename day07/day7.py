import sys
from enum import Enum


class Opcode(Enum):
    ADD = 1
    MULTIPY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF = 5
    JUMP_NOT_IF = 6
    LESS_THAN = 7
    EQUAL_TO = 8
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


def lookup_value(memory, mode, position):
    try:
        if mode == '0':
            return memory[position]
        elif mode == '1':
            return position
    except IndexError:
        pass


def lookup_values(memory, parameter_modes, cursor):
    param_1 = lookup_value(memory, parameter_modes[0], cursor + 1)
    param_2 = lookup_value(memory, parameter_modes[1], cursor + 2)
    param_3 = lookup_value(memory, parameter_modes[2], cursor + 3)

    return param_1, param_2, param_3


def run_program(program, cursor=0, input_value=[5]):
    output = []
    input_values = iter(input_value)

    while True:
        opcode, parameter_modes = split_instruction(program[cursor])

        params = lookup_values(program, parameter_modes, cursor)

        if opcode is Opcode.HALT:
            return output
        elif opcode is Opcode.ADD:
            program[params[2]] = program[params[0]] + program[params[1]]

            cursor += 4
        elif opcode is Opcode.MULTIPY:
            program[params[2]] = program[params[0]] * program[params[1]]

            cursor += 4
        elif opcode is Opcode.INPUT:
            program[params[0]] = next(input_values)

            cursor += 2
        elif opcode is Opcode.OUTPUT:
            output.append(program[params[0]])

            cursor += 2
        elif opcode is Opcode.JUMP_IF:
            if program[params[0]]:
                cursor = program[params[1]]
            else:
                cursor += 3
        elif opcode is Opcode.JUMP_NOT_IF:
            if not program[params[0]]:
                cursor = program[params[1]]
            else:
                cursor += 3
        elif opcode is Opcode.LESS_THAN:
            program[params[2]] = 1 if program[params[0]] < program[params[1]] else 0

            cursor += 4
        elif opcode is Opcode.EQUAL_TO:
            program[params[2]] = 1 if program[params[0]] == program[params[1]] else 0

            cursor += 4
        else:
            print(f"missing opcode: {opcode}")


def run_amps(phase_options, program):
    option = phase_options

    pass1 = int(run_program(program, input_value=[option[0], 0])[0])
    pass2 = int(run_program(program, input_value=[option[1], pass1])[0])
    pass3 = int(run_program(program, input_value=[option[2], pass2])[0])
    pass4 = int(run_program(program, input_value=[option[3], pass3])[0])
    pass5 = int(run_program(program, input_value=[option[4], pass4])[0])

    return pass5

def main():
    with open('input') as input:
        program_string = input.readlines()[0]

    program = list(parse_program(program_string))
    # return run_program(program, input_value=param)
    # return run_amps([4, 3, 2, 1, 0], program)
    # return run_amps([0,1,2,3,4], program)
    return run_amps([1,0,4,3,2], program)


if __name__ == "__main__":
    print(main())
    # main(iter([3, 4]))
    # main(iter([2, 43]))
    # main(iter([1, 432]))
    # main(iter([0, 4321]))
