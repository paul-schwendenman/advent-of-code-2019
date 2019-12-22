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


def process_instructions(instructions: Iterable[str], deck: Deque) -> Deque:
    for instruction in instructions:
        if instruction[:3] == "cut":
            number_of_cards = int(instruction[4:])
            deck = cut(deck, number_of_cards)
        elif instruction[:20] == 'deal with increment ':
            spaces = int(instruction[20:])
            deck = increment(deck, spaces)
        elif instruction == 'deal into new stack':
            deck = new_stack(deck)

    return deck



def main():
    pass


if __name__ == "__main__":
    main()
