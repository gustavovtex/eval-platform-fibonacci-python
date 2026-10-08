"""fibonacci (specs/002-fibonacci, specs/003-fibonacci-validation, specs/004-fibonacci-sequence)."""

MAX_SEQUENCE_LENGTH = 10000
"""The longest sequence fibonacci_sequence builds (specs/004-fibonacci-sequence)."""


def _check_non_negative_int(name: str, n: object) -> None:
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f"{name} expects an int, got {n!r}")
    if n < 0:
        raise ValueError(f"{name} expects n >= 0, got {n}")


def fibonacci(n: int) -> int:
    """F(n) for an integer n >= 0, computed iteratively in O(n)."""
    _check_non_negative_int("fibonacci", n)
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def fibonacci_sequence(count: int) -> list[int]:
    """[F(0), ..., F(count - 1)], built in one pass. Every call builds and returns a new list."""
    _check_non_negative_int("fibonacci_sequence", count)
    if count > MAX_SEQUENCE_LENGTH:
        raise ValueError(f"fibonacci_sequence expects count <= {MAX_SEQUENCE_LENGTH}, got {count}")
    sequence = []
    previous, current = 0, 1
    for _ in range(count):
        sequence.append(previous)
        previous, current = current, previous + current
    return sequence
