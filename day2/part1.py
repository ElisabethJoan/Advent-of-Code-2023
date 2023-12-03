red = 12
green = 13
blue = 14

def solution(inp): 
    games = [[game.strip() for game in line.split(';')] for line in inp.split('\n')]
    sum_ids = 0
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
       
        if (game_max['red'] <= red and game_max['green'] <= green and game_max['blue'] <= blue):
            sum_ids = sum_ids + game[0]

    return sum_ids

raw = open('input').read().rstrip()
print(solution(raw))
