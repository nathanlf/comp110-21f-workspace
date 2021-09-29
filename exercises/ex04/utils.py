"""List utility functions."""

__author__ = "730483098"


def all(num_list: list[int], num: int) -> bool:
    """Returns True if all values in a given list are the same as a given integer. False otherwise."""
    i: int = 0

    if len(num_list) == 0:
        return False

    while i < len(num_list):
        if num_list[i] != num:
            return False
        i += 1
    
    return True


def is_equal(nums_one: list[int], nums_two: list[int]) -> bool:
    """Returns True if lists are equal, False otherwise."""
    i: int = 0

    if len(nums_one) != len(nums_two):
        return False

    while i < len(nums_one):
        if nums_one[i] != nums_two[i]:
            return False
        i += 1

    return True


def max(in_list: list[int]) -> int:
    if len(in_list) == 0:
        raise ValueError("max() arg is an empty List")

    max_num: int = in_list[0]
    i: int = 0

    while i < len(in_list):
        if in_list[i] > max_num:
            max_num = in_list[i]

        i += 1
    
    return max_num