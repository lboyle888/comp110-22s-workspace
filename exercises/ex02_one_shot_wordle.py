"""One shot wordle - EX 02"""

__author__ = "730473612"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)} letter guess? ")
"""does not continue if string is wrong length"""
while len(guess) != len(secret_word):
    guess = input(f"That was not { len(secret_word) } letters! Try again: ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
count: int = 0
boxes: str = ""
checker: bool = False
yellow_count: int = 0
"""Outer while loop to check each character"""
while count < len(secret_word):
    """adds a green box to string if correct character"""
    if secret_word[count] == guess[count]:
        boxes = boxes + GREEN_BOX
    else:
        """checks for character in incorrect position"""
        while (not checker) and yellow_count < len(secret_word):
            if secret_word[yellow_count] == guess[count]:
                checker = True
            else:
                yellow_count += 1
        """adds yellow box if in incorrect position and white box for wrong"""
        if checker:
            boxes = boxes + YELLOW_BOX
            checker = False
        else:
            boxes = boxes + WHITE_BOX
    count += 1
    yellow_count = 0
print(boxes)
"""tells user if guess is correct"""
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")