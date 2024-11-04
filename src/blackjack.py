from person import *
from deck import *
import os
import time as t
from const import *
from utils import exit_signal


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class BlackJack:
    def __init__(self) -> None:
        self.player_amount: int = 0
        self.players: list[Player] = []
        self.bets: list[float] = []
        self.resetDeckCount: int = 0
        self.decks: list[Deck] = []
        self.dealer: Dealer = Dealer()

    def initial_bets(self):
        print("PLACE YOUR BETS")
        for i in range(len(self.players)):
            while 1:
                try:
                    bet = int(input(f"PLAYER {self.players[i].name.upper()} ({self.players[i].chips} Chips), bet: "))
                    if bet < 0 or bet > self.players[i].chips:
                        raise ValueError("")
                    break
                except ValueError as _:
                    print("You must enter a valid number, "
                          "between 1 and the amount of chips you have")
                except EOFError as _:
                    exit_signal(1, "signal ctrl+D")

            self.bets[i] = (self.players[i].bet(bet))
        cls()
        t.sleep(0.5)

        print("STARTING TO DEAL")
        t.sleep(2)
        cls()

    def start_game(self) -> None:
        #the user selects the number of players
        while True:
            try:
                self.player_amount = int(input("Enter the amount of players (1-4): "))
                if self.player_amount < 1 or self.player_amount > 4:
                    raise ValueError("")
                break
            except ValueError as _:
                print("You must enter a number between 1 and 4, both included")
            except EOFError as _:
                exit_signal(1, "signal ctrl+D")

        #select player names
        for i in range (0, self.player_amount):
            names = []
            for player in self.players:
                names.append(player.name)

            x = 0
            name = ""
            while x == 0:
                try:
                    name = input(f"Enter the player {i+1} name: ")
                except EOFError as _:
                    exit_signal(1, "signal ctrl+D")
                
                if name in names:
                    print("NAMES MUST BE UNIQUE, PICK ANOTHER NAME")
                else:
                    x = 1
                    
            self.players.append(Player(name))
            self.bets.append(0)

        #every player makes the initial bet
        cls()

    #cleans the player and dealer cards
    def end_game(self) -> None:
        dealer_score = self.dealer.get_score()

        for i, player in enumerate(self.players):
            player_score = player.get_score()
            
            if player_score == BUSTED:
                print(f"{player.name.upper()} loses {self.bets[i]}")

            elif player.has_blackjack():
                if self.dealer.has_blackjack():
                    player.chips += self.bets[i]
                    print(f"{player.name.upper()} wins 0")
                else:
                    player.chips += BLACKJACK_WIN_RATIO * self.bets[i]
                    print(f"{player.name} wins {BLACKJACK_WIN_RATIO * self.bets[i]}")

            elif self.dealer.has_blackjack():
                #dealer wins
                print(f"{player.name.upper()} loses {self.bets[i]}")

            elif player_score > dealer_score:
                player.chips += WIN_RATIO * self.bets[i]
                print(f"{player.name.upper()} wins {WIN_RATIO * self.bets[i]}")

            elif player_score == dealer_score:
                player.chips += self.bets[i]
                print(f"{player.name.upper()} wins 0")
            
            else:
                #dealer wins
                print(f"{player.name.upper()} loses {self.bets[i]}")

            
        print("")
        t.sleep(1.2)
        aux = []
        for player in self.players:
            print(f"{player.name.upper()}'S CHIPS: {player.chips}")
            self.bets[i] = 0
            player.hand = []
            if player.chips <= 0:
                print(f"{player.name.upper()} HAS 0 CHIPS, HE CAN NO LONGER PLAY")
            else:
                aux.append(player)
            print("")
            
        self.players = aux
        self.dealer.hand = []
        
        

    
    def print_dealer(self) -> None:
        score = self.dealer.get_score()
        if score == BUSTED:
            score = "BUSTED"
        print(f"DEALER SCORE: {score}: ")
        self.dealer.show()
        print("")



    def print_player(self, player: Player, bet: float) -> None:
        score = player.get_score()
        if score == BUSTED:
            score = "BUSTED"
        print(f"{player.name.upper()} (BET: {bet})  SCORE: {score}: ")
        player.show()
        print("")

    def print_players(self, players: list[Player], bets: list[float]):
        self.dealer.show_first()
        for i, player in enumerate(players):
            self.print_player(player, bets[i])
            
            


    #recives true if the card is going to be dealt to the dealer or false if isn't
    # going to be dealt to all players
    def deal(self, x: bool) -> None:
        if x is True:
            self.dealer.hand.append(self.take_card())
            cls()
            self.print_players(self.players, self.bets)
            t.sleep(1.2)
            
            
        
        else:
            cls()
            self.print_players(self.players, self.bets)
            for player in self.players:
                player.hand.append(self.take_card())
                cls()
                self.print_players(self.players, self.bets)
                t.sleep(1.2)
                

    #DECK MANAGEMENT
    def random_decks(self) -> None:
        if self.resetDeckCount == RESET_DECK_COUNT:
            self.resetDeckCount = 0

        if self.resetDeckCount == 0:
            self.decks.clear()
            for i in range (0, NUMBER_OF_DECKS):
                self.decks.append(Deck())
            self.shuffle()
        cls()

    def shuffle(self) -> None:
        for deck in self.decks:
            deck.shuffle()

    def take_card(self) -> None:
        card = Card("-1", "-1", (-1,-1))
        while card.numericalValue == (-1, -1):
            aux_deck = random.choice(self.decks)
            card = aux_deck.take_card()
        return card
    
    def dealers_turn(self) -> None:
        score = self.dealer.get_score()

        best_player_score = -1
        #get the best score without blackjack
        for player in self.players:
            if player.has_blackjack():
                continue
            temp_score = player.get_score()
            if temp_score > best_player_score:
                best_player_score = temp_score

        #the dealer takes cards 
        while score < int(DEALER_STOP) and score != int(BUSTED) \
            and score <= best_player_score:
            
            cls()
            
            self.print_dealer()
            self.dealer.hand.append(self.take_card())
            for i, player in enumerate(self.players):
                self.print_player(player, self.bets[i])

            score = self.dealer.get_score()
            t.sleep(1.2)

        #the final board is printed
        # t.sleep(1.2)
        cls()
        self.print_dealer()
        for i, player in enumerate(self.players):
            self.print_player(player, self.bets[i])
        t.sleep(4)
        # self.cls()


    def choose_move(self, player: Player, bet: float) -> None:
        can_double = True
        while player.get_score() <= int(OBJECTIVE) \
            and player.get_score() != int(BUSTED):

            decision = 0
            while decision not in [HIT, DOUBLE, SPLIT, STAND]:
                try:
                    print(f"{player.name.upper()} choose your action: ")
                    decision = int(input(f"\
                                        \n\tHIT:    {HIT}\
                                        \n\tDOUBLE: {DOUBLE}\
                                        \n\tSPLIT:  {SPLIT}\
                                        \n\tSTAND:  {STAND}\
                                        \n\tACTION ({player.name.upper()}): "))
                    if decision not in [HIT, DOUBLE, SPLIT, STAND]:
                        raise ValueError
                except ValueError:
                    print("YOU MUST ENTER A NUMBER BETWEEN 1 AND 4")
                except EOFError as _:
                    exit_signal(1, "signal ctrl+D")

            if decision == HIT:
                player.hand.append(self.take_card())
                can_double = False

            elif decision == DOUBLE:
                
                if can_double is False:
                    print("\nYOU CAN NOT DOUBLE AFTER A HIT OR A SPLIT")
                    t.sleep(2)
                    cls()
                    self.print_players(self.players, self.bets)
                    continue

                if player.chips < bet:
                    print("NOT ENOUGH CHIPS")
                    t.sleep(1.2)
                    cls()
                    self.print_players(self.players, self.bets)
                    continue
                bet += player.bet(bet)
                for i in range(0, self.player_amount):
                    if player == self.players[i]:
                        self.bets[i] = bet
  
                player.hand.append(self.take_card())
                

                t.sleep(1.2)
                cls()
                self.print_players(self.players, self.bets)
 
                break

            elif decision == SPLIT:
                if len(player.hand) != 2 or player.hand[0].value != player.hand[1].value:
                    print("YOU CAN NOT SPLIT THIS HAND")
                    t.sleep(1.2)
                    cls()
                    self.print_players(self.players, self.bets)
                    continue
                
                print("NOT IMPLEMENTED YET")
                t.sleep(1.2)
                cls()
                self.print_players(self.players, self.bets)

            elif decision == STAND:
                t.sleep(1.2)
                cls()
                self.print_players(self.players, self.bets)

                break

            t.sleep(1.2)
            cls()
            self.print_players(self.players, self.bets)
   



    def players_turn(self) -> None:
        for i, player in enumerate(self.players):
            if player.has_blackjack():
                print(f"PLAYER {player.name.upper()} HAS BLACKJACK")
                t.sleep(1.2)
                continue
            self.choose_move(player, self.bets[i])
            
        
    def game_loop(self) -> None:
        
        self.start_game()

        while 1:

            #the players place their bets for this game
            self.initial_bets()

            #the decks are shuffled and initialized
            self.random_decks()

            #prints the table status
            self.print_players(self.players, self.bets)
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

            #if dealer has BlackJack all the players without BJ will lose their bets
            # and the ones with BJ will get their bet returned
            if self.dealer.has_blackjack():
                self.dealers_turn()
                print("DEALER HAS BLACKJACK")
                self.end_game()
            else:
                #player decide their actions
                self.players_turn()

                #the dealer gets the cards
                self.dealers_turn()
                self.end_game()

            if len(self.players) == 0:  
                t.sleep(3)
                print("ALL PLAYERS HAVE 0 CHIPS")
                return

            #after the round is finished you can choose to end the round 
            # or to play another
            try:
                decision = input(
                                "IF YOU DON'T WANT TO PLAY ANOTHER ROUND "
                                "PRESS 'Q' TO EXIT, "
                                "OTHERWISE PRESS ANY KEY: ")
            except EOFError as _:
                exit_signal(1, "signal ctrl+D")

            if decision.upper() == 'Q':
                print("GAME ENDED")
                return
            cls()
                

    