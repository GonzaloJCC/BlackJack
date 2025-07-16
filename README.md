# BlackJack
A blackjack game built in Python. Featuring almost the same functionalities of a real casino, but without real money.

---

## 📋 Requirements
- Python 3.10 or higher
- [Optional] `make` (to simplify running commands)

---

## 🛠️ Built with
- `Python 3.10.12`
- `Pygame 2.6.1`

---

## Installation and Running the Project

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project folder:
   ```bash
   cd BlackJack
   ```

### Option 1: Using `make`
If you have `make` installed, simply run the following commands:

```bash
# Create the virtual environment and install dependencies
make install

# Run the game
make run
```

### Option 2: Manual Setup
If you don't have `make`, follow these steps:

3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

5. Install the required modules:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

6. Start the game:
   ```bash
   python3 -m src.main
   ```

---

## 📁 Project Structure
```
BlackJack/
├── src/                # Source code
│   ├── blackjack.py    # Game logic
│   ├── button.py       # Button class for the GUI
│   ├── const.py        # Constants
│   ├── deck.py         # Deck and card management
│   ├── graphics.py     # GUI and game screens
│   ├── main.py         # Entry point
│   ├── person.py       # Player and dealer classes
│   ├── text_box.py     # Text box class for the GUI
│   └── utils.py        # Utility functions
├── assets/             # Game assets (icons, sounds, cards, fonts)
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

---

## 🎞️ Preview
https://github.com/user-attachments/assets/4d24b136-3dd6-4071-b6a0-0054b458e664

---

## ⚠️ Known Issues:
- Players cannot bet when their chips are between 0 and 1 in no gui mode.


