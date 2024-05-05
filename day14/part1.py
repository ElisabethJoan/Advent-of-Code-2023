def solution(inp):
    lines = [''.join(line) for line in zip(*inp.split('\n'))]
    sorted_lines = []
    for line in lines:
        splits = line.split('#')
        new_order = ''
        for split in splits:
            temp = sorted(split, reverse=True)
            new_order = new_order + '#' + ''.join(temp)
        sorted_lines.append(new_order[1:])

    load = 0
    for line in sorted_lines:
        for i in range(len(line)):
            if (line[i] == 'O'):
                load += len(line) - i

    return load


raw = open('test').read().rstrip()
print(solution(raw))
