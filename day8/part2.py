def solution(inp):
    lines = [line for line in inp.split('\n')]
    instructions = lines[0]
    start_locations = []
    mmap = {}
    for line in lines[2:]:
        temp = line.split(' = ')
        temp2 = temp[1].strip('()').split(', ')
        mmap['L' + temp[0]] = temp2[0]
        mmap['R' + temp[0]] = temp2[1]
        if (temp[0][-1] == 'A'):
            start_locations.append(temp[0])

    step_counts = []
    for location in start_locations:
        steps = 0
        index = 0
        current_location = location
        while (current_location[-1] != 'Z'):
            if (index == len(instructions)):
                index = 0
            
            instruction = instructions[index]
            current_location = mmap[instruction + current_location]
            steps += 1
            index += 1
        
        step_counts.append(steps)

    lcm = 1
    for step in step_counts:
        lcm = lcm * step // gcd(lcm, step)

    return lcm

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


raw = open('input').read().rstrip()
print(solution(raw))


# Attemp 1 - it was worth a try :^)
# def solution(inp):
#     lines = [line for line in inp.split('\n')]
#     instructions = lines[0]
#     current_locations = []
#     mmap = {}
#     for line in lines[2:]:
#         temp = line.split(' = ')
#         temp2 = temp[1].strip('()').split(', ')
#         mmap['L' + temp[0]] = temp2[0]
#         mmap['R' + temp[0]] = temp2[1]
#         if (temp[0][-1] == 'A'):
#             current_locations.append(temp[0])
#
#     steps = 0
#     index = 0
#     while (any('Z' != x[-1] for x in current_locations)):
#         if (index == len(instructions)):
#             index = 0
# 
#         for i in range(len(current_locations)):
#             instruction = instructions[index]
#             current_locations[i] = mmap[instruction + current_locations[i]]
#         
#         steps += 1
#         index += 1
# 
#     return counter * overflow 
