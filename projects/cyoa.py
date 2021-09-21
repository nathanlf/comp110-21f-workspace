"""A number guessing game."""

__author__ = "730483098"

# Emoji Constants
WELCOME: str = "\U0000203C"
FIVE_GUESSES_LEFT: str = "\U0001f600"
FOUR_GUESSES_LEFT: str = "\U0001f642"
THREE_GUESSES_LEFT: str = "\U0001f610"
TWO_GUESSES_LEFT: str = "\U0001f626"
ONE_GUESS_LEFT: str = "\U0001f630"
GAME_OVER: str = "\U0001F614"

# Upper and Lower bounds for range of numbers
UPPER: int = 5
LOWER: int = 1

points: int  # make number guessing game - Make it so every time they guess correctly, they get an extra "LIFE" (guess)
player: str  # make it so the player has multiple lives, points for how many times they get it right - use emojis for fun
guesses_remaining: int = 5


def main() -> None:
    """Entry point into the program."""
    global points  # Ask about this? I don't think this is fine - This doesn't make sense to me - office hours! zoom
    global guesses_remaining
    points = 0
    greet()

    # Program starts now! 1. Make a random number between 1 and 5
    # Compare function ? User guess and randnum as parameters? 
    
    # Game loop - Would you like to play again? Keep track of total points accumulated / highest streak? - add a quit option obviously
    import random
    rand_num: int

    while guesses_remaining > 0:
        rand_num = random.randint(LOWER, UPPER)
        guess: int = int(input((f"Guess the number between {LOWER} and {UPPER}: ")))
        
        result: bool = compare(guess, rand_num)
        
        if result and guesses_remaining > 0:
            points += 1
            guesses_remaining += 1
        else:
            guesses_remaining -= 1


def greet() -> None:
    """Greets the user and provides information about the game."""
    print(f"Welcome {WELCOME + FIVE_GUESSES_LEFT} The objective of this game is to guess the correct number in a certain range of integers.")
    print("Each time you guess the number correctly, you gain one point!\n")
    print("The number you're trying to guess will remain the same until you either guess the number or run out of guesses.")
    print("The game will keep track of your total numbers guessed correctly and how many guesses you have left.\n")

    player = input("Please enter your name: ")

    print(f"Good luck, {player}, and have fun!\n")


def compare(guess: int, target: int) -> bool:
    """Compares two integer values for equality."""
    if guess == target:
        return True
    else:
        return False


if __name__ == "__main__":
    main()