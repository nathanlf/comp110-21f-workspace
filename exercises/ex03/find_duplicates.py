"""Finding duplicate letters in a word."""

__author__ = "730483098"

has_dupes: bool = False
word: str = input("Enter a word: ")
i: int = 0

while(i < len(word)):
    j: int = 0
    while(j < len(word)):
        if word[i] == word[j] and i != j:
            has_dupes = True
        j += 1
    i += 1

print("Found duplicate: " + str(has_dupes))