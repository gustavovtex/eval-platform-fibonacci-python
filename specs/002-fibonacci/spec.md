# 002 — fibonacci

## Goal

Provide `fibonacci(n)`, the n-th Fibonacci number, with `F(0) = 0`, `F(1) = 1` and
`F(n) = F(n - 1) + F(n - 2)`.

## Requirements

1. `fibonacci(n)` is defined in `numkit/fibonacci.py`.
2. For an integer `n >= 0`, `fibonacci(n)` returns `F(n)` as an exact `int`.
3. The computation is iterative and runs in O(n) time: no recursion, no exponential blow-up.
4. `README.md` lists the new function in its specs table and shows a usage example.

## Out of scope

Input validation. It comes in a later spec.
