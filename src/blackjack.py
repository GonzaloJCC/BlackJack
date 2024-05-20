from person import *
from deck import *
import random as r
import os
import time as t

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

#cleans the player and dealer cards
def end():
    pass
def printPlayers(players, bets):
    for i, player in enumerate(players):
        print(f"{player.name.upper()} (BET: {bets[i]}): ")
        player.show()
        print("")
def dealPlayers(players):
    for player in (players):
        auxDeck = random.choice(decks)
        chosenCard = random.choice(auxDeck.deck)
        auxDeck.deck.remove(chosenCard)
        player.hand.append(chosenCard)
        cls()
        dealer.showFirst()
        printPlayers(players, bets)
        t.sleep(1.2)

def dealDealer(dealer, players, bets):        
    auxDeck = random.choice(decks)
    chosenCard = random.choice(auxDeck.deck)
    auxDeck.deck.remove(chosenCard)
    dealer.hand.append(chosenCard)
    t.sleep(1.2)
    cls()
    dealer.showFirst()
    printPlayers(players, bets)
    t.sleep(1.2)
#main
playerAmmount = 0
players = []
bets = [4]
resetDeckCount = 0
decks = []
dealer = Dealer()

#TODO - make a menu BLACKJACK, press any key to start

while(playerAmmount < 1 or playerAmmount > 4):
    playerAmmount = int(input("Enter the ammount of players(1-4): "))
    

for i in range (0, playerAmmount):
    name = input(f"Enter the player {i+1} name: ")
    players.append(Player(name))
    bets.append(0)

#TODO - make functions for the deal loops
#TODO - cambiar for loops por for i, player in enumerate(players):
while(1):
    if(resetDeckCount == 3):
        resetDeckCount = 0;
    if(resetDeckCount == 0):
        decks.clear()
        for i in range (0, 6):
            decks.append(Deck())

    print("PLACE YOUR BETS")
    for i in range(0, playerAmmount):
        
        bet = int(input(f"PLAYER {players[i].name}, bet: "))
        bets[i] = (players[i].Bet(bet))
    
    t.sleep(0.5)
    cls()
    print("STARTING TO DEAL")
    t.sleep(2)

    cls()
    #Deal card 1 to players
    dealPlayers(players)

    #Deal card 1 to dealer
    dealDealer(dealer, players, bets)
    
    #Deal card 2 to players
    dealPlayers(players)

    #Deal card 2 to dealer
    dealDealer(dealer, players, bets)
    
    t.sleep(70)
    