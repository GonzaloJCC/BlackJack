import random



#class card
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value}{self.suit}"


#class deck, stores 52 different cards and has different methods required to play games
class Deck:
    def __init__(self):
        suits = ["♧", "♤", "♥", "♦"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.deck = []  #the deck of cards

        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.deck.append(card)
        
    def shuffle(self):
        pass
    def deal(self):

        pass






