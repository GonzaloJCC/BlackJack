from person import *
from deck import *
import random as r
import os
import time as t
from const import *
#TODO -  para imprimir score comprobar si es -1, en ese caso imprimir busted
class BlackJack:
    #TODO - cambiar listas players y bet a un diccionario player -> bet
    def __init__(self) -> None:
        self.playerAmmount = 0
        self.players = []
        self.bets = []
        self.resetDeckCount = 0
        self.decks = []
        self.dealer = Dealer()
    
    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def startGame(self):
        #NOTE - the user selects the  number of players
        while True:
            try:
                self.playerAmmount = int(input("Enter the amount of players (1-4): "))
                if self.playerAmmount < 1 or self.playerAmmount > 4:
                    raise ValueError("You must enter a number between 1 and 4, both included")
                break
            except ValueError as e:
                print("You must enter a number between 1 and 4, both included")

        #select player names
        for i in range (0, self.playerAmmount):
            name = input(f"Enter the player {i+1} name: ")
            self.players.append(Player(name))
            self.bets.append(0)

        #NOTE - every player makes the initial bet
        self.cls()
        print("PLACE YOUR BETS")
        for i in range(self.playerAmmount):
            while 1:
                try:
                    bet = int(input(f"PLAYER {self.players[i].name} ({self.players[i].chips} Chips), bet: "))
                    if(bet < 0 or bet > 9999999):
                        raise ValueError("You must enter a number")
                    break
                except ValueError as e:
                    print("You must enter a valid number, between 1 and the ammount of chips you have")

            self.bets[i] = (self.players[i].Bet(bet))
        self.cls()
        t.sleep(0.5)

        print("STARTING TO DEAL")
        t.sleep(2)
        self.cls()


    #cleans the player and dealer cards
    def endGame(self):
        dealerScore = self.dealer.getScore()
        # self.cls()
        for i, player in enumerate(self.players):
            playerScore = player.getScore()
            
            if player.hasBlackjack():
                if self.dealer.hasBlackjack():
                    player.chips += self.bets[i]
                    print(f"{player.name} wins 0")
                else:
                    player.chips += BLACKJACK_WIN_RATIO * self.bets[i]
                    print(f"{player.name} wins {BLACKJACK_WIN_RATIO * self.bets[i]}")

            elif self.dealer.hasBlackjack():
                #dealer wins
                print(f"{player.name} loses {self.bets[i]}")

            elif playerScore > dealerScore:
                player.chips += WIN_RATIO * self.bets[i]
                print(f"{player.name} wins {WIN_RATIO * self.bets[i]}")

            elif playerScore == dealerScore:
                player.chips += self.bets[i]
                print(f"{player.name} wins 0")
            
            else:
                #dealer wins
                print(f"{player.name} loses {self.bets[i]}")


            self.bets[i] = 0
    
    def printDealer(self):
        score = self.dealer.getScore()
        if score == -1:
            score = "BUSTED"
        print(f"DEALER SCORE: {score}: ")
        self.dealer.show()
        print("")
        


    def printPlayer(self, player, bet):
        score = player.getScore()
        if score == -1:
            score = "BUSTED"
        print(f"{player.name.upper()} (BET: {bet})  SCORE: {score}: ")
        player.show()
        print("")

    def printPlayers(self, players, bets):
        self.dealer.showFirst()
        for i, player in enumerate(players):
            self.printPlayer(player, bets[i])
            
            


    #recives true if the card is going to be dealed to the dealer or false if its going to be dealed to all players
    def deal(self, x: bool):
        if x == True:
            self.dealer.hand.append(self.takeCard())
            self.cls()
            self.printPlayers(self.players, self.bets)
            t.sleep(1.2)
            
            
        
        else:
            self.cls()
            self.printPlayers(self.players, self.bets)
            for player in (self.players):
                player.hand.append(self.takeCard())
                self.cls()
                self.printPlayers(self.players, self.bets)
                t.sleep(1.2)
                

    #DECK MANAGEMENT
    def randomDecks(self):
        if self.resetDeckCount == RESET_DECK_COUNT:
            self.resetDeckCount = 0;
        
        if self.resetDeckCount == 0:
            self.decks.clear()
            for i in range (0, NUMBER_OF_DECKS):
                self.decks.append(Deck())
            self.shuffle()
        self.cls()

    def shuffle(self):
        for deck in self.decks:
            deck.shuffle()

    def takeCard(self):
        card = Card("-1", "-1", -1)
        while card.numericalValue == -1:
            auxDeck = random.choice(self.decks)
            card = auxDeck.takeCard()
        return card
    
    def dealersTurn(self):
        score = self.dealer.getScore()

        bestPlayerScore = -1
        #get the best score without blackjack
        for player in self.players:
            if player.hasBlackjack():
                continue
            tempScore = player.getScore()
            if tempScore > bestPlayerScore:
                bestPlayerScore = tempScore

        #the dealer takes cards 
        while score < int(DEALER_STOP) and score != int(BUSTED) and score <= bestPlayerScore:
            
            self.cls()
            
            self.printDealer()
            self.dealer.hand.append(self.takeCard())
            for i, player in enumerate(self.players):
                print(f"{player.name.upper()} (BET: {self.bets[i]})  SCORE: {player.getScore()}: ")
                player.show()
                print("")

            score = self.dealer.getScore()
            t.sleep(1.2)

        #the final board is printed
        # t.sleep(1.2)
        self.cls()
        self.printDealer()
        for i, player in enumerate(self.players):
            print(f"{player.name.upper()} (BET: {self.bets[i]})  SCORE: {player.getScore()}: ")
            player.show()
            print("")
        t.sleep(4)
        # self.cls()



    #TODO - make a menu BLACKJACK, press any key to start
    # input("PRESS ANY KEY TO START: ")
    def gameLoop(self):
        
        self.startGame()

        while(1):

            #the decks are shuffled and initialized
            self.randomDecks()

            #prints the table status
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
            if self.dealer.hasBlackjack():
                print("DEALER HAS BLACKJACK")
                self.endGame()
                t.seep(700)

            self.dealersTurn()
            self.endGame()




            t.sleep(70)
            #after the round is finished you can choose to end the round or to play another
            decision = input("IF YOU DON'T WANT TO PLAY ANOTHER ROUND PRESS 'Q' TO EXIT, OTHERWISE PRESS ANY KEY: ")
            if decision.upper() == 'Q':
                print("GAME ENDED")
                t.sleep(700)

    