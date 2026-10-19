# Banker Roulette
# Randomization and Lists
# Concepts: Lists, input(), split(), random.choice()
# Randomly selects a person to pay the bill.

import random

friends = input("Enter everyone's names, separated by commas: ").split(", ")

random_person = random.choice(friends)

print(f"{random_person} is going to buy the meal today!")