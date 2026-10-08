"""fibonacci (specs/002-fibonacci)."""


def fibonacci(n: int) -> int:
    """F(n) for an integer n >= 0, computed iteratively in O(n)."""
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous
