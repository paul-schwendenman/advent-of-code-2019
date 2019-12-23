from collections import deque
from typing import Iterable, Deque, Iterator, Tuple, Optional
from enum import Enum, auto


class Operation(Enum):
    CUT = auto()
    STACK = auto()
    INCREMENT = auto()


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


def process_instructions(instructions: Iterable[Tuple[Operation, int]], deck: Deque) -> Deque:
    for count, (instruction, value) in enumerate(instructions):
        # print(f'{count:2}. {instruction}')
        if instruction == Operation.CUT:
            deck = cut(deck, value)
        elif instruction == Operation.INCREMENT:
            deck = increment(deck, value)
        elif instruction == Operation.STACK:
            deck = new_stack(deck)

    return deck


def parse_instructions(instructions: Iterable[str]) -> Iterator[Tuple[Operation, Optional[int]]]:
    for instruction in instructions:
        print(f'{instruction}')
        if instruction[:3] == "cut":
            yield (Operation.CUT, int(instruction[4:]))
        elif instruction[:20] == 'deal with increment ':
            yield (Operation.INCREMENT, int(instruction[20:]))
        elif instruction == 'deal into new stack':
            yield (Operation.STACK, None)


def part1():
    with open('input') as file_input:
        instructions = parse_instructions(file_input.read().splitlines())

    deck = deque(range(10007))
    deck = process_instructions(instructions, deck)

    return deck.index(2019)


def main():
    with open('input') as file_input:
        instructions = file_input.read().splitlines()

    number_of_cards = 119315717514047
    value_at_2020 = 2020
    for instruction in reversed(instructions):
        if instruction[:3] == "cut":
            value_at_2020 -= int(instruction[4:])
            value_at_2020 %= number_of_cards
        elif instruction[:20] == 'deal with increment ':
            spaces = int(instruction[20:])

        elif instruction == 'deal into new stack':
            value_at_2020 = number_of_cards - value_at_2020
        else:
            raise ValueError(f"Invalid instruction: '{instruction}'")

    return value_at_2020


if __name__ == "__main__":
    # print(main())
    for i in (2, 3):
        deck = deque(range(7))
        print(f'{i}. {increment(deck, i)}')
