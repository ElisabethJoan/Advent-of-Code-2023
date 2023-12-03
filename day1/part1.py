def solution(inp):
    nums = [[char for char in line if char.isdigit()] for line in inp.split('\n')]
    combined = [int(num[0] + num[-1]) for num in nums]
    return sum(combined)

raw = open('input').read().rstrip()
print(solution(raw))
