STARTING_CHIPS = 1000

#score dealer must stop (all 17)
DEALER_STOP = 17

#actions
HIT = "Hit"
DOUBLE = "Double"
SPLIT = "Split"
STAND = "Stand"


class Player:
    def __init__(self, name):
        self.hand = []
        self.chips = STARTING_CHIPS
        self.name = name

    def Bet(self, ammount):
        while(ammount > self.chips or ammount < 1):
            print("You don't have enough chips to bet, enter a valid number")
            ammount = int(input("Bet: "))

        self.chips-ammount
        return ammount
    def show(self):
        # print(f" PLAYER {self.name}:")
        for each in (self.hand):
            print(each, end = " ")
        print("")

    def empty(self):
        self.hand.clear



class Dealer:
    def __init__(self):
        self.hand = []
    
    def showFirst(self):
        print("DEALER")
        for i in range(0, len(self.hand)):
            if(i == 1):
                print("[X]", end= " ")
            else:
                print(self.hand[i], end = " ")
        print("\n")
    
    def empty(self):
        self.hand.clear

        
        