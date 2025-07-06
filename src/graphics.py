from src.const import *
from src.button import Button
from src.blackjack import BlackJack
import pygame
import sys

class Graphics():
    # GUI variables

    def __init__(self) -> None:
        self.buttons = []
        self.current_screen = MENU_SCREEN
        self.player_amount: int = 0

    # Function in charge of the graphic section
    def start_gui(self):

        pygame.init()
        pygame.display.set_caption(TITLE)
        icon = pygame.image.load("./assets/icon/icon.png")
        pygame.display.set_icon(icon)

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        clock = pygame.time.Clock()

        bj = BlackJack()
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
                self.play()

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

        one_button = Button(pos_x=700, pos_y=300, width=500, height=150, button_color=COLOR_BLACK,
                                text="1", text_color=COLOR_WHITE, font=FONT_IMPACT, font_size=100, sound=BUTTON_SOUND)
        

    def select_player_names(self, screen):
        pass


    def play(self):         # TODO: Complete the play function
        print("TEST")
        self.set_screen(MENU_SCREEN)

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