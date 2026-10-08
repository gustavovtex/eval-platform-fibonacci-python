"""fibonacci (specs/002-fibonacci, specs/003-fibonacci-validation)."""


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
