from src.blackjack import BlackJack
from src.blackjack import cls
from src.graphics import Graphics
import argparse


def game_rules():
    
    cls()
    print("GAME RULES:\n")
    print("\t-> Dealer must stand on all 17")
    print("\t-> A split after another split is not allowed")
    print("\t-> A double after a split is not allowed")
    print("\t-> The game is played with 6 decks, every 15 rounds the decks will be swapped with" \
    "\n\t   6 new ones")
    print("\t-> A win with blackjack will multiply the bet by 2.5")
    print("\t-> A win without blackjack will multiply the bet by 2")
    print("\n\n\n")
    x = input("Type anything to exit this menu: ")
    cls()

def main(no_gui=False) -> None:


    cls()
    print("Game Running...")
    if no_gui is False:
            gr = Graphics()
            gr.start_gui()
            return
    while True:
        
        
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
    parser = argparse.ArgumentParser(description="Main program, optionally disables graphic interface")
    parser.add_argument(
        "--no-gui",
        action="store_true",
        help="Executes the program without graphic interface"
    )
    args = parser.parse_args()
    main(no_gui=args.no_gui)