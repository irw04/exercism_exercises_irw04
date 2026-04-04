"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card.upper() in ["K", "Q", "J"]:
        return 10
    elif card.upper() in 'A':
        return 1
    elif card.upper() == "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10":
        return int(card)
    else: 
        return "invalid response"
        

def higher_card(card_one, card_two):
    card1 = value_of_card(card_one)
    card2 = value_of_card(card_two)
    
    if card1 > card2: 
        return str(card1)
    elif card1 < card2:
        return str(card2)
    elif card1 == card2:
        return str(card_one), str(card_two)


def value_of_ace(card_one, card_two):
    if card_one == "A":
        card1 = 11
    else:
        card1 = value_of_card(card_one)
    if card_two == "A":
        card2 = 11
    else:
        card2 = value_of_card(card_two)
    
    if card1 + card2 <= 10:
        return 11
    elif card1 + card2 == 10:
        return 11
    else: 
        return 1
    

def is_blackjack(card_one, card_two):
    if card_one == "A":
        card1 = 11
    else:
        card1 = value_of_card(card_one)
    if card_two == "A":
        card2 = 11
    else:
        card2 = value_of_card(card_two)
    
    if card1 + card2 == 21:
        return True
    else: 
        return False
def can_split_pairs(card_one, card_two):
    if card_one == "A":
        card1 = 11
    else:
        card1 = value_of_card(card_one)
    if card_two == "A":
        card2 = 11
    else:
        card2 = value_of_card(card_two)

    if card1 == card2:
        return True 
    else:
        return False
        
def can_double_down(card_one, card_two):
    card1 = value_of_card(card_one)
    card2 = value_of_card(card_two)

    if card1 + card2 == 9 or card1 + card2 == 10 or card1 + card2 == 11:
        return True
    else:
        return False
    
