from person import *
from deck import *
import random as r
import os
import time as t

class blackJack:

    def __init__(self) -> None:
        self.playerAmmount = 0
        self.players = []
        self.bets = [4]
        self.resetDeckCount = 0
        self.decks = []
        self.dealer = Dealer()
        
    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    #cleans the player and dealer cards
    def end():
        pass
    def printPlayers(self, players, bets):
        self.dealer.showFirst()
        for i, player in enumerate(players):
            print(f"{player.name.upper()} (BET: {bets[i]}): ")
            player.show()
            print("")

    #recives true if the card is going to be dealed to the dealer or false if its going to be dealed to all players
    def deal(self, x: bool):
        if x == True:
            auxDeck = random.choice(self.decks)
            chosenCard = random.choice(auxDeck.deck)
            auxDeck.deck.remove(chosenCard)
            self.dealer.hand.append(chosenCard)
            self.cls()
            self.printPlayers(self.players, self.bets)
            t.sleep(1.2)
        
        else:
            self.cls()
            self.printPlayers(self.players, self.bets)
            for player in (self.players):
                auxDeck = random.choice(self.decks)
                chosenCard = random.choice(auxDeck.deck)
                auxDeck.deck.remove(chosenCard)
                player.hand.append(chosenCard)
                self.cls()
                self.printPlayers(self.players, self.bets)
                t.sleep(1.2)


    #TODO esta funcion debertia ir en dealer
    def dealerHasBlackJack(self):
        return True    
    #main
    #TODO - make a menu BLACKJACK, press any key to start
    # input("PRESS ANY KEY TO START: ")

    def gameLoop(self):
        while True:
            try:
                playerAmmount = int(input("Enter the amount of players (1-4): "))
                if playerAmmount < 1 or playerAmmount > 4:
                    raise ValueError("You must enter a number between 1 and 4, both included")
                break
            except ValueError as e:
                print("You must enter a number between 1 and 4, both included")


        for i in range (0, playerAmmount):
            name = input(f"Enter the player {i+1} name: ")
            self.players.append(Player(name))
            self.bets.append(0)
        while(1):
            


            if(self.resetDeckCount == 3):
                self.resetDeckCount = 0;
            if(self.resetDeckCount == 0):
                self.decks.clear()
                for i in range (0, 6):
                    self.decks.append(Deck())
            self.cls()
            print("PLACE YOUR BETS")
            for i in range(playerAmmount):
                    
                bet = int(input(f"PLAYER {self.players[i].name} ({self.players[i].chips} Chips), bet: "))
                self.bets[i] = (self.players[i].Bet(bet))
            self.cls()
            t.sleep(0.5)
                
            print("STARTING TO DEAL")
            t.sleep(2)
            self.cls()
            self.printPlayers(self.players, self.bets)
            t.sleep(1.2)

            #Deal card 1 to players
            self.deal(False)

            #Deal card 1 to dealer
            self.deal(True)
                
            #Deal card 2 to players
            self.deal(False)

            #Deal card 2 to dealer
            self.deal(True)
            #Now all the players and the dealer have 2 cards each

            #if dealer has BlackJack all the players without BJ will lose their bets and the ones with BJ will get their bet returned
            if self.dealerHasBlackJack():
                print(1)


            t.sleep(70)
            #after the round is finished you can choose to end the round or to play another
            decision = input("IF YOU DON'T WANT TO PLAY ANOTHER ROUND PRESS 'Q' TO EXIT, OTHERWISE PRESS ANY KEY: ")
            if decision.upper == 'q':
                print("GAME ENDED")
                t.sleep(700)

    