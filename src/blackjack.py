from person import *
class Table:
    def __init__(self):
        pass




#main
playerAmmount = 0
players = []
bets = [4]

while(playerAmmount < 1 or playerAmmount > 4):
    playerAmmount = int(input("Enter the ammount of players(1-4): "))
    

for i in range (0, playerAmmount):
    name = input(f"Enter the player {i+1} name: ")
    players.append(Player(name))
    bets.append(0)


while(1):
    print("PLACE YOUR BETS")
    for i in range(0, playerAmmount):
        
        bet = int(input(f"PLAYER {i+1}, bet: "))
        bets[i] = (players[i].Bet(bet))