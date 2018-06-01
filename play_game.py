import hearts_game.my_utils as utils
import random


player_1 = str(input("What is your name player 1?"))
player_2 = str(input("What is your name player 2?"))
player_3 = str(input("What is your name player 3?"))
player_4 = str(input("What is your name player 4?"))

player_1_hand = []
player_1_score = 0
player_2_hand = []
player_2_score = 0
player_3_hand = []
player_3_score = 0
player_4_hand = []
player_4_score = 0

deck_2 = []
deck_2.extend(utils.deck)

w = 52
for i in range(13):
    random_num = random.randrange(w)
    player_1_hand.append(deck_2[random_num])
    del deck_2[random_num]
    w = w-1
    random_num = random.randrange(w)
    player_2_hand.append(deck_2[random_num])
    del deck_2[random_num]
    w = w-1
    random_num = random.randrange(w)
    player_3_hand.append(deck_2[random_num])
    del deck_2[random_num]
    w = w-1
    random_num = random.randrange(w)
    player_4_hand.append(deck_2[random_num])
    del deck_2[random_num]
    w = w-1

print(player_1, "'s hand is:")
for card in player_1_hand:
    y = utils.naming(card)
    print(y)
print(player_1, "'s score is", player_1_score)

print(player_2, "'s hand is:")
for card in player_2_hand:
    y = utils.naming(card)
    print(y)
print(player_2, "'s score is", player_2_score)

print(player_3, "'s hand is:")
for card in player_3_hand:
    y = utils.naming(card)
    print(y)
print(player_3, "'s score is", player_3_score)

print(player_4, "'s hand is:")
for card in player_4_hand:
    y = utils.naming(card)
    print(y)
print(player_4, "'s score is", player_4_score)
print(deck_2)
print(player_1_hand)
print(player_2_hand)
print(player_3_hand)
print(player_4_hand)

turn = 0
turn_hand = 0
leader = 0
x = 0
x_player = 0
f = 0
f_player = 0
y = 0
y_player = 0
z = 0
z_player = 0

if "c2" in player_1_hand:
    leader = player_1
    turn = player_1
    player_1_hand.remove("c2")
elif "c2" in player_2_hand:
    leader = player_2
    turn = player_2
    player_2_hand.remove("c2")
elif "c2" in player_3_hand:
    leader = player_3
    turn = player_3
    player_3_hand.remove("c2")
elif "c2" in player_4_hand:
    leader = player_4
    turn = player_4
    player_4_hand.remove("c2")
print(leader, "plays 2 of clubs")

if turn == player_1:
    g = utils.hand_contains(player_1_hand)
elif turn == player_2:
    g = utils.hand_contains(player_2_hand)
elif turn == player_3:
    g = utils.hand_contains(player_3_hand)
elif turn == player_4:
    g = utils.hand_contains(player_4_hand)
for k in range(12):
    print("\n")

f = turn
f_player = 0
played_cards = []
played_card_names = []
played_card_names.append("c2")
played_cards.append(2)
lead = "c"
for d in range(3):
    if turn == player_1:
        turn = player_2
        turn_hand = player_2_hand
    if turn == player_2:
        turn = player_3
        turn_hand = player_3_hand
    if turn == player_3:
        turn = player_4
        turn_hand = player_4_hand
    if turn == player_4:
        turn = player_1
        turn_hand = player_1_hand
    print("it's", turn, "'s turn")

    g = utils.hand_contains(turn_hand)

    played = utils.play_card(turn_hand, turn, lead)

    if turn_hand == player_1_hand:
        player_1_hand.remove(played)
    if turn_hand == player_2_hand:
        player_2_hand.remove(played)
    if turn_hand == player_3_hand:
        player_3_hand.remove(played)
    if turn_hand == player_4_hand:
        player_4_hand.remove(played)
    if not played[0] == lead:
        played_cards.append(0)
    else:
        played_cards.append(utils.value(played))
    played_card_names.append(played)
    if d == 0:
        x_player = 1
        x = turn
    if d == 1:
        y_player = 2
        y = turn
    if d == 2:
        z_player = 3
        z = turn

winner = utils.max_int_in_list(played_cards)

s = 0
if winner == played_cards[x_player]:
    leader = x
    for card in played_card_names:
        value = utils.score(card)
        s = s + value
        if x == player_1:
            player_1_score = player_1_score + s
        if x == player_2:
            player_2_score = player_2_score + s
        if x == player_3:
            player_3_score = player_3_score + s
        if x == player_4:
            player_4_score = player_4_score + s

if winner == played_cards[f_player]:
    leader = f
    for card in played_card_names:
        value = utils.score(card)
        s = s + value
        if f == player_1:
            player_1_score = player_1_score + s
        if f == player_2:
            player_2_score = player_2_score + s
        if f == player_3:
            player_3_score = player_3_score + s
        if f == player_4:
            player_4_score = player_4_score + s

if winner == played_cards[y_player]:
    leader = y
    for card in played_card_names:
        value = utils.score(card)
        s = s + value
        if y == player_1:
            player_1_score = player_1_score + s
        if y == player_2:
            player_2_score = player_2_score + s
        if y == player_3:
            player_3_score = player_3_score + s
        if y == player_4:
            player_4_score = player_4_score + s

if winner == played_cards[z_player]:
    leader = z
    for card in played_card_names:
        value = utils.score(card)
        s = s + value
        if z == player_1:
            player_1_score = player_1_score + s
        if z == player_2:
            player_2_score = player_2_score + s
        if z == player_3:
            player_3_score = player_3_score + s
        if z == player_4:
            player_4_score = player_4_score + s

print(player_1, "'s hand is:")
for card in player_1_hand:
    y = utils.naming(card)
    print(y)
print(player_1, "'s score is", player_1_score)

print(player_2, "'s hand is:")
for card in player_2_hand:
    y = utils.naming(card)
    print(y)
print(player_2, "'s score is", player_2_score)

print(player_3, "'s hand is:")
for card in player_3_hand:
    y = utils.naming(card)
    print(y)
print(player_3, "'s score is", player_3_score)

print(player_4, "'s hand is:")
for card in player_4_hand:
    y = utils.naming(card)
    print(y)
print(player_4, "'s score is", player_4_score)



#still has bugs, been play testing it  and fixing as I find mistakes, at the moment it's a single demo round
#once the round is working smoothly and securely the next step is to make a one round function
#there is a glitch in the prompt question of the play card, ask swett he was working on it with me but we didn't get it
