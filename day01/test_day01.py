from day01 import calculate_fuel

def test_example_1():
    assert calculate_fuel(12) == 2

def test_example_2():
    assert calculate_fuel(14) == 2

def test_example_3():
    assert calculate_fuel(1969) == 654

def test_example_4():
    assert calculate_fuel(100756) == 33583
