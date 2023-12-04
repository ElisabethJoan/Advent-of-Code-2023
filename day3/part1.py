def solution(inp):
    lines = [line for line in inp.split('\n')]
    part_sum = 0;
    for i in range(len(lines)):
        j = 0
        while(j < len(lines[i])):
            if (lines[i][j].isdigit()):
                part_num = False
                counter = j + 1
                number = lines[i][j]
                while(counter < len(lines) and lines[i][counter].isdigit()):
                    number += lines[i][counter]
                    counter += 1
                
                for k in range(0, len(number) + 2):
                    if (j + k - 1 < len(lines[i])):
                        if (not lines[i - 1][j + k - 1].isalnum() 
                            and lines[i - 1][j + k - 1] != '.'):
                            part_num = True

                        if (i + 1 < len(lines)):
                            if (not lines[i + 1][j + k - 1].isalnum() 
                                and lines[i + 1][j + k - 1] != '.'):
                                part_num = True

                if (not lines[i][j - 1].isalnum() 
                    and lines[i][j - 1] != '.'):
                    part_num = True

                if (j + len(number) < len(lines[i])):
                    if (not lines[i][j + len(number)].isalnum() 
                        and lines[i][j + len(number)] != '.'):
                        part_num = True
                
                if (part_num):
                    part_sum += int(number)
                j += (counter - 1) - (counter - len(number))

            j += 1
                    
    return part_sum


raw = open('input').read().rstrip()
print(solution(raw))
