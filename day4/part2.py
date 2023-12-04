def solution(inp): 
    lines = [line.split(':')[1] for line in inp.split('\n')]
    cards = [[y.strip() for y in x.split('|')] for x in lines]
    cards = [[{z for z in y.split()} for y in x] for x in cards]
    
    total = len(cards[0][1])
    points = 0

    def play_games(winners, index):
        nonlocal points
        for i in range(index + 1, index + winners + 1):
            matches = total - len(cards[i][1] - cards[i][0]) 
            points += 1
            if (matches > 0):
                play_games(matches, i)
    
    play_games(len(cards), -1)

    return points

raw = open('input').read().rstrip()
print(solution(raw))
