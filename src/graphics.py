from src.const import *
from src.person import *
from copy import deepcopy
from src.button import Button
from src.text_box import Text_box
from src.blackjack import BlackJack
import time as t
import pygame
import sys

class Graphics(BlackJack):
    # GUI variables

    def __init__(self) -> None:
        super().__init__()
        self.buttons = []
        self.current_screen = MENU_SCREEN
        self.STAND_FLAG = False

    # Function in charge of the graphic section
    def start_gui(self):

        pygame.init()
        pygame.display.set_caption(TITLE)
        icon = pygame.image.load("./assets/icon/icon.png")
        pygame.display.set_icon(icon)

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        clock = pygame.time.Clock()

        RUNNING = True
        while RUNNING:

            screen.fill(COLOR_DARK_GRAY)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.current_screen == RULES_SCREEN:
                            self.current_screen = MENU_SCREEN

                # Handle button clicks
                for button in self.buttons:
                    button.clicked(event)

            # Render the current screen
            if self.current_screen == MENU_SCREEN:
                self.menu()
            elif self.current_screen == RULES_SCREEN:
                self.show_game_rules(screen)
            elif self.current_screen == SELECT_PLAYER_AMOUNT_SCREEN:
                self.select_player_amount(screen)
            elif self.current_screen == SELECT_PLAYERS_NAMES_SCREEN:
                self.select_player_names(screen)
            elif self.current_screen == PLAY_SCREEN:
                self.play(screen)

            # Draw self.buttons
            for button in self.buttons:
                button.draw(screen)

            pygame.display.update()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()


    ###########
    # SCREENS #
    ###########

    def menu(self) -> None:
        """
        Displays the self.buttons of the main menu
        """
        if not self.buttons:  # Only create self.buttons if they don't exist
            play_button = Button(pos_x=700, pos_y=300, width=500, height=150, button_color=COLOR_BLACK,
                                text="PLAY", text_color=COLOR_WHITE, font=FONT_IMPACT, font_size=100, sound=BUTTON_SOUND, callback=lambda: self.set_screen(SELECT_PLAYER_AMOUNT_SCREEN))
            rules_button = Button(pos_x=700, pos_y=500, width=500, height=150, button_color=COLOR_BLACK,
                                text="GAME RULES", text_color=COLOR_WHITE, font=FONT_IMPACT, font_size=100, sound=BUTTON_SOUND, callback=lambda: self.set_screen(RULES_SCREEN))
            self.buttons.extend([play_button, rules_button])

    def show_game_rules(self, screen) -> None:
        """
        Displays the game rules.
        """
        self.draw_text(600, 50, screen, "            GAME RULES", FONT_VERDANA, 50, text_color=COLOR_WHITE)

        pygame.draw.line(screen, COLOR_WHITE, (550, 120), (1350, 120), 3)

        # The game rules
        rules = [
            "Dealer must stand on all 17",
            "A split after another split is not allowed",
            "A double after a split is not allowed",
            "The game is played with 6 decks",
            "Every 15 rounds the decks will be swapped with 6 new ones",
            "A win with blackjack will multiply the bet by 2.5",
            "A win without blackjack will multiply the bet by 2"
        ]

        # Draw each rule
        y_offset = 150
        for rule in rules:
            self.draw_text(600, y_offset, screen, f"- {rule}", FONT_VERDANA, 30, text_color=COLOR_WHITE)
            y_offset += 50

        pygame.draw.rect(screen, COLOR_WHITE, (550, y_offset + 20, 800, 3))
        self.draw_text(545, y_offset + 70, screen, "PRESS ESC TO RETURN TO THE MAIN MENU.", FONT_VERDANA, 50, text_color=COLOR_WHITE)

    def select_player_amount(self, screen):
        """
        Returns the ammount of players and their names
        """
        
        self.draw_text(600, 50, screen, "Enter the amount of players", FONT_VERDANA, 50, text_color=COLOR_WHITE)

        one_button = Button(pos_x=700, pos_y=300, width=150, height=150, button_color=COLOR_BLACK,
                                text="1", text_color=COLOR_WHITE, font=FONT_IMPACT, font_size=100, sound=BUTTON_SOUND, callback=lambda: self.set_player_amount(1))
        two_button = Button(pos_x=1000, pos_y=300, width=150, height=150, button_color=COLOR_BLACK,
                                text="2", text_color=COLOR_WHITE, font=FONT_IMPACT, font_size=100, sound=BUTTON_SOUND, callback=lambda: self.set_player_amount(2))
        three_button = Button(pos_x=700, pos_y=600, width=150, height=150, button_color=COLOR_BLACK,
                                text="3", text_color=COLOR_WHITE, font=FONT_IMPACT, font_size=100, sound=BUTTON_SOUND, callback=lambda: self.set_player_amount(3))
        four_button = Button(pos_x=1000, pos_y=600, width=150, height=150, button_color=COLOR_BLACK,
                                text="4", text_color=COLOR_WHITE, font=FONT_IMPACT, font_size=100, sound=BUTTON_SOUND, callback=lambda: self.set_player_amount(4))

        self.buttons.extend([one_button, two_button, three_button, four_button])

    def set_player_amount(self, amount: int):
            self.player_amount = amount
            self.set_screen(SELECT_PLAYERS_NAMES_SCREEN)

    def select_player_names(self, screen):
        names = []
        tb = Text_box(pos_x=800, pos_y=400, width=400, height=70)
        current_player = 0
        error_message = ""

        while current_player < self.player_amount:
            screen.fill(COLOR_DARK_GRAY)
            self.draw_text(600, 300, screen, f"Enter player {current_player + 1} name: (press enter to confirm)", FONT_VERDANA, 40, text_color=COLOR_WHITE)
            tb.draw(screen)
            if error_message:
                self.draw_text(600, 500, screen, error_message, FONT_VERDANA, 40, text_color=COLOR_RED)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                result = tb.handle_event(event)
                if result is not None:
                    if result in names:
                        error_message = "NAMES MUST BE UNIQUE, PICK ANOTHER NAME"
                        tb.clear()
                    elif "&" in result:
                        error_message = "'&' CHARACTER NOT ALLOWED"
                        tb.clear()
                    elif result.strip() == "":
                        error_message = "NAME MUST NOT BE EMPTY"
                        tb.clear()
                    else:
                        names.append(result)
                        current_player += 1
                        tb.clear()
                        error_message = ""

        self.start_game(self.player_amount, names)
        self.set_screen(PLAY_SCREEN)

    def select_bets(self, screen):
        bets = []
        tb = Text_box(pos_x=750, pos_y=400, width=400, height=70)
        current_player = 0
        error_message = ""

        while current_player < self.player_amount:
            screen.fill(COLOR_DARK_GRAY)
            self.draw_text(700, 300, screen, f"PLAYER '{self.players[current_player].name.upper()}' ({self.players[current_player].chips} Chips), bet: ", FONT_VERDANA, 40, text_color=COLOR_WHITE)
            tb.draw(screen)
            if error_message:
                self.draw_text(700, 500, screen, error_message, FONT_VERDANA, 40, text_color=COLOR_RED)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                result = tb.handle_event(event)
                if result is not None:
                    try:
                        bet = round(float(result), 2)
                        if bet <= 0:
                            error_message = "BET MUST BE GREATER THAN 0"
                            tb.clear()
                        elif bet > self.players[current_player].chips:
                            error_message = "BET MUST NOT EXCEED AVAILABLE CHIPS"
                            tb.clear()
                        else:
                            bets.append(bet)
                            current_player += 1
                            tb.clear()
                            error_message = ""
                    except ValueError:
                        error_message = "BET MUST BE A VALID NUMBER"
                        tb.clear()

        self.initial_bets(bets)
        screen.fill(COLOR_DARK_GRAY)
        #Delete after:
        self.set_screen(MENU_SCREEN)

    def display_board(self, screen):  #TODO: buttons, etc.
        screen.fill(COLOR_BOARD)
        # print all players
        for i, player in enumerate(self.players):
            self.draw_text(40 + i * 250, 520, screen, f"{player.name.upper()} - {self.bets[i]}$", FONT_VERDANA, 25, text_color=COLOR_BLACK)
            score = player.get_score()
            score_string = ""
            if score == int(OBJECTIVE) and len(player.hand) == 2:
                score_string = "BLACKJACK!"
            else:
                score_string = f"SCORE: {score}" if score != -1 else "BUSTED"
            
            self.draw_text(40 + i * 250+65, 580, screen, f"{score_string}", FONT_VERDANA, 25, text_color=COLOR_BLACK)
            pygame.draw.rect(screen, COLOR_CARD_HOLDER, (40 + i * 250, 620, 230, 400))# (x, y, width, height)
            if player.hand:
                j=0
                for card in player.hand:
                    screen.blit(pygame.image.load(card.img), ((45 + i * 250)+j/3, 780-j))# (x, y)
                    j+=30

        # print the dealer
        score = self.dealer.get_score()
        if score == -1:
            score = "BUSTED"
        elif len(self.dealer.hand) == 2:
            score = "???"

        self.draw_text(800, 10, screen, f"DEALER'S SCORE: {score}", FONT_VERDANA, 25, text_color=COLOR_BLACK)
        pygame.draw.rect(screen, COLOR_CARD_HOLDER, (350, 50, 1300, 300))# (x, y, width, height)
        if self.dealer.hand:
            j=0
            for card in self.dealer.hand:
                if len(self.dealer.hand) == 2 and j == 80:
                    screen.blit(pygame.image.load("./assets/cards/reverse.png"), ((300+160/2+j), 80))# (x, y)
                else:
                    screen.blit(pygame.image.load(card.img), ((300+160/2+j), 80))# (x, y)
                j+=80

        # print the deck
        screen.blit(pygame.image.load("./assets/cards/deck.png"), (1700, 90))# (x, y)

        pygame.display.update()

    def play(self, screen):
        print("TEST")
        while True:
            #the players place their bets for this game
            self.select_bets(screen)

            #the decks are shuffled and initialized
            self.random_decks(gui=True)

            # #prints the table status
            self.display_board(screen)
            t.sleep(SPEED*0.5)
            
            #Deal card 1 to players
            self.deal_gui(False, screen)
            
            #Deal card 1 to dealer
            self.deal_gui(True,screen)

            #Deal card 2 to players
            self.deal_gui(False, screen)
            
            #Deal card 2 to dealer
            self.deal_gui(True, screen)

            # #if dealer has BlackJack all the players without BJ will lose their bets
            # # and the ones with BJ will get their bet returned
            # if self.dealer.has_blackjack():
            #     self.dealers_turn()
            #     screen.fill(COLOR_BLACK)
            #     self.draw_text(600, 50, screen, "DEALER HAS BLACKJACK", FONT_VERDANA, 50, text_color=COLOR_WHITE)
            #     self.end_game()
            #     t.sleep(SPEED)
            #     continue # players bet in the new round


            for i, player in enumerate(self.players):
                while player.get_score() < int(OBJECTIVE) and player.get_score() != int(BUSTED):
                    self.bet_buttons(player, i)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                        # Handle button clicks
                        for button in self.buttons:
                            button.clicked(event) 

                    self.display_board(screen)
                    # Draw self.buttons
                    for button in self.buttons:
                        button.draw(screen)

                    pygame.display.update()
                    if self.STAND_FLAG:
                        self.STAND_FLAG = False
                        break

            #the dealer gets the cards
            # self.dealers_turn()
            # self.end_game()
        
    def bet_buttons(self, player, i): #TODO: speed button
        self.buttons = []
        hit_button = Button(40 + i * 250, 440, 50, 30, COLOR_CYAN, "HIT", COLOR_BLACK, font_size=10, callback=lambda: self.choose_move_gui(player, self.bets[i], HIT))
        stand_button = Button(100 + i * 250, 440, 50, 30, COLOR_CYAN, "STAND", COLOR_BLACK, font_size=10, callback=lambda: self.choose_move_gui(player, self.bets[i], STAND))
        self.buttons.append(hit_button)
        self.buttons.append(stand_button)

        if len(player.hand) != 2 or "&" in player.name or (player.chips - self.bets[i] < self.bets[i]):
            return

        double_button = Button(40 + i * 250, 480, 50, 30, COLOR_CYAN, "DOUBLE", COLOR_BLACK, font_size=10, callback=lambda: self.choose_move_gui(player, self.bets[i], DOUBLE))
        self.buttons.append(double_button)

        if player.hand[0].value != player.hand[1].value:
            return
        split_button = Button(100 + i * 250, 480, 50, 30, COLOR_CYAN, "SPLIT", COLOR_BLACK, font_size=10, callback=lambda: self.choose_move_gui(player, self.bets[i], SPLIT))
        self.buttons.append(split_button)

    ######################
    # AUXILIAR FUNCTIONS #
    ######################

    def set_screen(self, screen_name) -> None:
        """
        Sets the screen to be displayed
        """
        self.current_screen = screen_name
        self.buttons = []

    def use_font(self, font_name: str=None, font_size: int=40, bold: bool=False, italic:bool =False):
        """
        Loads a font and returns it
        """
        return pygame.font.SysFont(font_name, font_size, bold, italic)

    def draw_text(self, pos_x, pos_y, screen, text, font_name: str=None, font_size: int=40, text_color=COLOR_WHITE) -> None:
        """
        Draws the input text with the giving parameters
        """
        img = self.use_font(font_name, font_size).render(text, True, text_color)
        screen.blit(img, (pos_x, pos_y))


    # Rewrite

    def deal_gui(self, x: bool, screen) -> None:
        """
        Deals a card to the dealer or all players.
        :param x: True if the card is dealt to the dealer, False otherwise.
        :return: None
        """
        if x:
            self.dealer.hand.append(self.take_card())
            self.display_board(screen)
            t.sleep(SPEED*0.5)
        else:
            self.display_board(screen)
            for player in self.players:
                player.hand.append(self.take_card())

                self.display_board(screen)
                t.sleep(SPEED*0.5)

    def choose_move_gui(self, player: Player, bet,  decision) -> None:
        """
        Allows a player to choose their move during their turn.
        :param player: The player making the move.
        :param bet: The player's current bet.
        :return: None
        """
        if decision == HIT:
            player.hand.append(self.take_card())

        elif decision == DOUBLE:
            bet += player.bet(bet)
            for i in range(self.player_amount):
                if player == self.players[i]:
                    self.bets[i] = bet

            player.hand.append(self.take_card())
        elif decision == SPLIT:
            print(f"{player.name} SPLIT")
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

        elif decision == STAND:
            self.STAND_FLAG = True
