# 🃏 Blackjack Game

A simple command-line Blackjack game built with Python as part of my programming learning journey.

The player competes against a computer dealer, aiming to reach a score as close to 21 as possible without going over.

## Features

- Random card dealing
- Automatic score calculation
- Ace adjustment from 11 to 1 when necessary
- Blackjack detection
- Computer dealer that draws cards until reaching at least 17
- Win, lose, and draw detection
- Option to play multiple rounds

## How It Works

1. The player and dealer receive two cards each.
2. The player can draw additional cards or keep their current hand.
3. The dealer draws cards until reaching a score of at least 17.
4. The final scores are compared to determine the winner.

A two-card Blackjack is internally represented by a score of `0` to distinguish it from a regular total of 21.

## Python Concepts Practiced

- **Functions:** Organizing the game into reusable components
- **Lists:** Storing and updating players' hands
- **Loops:** Managing turns and repeated games
- **Conditionals:** Handling game rules and outcomes
- **Random module:** Selecting random card values
- **Return values:** Passing calculated results between functions

## Getting Started

**Requirements:** Python 3

Clone the repository:

```bash
git clone https://github.com/sumytsuki/python-learning-journey.git
```

Navigate to the Blackjack project directory and run:

```bash
python main.py
```

Make sure `art.py`, containing the game logo, is in the same directory as `main.py`.

## Project Structure

```text
blackjack/
├── main.py
├── art.py
└── README.md
```

## What I Learned

This project helped me practice breaking a program into smaller functions, managing game state with loops and conditionals, and working with mutable lists.

It also helped me better understand how different functions interact to create a complete program.

## About This Project

This project was developed as part of my Python learning journey, based on a programming course exercise.

My focus was on understanding the game logic, practicing Python fundamentals, and improving code readability rather than adding advanced features.