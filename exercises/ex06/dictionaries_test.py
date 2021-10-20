"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730483098"


def test_invert_empty() -> None:
    """Tests when the given dictionary is empty."""
    dictionary: dict[str, str] = dict()
    assert invert(dictionary) == {}


def test_invert_one_pair() -> None:
    """Tests when the given dictionary has one key-value pair."""
    dictionary: dict[str, str] = {'a': 'b'}
    assert invert(dictionary) == {'b': 'a'}


def test_invert_multiple_pairs() -> None:
    """Tests when the given dictionary has one key-value pair."""
    dictionary: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(dictionary) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_favorite_color_empty() -> None:
    """Tests when the given dictionary is empty."""
    dictionary: dict[str, str] = {}
    assert favorite_color(dictionary) == ""


def test_favorite_color_one_pair() -> None:
    """Tests when the given dictionary has one key-value pair."""
    dictionary: dict[str, str] = {'Nathan': 'blue'}
    assert favorite_color(dictionary) == "blue"


def test_favorite_color_multiple_pairs() -> None:
    """Tests when the given dictionary has more than one key-value pair."""
    dictionary: dict[str, str] = {'Nathan': 'blue', 'Josh': 'red', 'Khat': 'red'}
    assert favorite_color(dictionary) == "red"


def test_count_empty() -> None:
    """Tests when the given list is empty."""
    my_list: list[str] = list()
    assert count(my_list) == {}


def test_count_one_value() -> None:
    """Tests when the given list has one value."""
    my_list: list[str] = ['uno']
    assert count(my_list) == {'uno': 1}


def test_count_multiple_values() -> None:
    """Tests when the given list has more than one value."""
    my_list: list[str] = ['uno', 'dos', 'dos']
    assert count(my_list) == {'uno': 1, 'dos': 2}