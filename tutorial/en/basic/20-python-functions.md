---
layout: tutorial.njk
title: Python Functions
order: 20
permalink: /tutorial/en/python-functions/
---

<img src="/img/tutorial/17-belajar-fungsi-python-programming.webp" alt="Python Functions" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

A function is a reusable block of code used to perform a specific task.

### Defining Python Functions

Use `def` followed by the function name and parameters:

```python
def print_message(text):
    """Print a message to the console."""
    print(text)
```

Important rules:

- Function blocks start with `def`.
- Parameters are written inside parentheses.
- The function body is indented.
- `return` sends a value back to the caller.
- If no `return` is given, the function returns `None`.

### Parameters and Arguments

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))
print(greet("Bob", greeting="Hi"))
```

### Keyword Arguments

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(name="Milo", animal="cat")
```

### Special Parameter Types (Python 3)

Python supports positional-only and keyword-only parameters:

```python
def combine(a, b, /, sep="-", *, upper=False):
    text = f"{a}{sep}{b}"
    return text.upper() if upper else text

print(combine("py", "thon"))
print(combine("py", "thon", sep="_", upper=True))
```

- Parameters before `/` are positional-only.
- Parameters after `*` are keyword-only.

### Variable-Length Arguments

```python
def total(*numbers):
    return sum(numbers)


def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

print(total(1, 2, 3, 4))
show_info(name="Alice", age=22)
```

### `lambda` (Anonymous Function)

For short one-line functions:

```python
square = lambda x: x * x
print(square(5))
```

Use `def` for complex logic to keep code readable.
