# Sumy's Calculator

A command-line calculator built with Python as part of my learning journey.

This project started as a calculator exercise from the *100 Days of Code* course. I customized it with a personal terminal design, input validation, and improved calculation flow.

## Features

- Addition, subtraction, multiplication, and division
- Continue calculating with the previous result
- Start a new calculation without restarting the program
- Input validation for invalid numbers and operations
- Division-by-zero handling
- Custom ASCII calculator design

## Concepts Practiced

- Functions and return values
- Dictionaries storing function references
- `while` loops and nested loops
- Conditional statements
- Exception handling (`try`, `except`)
- String formatting with f-strings
- Importing modules
- The `if __name__ == "__main__"` pattern

## How to Run

Run the program from the calculator directory:

```bash
python main.py
```

## Example

```text
Enter the first number: 12

Available operations: +  -  *  /
Choose an operation: *
Enter the next number: 3

Result: 12 * 3 = 36

[y] Continue with result
[n] Start a new calculation
[q] Quit
Your choice:
```

## Future Improvements

- Add calculation history
- Support exponentiation and square roots
- Add automated unit tests
- Build a graphical interface

## Learning Note

The original exercise helped me understand how Python dictionaries can store functions and how return values can be reused across calculations.

I extended the exercise to practice input validation, exception handling, and managing repeated calculations without recursive function calls.