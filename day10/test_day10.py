from day10 import main, Point, calc_angle, Point


# def test_main_1():
#     assert main('test1.in') == (Point(3, 4), 8)


# def test_main_2():
#     point, count = main('test2.in')
#     assert main('test2.in') == (Point(5, 8), 33)

def test_calc_angle_vertical():
    assert calc_angle(Point(0, 0), Point(0, -1)) == 0
