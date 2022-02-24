"""Docstring."""

schools: dict[str, int]
schools = {"UNC": 19000, "Duke": 6000, "NCSU": 24000}
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")