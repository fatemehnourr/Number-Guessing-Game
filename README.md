# Number Guessing Game

A simple Python number guessing game with input validation and random number generation.

## How It Works

1. The game first asks you to enter a "level," which determines the range for the random number.
   - For example, if you enter `10` as the level, the program will choose a random number between 1 and 10.
2. You will then be prompted to guess the number.
   - If your guess is too low, the program will tell you "Too small!"
   - If your guess is too high, the program will say "Too large!"
   - If you guess correctly, the program will congratulate you with "Just Right!" and the game will end.

## Features

- Input validation to ensure that only positive integers are accepted.
- Simple and user-friendly command-line interface.
- Uses Python's built-in `random` module for number generation.

## How to Run

1. Ensure you have Python installed on your computer.
2. Download or clone this repository.
3. Run the script using Python:

   ```bash
   python guessing_game.py
   ```

4. Follow the prompts in the command line.
