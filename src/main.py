from blackjack import BlackJack


def main() -> None:
    #cambiar constructor para recibir player
    #almacenar datos del usuario, funcion de crear cuenta etc
    bj = BlackJack()
    bj.gameLoop()


if __name__ == "__main__":
    main()