"""The Most Boring Object, Reviewed in One Line — a make.fun entry.

Prints exactly one line, at most 200 characters, reviewing the most
boring everyday object I could think of: the doorstop.
"""

LINE = (
    "The doorstop: five stars for effort, zero for ambition — it has "
    "held the same door, the same way, for nine years, and, between us, "
    "so have I."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
