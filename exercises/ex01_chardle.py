"""Chardle Code - EX 01."""
__author__ = "730473612"

word: str = input("Enter a 5-character word: ")
letter: str = input("Enter a single character: ")
count: int = 0
if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
if (len(letter) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + letter + " in " + word)
if (word[0] == letter):
    print(letter + " found at index 0")
    count += 1
if (word[1] == letter):
    print(letter + " found at index 1")
    count += 1
if (word[2] == letter):
    print(letter + " found at index 2")
    count += 1
if (word[3] == letter):
    print(letter + " found at index 3")
    count += 1
if (word[4] == letter):
    print(letter + " found at index 4")
    count += 1

if count > 0:
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print("1 instance of " + letter + " found in " + word)
else:
    print("No instances of " + letter + " found in " + word)