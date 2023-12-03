numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        }

def solution(inp):
    strings = [line for line in inp.split('\n')]
    digits = [[int(char) for char in line if char.isdigit()] for line in strings]
    combinations = []
    for string in strings:
        combination = []
        indexes = []
        for idx, char in enumerate(string):
            if (char.isdigit()):
                combination.append(char)
                indexes.append(idx)

        if (len(combination) == 1):
            combination.append(combination[0])
            indexes.append(indexes[0])

        if (len(combination) > 2):
            combination = [combination[0], combination[-1]]
        
        for number in numbers:
            f_index = string.find(number)
            l_index = string.rfind(number)
            if (f_index > -1):
                if (f_index < indexes[0]):
                    combination[0] = numbers[number]
                    indexes[0] = f_index
                if (f_index > indexes[-1]):
                    combination[-1] = numbers[number]
                    indexes[-1] = f_index

            if (l_index > -1):
                if (l_index < indexes[0]):
                    combination[0] = numbers[number]
                    indexes[0] = l_index
                if (l_index > indexes[-1]):
                    combination[-1] = numbers[number]
                    indexes[-1] = l_index

        combinations.append(combination)

    return sum([int(''.join(combination)) for combination in combinations])

raw = open('input').read().rstrip()
print(solution(raw))
