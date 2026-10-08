# 003 — fibonacci: input validation

## Goal

Make `fibonacci(n)` refuse bad input the same way `factorial(n)` does.

## Requirements

1. `fibonacci(n)` keeps its behavior for every integer `n >= 0`, and now raises:
   - `TypeError` when `n` is not an `int` (for example `1.5`, `"3"`, `None`). `bool` is not
     accepted, even though it is a subclass of `int`.
   - `ValueError` when `n` is a negative integer.
2. The checks live in one place that `fibonacci` uses, so the next function over Fibonacci numbers
   can reuse them instead of copying them.
3. `fibonacci` stays iterative and O(n).
4. `README.md` lists this spec.

## Note

The Node.js twin of this repository also adds `fibonacciBig(n)` in its spec 003, because a
JavaScript `number` loses precision above F(78). Python integers are unbounded, so `fibonacci(n)`
already covers that case here.
