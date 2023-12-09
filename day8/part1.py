def solution(inp):
    lines = [line for line in inp.split('\n')]
    instructions = lines[0]
    mmap = {}
    for line in lines[2:]:
        temp = line.split(' = ')
        temp2 = temp[1].strip('()').split(', ')
        mmap['L' + temp[0]] = temp2[0]
        mmap['R' + temp[0]] = temp2[1]

    steps = 0
    index = 0
    current_location = 'AAA'
    while (current_location != 'ZZZ'):
        if (index == len(instructions)):
            index = 0
        
        instruction = instructions[index]
        current_location = mmap[instruction + current_location]
        steps += 1
        index += 1

    return steps

raw = open('input').read().rstrip()
print(solution(raw))
