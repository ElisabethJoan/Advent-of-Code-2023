def solution(inp):
    maps = [line for line in inp.split('\n\n')]

    total = 0
    for current_map in maps:
        map_lists = [line for line in current_map.split('\n')]
        lines = find_reflection(map_lists)

        if (lines == 0):
            vertical = [''.join(line) for line in zip(*map_lists)]
            total += find_reflection(vertical) 
        else:
            total += (lines * 100)

    return total

def find_reflection(ash_map):
    row_count = len(ash_map)
    for i in range(1, row_count):
        reflection = True
        reflection_width = min(i, row_count - i)
        top = ash_map[i - reflection_width:i]
        bottom = ash_map[i:i + reflection_width][::-1]
        if any(top_c != bottom_c for top_c, bottom_c in zip(top, bottom)):
            reflection = False
            continue
        if reflection:
            return i

    return 0


raw = open('input').read().rstrip()
print(solution(raw))
