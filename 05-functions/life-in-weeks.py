# Life in Weeks
# Functions
# Concepts: Functions, Parameters, Arithmetic Operators, f-strings
# Calculates how many weeks remain until the age of 90.

def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52

    print(f"You have {weeks_remaining} weeks left.")


life_in_weeks(26)