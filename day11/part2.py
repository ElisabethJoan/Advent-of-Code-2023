def solution(inp):
    universe = [line for line in inp.split('\n')]
    horizontal_empties = expand_universe(universe)
    vertical_empties = expand_universe([''.join(line) for line in zip(*universe)])

    galaxies = []
    for y, line in enumerate(universe):
        for x in [i for i, ltr in enumerate(line) if ltr == '#']:
            y_crosses = 0
            for i in horizontal_empties:
                if (i < y):
                    y_crosses += 1
            x_crosses = 0
            for i in vertical_empties:
                if (i < x):
                    x_crosses += 1

            galaxies.append((x + (x_crosses * 999999), y + (y_crosses * 999999)))

    shortest_sum = 0
    galaxy_pairs = list(create_pairs(galaxies))
    for i, j in galaxy_pairs:
        manhattan_dist = abs(j[0] - i[0]) + abs(j[1] - i[1])
        shortest_sum += manhattan_dist

    return shortest_sum

def expand_universe(universe):
    empty_lines = []
    for index, line in enumerate(universe):
        if (all(char == line[0] for char in line)):
            empty_lines.append(index)

    return empty_lines

def create_pairs(l):
    for i, value in enumerate(l):
        for j in range(i + 1, len(l)):
            yield [value, l[j]]


raw = open('input').read().rstrip()
print(solution(raw))
