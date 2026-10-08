"""factorial (specs/001-factorial)."""


def factorial(n: int) -> int:
    """n! for an integer n >= 0."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f"factorial expects an int, got {n!r}")
    if n < 0:
        raise ValueError(f"factorial expects n >= 0, got {n}")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
