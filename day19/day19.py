from intcode import open_program, IntCode
from collections import defaultdict, namedtuple


Point = namedtuple('Point', 'x y')


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


def part2():
    program = open_program('input')
    # computer = IntCode(program)

    base_y = 475
    base_x = 975

    for i in range(100):
        last = 0
        for j in range(100):
            count = 0
            # grid = defaultdict(int)
            for y in range(base_y+j, base_y+j+100):
                for x in range(base_x+i, base_x+i+100):
                    computer = IntCode(program[:])
                    computer.add_input(x)
                    computer.add_input(y)
                    computer.run()

                    output = computer.get_output()
                    if output:
                        count += 1
                        # grid[Point(x, y)] = 1
                        # print('#', end='')
                    else:
                        pass
                        # print('.', end='')
                        # print(x,y)
                # print('')

            if count == 10000:
                print(Point(base_x + i, base_y + j))
                print(Point(x, y))
                return (base_x + i) * 10000 + (base_y + j)
            else:
                print(count, Point(x, y))

            if last > count:
                break
            else:
                last = count


def main():
    # print(part1())
    print(part2())


if __name__ == "__main__":
    main()
