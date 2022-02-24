"""Tests for List Functions Of Various Types."""

__author__ = "730473612"

from utils import only_evens, sub, concat


def test_only_evens_all_even() -> None:
    """Checks that all values are returned."""
    evens: list[int] = [2, 2, 4, 6]
    assert only_evens(evens) == [2, 2, 4, 6]


def test_only_evens_all_odd() -> None:
    """Checks that no values are returned."""
    evens: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(evens) == []


def test_only_evens_use_1() -> None:
    """Checks that only evens are returned."""
    evens: list[int] = [10, 20, 21, 22, 23, 25]
    assert only_evens(evens) == [10, 20, 22]


def test_only_evens_use_2() -> None:
    """Checks that only evens are returned."""
    evens: list[int] = [1, 2, 7, 9, 10, 100]
    assert only_evens(evens) == [2, 10, 100]


def test_sub_use_1() -> None:
    """Checks that only elements within subset are returned."""
    start: int = 1
    end: int = 3
    nums: list[int] = [10, 20, 30, 40]
    assert sub(nums, start, end) == [20, 30]
    

def test_sub_use_2() -> None:
    """Checks that only elements within subset are returned."""
    start: int = -3
    end: int = 7
    nums: list[int] = [1, 2, 3, 4, 5]
    assert sub(nums, start, end) == [1, 2, 3, 4, 5]


def test_sub_empty() -> None:
    """Checks that an empty list is returned if an empty list is inputted."""
    start: int = 1
    end: int = 3
    nums: list[int] = []
    assert sub(nums, start, end) == []


def test_concat_empties() -> None:
    """Checks that two empty lists will return an empty list."""
    first: list[int] = []
    second: list[int] = []
    assert concat(first, second) == []


def test_concat_use_1() -> None:
    """Checks that two empty lists will return an empty list."""
    first: list[int] = [1, 2, 3]
    second: list[int] = [4, 5, 6]
    assert concat(first, second) == [1, 2, 3, 4, 5, 6] 


def test_concat_use_2() -> None:
    """Checks that two empty lists will return an empty list."""
    first: list[int] = [-1, -1, 10, 100]
    second: list[int] = [-2, -2, 20, 200]
    assert concat(first, second) == [-1, -1, 10, 100, -2, -2, 20, 200] 
    
