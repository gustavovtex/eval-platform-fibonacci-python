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

factorial(5)  # 120
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
