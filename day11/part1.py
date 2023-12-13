def solution(inp):
    horizontal = [line for line in inp.split('\n')]
    horizontal = expand_universe(horizontal)
    vertical = [''.join(line) for line in zip(*horizontal)]
    vertical = expand_universe(vertical)
    expanded_universe = [''.join(line) for line in zip(*vertical)]

    galaxies = []
    for y, line in enumerate(expanded_universe):
        for x in [i for i, ltr in enumerate(line) if ltr == '#']:
            galaxies.append((x, y))

    shortest_sum = 0
    galaxy_pairs = list(create_pairs(galaxies, 2))
    for i, j in galaxy_pairs:
        manhattan_dist = abs(j[0] - i[0]) + abs(j[1] - i[1])
        shortest_sum += manhattan_dist

    return shortest_sum

def expand_universe(universe):
    skip = False
    for index, line in enumerate(universe):
        if (skip):
            skip = False
            continue
        if (all(char == line[0] for char in line)):
            universe.insert(index, '.' * len(line))
            skip = True

    return universe

def create_pairs(l):
    for i, value in enumerate(l):
        for j in range(i + 1, len(l)):
            yield [value, l[j]]


raw = open('input').read().rstrip()
print(solution(raw))
