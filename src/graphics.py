from src.const import *
from src.button import Button
from src.text_box import Text_box
from src.blackjack import BlackJack
import pygame
import sys

class Graphics(BlackJack):
    # GUI variables

    def __init__(self) -> None:
        super().__init__()
        self.buttons = []
        self.current_screen = MENU_SCREEN


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
        tb = Text_box(pos_x=750, pos_y=400, width=400, height=70)
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
            self.draw_text(600, 300, screen, f"PLAYER '{self.players[current_player].name.upper()}' ({self.players[current_player].chips} Chips), bet: ", FONT_VERDANA, 40, text_color=COLOR_WHITE)
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

    def play(self, screen):         # TODO: Complete the play function
        print("TEST")
        while True:
            #the players place their bets for this game
            self.select_bets(screen)

            #the decks are shuffled and initialized
            self.random_decks(gui=True)
            print("TEST2")
            print(self.bets)
            break

            # #prints the table status
            # self.print_players(self.players, self.bets) # call self.display board(screen)
            # t.sleep(SPEED*0.5)
            
            # #Deal card 1 to players
            # self.deal(False)
            
            # #Deal card 1 to dealer
            # self.deal(True)
            
            # #Deal card 2 to players
            # self.deal(False)
            
            # #Deal card 2 to dealer
            # self.deal(True)

        

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