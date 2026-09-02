# Dynamic Command-Line Caesar Cipher Tool
"""
This micro-tool takes text input along with a user-specified shift key via the command line or prompt to
encode or decode messages using the Caesar cipher encryption technique. It processes raw input strings by
shifting alphabetic characters while ignoring special symbols, verifying valid data types using string methods,
and dynamically handling standard system parameters.
"""

import sys


def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def main():
    print("===== Caesar Cipher Tool =====")

    # Get text from command line or user input
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = input("Enter the message: ")

    # Get shift key
    if len(sys.argv) > 2:
        shift_input = sys.argv[2]
    else:
        shift_input = input("Enter shift key: ")

    # Validate shift key
    if not shift_input.lstrip("-").isdigit():
        print("Error: Shift key must be an integer.")
        return

    shift = int(shift_input)

    # Get operation
    if len(sys.argv) > 3:
        operation = sys.argv[3].lower()
    else:
        operation = input("Enter 'encode' or 'decode': ").lower()

    # Validate operation
    if operation not in ["encode", "decode"]:
        print("Error: Please enter either 'encode' or 'decode'.")
        return

    # Decode means shifting in the opposite direction
    if operation == "decode":
        shift = -shift

    result = caesar_cipher(text, shift)

    print("\nOriginal message:", text)
    print("Operation:", operation)
    print("Shift:", abs(shift))
    print("Result:", result)


if __name__ == "__main__":
    main()