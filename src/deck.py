import random
from typing import Tuple

def get_numerical_value(value) -> Tuple[int, int]:
    """
    Returns the numerical value(s) of a card based on its face value.
    For example:
        - "A" (Ace) returns (1, 11)
        - "J", "Q", "K" (Face cards) return (10, 10)
        - Numeric cards return their value as both elements of the tuple.
    :param value: The face value of the card as a string.
    :return: A tuple containing the numerical values of the card.
    """
    if value == "A":
        return 1, 11
    
    if value == "J" or value == "Q" or value == "K":
        return 10, 10
    
    aux = int(value)

    return aux, aux

# Class Card
class Card:
    """
    Represents a single playing card with a value, suit, and numerical value.
    """
    def __init__(self, value: str, suit: str, numerical_value: Tuple[int, int]):
        """
        Initializes a card with its value, suit, and numerical value.
        :param value: The face value of the card (e.g., "A", "2", "K").
        :param suit: The suit of the card (e.g., "♧", "♤", "♥", "♦").
        :param numerical_value: A tuple representing the numerical value(s) of the card.
        """
        self.value = value
        self.numericalValue = numerical_value
        self.suit = suit
        self.img = f"./assets/cards/{self.suit}/{self.value}.png"

    def __str__(self) -> str:
        """
        Returns a string representation of the card.
        :return: A string combining the card's value and suit (e.g., "A♧").
        """
        return f"{self.value}{self.suit}"


class Deck:
    """
    Represents a deck of 52 playing cards with methods to shuffle and draw cards.
    """
    def __init__(self):
        """
        Initializes a deck of 52 cards, one for each combination of value and suit.
        """
        suits = ["♧", "♤", "♥", "♦"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.deck = []  # The deck of cards

        for suit in suits:
            for value in values:
                numerical_value = get_numerical_value(value)
                card = Card(value, suit, numerical_value)
                self.deck.append(card)

    def __str__(self) -> str:
        """
        Returns a string representation of the entire deck.
        :return: A comma-separated string of all cards in the deck.
        """
        return ', '.join(str(card) for card in self.deck)

    def shuffle(self) -> None:
        """
        Shuffles the deck to randomize the order of the cards.
        :return: None
        """
        random.shuffle(self.deck)

    def take_card(self) -> Card:
        """
        Removes a card from the deck and returns it.
        If the deck is empty, returns a placeholder card with value: -1, suit: -1, numerical_value: (-1, -1).
        :return: The card taken from the deck, or a placeholder card if the deck is empty.
        """
        if not self.deck:
            return Card("-1", "-1", (-1, -1))
        return self.deck.pop()





