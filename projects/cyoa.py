"""A number guessing game."""

__author__ = "730483098"

import random  # import at top of file

# Emoji Constants
WELCOME: str = "\U0000203C"
HAPPY: str = "\U0001f600"
GAME_OVER: str = "\U0001F614"
HEART: str = "\U0001F496"

# Upper and Lower bounds for range of numbers
UPPER_EASY: int = 3
UPPER_HARD: int = 5
LOWER: int = 1

# Global Variables
points: int
player: str


def main() -> None:
    """Entry point into the program."""
    global points  # If I don't do this, the guessing_easy method doesn't change points properly. Global variables still confuse me a little.
    points = 0  # Initialized in main procedure
    user_in: int = 0  # Initialized first to allow the game loop to begin

    greet()

    while user_in != 3:  # Game Loop
        user_in = int(input("\nEnter the number of the option you choose.\n(1) Easy Difficulty\n(2) Hard Difficulty\n(3) Exit Game\n"))

        if user_in == 1:
            guessing_easy()
        elif user_in == 2:
            points = guessing_hard(points)

    # Goodbye message
    goodbye(points, player)


def greet() -> None:
    """Greets the user and provides information about the game."""
    global player

    print(f"Welcome{WELCOME + HAPPY} The objective of this game is to guess the correct number in a certain range of integers.")
    print("For each game session, you will have the choice between two difficulties: Easy and Hard")
    print("\nEach time you guess the number correctly on EASY, you gain FIVE points! If you guess incorrectly, you lose ONE point.")
    print("Each time you guess the number correctly on HARD, you gain TEN points! If you guess incorrectly, you lose TWO points.\n")
    print("The number you're trying to guess will be a new random number (that could potentially be the same) each time you guess.")
    print("The game will keep track of your total number of points (reset before every game) and how many guesses you have left per game session.\n")
    print("P.S. Each time you guess correctly, you gain an extra guess (two on Hard mode)! Also, encouraging messages will be provided.")

    player = input("Please enter your name: ")

    print(f"Good luck, {player}, and have fun!\n")


def guessing_easy() -> None:
    """Number guessing game on easy difficulty."""
    print(f"{player}, you chose: EASY difficulty.\n")

    global points  # So this procedure can change points from here
    points = 0
    guesses_remaining: int = 5  # Player "lives" reset after each game session

    while guesses_remaining > 0:
        rand_num: int = random.randint(LOWER, UPPER_EASY)
        guess: int = int(input((f"\nGuess the number between {LOWER} and {UPPER_EASY}: ")))
        result: int = compare(guess, rand_num)
        
        if result == 1:
            print("Correct!")
            points += 5
            guesses_remaining += 1
        else:
            print("Incorrect.")
            points -= 1
            guesses_remaining -= 1
            encourage()  # Gives player encouragement if they guess wrong

        if guesses_remaining > 0:
            print(f"Current Points: {points}\nCurrent Guesses Remaining: {guesses_remaining}\n")
        else:
            print("You ran out of guesses! Try again?")


def guessing_hard(points: int) -> int:
    """Number guessing game on hard difficulty."""
    print(f"{player}, you chose: HARD difficulty\nGuess the integer between {LOWER} and {UPPER_HARD}.")

    points = 0
    guesses_remaining: int = 5

    while guesses_remaining > 0:
        rand_num: int = random.randint(LOWER, UPPER_HARD)
        guess: int = int(input((f"\nGuess the number between {LOWER} and {UPPER_HARD}: ")))
        result: int = compare(guess, rand_num)
        
        if result == 1:
            print("Correct!")
            points += 5
            guesses_remaining += 1 
        else:
            print("Incorrect.")
            points -= 1
            guesses_remaining -= 1
            encourage()  # Gives player encouragement if they guess wrong

        if guesses_remaining > 0:
            print(f"Current Points: {points}\nCurrent Guesses Remaining: {guesses_remaining}\n")
        else:
            print("You ran out of guesses! Try again?")          
    return points


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
        print(f"I know things may be a little tough at times, but I believe in you, {player}.")
    elif num == 4:
        print(f"YOU{HEART}GOT{HEART}THIS{HEART}{player}{HEART}")
    else:
        print(f"{HEART+HEART+HEART+HEART+HEART+HEART+HEART+HEART+HEART+HEART}i love u {player} keep going")


def goodbye(points: int, player: str) -> None:
    """Says goodbye and displays final points."""
    print(f"Your final score is: {points}")
    print(f"\nThanks for playing, {player}! Goodbye.")


if __name__ == "__main__":
    main()