# Sumy's Calculator
# Mini Projects
# Concepts: Functions, Dictionaries, while Loops, Conditionals, Error Handling
# A command-line calculator that supports continuous calculations.

from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    print("Welcome to Sumy's Calculator!\n")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        while True:
            print("\nAvailable operations: +  -  *  /")
            symbol = input("Choose an operation: ").strip()

            if symbol not in operations:
                print("Invalid operation. Try again.")
                continue

            try:
                num2 = float(input("Enter the next number: "))
                result = operations[symbol](num1, num2)

            except ValueError:
                print("Please enter a valid number.")
                continue

            except ZeroDivisionError:
                print("You cannot divide by zero.")
                continue

            print(f"\nResult: {num1:g} {symbol} {num2:g} = {result:g}")

            choice = input(
                "\n[y] Continue with result"
                "\n[n] Start a new calculation"
                "\n[q] Quit"
                "\nYour choice: "
            ).lower().strip()

            if choice == "y":
                num1 = result
            elif choice == "n":
                print("\nStarting a new calculation...\n")
                break
            elif choice == "q":
                print("\nThanks for using Sumy's Calculator!")
                return
            else:
                print("Unknown choice. Starting a new calculation.\n")
                break


if __name__ == "__main__":
    calculator()
