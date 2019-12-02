from day02 import parse_program, run_program

def test_parse_program():
    assert list(parse_program("1,9,10,70")) == [1, 9, 10, 70]

def test_empty_program():
    assert run_program([99]) == [99]

def test_simple_addition_program():
    assert run_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]