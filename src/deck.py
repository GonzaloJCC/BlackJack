import random
from typing import Tuple

def get_numerical_value(value) -> Tuple[int, int]:
    if value == "A":
        return 1, 11
    
    if value == "J" or value == "Q" or value == "K":
        return 10, 10
    
    aux = int(value)

    return aux, aux

#class card
class Card:
    def __init__(self, value: str, suit: str, numerical_value: Tuple[int, int]):
        self.value = value
        self.numericalValue = numerical_value
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.value}{self.suit}"


#class deck, stores 52 different cards and has different methods required to play games
class Deck:
    def __init__(self):
        suits = ["♧", "♤", "♥", "♦"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.deck = []  #the deck of cards

        for suit in suits:
            for value in values:
                numerical_value = get_numerical_value(value)
                card = Card(value, suit, numerical_value)
                self.deck.append(card)

    def __str__(self) -> str:
        return ', '.join(str(card) for card in self.deck)

    def shuffle(self) -> None:
        """
        Shuffles the deck.
        :return: None
        """
        random.shuffle(self.deck)

    #If there are no cards left we return the card -1 -1 -1
    def take_card(self) -> Card:
        """
        Removes a card from the deck and returns it..
        :return: The card taken, or a card with value: -1, suit: -1, numerical_value: (-1, -1)
                 if there are no cards left.
        """
        if not self.deck:
            return Card("-1", "-1", (-1,-1))
        return self.deck.pop()





