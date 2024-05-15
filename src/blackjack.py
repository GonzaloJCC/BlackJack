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
def printPlayers(playerAmmount, players):
    for i in range(0, playerAmmount):
        print(f"PLAYER {players[i].name}: ")
        players[i].show()
        print("")


#main
playerAmmount = 0
players = []
bets = [4]
resetDeckCount = 0
decks = []
dealer = Dealer()
while(playerAmmount < 1 or playerAmmount > 4):
    playerAmmount = int(input("Enter the ammount of players(1-4): "))
    

for i in range (0, playerAmmount):
    name = input(f"Enter the player {i+1} name: ")
    players.append(Player(name))
    bets.append(0)


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
        t.sleep(1)

    #Deal card 1 to players
    for i in range(0, playerAmmount):
        auxDeck = random.choice(decks)
        chosenCard = random.choice(auxDeck.deck)
        auxDeck.deck.remove(chosenCard)
        players[i].hand.append(chosenCard)
        players[i].show()
        t.sleep(1)
    cls()
    printPlayers(playerAmmount, players)
    


    #Deal card 1 to dealer
    auxDeck = random.choice(decks)
    chosenCard = random.choice(auxDeck.deck)
    auxDeck.deck.remove(chosenCard)
    dealer.hand.append(chosenCard)
    t.sleep(2)
    cls()
    dealer.showFirst()
    printPlayers(playerAmmount, players)
    t.sleep(2)
    cls()
    dealer.showFirst()

    #Deal card 2 to players
    for i in range(0, playerAmmount):
        auxDeck = random.choice(decks)
        chosenCard = random.choice(auxDeck.deck)
        auxDeck.deck.remove(chosenCard)
        players[i].hand.append(chosenCard)
        players[i].show()
    t.sleep(2)
    cls()
    dealer.showFirst()
    printPlayers(playerAmmount, players)

    #Deal card 2 to dealer
    auxDeck = random.choice(decks)
    chosenCard = random.choice(auxDeck.deck)
    auxDeck.deck.remove(chosenCard)
    dealer.hand.append(chosenCard)
    t.sleep(2)
    cls()
    dealer.showFirst()
    printPlayers(playerAmmount, players)
    
    t.sleep(70)
    