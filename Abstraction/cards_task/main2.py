import random

class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = self.create_deck()

    def create_deck(self):
        deck_list = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                deck_list.append((suit, rank))
        print(deck_list)
        return deck_list

deck = DeckOfCards()
