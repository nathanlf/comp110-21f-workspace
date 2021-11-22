"""Helper functions for analysis."""

__author__ = "730483098"


def percentage(table: dict[str, int], response: str) -> float:
    """Calculates the percentage of values in a dictionary that have a certain value out of the total."""
    total: int = 0
    for val in table:
        total += table[val]
    return table[response] / total