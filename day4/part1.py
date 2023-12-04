def solution(inp): 
    lines = [line.split(':')[1] for line in inp.split('\n')]
    cards = [[y.strip() for y in x.split('|')] for x in lines]
    cards = [[{z for z in y.split()} for y in x] for x in cards]
    
    total = len(cards[0][1])
    points = 0

    for card in cards:
        matches = total - len(card[1] - card[0])
        if (matches == 0):
            continue
        points += 2 ** (matches - 1)

    return points

raw = open('input').read().rstrip()
print(solution(raw))
