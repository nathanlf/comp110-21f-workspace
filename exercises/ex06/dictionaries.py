"""Practice with dictionaries."""

__author__ = "730483098"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary's keys with its values."""
    inverted: dict[str, str] = dict()

    for key in dictionary:
        if dictionary[key] in inverted:
            raise KeyError("There cannot be duplicates of the same key (in the inverse dictionary)!")
        inverted[dictionary[key]] = key

    return inverted


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the most popular color in a list of favorite colors."""
    colors: dict[str, int] = dict()

    for key in dictionary:
        color: str = dictionary[key]
        if color in colors:
            colors[color] += 1
        else:
            colors[color] = 1

    popular: str = ""
    largest = 0
    for key in colors:
        if colors[key] > largest:
            largest = colors[key]
            popular = key

    return popular


def count(vals: list[str]) -> dict[str, int]:
    """Returns a dictionary with the values of the list and how frequently they occur."""
    freq: dict[str, int] = dict()
    i: int = 0
    while i < len(vals):
        if vals[i] in freq:
            freq[vals[i]] += 1
        else:
            freq[vals[i]] = 1
        i += 1

    return freq