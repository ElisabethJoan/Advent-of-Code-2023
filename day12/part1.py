def solution(inp):
    lines = [line.split() for line in inp.split('\n')]
    condition_records = [(line[0], [int(x) for x in line[1].split(',')]) for line in lines]

    def dfs(cache, springs, damage, springdex, damage_index, op_springs):
        if (springdex, damage_index, op_springs) in cache:
            return cache[(springdex, damage_index, op_springs)]
        if springdex == len(springs):
            return ((damage_index == len(damage) and op_springs == 0) or
                    (damage_index == len(damage) - 1 and op_springs == damage[damage_index]))

        arrangements = 0
        if (springs[springdex] in ".?"):
            if (op_springs == 0):
                arrangements += dfs(cache, springs, damage, springdex + 1, damage_index, 0)
            elif (damage[damage_index] == op_springs):
                arrangements += dfs(cache, springs, damage, springdex + 1, damage_index + 1, 0)
        if (springs[springdex] in '#?' and damage_index < len(damage) and op_springs < damage[damage_index]): 
            arrangements += dfs(cache, springs, damage, springdex + 1, damage_index, op_springs + 1)
        
        cache[(springdex, damage_index, op_springs)] = arrangements
        return arrangements

    arrangement_sum = 0
    for springs, damage in condition_records:
        arrangement_sum += dfs({}, springs, damage, 0, 0, 0)
    return arrangement_sum

raw = open('input').read().rstrip()
print(solution(raw))
