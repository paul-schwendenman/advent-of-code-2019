def parse_program(program):
    return (int(item) for item in program.split(','))


def run_program(program, cursor=0, input_value=5):
    opcode = program[cursor]

    if opcode == 99:
        return program
    elif opcode == 1101:
        program[program[cursor + 3]] = program[cursor + 1] + program[cursor + 2]

        return run_program(program, cursor + 4, input_value)
    elif opcode == 1001:
        program[program[cursor + 3]] = program[program[cursor + 1]] + program[cursor + 2]

        return run_program(program, cursor + 4, input_value)
    elif opcode == 101:
        program[program[cursor + 3]] = program[cursor + 1] + program[program[cursor + 2]]

        return run_program(program, cursor + 4, input_value)
    elif opcode == 1:
        program[program[cursor + 3]] = program[program[cursor + 1]] + program[program[cursor + 2]]

        return run_program(program, cursor + 4, input_value)
    elif opcode == 1102:
        program[program[cursor + 3]] = program[cursor + 1] * program[cursor + 2]

        return run_program(program, cursor + 4, input_value)
    elif opcode == 1002:
        program[program[cursor + 3]] = program[program[cursor + 1]] * program[cursor + 2]

        return run_program(program, cursor + 4, input_value)
    elif opcode == 102:
        program[program[cursor + 3]] = program[cursor + 1] * program[program[cursor + 2]]

        return run_program(program, cursor + 4, input_value)
    elif opcode == 2:
        program[program[cursor + 3]] = program[program[cursor + 1]] * program[program[cursor + 2]]

        return run_program(program, cursor + 4, input_value)
    elif opcode == 3:
        program[program[cursor + 1]] = input_value

        return run_program(program, cursor + 2, input_value)
    elif opcode == 104:
        print(program[cursor + 1])

        return run_program(program, cursor + 2, input_value)
    elif opcode == 4:
        print(program[program[cursor + 1]])

        return run_program(program, cursor + 2, input_value)
    elif opcode == 1105:
        if program[cursor + 1]:
            return run_program(program, program[cursor + 2], input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode == 1005:
        if program[program[cursor + 1]]:
            return run_program(program, program[cursor + 2], input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode == 105:
        if program[cursor + 1]:
            return run_program(program, program[program[cursor + 2]], input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode == 5:
        if program[program[cursor + 1]]:
            return run_program(program, program[program[cursor + 2]], input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode == 1106:
        if not program[cursor + 1]:
            return run_program(program, program[cursor + 2], input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode == 1006:
        if not program[program[cursor + 1]]:
            return run_program(program, program[cursor + 2], input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode == 106:
        if not program[cursor + 1]:
            return run_program(program, program[program[cursor + 2]], input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode == 6:
        if not program[program[cursor + 1]]:
            return run_program(program, program[program[cursor + 2]], input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode == 1107:
        program[program[cursor + 3]] = 1 if program[cursor + 1] < program[cursor + 2] else 0

        return run_program(program, cursor + 4, input_value)
    elif opcode == 1007:
        program[program[cursor + 3]] = 1 if program[program[cursor + 1]] < program[cursor + 2] else 0

        return run_program(program, cursor + 4, input_value)
    elif opcode == 107:
        program[program[cursor + 3]] = 1 if program[cursor + 1] < program[program[cursor + 2]] else 0

        return run_program(program, cursor + 4, input_value)
    elif opcode == 7:
        program[program[cursor + 3]] = 1 if program[program[cursor + 1]] < program[program[cursor + 2]] else 0

        return run_program(program, cursor + 4, input_value)
    elif opcode == 1108:
        program[program[cursor + 3]] = 1 if program[cursor + 1] == program[cursor + 2] else 0

        return run_program(program, cursor + 4, input_value)
    elif opcode == 1008:
        program[program[cursor + 3]] = 1 if program[program[cursor + 1]] == program[cursor + 2] else 0

        return run_program(program, cursor + 4, input_value)
    elif opcode == 108:
        program[program[cursor + 3]] = 1 if program[cursor + 1] == program[program[cursor + 2]] else 0

        return run_program(program, cursor + 4, input_value)
    elif opcode == 8:
        program[program[cursor + 3]] = 1 if program[program[cursor + 1]] == program[program[cursor + 2]] else 0

        return run_program(program, cursor + 4, input_value)
    else:
        print(f"missing opcode: {opcode}")


def main(param=1):
    with open('day05/input') as input:
        program_string = input.readlines()[0]

    program = list(parse_program(program_string))
    run_program(program, input_value=param)


if __name__ == "__main__":
    main(1)
    main(5)
