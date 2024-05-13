from deck import *

def test():
    deck = Deck()
    count = 0
    for i in deck.deck:
        print(i)
        count+=1

    print(count)


test()