f = open('aoc22.txt','r')
problem_input = []
for line in f:
    problem_input += [line[:-1]]
f.close()
p1 = []
p2 = []
end_p1 = 0
for x in range(1,len(problem_input)):
    if problem_input[x] == '':
        end_p1 = x
        break
    p1 += [int(problem_input[x])]
for x in range(end_p1 + 2, len(problem_input)):
    p2 += [int(problem_input[x])]
current_round = 1
while True:
    p1_card = p1.pop(0)
    p2_card = p2.pop(0)
    if p1_card > p2_card:
        p1 += [p1_card]
        p1 += [p2_card]
    else:
        p2 += [p2_card]
        p2 += [p1_card]
    if len(p1) == 0 or len(p2) == 0:
        break
    current_round += 1
if len(p1) == 0:
    winning_deck = p2[:]
else:
    winning_deck = p1[:]
multiplier = len(winning_deck)
score = 0
for card in winning_deck:
    score += multiplier * card
    multiplier -= 1
print('Part 1:')
print('Winning score is ' + str(score))
game_number = 0

def play_game(deck1, deck2):
    p1_decklist = [deck1[:]]
    p2_decklist = [deck2[:]]
    global game_number
    game_number += 1
    game_round = 0
    while True:
        game_round += 1
        if len(deck1) == 0:
            winner = (deck1, deck2, 2)
            game_number -= 1
            return winner
        elif len(deck2) == 0:
            winner = (deck1, deck2, 1)
            game_number -= 1
            return winner
        if len(p1_decklist) > 1:
            if deck1 in p1_decklist[:-1] and deck2 in p2_decklist[:-1]:
                winner = (deck1, deck2, 1)
                game_number -= 1
                return winner        
        
        p1_card = deck1.pop(0)
        p2_card = deck2.pop(0)
        if len(deck1) >= p1_card and len(deck2) >= p2_card:
            new_deck1 = deck1[:p1_card]
            new_deck2 = deck2[:p2_card]
            subgame_winner = play_game(new_deck1, new_deck2)

            if subgame_winner[2] == 1:
                deck1 += [p1_card]
                deck1 += [p2_card]
            else:
                deck2 += [p2_card]
                deck2 += [p1_card]
        else:
            if p1_card > p2_card:
                deck1 += [p1_card]
                deck1 += [p2_card]
            else:
                deck2 += [p2_card]
                deck2 += [p1_card]
        p1_decklist += [deck1[:]]
        p2_decklist += [deck2[:]]
    return winner
p1 = []
p2 = []
end_p1 = 0
for x in range(1,len(problem_input)):
    if problem_input[x] == '':
        end_p1 = x
        break
    p1 += [int(problem_input[x])]
for x in range(end_p1 + 2, len(problem_input)):
    p2 += [int(problem_input[x])]
game_result = play_game(p1, p2)
if game_result[2] == 1:
    winning_deck = game_result[0]
else:
    winning_deck = game_result[1]
multiplier = len(winning_deck)
score = 0
for card in winning_deck:
    score += multiplier * card
    multiplier -= 1
print('Part 2:')
print('Winning score is ' + str(score))


