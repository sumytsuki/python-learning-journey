# Hangman
# Mini Projects
# Concepts: while Loops, for Loops, Lists, Conditionals, String Manipulation, random.choice()
# A word-guessing game where the player has six attempts to find the hidden word.

import random
from art import stages, logo

word_list = ["aardvark", "baboon", "camel", "python", "developer"]

lives = 6

print(logo)

chosen_word = random.choice(word_list)
correct_letters = []

game_over = False

while not game_over:
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"YOU LOSE! The word was {chosen_word}.")

    if "_" not in display:
        game_over = True
        print("YOU WIN!")

    print(stages[lives])
