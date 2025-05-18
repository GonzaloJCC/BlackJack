from src.blackjack import BlackJack
from src.blackjack import cls
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

    


def game_rules():
    
    cls()
    print("GAME RULES:\n")
    print("\t-> Dealer must stand on all 17")
    print("\t-> A split after another split is not allowed")
    print("\t-> A double after a split is not allowed")
    print("\t-> The game is played with 6 decks, every 15 rounds the decks will be swapped with" \
    "\n\t   6 new ones")
    print("\t-> A win with blackjack will multiply the bet by 2.5")
    print("\t-> A win withoyt blackjack will multyply the bet by 2")
    print("\n\n\n")
    x = input("Type anything to exit this menu: ")
    cls()

def main() -> None:
    cls()
    while True:
        if GUI_FLAG:
            start_gui()
        print("WELCOME!")
        print("IF YOU WANT TO KNOW THE RULES TYPE 'R'")
        print("IF YOU WANT TO PLAY TYPE 'P'")
        decision = input("> ").upper()
        
        if decision not in ['R', 'P']:
            print("YOU MUST TYPE A VALID INPUT\n")
            continue

        if decision == 'P':
            break

        if decision == 'R':
            game_rules()



    #cambiar constructor para recibir player
    #almacenar datos del usuario, funcion de crear cuenta etc
    bj = BlackJack()
    bj.game_loop()


if __name__ == "__main__":
    main()