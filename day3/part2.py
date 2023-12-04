
def solution(inp):
    lines = [line for line in inp.split('\n')]
    gear_sum = 0;
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (lines[i][j] == '*'):
                numbers = set()
                for k in range(-1, 2):
                    if (lines[i + 1][j + k].isdigit()): 
                        numbers.add(num_width(lines, i + 1, j, k))

                    if (lines[i - 1][j + k].isdigit()):
                        numbers.add(num_width(lines, i - 1, j, k))

                if (lines[i][j - 1].isdigit()):
                    numbers.add(num_width(lines, i, j, -1))

                if (lines[i][j + 1].isdigit()):
                    numbers.add(num_width(lines, i, j, 1))

                if (len(numbers) == 2):
                    numbers = list(numbers)
                    gear_sum += numbers[0] * numbers[1]

    return gear_sum

def num_width(lines, i, j, k):
    c = ''
    l_index = 0
    while (c != '.'):
        c = lines[i][j + k - l_index]
        if (not c.isdigit()):
            break
        l_index += 1
    number = ''
    c = ''
    index = 1
    while (c != '.'):
        if (j + k + index - l_index > len(lines[i - 1]) - 1):
            break
        c = lines[i][j + k + index - l_index]
        if (not c.isdigit()):
            break
        number += c 
        index += 1
   
    return int(number)

raw = open('input').read().rstrip()
print(solution(raw))
