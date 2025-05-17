from src.const import *
from src.utils import exit_signal

class Person:
    def __init__(self):
        self.hand = []

    def show(self) -> None:
        """
        This function prints a person's hand.
        :return: None
        """
        for each in self.hand:
            print(each, end=" ")
        print("")

    def empty(self) -> None:
        """
        Flushes the person's hand.
        :return: None
        """
        self.hand.clear()

    def has_blackjack(self) -> bool:
        """
        Function used to check if this person has a blackjack.
        :return: True if the person has a blackjack, False otherwise.
        """
        if len(self.hand) != 2:
            return False
        return self.hand[0].numericalValue[1] + self.hand[1].numericalValue[1] == OBJECTIVE

    def get_score(self) -> int:
        """
        Gets this person's score.
        :return: The score of the person, or -1 if score > 21.
        """
        score = 0
        ace_count = 0

        if not self.hand:
            return 0

        for card in self.hand:
            value = card.numericalValue
            if value == (1, 11):
                ace_count += 1
            else:
                score += value[0]

        score += ace_count * 11

        while score > OBJECTIVE and ace_count > 0:
            score -= 10
            ace_count -= 1

        return score if score <= OBJECTIVE else BUSTED


class Player(Person):
    def __init__(self, name: str):
        super().__init__()
        self.chips = STARTING_CHIPS
        self.name = name

    def bet(self, amount) -> int:
        """
        This function allows a player to bet chips at the beginning of a round.
        :param amount: The quantity of chips the player wants to bet.
        :return: The amount of chips bet.
        """
        while amount > self.chips or amount < 1:
            print("You don't have enough chips to bet, enter a valid number")
            try:
                amount = round(float(input("Bet: ")), 2)
            except EOFError as _:
                exit_signal(1, "signal ctrl+D")

        # self.chips -= amount
        return amount


class Dealer(Person):
    def __init__(self):
        super().__init__()

    def show_first(self) -> None:
        """
        Prints the hand of the dealer, hiding the second card.
        :return: None
        """
        print("DEALER SCORE: ?")
        for i in range(len(self.hand)):
            if i == 1:
                print("[X]", end=" ")
            else:
                print(self.hand[i], end=" ")
        print("\n")


        
        