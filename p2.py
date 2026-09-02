#Dynamic Command-Line Caesar Cipher Tool
"""This micro-tool takes text input along with a user-specified shift key via the command line or prompt to
encode or decode messages using the Caesar cipher encryption technique. It processes raw input strings by
shifting alphabetic characters while ignoring special symbols, verifying valid data types using string methods,
and dynamically handling standard system parameters."""

import string

# Read multiline text
text = """Python is easy.
Python is powerful!
Madam is a palindrome.
Level is another palindrome."""

# Convert text to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Convert text into individual words
words = text.split()

# Count total words
total_words = len(words)

# Create frequency table
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Find palindromes
palindromes = []

for word in words:
    if len(word) > 1 and word == word[::-1]:
        if word not in palindromes:
            palindromes.append(word)

# Display the report
print("\n===== TEXT ANALYSIS REPORT =====")

print("\nTotal words:", total_words)

print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)

print("\nPalindromes:")
if len(palindromes) > 0:
    for word in palindromes:
        print(word)
else:
    print("No palindromes found.")