def load_intial_state(filename='input'):
    with open(filename) as file_input:
        lines = file_input.read().splitlines()

    return [[True if item == '#' else False for item in line] for line in lines]


def get_neighboors(state, x, y):
    yield state[y-1][x] if y > 0 else False
    yield state[y][x-1] if x > 0 else False
    yield state[y+1][x] if y < 4 else False
    yield state[y][x+1] if x < 4 else False


def count_neighboors(state, x, y):
    value = 0

    for neighboor in get_neighboors(state, x, y):
        if neighboor:
            value += 1

    return value


def step_simulation(state):
    new_state = [[False for _ in range(5)] for _ in range(5)]
    for y, row in enumerate(state):
        for x, space in enumerate(row):
            count = count_neighboors(state, x, y)
            print(f'{(x, y)} {"#" if space else "."} \t{count}', end='\t')
            if space:
                if count == 1:
                    print('survive')
                    new_state[y][x] = True
                else:
                    print('die')
                    new_state[y][x] = False
            else:
                if count in (1, 2):
                    print('spawn')
                    new_state[y][x] = True
                else:
                    print('idle')
    return new_state


def print_grid(state):
    for y in range(5):
        for x in range(5):
            print('#' if state[y][x] else '.', end='')
        print('')
    print('')


def main():
    intial_state = load_intial_state('input.example')

    print_grid(intial_state)

    state = step_simulation(intial_state)

    print_grid(state)

    state = step_simulation(state)

    print_grid(state)


if __name__ == "__main__":
    main()
