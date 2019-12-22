from day22 import new_stack, cut, increment
from collections import deque


def test_new_stack():
    deck = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert new_stack(deck) == deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


def test_cut():
    deck = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert cut(deck, 3) == deque([3, 4, 5, 6, 7, 8, 9, 0, 1, 2])


def test_cut2():
    deck = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert cut(deck, -4) == deque([6, 7, 8, 9, 0, 1, 2, 3, 4, 5])


def test_increment():
    deck = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert increment(deck, 3) == deque([0, 7, 4, 1, 8, 5, 2, 9, 6, 3])
