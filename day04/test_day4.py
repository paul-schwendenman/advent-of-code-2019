from day4 import has_double_digit, never_decreases


def test_has_double_digit():
    assert has_double_digit(122345)


def test_does_not_have_double_digit():
    assert not has_double_digit(123456)


def test_never_decreases():
    assert never_decreases("123455")


def test_not_decreasing():
    assert not never_decreases("123450")
