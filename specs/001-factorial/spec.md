# 001 — factorial

## Goal

Provide `factorial(n)`, the product of all positive integers up to `n`.

## Requirements

1. `factorial(n)` is defined in `numkit/factorial.py`.
2. `factorial(0)` is `1`.
3. For any integer `n >= 1`, `factorial(n)` returns `n!` as an `int`. Python integers are
   unbounded, so there is no upper limit.
4. Any other input raises:
   - `TypeError` when `n` is not an `int` (for example `1.5`, `"3"`, `None`). `bool` is not
     accepted, even though it is a subclass of `int`.
   - `ValueError` when `n` is a negative integer.
