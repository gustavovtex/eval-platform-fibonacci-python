# eval-platform-fibonacci-python

Small number utilities in plain Python, with no dependencies.

This repository is a fixture for the [eval platform](https://github.com/vtex/eval-platform): its
pull requests are small, each one carries its own spec under `specs/`, and the whole test suite
runs in under a second. That makes it a cheap way to check that an evaluation works end to end,
locally and in production. It is not meant to tell models apart: the tasks are too easy for that.

A twin repository, `eval-platform-fibonacci-node`, has the same history in Node.js.

## Usage

```python
from numkit.factorial import factorial
from numkit.fibonacci import fibonacci, fibonacci_sequence

factorial(5)  # 120
fibonacci(10)  # 55
fibonacci_sequence(5)  # [0, 1, 1, 2, 3]
```

## Tests

```sh
python -m unittest discover -s tests -v
```

Python 3.10 or newer. Nothing to install: the tests use the standard library's `unittest`.

## Specs

Every change starts with a spec in `specs/NNN-name/spec.md`.

| Spec | Feature |
|---|---|
| [001-factorial](specs/001-factorial/spec.md) | `factorial(n)` |
| [002-fibonacci](specs/002-fibonacci/spec.md) | `fibonacci(n)` |
| [003-fibonacci-validation](specs/003-fibonacci-validation/spec.md) | input validation |
| [004-fibonacci-sequence](specs/004-fibonacci-sequence/spec.md) | `fibonacci_sequence(count)` |
