from day20 import Point


def test_Point_get_neighboors():
    expected_points = [Point(x=-1, y=0), Point(x=1, y=0), Point(x=0, y=-1), Point(x=0, y=1)]
    assert list(Point(0, 0).get_neighboors()) == expected_points


def test_Point_addition():
    assert Point(1, 2) + Point(1, 2) == Point(2, 4)
