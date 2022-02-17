"""Playable Wordle Using Functions."""

__author__ = "730473612"


def contains_char(given_word: str, char: str) -> bool:
    """Searches for given character in inputted string, returns true if present, false if not."""
    assert len(char) == 1
    i: int = 0
    while i < len(given_word):
        if given_word[i] == char:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emojifies the guessed word when compared to secret word."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    count: int = 0
    emoji_block: str = ""
    while count < len(secret):
        if guess[count] == secret[count]:
            emoji_block += GREEN_BOX
        else:
            if contains_char(secret, guess[count]):
                emoji_block += YELLOW_BOX
            else:
                emoji_block += WHITE_BOX
        count += 1
    return emoji_block


def input_guess(length: int) -> str:
    """Takes an input from user, checks length, and returns input if correct length."""
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    codes: str = "codes"
    win: bool = False
    while turns <= 6 and not(win):
        print(f"== Turn {turns}/6")
        user_guess: str = input_guess(len(codes))
        emoji_block: str = emojified(user_guess, codes)
        if user_guess == codes:
            print(emoji_block)
            win = True   
        else:
            print(emoji_block)
            turns += 1
    if win:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()