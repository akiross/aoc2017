"""Advent of Code 2017, day one puzzles solved in various ways."""


import sys
from itertools import chain


def compute(x, offset=1):
    """Compute puzzle result, uzing zip."""
    # I use chain to efficiently generate values without using too much memory
    return sum(int(a) for a, b in zip(x, chain(x[offset:], x)) if a == b)


def compute_2(x, offset=1):
    """Compute by looping and checking ahead."""
    y = 0
    x2 = x + x[:offset]  # Lists are concatenated, but they take memory
    for i in range(len(x)):
        if x2[i] == x2[i+offset]:
            y += int(x2[i])
    return y


if __name__ == '__main__':
    # Do some tests
    X = '1122 1111 1234 91212129 2233 389344583 333'.split()
    Y = [3, 4, 0, 9, 5, 7, 9]
    results = [compute(x) == y for x, y in zip(X, Y)]
    if all(results):
        print('All tests passed!')
    else:
        print('Failed tests:', results)

    # Actual data, remember to strip spaces >_<
    data = open(sys.argv[1]).read().strip()

    # Solution of first puzzle
    print('First', compute(data), compute_2(data))

    X = '1212 1221 123425 123123 12131415'.split()
    Y = [6, 0, 4, 12, 4]
    results = [compute(x, len(x)//2) == y for x, y in zip(X, Y)]
    if all(results):
        print('All tests passed!')
    else:
        print('Failed tests:', results)

    l = len(data) // 2
    print('Second', compute(data, l), compute_2(data, l))
