# Treasure Island
# Conditionals
# Concepts: input(), if/elif/else, Nested Conditions, Comparison Operators
# A text-based adventure game where choices determine the outcome.

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    "You're at a crossroad. Where do you want to go? "
    'Type "left" or "right": '
).lower()

if choice1 == "left":
    choice2 = input(
        'You come to a lake. Type "wait" or "swim": '
    ).lower()

    if choice2 == "wait":
        choice3 = input(
            "You arrive at an island with three doors. "
            'Type "red", "yellow" or "blue": '
        ).lower()

        if choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by a trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")