from day6 import main, calc_orbits


# def test_mais

def test_calc_orbits():
    assert calc_orbits(["COM)B", "B)C"]) == 3

def test_calc_orbits2():
    assert calc_orbits(['COM)B\n', 'B)C\n', 'C)D\n', 'D)E\n', 'E)F\n', 'B)G\n', 'G)H\n', 'D)I\n', 'E)J\n', 'J)K\n', 'K)L\n']) == 42

# def test_calc_orbits2():
#     assert calc_orbits(["COM)B", "B)C", "C)D"]) == 6
