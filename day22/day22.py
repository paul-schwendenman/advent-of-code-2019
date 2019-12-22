from collections import deque
from typing import Iterable, Deque


def new_stack(deck: Deque) -> Deque:
    deck.reverse()
    return deck


def cut(deck: Deque, n_cards: int) -> Deque:
    deck.rotate(-n_cards)
    return deck


def increment(deck: Deque, spaces: int) -> Deque:
    number_of_cards = len(deck)
    table = [None] * number_of_cards

    pos = 0
    while deck:
        table[pos] = deck.popleft()
        pos += spaces
        if pos > number_of_cards:
            pos = (pos % number_of_cards)

    return Deque(table)



    return deck

def main():
    pass


if __name__ == "__main__":
    main()
