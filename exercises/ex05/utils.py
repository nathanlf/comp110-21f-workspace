"""List utility functions part 2."""

__author__ = "730483098"

# Define your functions below


def only_evens(nums: list[int]) -> list[int]:
    """Returns a list of even integers."""
    even_list: list[int] = list()
    i: int = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            even_list.append(nums[i])
        i += 1

    return even_list


def sub(nums: list[int], start: int, end: int) -> list[int]:
    """Returns a subset of a given list of integers."""
    sub_list: list[int] = list()
    if len(nums) < 0 or len(nums) < start or end <= 0:
        return sub_list  # Returns an empty list

    # Additional start/stop variables created to retain initial value of start & end in memory
    i: int = start
    stop: int = end

    if start < 0:
        i = 0
    if end > len(nums):
        stop = len(nums)  # When it says "end with the end of the list" - does it mean to include the end INDEX or not?
    
    while i < stop:
        sub_list.append(nums[i])
        i += 1

    return sub_list


def concat(nums_one: list[int], nums_two: list[int]) -> list[int]:
    """Returns a list of all elements of the first list followed by all elements of the second list."""
    concat_list: list[int] = list()

    i: int = 0
    while i < len(nums_one):
        concat_list.append(nums_one[i])
        i += 1

    j: int = 0
    while j < len(nums_two):
        concat_list.append(nums_two[j])
        j += 1

    return concat_list