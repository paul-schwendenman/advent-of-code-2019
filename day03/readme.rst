Day 03
========

Performance
-------------

Part 1::

    python -m timeit -n 20 -s 'from day3 import main, main2; lines = open("input").readlines()' 'main(lines[0], lines[1])'


Part 2::


    python -m timeit -n 20 -s 'from day3 import main, main2; lines = open("input").readlines()' 'main2(lines[0], lines[1])'
