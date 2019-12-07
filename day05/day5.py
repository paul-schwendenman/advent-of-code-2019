def parse_program(program):
    return (int(item) for item in program.split(','))


def split_instruction(instruction):
    opcode = instruction % 100
    instruction = list(str(instruction))
    parameter_modes = (["0"] * 5 + instruction)[-3:-6:-1]

    return opcode, parameter_modes


def lookup_value(memory, mode, position):
    if mode == '0':
        return memory[memory[position]]
    elif mode == '1':
        return memory[position]


def run_program(program, cursor=0, input_value=5):
    opcode, parameter_modes = split_instruction(program[cursor])

    if opcode == 99:
        return program
    elif opcode == 1:
        param_1 = lookup_value(program, parameter_modes[0], cursor + 1)
        param_2 = lookup_value(program, parameter_modes[1], cursor + 2)
        program[program[cursor + 3]] = param_1 + param_2

        return run_program(program, cursor + 4, input_value)
    elif opcode == 2:
        param_1 = lookup_value(program, parameter_modes[0], cursor + 1)
        param_2 = lookup_value(program, parameter_modes[1], cursor + 2)
        program[program[cursor + 3]] = param_1 * param_2

        return run_program(program, cursor + 4, input_value)
    elif opcode == 3:
        program[program[cursor + 1]] = input_value

        return run_program(program, cursor + 2, input_value)
    elif opcode == 104:
        print(program[cursor + 1])

        return run_program(program, cursor + 2, input_value)
    elif opcode == 4:
        param_1 = lookup_value(program, parameter_modes[0], cursor + 1)
        print(param_1)

        return run_program(program, cursor + 2, input_value)
    elif opcode == 5:
        param_1 = lookup_value(program, parameter_modes[0], cursor + 1)
        param_2 = lookup_value(program, parameter_modes[1], cursor + 2)
        if param_1:
            return run_program(program, param_2, input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode == 6:
        param_1 = lookup_value(program, parameter_modes[0], cursor + 1)
        param_2 = lookup_value(program, parameter_modes[1], cursor + 2)
        if not param_1:
            return run_program(program, param_2, input_value)

        return run_program(program, cursor + 3, input_value)
    elif opcode == 7:
        param_1 = lookup_value(program, parameter_modes[0], cursor + 1)
        param_2 = lookup_value(program, parameter_modes[1], cursor + 2)
        program[program[cursor + 3]] = 1 if param_1 < param_2 else 0

        return run_program(program, cursor + 4, input_value)
    elif opcode == 8:
        param_1 = lookup_value(program, parameter_modes[0], cursor + 1)
        param_2 = lookup_value(program, parameter_modes[1], cursor + 2)
        program[program[cursor + 3]] = 1 if param_1 == param_2 else 0

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
