import hearts_game.card_dictionaries as d
def naming(card):
    if card in d.card_names.keys():
        return (d.card_names[card])
    else:
        return ("error")

def has_a(hand, suite):
    has = False
    for card in hand:
        if card[0] == suite:
            has = True
    return has



def value(card):
    if card in d.card_value.keys():
        return (d.card_value[card])
    else:
        return ("error")

def score(card):
    if card in d.card_score.keys()\
            :
        return (d.card_score[card])
    else:
        return 0

deck = ["c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck", "ca", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk", "sa","d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk", "da","h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk", "ha",]

def prompt_question(prompt, valid_options):
    response = input(prompt)
    print(valid_options)
    while not response.lower() in valid_options:
        print("Sorry, I did not understand your choice.")
        print(response.lower())
        response = input(prompt)
    return response.lower()

def hand_contains(hand):
    x = prompt_question("would you like to know what cards you have?", ["yes", "no"])
    if x == "yes":
        for card in hand:
            y = naming(card)
            print(y)


def play_card(hand, player, led):
    global deck
    z = True
    while z:
        x = str(prompt_question("what card do you want to play?", deck))
        if x[0] == led:
            if x in hand:
                y = naming(x)
                print("player", player, "plays", y)
                z = False
                return x
            else:
                print("you don't have that card")
        else:
            if has_a(hand, led):
                print("must play a card of the lead suite, i.e.", d.lead[led])
            else:
                if x in hand:
                    y = naming(x)
                    print("player", player, "plays", y)
                    z = False
                    return x
                else:
                    print("you don't have that card")


def max_int_in_list(list):
    yet = True
    while yet:
        for integer in list:
            Blah = False
            for int in list:
                if abs(integer) < abs(int):
                     Blah = True
            if not Blah:
                yet = False
                z = integer
                return z
