"""Tests functions using dictionaries."""

__author__ = "730473612"

from dictionary import invert, favorite_color


def invert_empty() -> None:
    """Tests that invert will return an empty function if an empty function is entered."""
    test: dict[str, str] = {}
    assert invert(test) == {}


def invert_use_case_1() -> None:
    """Tests that invert will return an inverse function for a single key."""
    test: dict[str, str] = {"a": "b"}
    assert invert(test) == {"b": "a"}


def invert_use_case_2() -> None:
    """Tests that invert will return an inverse function for a multiple keys."""
    test: dict[str, str] = {"Jack": "Jill", "Luke": "Sean"}
    assert invert(test) == {"Jill": "Jack", "Sean": "Luke"}


def color_empty() -> None:
    """Tests that an empty dictionary will return an empty string."""
    test: dict[str, str] = {}
    assert favorite_color(test) == ""


def color_use_case_1() -> None:
    """Tests that a dictionary with one input wil return one input."""