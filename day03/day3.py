X_MAX = 100
Y_MAX = 100
X_MID = int(X_MAX / 2)
Y_MID = int(Y_MAX / 2)


def manhattan_distance(pos_a, pos_b):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])


def print_grid(grid):
    for row in grid:
        print("".join(row))


def spilt_instruction(instruction):
    return instruction[0], int(instruction[1:])


def find_line_size(path):
    x_min, x_max = 0, 0
    y_min, y_max = 0, 0
    x, y = 0, 0

    for instruction in path:
        direction, length = spilt_instruction(instruction)
        if direction == 'R':
            x += length
            x_max = max(x_max, x)
        elif direction == 'L':
            x -= length
            x_min = min(x_min, x)
        elif direction == 'U':
            y += length
            y_max = max(y_max, y)
        elif direction == 'D':
            y -= length
            y_min = min(y_min, y)

    return (x_min, y_min), (x_max, y_max)


def convert_instructions_to_path(instructions):
    x, y = 0, 0
    path = []

    for instruction in instructions:
        direction, length = spilt_instruction(instruction)
        if direction == 'R':
            for i in range(length):
                x += 1
                path.append((x, y))
        elif direction == 'L':
            for i in range(length):
                x -= 1
                path.append((x, y))
        elif direction == 'U':
            for i in range(length):
                y += 1
                path.append((x, y))
        elif direction == 'D':
            for i in range(length):
                y -= 1
                path.append((x, y))
    return path


def find_intersections(path1, path2):
    path1 = convert_instructions_to_path(path1.split(','))
    path2 = convert_instructions_to_path(path2.split(','))
    return set(path1).intersection(set(path2))


def find_closest_intersection(coords):
    print([manhattan_distance((0, 0), coord) for coord in coords])
    return min(manhattan_distance((0, 0), coord) for coord in coords)


def main(path1, path2):
    coords = find_intersections(path1, path2)

    c = list(coords)
    print(c)
    print([a + b for a, b in c])

    return find_closest_intersection(coords)


if __name__ == "__main__":
    grid = [['.' for _ in range(X_MAX)] for _ in range(Y_MAX)]
    grid[Y_MID][X_MID] = 'o'
    print_grid(grid)

    line = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
    print(find_line_size(line))
