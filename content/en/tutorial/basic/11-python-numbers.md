---
layout: tutorial.njk
lang: en
title: Python Number
order: 11
permalink: /en/tutorial/python-numbers/
---

<img src="/img/tutorial/11-tipe-data-number-pada-python.webp" alt="Python Number Data Types - Int, Float, Complex" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python has three built-in numeric types:

- `int` (integer)
- `float` (floating-point)
- `complex` (complex numbers)

Numbers are immutable: changing a number value creates a new object.

| Type | Examples |
| -------- | ------------------------- |
| `int` | `20`, `-13`, `0`, `0x56` |
| `float` | `0.1`, `1.20`, `-92.0`, `6.02e23` |
| `complex` | `3+4j`, `35j`, `3.12e-12j` |

> In Python 3, integer literals like `020` are invalid. Use `20` for decimal or `0o24` for octal.

### Python Number Data Type Conversion

Use built-in constructors for conversion:

- `int(x)` converts `x` to integer.
- `float(x)` converts `x` to floating-point number.
- `complex(x)` converts `x` to complex number with real part `x`.
- `complex(x, y)` converts to complex number `x + yj`.

### Python Mathematical Functions

Python provides built-ins and the `math` module for mathematical operations.

| Name | Usage | Explanation |
| ------------ | ----------------- | -------------------------------------------------------------------- |
| Absolute | `abs(x)` | Absolute value of `x` |
| Power | `pow(x, y)` | Equivalent to `x ** y` |
| Round | `round(x, n)` | Rounds to `n` digits (or nearest integer if omitted) |
| Maximum | `max(a, b, ...)` | Largest value |
| Minimum | `min(a, b, ...)` | Smallest value |
| Square Root | `math.sqrt(x)` | Square root of `x` |
| Ceiling | `math.ceil(x)` | Smallest integer `>= x` |
| Floor | `math.floor(x)` | Largest integer `<= x` |
| Logarithm | `math.log(x)` | Natural logarithm |

```python
import math

print(abs(-9))
print(pow(2, 5))
print(round(2.675, 2))
print(math.sqrt(16))
```

### Python Random Number Functions

The `random` module is often used in simulations, tests, and games.

| Name | Usage | Explanation |
| --------- | ----------------------------------- | ----------------------------------------------------------- |
| Choice | `choice(seq)` | Random item from sequence |
| RandRange | `randrange(start, stop, step)` | Random value from range |
| Random | `random()` | Random float in `[0.0, 1.0)` |
| Seed | `seed(x)` | Set random seed |
| Shuffle | `shuffle(lst)` | Shuffle list in place |
| Uniform | `uniform(x, y)` | Random float in `[x, y]` |

### Python Trigonometric Functions

`math` provides trigonometric helpers:

| Name | Usage | Explanation |
| ------- | --------------------- | ------------------------------------------------- |
| Cosine | `math.cos(x)` | Cosine of `x` in radians |
| Sine | `math.sin(x)` | Sine of `x` in radians |
| Tangent | `math.tan(x)` | Tangent of `x` in radians |
| Degrees | `math.degrees(x)` | Convert radians to degrees |
| Radians | `math.radians(x)` | Convert degrees to radians |

### Python Mathematical Constants

| Name | Usage | Explanation |
| ---- | ---------- | ----------------------- |
| Pi | `math.pi` | Mathematical constant pi |
| e | `math.e` | Mathematical constant e |

### Floating-Point Arithmetic: Representation and Limits

Floating-point numbers are binary approximations, so some decimal values cannot be represented exactly.

```python
print(0.1 + 0.1 + 0.1)     # 0.30000000000000004
print(0.1 + 0.1 + 0.1 == 0.3)  # False
```

Use safer comparisons:

```python
import math

print(math.isclose(0.1 + 0.1 + 0.1, 0.3))  # True
```

For exact decimal arithmetic (for example, money), use `decimal`:

```python
from decimal import Decimal

price = Decimal("0.1") + Decimal("0.1") + Decimal("0.1")
print(price == Decimal("0.3"))  # True
```

For exact fractions, use `fractions.Fraction`:

```python
from fractions import Fraction

print(Fraction(1, 10) * 3 == Fraction(3, 10))  # True
```

### Notes on `round()`

Python uses "round half to even" for ties:

```python
print(round(0.5))  # 0
print(round(1.5))  # 2
print(round(2.5))  # 2
```
