from itertools import chain, cycle

def spiral_coords():
    """Generate sequence of coordinates."""
    spiral, pos = 1, [0, 0]
    #yield tuple(pos)
    while True:
        pos[0] += 1  # Step in the next spiral
        yield tuple(pos)
        for axis, offs in [(1, 1), (0, -1), (1, -1), (0, 1)]:
            while offs * pos[axis] < spiral:
                pos[axis] += offs
                yield tuple(pos)
        spiral += 1

def nbors(c):
    """Generate neighbors."""
    return [(c[0] + i, c[1] + j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

if __name__ == '__main__':
    # Memory location as input
    loc = 312051 

    # First problem
    spiral = int(loc ** 0.5) // 2 # Square root of number
    foo = [abs(x) for x in range(-spiral + 1, spiral + 1)]
    bar = range((2 * (spiral-1) + 1)**2 + 1, loc + 1)
    print(list(zip(cycle(foo), bar))[-1][0] + spiral)

    # Second problem
    grid = {(0, 0): 1}
    for c in spiral_coords():
        grid[c] = sum(grid.get(n, 0) for n in nbors(c))
        if grid[c] > loc:
            print(grid[c])
            break
