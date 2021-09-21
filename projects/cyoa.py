points: int = 0  # make quiz to find out what suitemate you are
player: str = ""  # DON'T FORGET TO FIX DOCSTRING FOR MAIN


def main() -> None:
    """Entry point into the program."""
    player = input("What is your name? ")
    print(f"Your name is: {player}!")


if __name__ == "__main__":
    main()