---
layout: tutorial.njk
lang: en
title: Hello World Python
order: 4
permalink: /en/tutorial/hello-world-python/
---

<img src="/img/tutorial/4-hello-world-python.webp" alt="Hello World Python" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

The first Python program is usually a single `print()` call. The `print()` function writes text to standard output (your terminal or console).

### Basic Syntax

```python
print("Hello World")
```

When you run the script above, Python prints:

`Hello World`

The text inside the parentheses is called an **argument**. String arguments must be wrapped in quotes, either single quotes (`'...'`) or double quotes (`"..."`). Both are equivalent:

```python
print('Hello World')
print("Hello World")
```

You can also print numbers and expressions without quotes:

```python
print(42)
print(10 + 5)
```

### Indentation

Python uses indentation (whitespace at the beginning of a line) to define code blocks. Unlike many languages that use braces `{}`, Python relies on consistent indentation:

```python
if True:
    print("This is indented")
```

Using incorrect indentation raises an `IndentationError`.

### Python Case Sensitivity

Python is case-sensitive. `print()` works, but `Print()` or `PRINT()` raises `NameError`.

This rule also applies to variable names and function names. For example, `name` and `Name` are two different variables.
