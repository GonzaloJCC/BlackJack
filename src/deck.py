import random

def getNumericalValue(value):
    if value == "A":
        return (1, 11)
    
    if value == "J" or value == "Q" or value == "K":
        return (10, 10)
    
    aux = int(value)

    return (aux, aux)

#class card
class Card:
    def __init__(self, value, suit, numericalValue):
        self.value = value
        self.suit = suit
        self.numericalValue = numericalValue

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
                numericalValue = getNumericalValue(value)
                card = Card(value, suit, numericalValue)
                self.deck.append(card)

    def __str__(self):
        return ', '.join(str(card) for card in self.deck)
    
    def shuffle(self):
        random.shuffle(self.deck)

    def takeCard(self):
        return self.deck.pop()





