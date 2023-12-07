def solution(inp): 
    lines = [line.split(':')[1].strip().split() for line in inp.split('\n')]
    race = (int(''.join(lines[0])), int(''.join(lines[1])))

    prod = 1
    for i in range(race[0] + 1):
        hold = i
        if (hold * (race[0] - hold) > race[1]):
            diff = (race[0] - hold) - hold + 1
            prod *= diff
            break
    return prod

raw = open('input').read().rstrip()
print(solution(raw))
