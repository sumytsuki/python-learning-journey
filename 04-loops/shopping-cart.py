# Shopping Cart
# Loops
# Concepts: Lists, for Loops, if/else, Arithmetic Operators, f-strings
# Calculates the total price and applies a 10% discount if it exceeds 500 TL.

prices = [120, 45, 300, 80]
total = 0

for price in prices:
    total += price

if total > 500:
    total *= 0.9

print(f"Total amount: {total:.2f} TL")