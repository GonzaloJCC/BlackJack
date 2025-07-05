from src.const import *
import pygame
import sys


# Function in charge of the graphic section
def start_gui():
    pygame.init()
    pygame.display.set_caption(TITLE)
    icon = pygame.image.load("./assets/icon/icon.png")
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    RUNNING = True
    while RUNNING:

        screen.fill(COLOR_DARK_GRAY)

        draw_text(500, 500, screen, "Hello World!", FONT_VERDANA, 40)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()

# Function to choose the font to use
def use_font(font_name: str=None, font_size: int=40, bold: bool=False, italic:bool =False):
    return pygame.font.SysFont(font_name, font_size, bold, italic)

# Function used to draw a text
def draw_text(pos_x, pos_y, screen, text, font_name, font_size, text_color=COLOR_WHITE):
    img = use_font(font_name, font_size).render(text, True, text_color)
    screen.blit(img, (pos_x, pos_y))

# Menu screen 
def menu():
    pass


# Similar to blackjack.py's gameloop
def play():
    pass