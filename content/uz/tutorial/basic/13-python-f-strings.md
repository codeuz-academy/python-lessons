---
layout: tutorial.njk
lang: uz
title: Python f-string'lar
order: 13
permalink: /uz/tutorial/python-f-strings/
---

F-string'lar (formatted string literals) - Python'da string formatlashning zamonaviy va eng samarali usuli. Python 3.6 da kiritilgan f-string'lar toza sintaksis va yaxshi unumdorlik sababli string formatlash uchun de-fakto standartga aylandi.

### F-string asosiy sintaksisi

F-string'lar qo'shtirnoqdan oldin `f` yoki `F` harfi bilan boshlanadi, Python ifodalari esa jingalak qavslar `{}` ichida yoziladi:

```python
name = "Bob"
age = 25

# Using f-string
print(f"Hello, my name is {name} and I am {age} years old")
# Output: Hello, my name is Bob and I am 25 years old

# Can also use capital F
print(F"Welcome, {name}!")
```

### Eski usullar bilan solishtirish

F-string'lar paydo bo'lishidan oldin string formatlashning bir nechta yo'li bor edi:

```python
name = "Alice"
score = 95.5

# Old way 1: Concatenation(+)
print("Name: " + name + ", Score: " + str(score))

# Old way 2: % formatting
print("Name: %s, Score: %.1f" % (name, score))

# Old way 3: .format()
print("Name: {}, Score: {}".format(name, score))

# Modern way: f-string(RECOMMENDED)
print(f"Name: {name}, Score: {score}")
```

F-string'lar o'qilishi oson va bajarilishi tezroq!

### F-string ichida ifodalar

F-string jingalak qavslar ichida istalgan Python ifodasini hisoblay oladi:

```python
# Mathematical operations
a = 10
b = 5
print(f"Addition: {a + b}")       # Output: Addition: 15
print(f"Multiplication: {a * b}") # Output: Multiplication: 50
print(f"Division: {a / b:.2f}")   # Output: Division: 2.00

# Calling methods
name = "python"
print(f"Uppercase: {name.upper()}")  # Output: Uppercase: PYTHON
print(f"Capitalize: {name.capitalize()}")  # Output: Capitalize: Python

# Calling functions
import math
print(f"Root 16: {math.sqrt(16)}")   # Output: Root 16: 4.0

# Lists and indexing
fruits = ["apple", "orange", "mango"]
print(f"First fruit: {fruits[0]}")    # Output: First fruit: apple
```

### Sonlarni formatlash

F-string format specifier'lar yordamida sonlarni ko'rsatishni boshqaradi:

```python
# Decimal format
pi = 3.14159265359
print(f"Pi: {pi:.2f}")           # Output: Pi: 3.14
print(f"Pi: {pi:.4f}")           # Output: Pi: 3.1416

# Thousands separator format
population = 1500000
print(f"Population: {population:,}")       # Output: Population: 1,500,000
print(f"Population: {population:_}")       # Output: Population: 1_500_000

# Percentage format
ratio = 0.756
print(f"Percentage: {ratio:.1%}")      # Output: Percentage: 75.6%

# Minimum width format
number = 42
print(f"Number: {number:5}")       # Output: Number:    42 (width 5)
print(f"Number: {number:05}")      # Output: Number: 00042 (padding zero)

# Binary, octal, hexadecimal format
num = 255
print(f"Binary: {num:b}")        # Output: Binary: 11111111
print(f"Octal: {num:o}")         # Output: Octal: 377
print(f"Hex: {num:x}")           # Output: Hex: ff
print(f"Hex(uppercase): {num:X}")  # Output: Hex(uppercase): FF
```

### Tekislash (alignment)

```python
text = "Python"

# Left align(default)
print(f"{text:<15}")     # Output: "Python         "

# Right align
print(f"{text:>15}")     # Output: "         Python"

# Center align
print(f"{text:^15}")     # Output: "    Python     "

# With filler characters
print(f"{text:*^15}")    # Output: "****Python*****"
print(f"{text:-<15}")    # Output: "Python---------"
```

### Dictionary bilan f-string

```python
student = {
    "name": "Sara",
    "id": "12345",
    "gpa": 3.85
}

print(f"Name: {student['name']}, GPA: {student['gpa']}")
# Output: Name: Sara, GPA: 3.85
```

### F-string bilan debugging (Python 3.8+)

`=` specifier debugging uchun juda qulay:

```python
x = 10
y = 20

# Old way
print(f"x = {x}, y = {y}")

# New way with = (Python 3.8+)
print(f"{x=}, {y=}")              # Output: x=10, y=20
print(f"{x + y=}")                # Output: x + y=30
print(f"{x * 2=}")                # Output: x * 2=20
```

### Multiline f-string

```python
name = "Alice"
job = "Developer"
city = "New York"

# Using triple quotes
bio = f"""
User Profile
===============
Name      : {name}
Job       : {job}
City      : {city}
"""

print(bio)
```

### Jingalak qavslarni escape qilish

Agar literal `{` va `}` ni chiqarish kerak bo'lsa, ikki marta yozing:

{% raw %}
```python
print(f"This is curly braces: {{}}")    # Output: This is curly braces: {}
print(f"Python Set: {{{1, 2, 3}}}")   # Output: Python Set: {1, 2, 3}
```
{% endraw %}

### Amaliy misol

```python
# Creating a simple table
products = [
    ("Laptop", 15000000),
    ("Mouse", 250000),
    ("Keyboard", 750000),
]

print(f"{'Product':<15}{'Price':>15}")
print("-" * 30)
for name, price in products:
    print(f"{name:<15}{price:>15,}")

# Output:
# Product                  Price
# ------------------------------
# Laptop            15,000,000
# Mouse                250,000
# Keyboard             750,000
```

