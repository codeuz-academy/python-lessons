---
layout: tutorial.njk
lang: uz
title: Python funksiyalari
order: 20
permalink: /tutorial/uz/python-functions/
---

<img src="/img/tutorial/17-belajar-fungsi-python-programming.webp" alt="Python funksiyalari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Funksiya - ma'lum bir vazifani bajarish uchun qayta ishlatiladigan (reusable) kod bloki.

### Python funksiyalarini aniqlash

`def` kalit so'zi, so'ng funksiya nomi va parametrlar yoziladi:

```python
def print_message(text):
    """Print a message to the console."""
    print(text)
```

Muhim qoidalar:

- Funksiya bloklari `def` bilan boshlanadi.
- Parametrlar `()` ichida yoziladi.
- Funksiya tanasi indentatsiya bilan ajratiladi.
- `return` qiymatni chaqiruvchiga qaytaradi.
- Agar `return` bo'lmasa, funksiya `None` qaytaradi.

### Parametrlar va argumentlar

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))
print(greet("Bob", greeting="Hi"))
```

### Keyword argumentlar

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(name="Milo", animal="cat")
```

### Maxsus parametr turlari (Python 3)

Python positional-only va keyword-only parametrlarni qo'llab-quvvatlaydi:

```python
def combine(a, b, /, sep="-", *, upper=False):
    text = f"{a}{sep}{b}"
    return text.upper() if upper else text

print(combine("py", "thon"))
print(combine("py", "thon", sep="_", upper=True))
```

- `/` dan oldingi parametrlar positional-only.
- `*` dan keyingi parametrlar keyword-only.

### O'zgaruvchan uzunlikdagi argumentlar

```python
def total(*numbers):
    return sum(numbers)


def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

print(total(1, 2, 3, 4))
show_info(name="Alice", age=22)
```

### `lambda` (anonim funksiya)

Qisqa, bir qatordan iborat funksiyalar uchun:

```python
square = lambda x: x * x
print(square(5))
```

Murakkab logika uchun kod o'qilishini saqlash maqsadida `def` ishlating.

