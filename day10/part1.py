pipes = {
        'L': ((0, -1), (1, 0)),
        'J': ((0, -1), (-1, 0)),
        '7': ((0, 1), (-1, 0)),
        'F': ((0, 1), (1, 0)),
        '|': ((0, 1), (0, -1)),
        '-': ((-1, 0), (1, 0))
    }

directions = [
        (0, 1),
        (0, -1),
        (-1, 0),
        (1, 0),
    ]

def solution(inp):
    lines = [line for line in inp.split('\n')]

    grid = {}
    start = None
    for y, row in enumerate(lines):
        for x, symbol in enumerate(row):
            grid[(x, y)] = symbol
            if (symbol == 'S'):
                start = (x, y)

    start_symbol = find_start_pipe(start, grid)
    grid[start] = start_symbol

    current_pipe = add_tuples(start, pipes[grid[start]][0])
    prev_pipe = start
    path_length = 1
    while (current_pipe != start):
        for connection in pipes[grid[current_pipe]]:
            if (add_tuples(current_pipe, connection) != prev_pipe):
                prev_pipe = current_pipe
                current_pipe = add_tuples(current_pipe, connection)
                break
        path_length += 1

    return path_length // 2


def find_start_pipe(coordinates, grid):
    connections = []
    for direction in directions:
        start_neighbour = add_tuples(coordinates, direction)
        if (start_neighbour in grid and grid[start_neighbour] in pipes):
            for connection in pipes[grid[start_neighbour]]:
                if (add_tuples(start_neighbour, connection) == coordinates):
                    connections.append(direction)

    for pipe, valid_connections in pipes.items():
        if (tuple(connections) == valid_connections or tuple(reversed(connections)) == valid_connections):
            return pipe

def add_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

raw = open('input').read().rstrip()
print(solution(raw))
