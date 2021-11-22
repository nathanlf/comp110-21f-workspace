"""Utility functions."""

__author__ = "730483098"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the flie when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]  # Assumes non-empty parameter
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Returns a new column-based 'table' with a certain number of rows from the data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        values: list[str] = []
        i: int = 0
        while i < n:
            values.append(table[column][i])
            i += 1
            if n > len(table[column]):
                return table
        result[column] = values

    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Returns a new dictionary that includes only the columns selected from the original dictionary."""
    result: dict[str, list[str]] = {}
    for name in names:
        result[name] = table[name]

    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two dictionary into a new column-based 'table'."""
    result: dict[str, list[str]] = {}
    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if column in result:
            for val in table2[column]:
                result[column].append(val)
        else:
            result[column] = table2[column]

    return result


def count(array: list[str]) -> dict[str, int]:
    """Returns a dictionary of unique values from the list and how many times they occur."""
    result: dict[str, int] = {}
    for item in array:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result