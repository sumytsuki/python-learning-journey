
# Password Generator
# Mini Projects
# Concepts: Lists, for Loops, range(), random.choice(), random.shuffle(), String Manipulation
# Generates a randomized password using letters, numbers, and symbols.

import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is: {password}")
