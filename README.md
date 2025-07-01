# BlackJack
A blackjack game built in Python. Featuring almost the same functionalities of a real casino, but without real money.

---

## Built with

- `Python 3.10.12`
- `Pygame 2.6.1`

---

## How to play

1. Clone the repository
 
2. Navigate to the project folder

3. Create a virtual environment: `python3 -m venv venv`
   
4. Activate the virtual environment: `source venv/bin/activate`

5. Install the required modules: `python3 -m pip install -r requirements.txt`

6. Start the game: `python3 -m src.main`

---

## Project Structure
```
BlackJack/
├── src/                # Source code
│   ├── blackjack.py    # Game logic
│   ├── const.py        # Constants
│   ├── deck.py         # Deck and card management
│   ├── main.py         # Entry point
│   ├── person.py       # Player and dealer classes
│   └── utils.py        # Utility functions
├── assets/             # Game assets (icons, sounds, cards)
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

---

## Game Rules
- The dealer must stand on all 17.
- A split after another split is not allowed.
- A double after a split is not allowed.
- The game is played with 6 decks, and every 15 rounds the decks are swapped with 6 new ones.
- A win with Blackjack multiplies the bet by **2.5**.
- A win without Blackjack multiplies the bet by **2**.

---

## Known Issues:
- Players cannot bet when their chips are between 0 and 1.
