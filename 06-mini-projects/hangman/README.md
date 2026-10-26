# Hangman

A command-line word-guessing game built with Python as part of my learning journey.

## How It Works

The program randomly selects a word, and the player tries to guess it one letter at a time.

The player has six lives. Each incorrect guess removes one life and updates the Hangman drawing.

The game ends when the player guesses every letter or runs out of lives.

## Concepts Practiced

- `while` and `for` loops
- Lists and membership operators
- Conditional statements
- Random word selection with `random.choice()`
- String manipulation
- Importing variables from another Python file
- Tracking game state

## How to Run

```bash
python main.py
```

## Future Improvements

- Add input validation for single-letter guesses.
- Expand the word list.
- Add difficulty levels.
- Allow players to restart without rerunning the program.