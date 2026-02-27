---
layout: tutorial.njk
lang: en
title: Python File I/O
order: 23
permalink: /en/tutorial/python-file-io/
---

<img src="/img/tutorial/19-dasar-dasar-io-python.webp" alt="Python File I/O" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

This section covers basic input/output operations in Python 3.

### Output with `print()`

`print()` converts values to text and writes to standard output.

```python
print("Python is a great programming language")
print("A", "B", "C", sep="-")
```

### Keyboard Input with `input()`

In Python 3, `input()` always returns a string.

```python
name = input("Your name: ")
age = int(input("Your age: "))
print(f"Hello {name}, next year you are {age + 1}")
```

### Reading Files

Use `with` to ensure files are closed automatically.

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

Common read methods:

- `read()` -> all content
- `readline()` -> one line
- `readlines()` -> list of lines

### Writing Files

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("learn python\n")
    f.write("File I/O is important\n")
```

File modes:

- `"r"` read
- `"w"` write (overwrite)
- `"a"` append
- `"x"` create new file
- Add `"b"` for binary mode (`"rb"`, `"wb"`)

### Safe JSON I/O Example

```python
import json

data = {"name": "Alice", "level": "intermediate"}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("user.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)
```
