# Password Generator

A command-line password generator built with Python as part of my learning journey.

## How It Works

The user specifies how many letters, symbols, and numbers the password should contain. The program randomly selects characters and shuffles them to generate a password.

## Concepts Practiced

- Lists and list methods (`append()`)
- `for` loops and `range()`
- Random selection with `random.choice()`
- Shuffling lists with `random.shuffle()`
- String manipulation
- User input and type conversion

## How to Run

```bash
python main.py
```

## Future Improvements

- Add input validation.
- Allow users to choose the total password length.
- Use Python's `secrets` module for cryptographically secure password generation.
- Add an option to exclude certain characters.