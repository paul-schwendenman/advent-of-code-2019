from day14 import main, main2


def test_main_example_1():
    assert main('example1.in') == 31


def test_main_example_2():
    assert main('example2.in') == 165


def test_main_example_3():
    assert main('example3.in') == 13312


def test_main_example_4():
    assert main('example4.in') == 180697


def test_main_puzzle_input():
    assert main('puzzle1.in') == 374457


def test_main2_example_3():
    assert main2('example3.in') == 82892753


def test_main2_example_4():
    assert main2('example4.in') == 5586022


def test_main2_puzzle_input():
    assert main2('puzzle1.in') == 3568888
