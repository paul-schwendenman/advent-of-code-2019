from intcode import open_program, IntCode

def part1():
    program = open_program('input')
    # computer = IntCode(program)

    count = 0
    for y in range(50):
        for x in range(50):
            computer = IntCode(program[:])
            computer.add_input(x)
            computer.add_input(y)
            computer.run()

            output = computer.get_output()
            if output:
                count += 1
            else:
                pass
                # print(x,y)

    return count



def main():
    print(part1())


if __name__ == "__main__":
    main()
