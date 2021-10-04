"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730483098"


def test_only_evens_empty() -> None:
    """Tests when the given list is empty."""
    nums: list[int] = list()
    assert only_evens(nums) == []


def test_only_evens_single_item_odd() -> None:
    """Tests when a given list contains a single item that is odd."""
    nums: list[int] = [1]
    assert len(only_evens(nums)) == 0


def test_only_evens_single_item_even() -> None:
    """Tests when a given list contains a single item that is even."""
    nums: list[int] = [2]
    assert only_evens(nums) == [2]


def test_only_evens_many_items_all_odd() -> None:
    """Tests when a given list contains many items that are all odd."""
    nums: list[int] = [1, 3, 5]
    assert only_evens(nums) == []


def test_only_evens_many_items_all_even() -> None:
    """Tests when a given list contains many items that are all even."""
    nums: list[int] = [2, 4, 6]
    assert only_evens(nums) == [2, 4, 6]


def test_only_evens_many_items_both() -> None:
    """Tests when a given list contains many items that are both even and odd."""
    nums: list[int] = [2, 3, 4, 5]
    assert only_evens(nums) == [2, 4]


def test_sub_empty() -> None:
    """Tests when the given list is empty."""
    nums: list[int] = list()
    assert sub(nums, 0, 1) == []


def test_sub_single_item() -> None:
    """Tests when the given list contains one item."""
    nums: list[int] = [3]
    assert sub(nums, 0, 1) == [3]


def test_sub_many_items() -> None:
    """Tests when the given list contains many items."""
    nums: list[int] = [3, 5, 2, -10, 4]
    assert sub(nums, 1, 3) == [5, 2]


def test_concat_both_empty() -> None:
    """Tests when the given lists are both empty."""
    nums1: list[int] = list()
    nums2: list[int] = list()
    assert concat(nums1, nums2) == []


def test_concat_list_one_empty() -> None:
    """Tests when the first given list is empty and the second contains items."""
    nums1: list[int] = list()
    nums2: list[int] = [1, 2, 3]
    assert concat(nums1, nums2) == [1, 2, 3]


def test_concat_list_two_empty() -> None:
    """Tests when the first given list contains items and the second is empty."""
    nums1: list[int] = [1, 2, 3]
    nums2: list[int] = list()
    assert concat(nums1, nums2) == [1, 2, 3]


def test_concat_single_item_both() -> None:
    """Tests when both given lists contain one item each."""
    nums1: list[int] = [1]
    nums2: list[int] = [2]
    assert concat(nums1, nums2) == [1, 2]


def test_concat_many_items_both() -> None:
    """Tests when both given lists contain many items."""
    nums1: list[int] = [1, 2, 3]
    nums2: list[int] = [4, 5, 6]
    assert concat(nums1, nums2) == [1, 2, 3, 4, 5, 6]