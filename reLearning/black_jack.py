from random import randint


cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": [11, 1]
}


"""
====> Todo for today's evening
    - get default cards which will be drawn by default
    - get default cards which will be drawn for dealer
    - now append a single card in your list of cards 
    - if the total is less than 21 you can continue 
    - else quit
    - if you quit and the total of your card is less than dealers and his total is 21 or less
    - dealer wins
    ==> conditions
     1 - total your or dealer card should be 21 or less
     2 - you have a choice to quit in between and the total will be determined cards in your hand
    ==> Advance conditions are
     1 - cards drawn should be checked is valid or not like a pack of cards has 4 of each type of card
     2 - if you want to make more realistic than you have to check theirs colors too
"""


def black_jack():
    card_keys_list = list(cards.keys())
    card1 = cards[card_keys_list[randint(1, 13)]]
    card2 = cards[card_keys_list[randint(1, 13)]]
    default_cards = [card1, card2]
    print(default_cards)


black_jack()
