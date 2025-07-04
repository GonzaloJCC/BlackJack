from src.person import *
from src.deck import *
import os
import time as t
from src.const import *
from src.utils import exit_signal
from copy import deepcopy


def cls():
    """
    Clears the console screen.
    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_player(player: Player, bet: float) -> None:
    """
    Prints the player's current hand and score.
    :param player: The player whose hand and score are to be printed.
    :param bet: The player's current bet.
    :return: None
    """
    score = player.get_score()
    if score == BUSTED:
        score = "BUSTED"
    print(f"{player.name.upper()} (BET: {bet:.2f})  SCORE: {score}: ")
    player.show()
    print("")


class BlackJack:
    def __init__(self) -> None:
        """
        Initializes the BlackJack game with default values.
        :return: None
        """
        self.player_amount: int = 0
        self.players: list[Player] = []
        self.players_copy: list[Player] = []
        self.bets: list[float] = []
        self.resetDeckCount: int = 0
        self.decks: list[Deck] = []
        self.dealer: Dealer = Dealer()

    def initial_bets(self):
        """
        Allows players to place their initial bets for the game.
        :return: None
        """
        print("PLACE YOUR BETS")
        for i in range(len(self.players)):
            while 1:
                try:
                    bet = round(float(input(f"PLAYER {self.players[i].name.upper()} ({self.players[i].chips} Chips), bet: ")), 2)
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
        t.sleep(SPEED*0.5)

        print("STARTING TO DEAL")
        t.sleep(SPEED*1)
        cls()

    def start_game(self) -> None:
        """
        Starts the game by allowing the user to select the number of players
        and their names.
        :return: None
        """
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
                elif "&" in name:
                    print("'&' CHARACTER NOT ALLOWED")
                elif name in ["", "", '', ' '] or len(name) == 0:
                    print("NAME MUST NOT BE EMPTY")
                else:
                    x = 1
                    
            self.players.append(Player(name))
            self.players_copy = deepcopy(self.players)
            self.bets.append(0)

        #every player makes the initial bet
        cls()

    #cleans the player and dealer cards
    def end_game(self) -> None:
        """
        Ends the current game round, calculates results, and updates player chips.
        :return: None
        """
        dealer_score = self.dealer.get_score()
        
        for i, player in enumerate(self.players):
            extra_chips = 0
            if player.name == "&":
                continue
            player_score = player.get_score()

            if player_score == BUSTED:
                print(f"{player.name.upper()} loses {self.bets[i]:.2f}")
                extra_chips = -1*self.bets[i]

            elif player.has_blackjack():
                if self.dealer.has_blackjack():
                    extra_chips = self.bets[i]
                    print(f"{player.name.upper()} wins 0")
                else:
                    extra_chips = BLACKJACK_WIN_RATIO * self.bets[i]
                    print(f"{player.name} wins {BLACKJACK_WIN_RATIO * self.bets[i]:.2f}")

            elif self.dealer.has_blackjack():
                #dealer wins
                print(f"{player.name.upper()} loses {self.bets[i]:.2f}")
                extra_chips = -1*self.bets[i]

            elif player_score > dealer_score:
                extra_chips = WIN_RATIO * self.bets[i]
                print(f"{player.name.upper()} wins {WIN_RATIO * self.bets[i]:.2f}")

            elif player_score == dealer_score:
                extra_chips = 0
                print(f"{player.name.upper()} wins 0")

            else:
                #dealer wins
                print(f"{player.name.upper()} loses {self.bets[i]:.2f}")
                extra_chips = -1*self.bets[i]

            true_name = player.name.split("&")[0]
            for p in self.players_copy:
                if true_name == p.name:   
                    p.chips += extra_chips

        self.players = deepcopy(self.players_copy)
        print("")
        t.sleep(SPEED*0.5)
        aux = []
        for player in self.players:
            print(f"{player.name.upper()}'S CHIPS: {player.chips:.2f}")
            self.bets[i] = 0
            player.hand = []
            if player.chips <= 0:
                print(f"{player.name.upper()} HAS 0 CHIPS, HE CAN NO LONGER PLAY")
            else:
                aux.append(player)
            print("")

        self.players = aux
        self.dealer.hand = []
        # self.players_copy = deepcopy(self.players)

    def print_dealer(self) -> None:
        """
        Prints the dealer's hand and score.
        :return: None
        """
        score = self.dealer.get_score()
        if score == BUSTED:
            score = "BUSTED"
        print(f"DEALER SCORE: {score}: ")
        self.dealer.show()
        print("")

    def print_players(self, players: list[Player], bets: list[float]):
        """
        Prints the current state of all players' hands and bets.
        :param players: List of players.
        :param bets: List of bets corresponding to the players.
        :return: None
        """
        self.dealer.show_first()
        for i, player in enumerate(players):
            if player.name == "&":
                continue
            print_player(player, bets[i])

    def deal(self, x: bool) -> None:
        """
        Deals a card to the dealer or all players.
        :param x: True if the card is dealt to the dealer, False otherwise.
        :return: None
        """
        if x:
            self.dealer.hand.append(self.take_card())
            cls()
            self.print_players(self.players, self.bets)
            t.sleep(SPEED*0.5)
        else:
            cls()
            self.print_players(self.players, self.bets)
            for player in self.players:
                player.hand.append(self.take_card())
                cls()
                self.print_players(self.players, self.bets)
                t.sleep(SPEED*0.5)
                

    #DECK MANAGEMENT
    def random_decks(self) -> None:
        """
        Initializes and shuffles the decks for the game.
        :return: None
        """
        if self.resetDeckCount == RESET_DECK_COUNT:
            self.resetDeckCount = 0

        if self.resetDeckCount == 0:
            self.decks.clear()
            for i in range(NUMBER_OF_DECKS):
                self.decks.append(Deck())
            self.shuffle()
        cls()

    def shuffle(self) -> None:
        """
        Shuffles all decks in the game.
        :return: None
        """
        for deck in self.decks:
            deck.shuffle()

    def take_card(self) -> Card:
        """
        Draws a card from a random deck.
        :return: A card object.
        """
        card = Card("-1", "-1", (-1, -1))
        while card.numericalValue == (-1, -1):
            aux_deck: Deck = random.choice(self.decks)
            card = aux_deck.take_card()
        return card

    def dealers_turn(self) -> None:
        """
        Executes the dealer's turn, where the dealer draws cards until
        reaching a stopping condition.
        :return: None
        """
        score = self.dealer.get_score()

        best_player_score = -1
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
                if player.name == "&":
                    continue
                print_player(player, self.bets[i])

            score = self.dealer.get_score()
            t.sleep(SPEED*0.5)

        #the final board is printed
        # t.sleep(SPEED*0.5)
        cls()
        self.print_dealer()
        for i, player in enumerate(self.players):
            if player.name == "&":
                    continue
            print_player(player, self.bets[i])
        t.sleep(SPEED*3)

    def choose_move(self, player: Player, bet: float) -> None:
        """
        Allows a player to choose their move during their turn.
        :param player: The player making the move.
        :param bet: The player's current bet.
        :return: None
        """
        can_double = True
        while player.get_score() < int(OBJECTIVE) \
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
                if not can_double:
                    print("\nYOU CAN NOT DOUBLE AFTER A HIT")
                    t.sleep(SPEED*1)
                    cls()
                    self.print_players(self.players, self.bets)
                    continue
                
                if "&" in player.name:
                    print("\nYOU CAN NOT DOUBLE AFTER A SPLIT")
                    t.sleep(SPEED*1)
                    cls()
                    self.print_players(self.players, self.bets)
                    continue

                if player.chips - bet < bet:
                    print("NOT ENOUGH CHIPS")
                    t.sleep(SPEED*0.5)
                    cls()
                    self.print_players(self.players, self.bets)
                    continue
                bet += player.bet(bet)
                for i in range(self.player_amount):
                    if player == self.players[i]:
                        self.bets[i] = bet

                player.hand.append(self.take_card())
                t.sleep(SPEED*0.5)
                cls()
                self.print_players(self.players, self.bets)
                break

            elif decision == SPLIT:

                if "&" in player.name:
                    print("\nYOU CAN NOT SPLIT AFTER A SPLIT")
                    t.sleep(SPEED*1)
                    cls()
                    self.print_players(self.players, self.bets)
                    continue
                 
                if len(player.hand) != 2 or player.hand[0].value != player.hand[1].value:
                    print("YOU CAN NOT SPLIT THIS HAND")
                    t.sleep(SPEED*0.5)
                    cls()
                    self.print_players(self.players, self.bets)
                    continue
                    
                if player.chips - bet < bet:
                    print("NOT ENOUGH CHIPS TO SPLIT THE HAND")
                    t.sleep(SPEED*0.5)
                    cls()
                    self.print_players(self.players, self.bets)
                    continue

                # print("NOT IMPLEMENTED YET")
                # t.sleep(SPEED*0.5)
                # cls()
                # self.print_players(self.players, self.bets)
                
                # remove the chips from the player
                player.bet(bet)
                # create 2 new players: player.name&1 and player.name&2
                new_name_1 = player.name + "&1"
                new_name_2 = player.name + "&2"
                p1 = Player(new_name_1)
                p2 = Player(new_name_2)

                # give them one card each
                p1.hand.append(player.hand[0])
                p2.hand.append(player.hand[1])

                # create 2 new list: new_players and new_bets
                new_players = []
                new_bets = []

                # append all players except the original, in its place append the 2 new players
                for i, aux in enumerate(self.players):
                    if aux.name == player.name:
                        new_players.append(Player("&"))
                        new_players.append(p1)
                        new_players.append(p2)

                        new_bets.append(0)
                        new_bets.append(bet)
                        new_bets.append(bet)
                        continue
                    new_players.append(aux)
                    new_bets.append(self.bets[i])
                
                # change the original lists
                self.players = deepcopy(new_players)
                self.bets = deepcopy(new_bets)

                # append all the bets except the one of the original player, in its place the same bet twice
                t.sleep(SPEED*0.5)
                cls()
                self.print_players(self.players, self.bets)
                break

            elif decision == STAND:
                t.sleep(SPEED*0.5)
                cls()
                self.print_players(self.players, self.bets)
                break

            t.sleep(SPEED*0.5)
            cls()
            self.print_players(self.players, self.bets)

    def players_turn(self) -> None:
        """
        Executes each player's turn, allowing them to make their moves.
        :return: None
        """
        i = 0
        while True:
            try:
                if self.players[i].has_blackjack():
                    print(f"PLAYER {self.players[i].name.upper()} HAS BLACKJACK")
                    t.sleep(SPEED*0.5)
                    i += 1
                    continue
                self.choose_move(self.players[i], self.bets[i])
            except:
                break
            i += 1

    def game_loop(self) -> None:
        """
        Main game loop that handles the flow of the game.
        :return: None
        """
        self.start_game()

        while True:

            #the players place their bets for this game
            self.initial_bets()

            #the decks are shuffled and initialized
            self.random_decks()

            #prints the table status
            self.print_players(self.players, self.bets)
            t.sleep(SPEED*0.5)
            
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
                t.sleep(SPEED*3)
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
