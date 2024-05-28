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
    dealer.showFirst()
    for i, player in enumerate(players):
        print(f"{player.name.upper()} (BET: {bets[i]}): ")
        player.show()
        print("")

#TODO: cambiar esta funcion a deal y añadirle como parametro un bool, si es true reparte al dealer si no no, eliminar dealDealer
def dealPlayers(players):
    cls()
    printPlayers(players, bets)
    for player in (players):
        auxDeck = random.choice(decks)
        chosenCard = random.choice(auxDeck.deck)
        auxDeck.deck.remove(chosenCard)
        player.hand.append(chosenCard)
        cls()
        printPlayers(players, bets)
        t.sleep(1.2)

def dealDealer(dealer, players, bets):        
    auxDeck = random.choice(decks)
    chosenCard = random.choice(auxDeck.deck)
    auxDeck.deck.remove(chosenCard)
    dealer.hand.append(chosenCard)
    cls()
    printPlayers(players, bets)
    t.sleep(1.2)

def dealerHasBlackJack():

    return True    
#main
playerAmmount = 0
players = []
bets = [4]
resetDeckCount = 0
decks = []
dealer = Dealer()

#TODO - make a menu BLACKJACK, press any key to start
# input("PRESS ANY KEY TO START: ")
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
    players.append(Player(name))
    bets.append(0)
while(1):
    


    if(resetDeckCount == 3):
        resetDeckCount = 0;
    if(resetDeckCount == 0):
        decks.clear()
        for i in range (0, 6):
            decks.append(Deck())
    cls()
    print("PLACE YOUR BETS")
    for i in range(playerAmmount):
            
        bet = int(input(f"PLAYER {players[i].name} ({players[i].chips} Chips), bet: "))
        bets[i] = (players[i].Bet(bet))
    cls()
    t.sleep(0.5)
        
    print("STARTING TO DEAL")
    t.sleep(2)
    cls()
    printPlayers(players, bets)
    t.sleep(1.2)

    #Deal card 1 to players
    dealPlayers(players)

    #Deal card 1 to dealer
    dealDealer(dealer, players, bets)
        
    #Deal card 2 to players
    dealPlayers(players)

    #Deal card 2 to dealer
    dealDealer(dealer, players, bets)
    #Now all the players and the dealer have 2 cards each

    #if dealer has BlackJack all the players without BJ will lose their bets and the ones with BJ will get their bet returned
    if dealerHasBlackJack():
        print(1)


    t.sleep(70)
    #after the round is finished you can choose to end the round or to play another
    decision = input("IF YOU DON'T WANT TO PLAY ANOTHER ROUND PRESS 'Q' TO EXIT, OTHERWISE PRESS ANY KEY: ")
    if decision.upper == 'q':
        print("GAME ENDED")
        t.sleep(700)

    