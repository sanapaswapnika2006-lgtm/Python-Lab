
import string

def clean_text(text):
    text = text.lower()
    return ''.join(ch for ch in text if ch.isalnum())


def are_anagrams(text1, text2):
    word1 = clean_text(text1)
    word2 = clean_text(text2)

    # Method 1: Sort characters
    if sorted(word1) == sorted(word2):
        return True
    return False


def character_count(text):
    count = {}

    for ch in clean_text(text):
        count[ch] = count.get(ch, 0) + 1

    return count


def find_anagrams(words):
    groups = {}

    for word in words:
        cleaned = clean_text(word)

        # Immutable tuple used as dictionary key
        key = tuple(sorted(cleaned))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return groups


# Input two words or phrases
text1 = input("Enter first word or phrase: ")
text2 = input("Enter second word or phrase: ")

if are_anagrams(text1, text2):
    print("The texts are anagrams.")
else:
    print("The texts are not anagrams.")

print("Character count of first text:", character_count(text1))

# Find anagrams in a list
words = ["listen", "silent", "enlist", "hello", "below", "elbow"]

print("\nAnagram Groups:")
for group in find_anagrams(words).values():
    if len(group) > 1:
        print(group)
