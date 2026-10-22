
# Caesar Cipher
# Mini Projects
# Concepts: Functions, Parameters, for Loops, Conditionals, String Manipulation, Modulo Operator
# Encrypts and decrypts messages by shifting letters in the alphabet.

alphabet = list("abcdefghijklmnopqrstuvwxyz")


def caesar(original_text, shift_amount, direction):
    output_text = ""

    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter

    print(f"Here is the {direction}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode" or direction == "decode":
        caesar(text, shift, direction)
    else:
        print("Invalid direction. Please choose 'encode' or 'decode'.")

    restart = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'.\n"
    ).lower()

    if restart == "no":
        should_continue = False
        print("Goodbye!")
