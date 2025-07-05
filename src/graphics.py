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

# Function to choose the font to use
def use_font(font_name: str=None, font_size: int=40, bold: bool=False, italic:bool =False):
    return pygame.font.SysFont(font_name, font_size, bold, italic)

# Function used to draw a text
def draw_text(pos_x, pos_y, screen, text, font_name, font_size, text_color=COLOR_WHITE) -> None:
    img = use_font(font_name, font_size).render(text, True, text_color)
    screen.blit(img, (pos_x, pos_y))

def menu():
    global BUTTONS
    if not BUTTONS:  # Only create buttons if they don't exist
        play_button = Button(pos_x=700, pos_y=300, width=500, height=150, button_color=COLOR_BLACK,
                              text="PLAY", text_color=COLOR_WHITE, font=FONT_IMPACT, font_size=100, sound=BUTTON_SOUND, callback=lambda: set_screen(PLAY_SCREEN))
        rules_button = Button(pos_x=700, pos_y=500, width=500, height=150, button_color=COLOR_BLACK,
                               text="GAME RULES", text_color=COLOR_WHITE, font=FONT_IMPACT, font_size=100, sound=BUTTON_SOUND, callback=lambda: set_screen(RULES_SCREEN))
        BUTTONS.extend([play_button, rules_button])

def play():
    print("TEST")
    set_screen(MENU_SCREEN)

def set_screen(screen_name):
    global CURRENT_SCREEN
    CURRENT_SCREEN = screen_name
    global BUTTONS
    BUTTONS = []

def go_to_rules():
    global CURRENT_SCREEN
    CURRENT_SCREEN = RULES_SCREEN
    global BUTTONS
    BUTTONS = []

def show_game_rules(screen) -> None:

    draw_text(600, 100, screen, "GAME RULES:", FONT_VERDANA, 40)
    draw_text(600, 200, screen, "Dealer must stand on all 17", FONT_VERDANA, 30)
    draw_text(600, 250, screen, "A split after another split is not allowed", FONT_VERDANA, 30)
    draw_text(600, 300, screen, "A double after a split is not allowed", FONT_VERDANA, 30)
    draw_text(600, 350, screen, "The game is played with 6 decks,", FONT_VERDANA, 30)
    draw_text(600, 390, screen, "     every 15 rounds the decks will be swapped with 6 new ones", FONT_VERDANA, 30)
    draw_text(600, 440, screen, "A win with blackjack will multiply the bet by 2.5", FONT_VERDANA, 30)
    draw_text(600, 490, screen, "A win without blackjack will multiply the bet by 2", FONT_VERDANA, 30)
    draw_text(600, 540, screen, "PRESS ESC TO RETURN TO MAIN MENU", FONT_VERDANA, 30)
