# 004 — fibonacci sequence

## Goal

Provide `fibonacci_sequence(count)`, the first `count` Fibonacci numbers, for callers that need the
whole sequence instead of a single term.

## Requirements

1. `fibonacci_sequence(count)` is defined in `numkit/fibonacci.py` and returns a `list` of `count`
   `int` values: `[F(0), F(1), ..., F(count - 1)]`. `fibonacci_sequence(0)` is `[]`.
2. `count` is validated like `fibonacci(n)`: `TypeError` when it is not an `int` (`bool` included),
   `ValueError` when it is negative. It is also capped: `ValueError` when it is above 10000.
3. The sequence is built in a single pass, O(count). Calling `fibonacci` once per term
   (O(count²)) does not meet this requirement.
4. Every call returns a new list. A caller may sort, extend or clear the list it received, and no
   later call returns a different result because of it. In particular, a module-level cache, if one
   is used, is never handed to the caller.
5. `fibonacci_sequence(10000)` completes in under 100 ms on a current laptop.
6. `README.md` lists this spec and shows `fibonacci_sequence` in the usage example.
