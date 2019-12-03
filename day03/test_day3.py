from day3 import manhattan_distance, find_line_size


def test_manhattan():
    assert manhattan_distance((0, 0), (3, 3)) == 6


def test_calc_grid_size():
    assert find_line_size(["R8", "U5", "L5", "D3"]) == ((0, 0), (8, 5))


def test_calc_grid_size2():
    assert find_line_size(["U7", "R6", "D4", "L4"]) == ((0, 0), (6, 7))
