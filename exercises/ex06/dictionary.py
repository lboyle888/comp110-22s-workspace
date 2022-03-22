"""Sets up functions using dictionaries."""

__author__ = "730473612"


def invert(ordered: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and returns the keys and values inverted."""
    inverse: dict[str, str] = {}
    new_values: list[str] = []
    new_keys: list[str] = []
    for key in ordered:
        new_values.append(key)
        new_keys.append(ordered[key])
    count: int = 0
    j: int = 0
    while count < len(new_keys):
        while j < len(new_keys):
            if count != j and new_keys[count] == new_keys[j]:
                raise KeyError("Two values are equal")
            j += 1
        count += 1
        j = 0
    length: int = len(new_values)
    i: int = 0
    while i < length:
        inverse[f"{new_keys[i]}"] = f"{new_values[i]}"
        i += 1
    return inverse


def favorite_color(colors: dict[str, str]) -> str:
    """Takes a dictionary and returns the most common key."""
    count: int = 0
    current_count: int = 0
    fav_color: str = ""
    for item in colors:
        for key in colors:
            if colors[item] == colors[key]:
                count += 1
        if count > current_count:
            current_count = count
            fav_color = colors[item]
        count = 0
    return fav_color


def count(values: list[str]) -> dict[str, int]:
    """Takes a list and returns a dictionary with values equal to number of times a string is in the list."""
    count: int = 0
    i: int = 0
    j: int = 0
    calculated: dict[str, int] = {}
    while i < len(values):
        while j < len(values):
            if i != j and values[i] == values[j]:
                count += 1
                values.pop(j)
            else:
                j += 1
        calculated[values[i]] = count + 1
        count = 0
        j = 0
        i += 1
    return calculated

    