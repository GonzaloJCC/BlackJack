from deck import *
from const import *


#TODO: crear clase padre de ambas

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

    def hasBlackjack(self):
        if len(self.hand) != 2:
            return False
        return (self.hand[0].numericalValue[1] + self.hand[1].numericalValue[1] == 21)
    
    def getScore(self):
        score = 0
        aces = []
        others = []

        if self.hand == []:
            return 0
        
        #filter the cards by ace or other
        for card in self.hand:
            if card.numericalValue[1] == 11:
                aces.append(card)
            else:
                others.append(card)
        
        for card in others:
            score += card.numericalValue[0]
            if score > OBJECTIVE:
                #busted
                return -1
            
        for card in aces:
            score += card.numericalValue[1] 
            if score >  OBJECTIVE:
                score -= card.numericalValue[1]
                if score > OBJECTIVE:
                    return -1
        
        return score


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
    
    def hasBlackjack(self):
        if len(self.hand) != 2:
            return False
        return (self.hand[0].numericalValue[1] + self.hand[1].numericalValue[1] == 21)
    
    def getScore(self):
        score = 0
        aces = []
        others = []

        if self.hand == []:
            return 0
        #filter the cards by ace or other
        for card in self.hand:
            if card.numericalValue[1] == 11:
                aces.append(card)
            else:
                others.append(card)
        
        for card in others:
            score += card.numericalValue[0]
            if score > OBJECTIVE:
                #busted
                return -1
            
        for card in aces:
            score += card.numericalValue[1] 
            if score >  OBJECTIVE:
                score -= card.numericalValue[1]
                if score > OBJECTIVE:
                    return -1
        return score
        


        
        