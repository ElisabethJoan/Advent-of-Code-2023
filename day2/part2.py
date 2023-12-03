
def solution(inp): 
    games = [[game.strip() for game in line.split(';')] for line in inp.split('\n')]
    sum_power = 0
    for game in games:
        game_max = { 'red': 0, 'green': 0, 'blue': 0 }
        id, game1 = game[0].split(': ')
        game[0] = int(id.split(' ')[1])
        game.insert(1, game1)
        for subgame in game[1:]:
            temp = [[pair for pair in score.split(' ')] for score in subgame.split(', ')]
            for hand in temp:
                if (int(hand[0]) > game_max[hand[1]]):
                    game_max[hand[1]] = int(hand[0])
       
        sum_power = sum_power + (game_max['red'] * game_max['green'] * game_max['blue'])

    return sum_power

raw = open('input').read().rstrip()
print(solution(raw))
