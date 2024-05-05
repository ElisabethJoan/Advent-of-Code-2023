def solution(inp):
    grid = [list(l) for l in inp.split('\n')]

    count = 0
    cache = {}
    skip = False
    target = 1000000000
    while count < target:
        grid = cycle(grid)
        state = str(grid)
        count += 1
        if not skip and state in cache:
            period = count - cache[state]
            count += ((target - count) // period) * period
            skip = True
        cache[state] = count
 
    load = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                load += len(grid) - i
    
    return load

def cycle(grid):
    for i in range(4):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 'O':
                    ny = y
                    grid[ny][x] = '.'
                    while ny >= 0 and grid[ny][x] == '.':
                        ny-=1
                    grid[ny+1][x] = 'O'
        grid = list(map(list,zip(*grid[::-1])))  
    return grid


raw = open('input').read().rstrip()
print(solution(raw))
