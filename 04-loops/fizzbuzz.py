# FizzBuzz
# Loops
# Concepts: for Loops, range(), if/elif/else, Modulo Operator
# Prints numbers from 1 to 100, replacing multiples of 3 and 5 with specific words.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)