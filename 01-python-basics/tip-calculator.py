# Tip Calculator
# Python Basics
# Concepts: Variables, input(), Type Conversion, Arithmetic Operators, f-strings
# Calculates how much each person should pay, including the tip.

print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill * (1 + tip / 100)
amount_per_person = total_bill / people

print(f"Each person should pay: ${amount_per_person:.2f}")