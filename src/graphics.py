from src.const import *
from src.button import Button
import pygame
import sys

# GUI global variables
BUTTONS = []
CURRENT_SCREEN = MENU_SCREEN

# Function in charge of the graphic section
def start_gui():

    global BUTTONS
    global CURRENT_SCREEN

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
                    if CURRENT_SCREEN == RULES_SCREEN:
                        CURRENT_SCREEN = MENU_SCREEN

            # Handle button clicks
            for button in BUTTONS:
                button.clicked(event)

        # Render the current screen
        if CURRENT_SCREEN == MENU_SCREEN:
            menu()
        elif CURRENT_SCREEN == RULES_SCREEN:
            show_game_rules(screen)
        elif CURRENT_SCREEN == PLAY_SCREEN:
            play()

        # Draw buttons
        for button in BUTTONS:
            button.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()




###########
# SCREENS #
###########

def play():         # TODO: Complete the play function
    print("TEST")
    set_screen(MENU_SCREEN)

def menu() -> None:
    """
    Displays the buttons of the main menu
    """
    global BUTTONS
    if not BUTTONS:  # Only create buttons if they don't exist
        play_button = Button(pos_x=700, pos_y=300, width=500, height=150, button_color=COLOR_BLACK,
                              text="PLAY", text_color=COLOR_WHITE, font=FONT_IMPACT, font_size=100, sound=BUTTON_SOUND, callback=lambda: set_screen(PLAY_SCREEN))
        rules_button = Button(pos_x=700, pos_y=500, width=500, height=150, button_color=COLOR_BLACK,
                               text="GAME RULES", text_color=COLOR_WHITE, font=FONT_IMPACT, font_size=100, sound=BUTTON_SOUND, callback=lambda: set_screen(RULES_SCREEN))
        BUTTONS.extend([play_button, rules_button])

def show_game_rules(screen) -> None:
    """
    Displays the game rules.
    """
    draw_text(600, 50, screen, "            GAME RULES", FONT_VERDANA, 50, text_color=COLOR_WHITE)

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
        draw_text(600, y_offset, screen, f"- {rule}", FONT_VERDANA, 30, text_color=COLOR_WHITE)
        y_offset += 50

    pygame.draw.rect(screen, COLOR_WHITE, (550, y_offset + 20, 800, 3))
    draw_text(545, y_offset + 70, screen, "PRESS ESC TO RETURN TO THE MAIN MENU.", FONT_VERDANA, 50, text_color=COLOR_WHITE)


######################
# AUXILIAR FUNCTIONS #
######################

def set_screen(screen_name) -> None:
    """
    Sets the screen to be displayed
    """
    global CURRENT_SCREEN
    CURRENT_SCREEN = screen_name
    global BUTTONS
    BUTTONS = []

def use_font(font_name: str=None, font_size: int=40, bold: bool=False, italic:bool =False):
    """
    Loads a font and returns it
    """
    return pygame.font.SysFont(font_name, font_size, bold, italic)

def draw_text(pos_x, pos_y, screen, text, font_name, font_size, text_color=COLOR_WHITE) -> None:
    """
    Draws the input text with the giving parameters
    """
    img = use_font(font_name, font_size).render(text, True, text_color)
    screen.blit(img, (pos_x, pos_y))