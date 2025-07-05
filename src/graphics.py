from src.const import *
import pygame
import sys

def start_gui():
    pygame.init()
    # cls()
    pygame.display.set_caption(TITLE)
    icon = pygame.image.load("./assets/icon/icon.png")
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()