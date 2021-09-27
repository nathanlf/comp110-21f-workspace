"""List utility functions."""

__author__ = "730483098"


def all(num_list: list[int], num: int) -> bool:
    """Returns True if all values in a given list are the same as a given integer. False otherwise."""
    i: int = 0
    all_equal: bool = True

    while i < len(num_list):
        if num_list[i] != num:
            all_equal = False
        i += 1
    
    return all_equal