---
layout: tutorial.njk
lang: uz
title: Python ro'yxat generatsiyasi (list comprehension)
order: 15
permalink: /uz/tutorial/python-list-comprehension/
---

List comprehension - mavjud list'dan yangi list yaratishning ixcham va chiroyli usuli. Bu Python'ga xos (pythonic) imkoniyatlardan biri bo'lib, kodni toza va o'qilishi oson qiladi.

### Asosiy sintaksis

```python
# Sintaksis: [ifoda for element in ketma-ketlik]

# Oddiy loop bilan
squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# List comprehension bilan (qisqaroq!)
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

### Shart bilan (`if`)

Elementlarni filtrlash uchun shart qo'shish mumkin:

```python
# Sintaksis: [ifoda for element in ketma-ketlik if shart]

# Faqat juft sonlar
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Faqat musbat sonlar
data = [-5, 3, -2, 8, -1, 7]
positive = [x for x in data if x > 0]
print(positive)  # [3, 8, 7]

# Muayyan harf bilan boshlanadigan satrlarni filtrlash
fruits = ["apple", "orange", "grape", "mango", "avocado"]
a_fruits = [f for f in fruits if f.startswith("a")]
print(a_fruits)  # ['apple', 'avocado']
```

### `if`-`else` bilan

`if`-`else` ishlatish uchun uni `for` dan oldin yozing:

```python
# Sintaksis: [agar_ifoda if shart else aks_ifoda for element in ketma-ketlik]

# Manfiy sonlarni 0 bilan almashtirish
numbers = [-3, 5, -1, 8, -2, 6]
result = [x if x > 0 else 0 for x in numbers]
print(result)  # [0, 5, 0, 8, 0, 6]

# Juft/toq deb belgilash
label = ["juft" if x % 2 == 0 else "toq" for x in range(5)]
print(label)  # ['juft', 'toq', 'juft', 'toq', 'juft']
```

### Nested list comprehension

Nested list'lar bilan ishlash uchun:

```python
# Ichki list'ni tekislash
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehension bilan matritsa yaratish
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# Ko'paytirish matritsasi
mult_matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(mult_matrix)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### Funksiyalar bilan

```python
# List comprehension ichida funksiya ishlatish
words = ["hello", "world", "python"]
uppercase = [w.upper() for w in words]
print(uppercase)  # ['HELLO', 'WORLD', 'PYTHON']

# O'z funksiyangizni ishlatish
def square(n):
    return n ** 2

result = [square(x) for x in range(5)]
print(result)  # [0, 1, 4, 9, 16]

# Lambda ishlatish
result = [(lambda x: x ** 2)(x) for x in range(5)]
print(result)  # [0, 1, 4, 9, 16]
```

### Dictionary comprehension

Xuddi shu g'oya dictionary uchun ham ishlaydi:

```python
# Sintaksis: {kalit: qiymat for element in ketma-ketlik}

# List'dan dictionary yaratish
names = ["Alice", "Bob", "Carol"]
lengths = {n: len(n) for n in names}
print(lengths)  # {'Alice': 4, 'Bob': 4, 'Carol': 5}

# Shart bilan dictionary
numbers = range(1, 6)
squares = {x: x**2 for x in numbers if x % 2 == 1}
print(squares)  # {1: 1, 3: 9, 5: 25}

# Dictionary'ni teskari aylantirish
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

### Set comprehension

List kabi, lekin natija set bo'ladi (takror element yo'q):

```python
# Sintaksis: {ifoda for element in ketma-ketlik}

# Takrorli list'dan set yaratish
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in numbers}
print(unique)  # {1, 2, 3, 4}

# Shart bilan set
even_unique = {x for x in range(20) if x % 2 == 0}
print(even_unique)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
```

### Generator expression

List comprehension'ga o'xshaydi, lekin `()` ishlatadi va xotirani tejaydi:

```python
# Generator ifodasi (lazy evaluation)
gen = (x ** 2 for x in range(1000000))
print(gen)  # <generator object ...>

# Faqat kerak bo'lganda hisoblaydi
print(next(gen))  # 0
print(next(gen))  # 1
print(sum(gen))   # Qolganlarining yig'indisi

# Katta ma'lumotlar uchun foydali
# List: hammasini xotirada saqlaydi
# Generator: bittadan hisoblaydi
```

### Amaliy misol

```python
# 1. Cleaning data
dirty_data = ["  Alice  ", "BOB", "carol  ", "  DAVID"]
clean_data = [name.strip().title() for name in dirty_data]
print(clean_data)  # ['Alice', 'Bob', 'Carol', 'David']

# 2. Extract file extension
files = ["doc.pdf", "image.png", "data.csv", "script.py"]
extensions = [f.split(".")[-1] for f in files]
print(extensions)  # ['pdf', 'png', 'csv', 'py']

# 3. Filter and transform at once
scores = [45, 78, 92, 56, 88, 34, 95]
passed = [f"Score: {n} (Passed)" for n in scores if n >= 60]
print(passed)  # ['Score: 78 (Passed)', 'Score: 92 (Passed)', ...]

# 4. Zip two lists
names = ["Alice", "Bob", "Carol"]
ages = [25, 30, 28]
combined = {n: a for n, a in zip(names, ages)}
print(combined)  # {'Alice': 25, 'Bob': 30, 'Carol': 28}

# 5. Create lookup table
letters = "abcdefghij"
positions = {l: i for i, l in enumerate(letters, start=1)}
print(positions)  # {'a': 1, 'b': 2, 'c': 3, ...}
```

### Qachon list comprehension ishlatish kerak?

<i class="fa-solid fa-circle-check" aria-hidden="true"></i> **List comprehension ishlating**, agar:
- Oddiy transformatsiya bilan yangi list yaratayotgan bo'lsangiz
- List ichidan elementlarni filtrlayotgan bo'lsangiz
- Kod o'qilishi yaxshilanayotgan bo'lsa

<i class="fa-solid fa-circle-xmark" aria-hidden="true"></i> **List comprehension'dan qoching**, agar:
- Logika juda murakkab bo'lsa (2 tadan ko'p shart)
- Bir nechta statement kerak bo'lsa
- Kod o'qilishi yomonlashsa

```python
# Juda murakkab - oddiy loop ishlating
# Bundan qoching:
result = [func(x) if cond1(x) else other(x) for x in data if cond2(x) and cond3(x)]

# Yaxshiroq:
result = []
for x in data:
    if cond2(x) and cond3(x):
        if cond1(x):
            result.append(func(x))
        else:
            result.append(other(x))
```
