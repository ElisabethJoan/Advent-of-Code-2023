def solution(inp): 
    rankings = [[rank_hand(hand), int(bid)] for hand, bid in (line.split() for line in inp.split('\n'))]
   
    rankings.sort()

    total = 0
    for i in range(1, len(rankings) + 1):
        total += i * rankings[i - 1][1]

    return total

def rank_hand(hand):
    new_hand = hand
    if (any('J' == card for card in hand) and not all('J' == card for card in hand)):
        most_common = max(set(hand.replace('J', '')), key=hand.count)
        new_hand = hand.replace('J', most_common)
    
    unique_cards = list(set(new_hand))
    hand_size = len(unique_cards)
    hand_rank = None

    if (hand_size == 5):
        hand_rank = 1
    elif (hand_size == 4):
        hand_rank = 2
    elif (hand_size == 3):
        if(any([2 == new_hand.count(card) for card in unique_cards])):
            hand_rank = 3
        else:
            hand_rank = 4
    elif (hand_size == 2):
        if(any([3 == new_hand.count(card) for card in unique_cards])):
            hand_rank = 5
        else:
            hand_rank = 6
    else:
        hand_rank = 7

    card_ranks = [card_sort(card) for card in hand]
    
    return [hand_rank] + card_ranks

order = { v: i for i, v in enumerate(reversed('AKQT98765432J'), 2)}
def card_sort(card):
    return order[card]


raw = open('test').read().rstrip()
print(solution(raw)) 

