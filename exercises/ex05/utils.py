"""List Functions Of Various Types."""

__author__ = "730473612"


def only_evens(nums: list[int]) -> list[int]:
    """Returns list of only even numbers."""
    i: int = 0
    evens: list[int] = []
    while i < len(nums):
        if nums[i] % 2 == 0:
            evens.append(nums[i])
        i += 1
    return evens


def sub(nums: list[int], start: int, end: int) -> list[int]:
    """Returns values from list of ints between start and end."""
    subset: list[int] = []
    i: int = start
    j: int = end
    if i < 0:
        i = 0
    if j > len(nums):
        j = len(nums)
    if len(nums) == 0 or start > len(nums) or end <= 0:
        return subset
    while i < j:
        subset.append(nums[i])
        i += 1
    return subset


def concat(first: list[int], second: list[int]) -> list[int]:
    """Returns elements of second list added to first list."""
    total: list[int] = first
    i: int = 0
    while i < len(second):
        total.append(second[i])
        i += 1
    return total
        
