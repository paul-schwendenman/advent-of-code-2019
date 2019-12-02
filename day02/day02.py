def parse_program(program):
    return (int(item) for item in program.split(','))


def run_program(program, cursor=0):
    opcode = program[cursor]

    if opcode == 99:
        return program
    elif opcode == 1:
        program[program[cursor + 3]] = program[program[cursor + 1]] + program[program[cursor + 2]]

        return run_program(program, 4) 

def main():
    pass

if __name__ == "__main__":
    main()