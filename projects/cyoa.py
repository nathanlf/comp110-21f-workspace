"""A number guessing game."""

__author__ = "730483098"

import random  # import at top of file

# Emoji Constants
WELCOME: str = "\U0000203C"
FIVE_GUESSES_LEFT: str = "\U0001f600"
FOUR_GUESSES_LEFT: str = "\U0001f642"
THREE_GUESSES_LEFT: str = "\U0001f610"
TWO_GUESSES_LEFT: str = "\U0001f626"
ONE_GUESS_LEFT: str = "\U0001f630"
GAME_OVER: str = "\U0001F614"
HEART: str = "\U0001F496"

# Upper and Lower bounds for range of numbers
UPPER: int = 5
LOWER: int = 1

# Global Variables
points: int 
player: str


def main() -> None:
    """Entry point into the program."""
    global points  # Ask about this? I don't think this is fine - This doesn't make sense to me - office hours! zoom
    global guesses_remaining
    points = 0
    guesses_remaining: int = 5  # Player starts with 5 "lives"
    user_in: int = 0

    greet()

    while user_in != 2:  # Game Loop
        points = 0  # Points reset after each game session
        guesses_remaining = 5  # Player "lives" reset after each game session
        while guesses_remaining > 0:
            rand_num: int = random.randint(LOWER, UPPER)
            guess: int = int(input((f"\nGuess the number between {LOWER} and {UPPER}: ")))
            result: int = compare(guess, rand_num)
            
            if result == 1:
                print("Correct!")
                points += 1
                guesses_remaining += 1
            else:
                print("Incorrect.")
                encourage()  # Gives player encouragement if they guess wrong
                guesses_remaining -= 1

            if guesses_remaining > 0:
                print(f"Current Points: {points}\nCurrent Guesses Remaining: {guesses_remaining}\n")
        
        print(f"Your final score is: {points}")
        user_in = int(input("(1) Continue Playing\n(2) Exit the game\n"))

        if user_in == 2:
            guesses_remaining = 0  # To exit the game

    print(f"\nThanks for playing {player}! Goodbye.")


def greet() -> None:
    """Greets the user and provides information about the game."""
    print(f"Welcome{WELCOME + FIVE_GUESSES_LEFT} The objective of this game is to guess the correct number in a certain range of integers.")
    print("Each time you guess the number correctly, you gain one point!\n")
    print("The number you're trying to guess will be a new random number (that could potentially be the same) each time you guess.")
    print("The game will keep track of your total numbers guessed correctly (points) and how many guesses you have left.\n")
    print("P.S. Each time you guess correctly, you gain an extra guess! Also, encouraging messages will be provided.")

    player = input("Please enter your name: ")

    print(f"Good luck, {player}, and have fun!\n")


def compare(guess: int, target: int) -> int:
    """Compares two integer values for equality."""
    if guess == target:
        return 1
    else:
        return 2


def encourage() -> None:
    """Provides encouragement to the user."""
    global player
    num = random.randint(1, 4)

    if num == 1:
        print(f"You're doing better than you know! Keep pushing, {player}!")
    elif num == 2:
        print(f"Has anyone ever told you that you're incredible, {player}? Because I am right now.")
    elif num == 3:
        print(f"I know this game may be a little tough at times, but I believe in you, {player}.")
    elif num == 4:
        print(f"YOU{HEART}GOT{HEART}THIS{HEART}{player}{HEART}")
    else:
        print(f"{HEART+HEART+HEART+HEART+HEART+HEART+HEART+HEART+HEART+HEART}i love u {player} keep going")


if __name__ == "__main__":
    main()