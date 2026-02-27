---
layout: tutorial.njk
lang: uz
title: Python izohlari (comments)
order: 5
permalink: /uz/tutorial/python-comments/
---

<img src="/img/tutorial/5-komentar-pada-python.webp" alt="Python izohlari (comments)" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Izohlar (comments) - bu source code ichidagi qaydlar bo'lib, Python ularni bajarish vaqtida e'tiborga olmaydi.

Izohlar orqali maqsadni (intent), taxminlarni (assumptions) va muhim detallarni tushuntiring.

### Bir qatorli izohlar

`#` dan foydalaning:

```python
# This is a comment
print("Hello World")  # Inline comment
```

### Ko'p qatorli tushuntirishlar

Python'da alohida "multi-line comment" sintaksisi yo'q. Keng tarqalgan uslub - bir nechta `#` qatorlardan foydalanish:

```python
# This block explains why we do something,
# not only what the code does.
# Keep comments concise and useful.
```

Uch tirnoqli matnlar (`""" ... """`) - bu string, haqiqiy comment emas. Odatda docstring uchun ishlatiladi.

### Docstring namunasi

```python
def greet(name):
    """Return greeting text for a name."""
    return f"Hello, {name}"
```

### To'liq misol

Quyidagi skript comment'lar real kod bilan qanday ishlashini ko'rsatadi. Faqat `print()` chaqiruvlari natija beradi:

```python
# Print a greeting
print("Hello World")

# The line below is commented out, so it will not run
# print("This will not be printed")

print("Bob")    # prints a name
print(123)      # prints a number
```

Natija:

```text
Hello World
Bob
123
```

