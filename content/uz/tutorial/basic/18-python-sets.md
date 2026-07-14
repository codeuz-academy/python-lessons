---
layout: tutorial.njk
lang: uz
title: Python to'plamlar (sets)
description: "Takrorlanmaydigan, tartibsiz to'plamlar va set'lar yaxshi bajaradigan birlashma va kesishma amallari bilan ishlang."
order: 18
permalink: /uz/tutorial/python-sets/
---

<img src="/img/tutorial/18-python-sets.webp" alt="Python to'plamlar (sets)" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Set — Python'dagi takrorlanmaydigan (`unique`) va tartibsiz (`unordered`) elementlar to'plami. Set'lar a'zolikni tekshirishda (`membership`), dublikatlarni olib tashlashda va `union` / `intersection` / `difference` kabi matematik amallarda juda samarali.

### Set yaratish

```python
# Jingalak qavslar bilan
fruits = {"apple", "orange", "mango"}
print(fruits)  # {'apple', 'orange', 'mango'}

# set() konstruktori bilan
numbers = set([1, 2, 3, 4, 5])
print(numbers)  # {1, 2, 3, 4, 5}

# Bo'sh set (albatta set() ishlating, {} emas)
empty = set()
print(empty)  # set()
print(type(empty))  # <class 'set'>

# {} dictionary yaratadi, set emas!
not_set = {}
print(type(not_set))  # <class 'dict'>
```

### Set xususiyatlari

```python
# 1. Takrorlanmas elementlar
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}

# 2. Tartibsiz
letters = {"c", "a", "b"}
print(letters)  # Tartib har xil bo'lishi mumkin

# 3. Indeks bilan olish mumkin emas
# letters[0]  # Xato! TypeError

# 4. Elementlar hashable (o'zgarmas) bo'lishi kerak
valid = {1, "hello", (1, 2)}  # To'g'ri
# invalid = {1, [1, 2]}  # Xato! List hashable emas
```

### Element qo'shish va o'chirish

```python
fruits = {"apple", "orange"}

# Bitta element qo'shish
fruits.add("mango")
print(fruits)  # {'apple', 'orange', 'mango'}

# Bir nechta element qo'shish
fruits.update(["banana", "grape"])
print(fruits)  # {'apple', 'orange', 'mango', 'banana', 'grape'}

# Elementni o'chirish (topilmasa xato beradi)
fruits.remove("apple")
print(fruits)

# Elementni o'chirish (topilmasa xato bermaydi)
fruits.discard("durian")  # Xato yo'q
print(fruits)

# Tasodifiy elementni o'chirish
item = fruits.pop()
print(f"O'chirildi: {item}")

# Barcha elementlarni o'chirish
fruits.clear()
print(fruits)  # set()
```

### A'zolik amallari

Set a'zolikni tekshirishda (membership) juda tez (O(1) murakkablik):

```python
numbers = {1, 2, 3, 4, 5}

# Set ichida mavjudligini tekshirish
print(3 in numbers)      # True
print(10 in numbers)     # False
print(10 not in numbers) # True

# Katta ma'lumotlarda list bilan solishtirish
# Set: O(1) - juda tez
# List: O(n) - katta ma'lumotlarda sekin
```

### Matematik amallar

#### Union

Ikkala set'dagi barcha elementlarni birlashtiradi:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# | operatori bilan
combined = A | B
print(combined)  # {1, 2, 3, 4, 5, 6}

# Metod bilan
combined = A.union(B)
print(combined)  # {1, 2, 3, 4, 5, 6}
```

#### Intersection

Ikkalasida ham bor bo'lgan elementlar:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# & operatori bilan
intersection = A & B
print(intersection)  # {3, 4}

# Metod bilan
intersection = A.intersection(B)
print(intersection)  # {3, 4}
```

#### Difference

Birinchi set'da bor, ikkinchisida yo'q elementlar:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# A - B: A da bor, B da yo'q elementlar
diff = A - B
print(diff)  # {1, 2}

# B - A: B da bor, A da yo'q elementlar
diff = B - A
print(diff)  # {5, 6}

# Metod bilan
diff = A.difference(B)
print(diff)  # {1, 2}
```

#### Symmetric difference

Ikkalasidan birida bor, lekin ikkalasida birga emas elementlar:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# ^ operatori bilan
sym_diff = A ^ B
print(sym_diff)  # {1, 2, 5, 6}

# Metod bilan
sym_diff = A.symmetric_difference(B)
print(sym_diff)  # {1, 2, 5, 6}
```

### Subset va superset

```python
A = {1, 2}
B = {1, 2, 3, 4, 5}

# A B ning subset'i (A ning barcha elementlari B da bor)
print(A.issubset(B))    # True
print(A <= B)           # True
print(A < B)            # True (to'liq subset)

# B A ning superset'i (B A ning barcha elementlarini o'z ichiga oladi)
print(B.issuperset(A))  # True
print(B >= A)           # True
print(B > A)            # True (to'liq superset)

# Umumiy element yo'qligini tekshirish
C = {10, 20, 30}
print(A.isdisjoint(C))  # True (kesishma yo'q)
print(A.isdisjoint(B))  # False (kesishma bor)
```

### Update amallari

Set'ni joyida (in-place) o'zgartiradigan amallar:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union bilan yangilash
A_copy = A.copy()
A_copy |= B
print(A_copy)  # {1, 2, 3, 4, 5, 6}

# Intersection bilan yangilash
A_copy = A.copy()
A_copy &= B
print(A_copy)  # {3, 4}

# Difference bilan yangilash
A_copy = A.copy()
A_copy -= B
print(A_copy)  # {1, 2}

# Yoki metodlar bilan
A_copy = A.copy()
A_copy.update(B)  # Birlashma
A_copy.intersection_update(B)  # Kesishma
A_copy.difference_update(B)  # Farq
```

### `frozenset` (immutable set)

Frozenset — set'ning o'zgarmas (`immutable`) varianti:

```python
# Frozenset yaratish
fs = frozenset([1, 2, 3, 4])
print(fs)  # frozenset({1, 2, 3, 4})

# O'zgartirib bo'lmaydi
# fs.add(5)  # Xato! AttributeError

# Dictionary kaliti yoki set elementi sifatida ishlatish mumkin
my_dict = {fs: "value"}
print(my_dict)

# Matematik amallar ishlaydi
fs2 = frozenset([3, 4, 5])
print(fs | fs2)  # frozenset({1, 2, 3, 4, 5})
print(fs & fs2)  # frozenset({3, 4})
```

### Set comprehension

```python
# Set comprehension - list comprehension'ga o'xshash
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Shart bilan
evens = {x for x in range(20) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

# Satrdan (takrorlanmas belgilar)
word = "mississippi"
unique_chars = {c for c in word}
print(unique_chars)  # {'m', 'i', 's', 'p'}
```

### Amaliy misol

```python
# 1. Dublikatlarni olib tashlash
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(data))
print(unique)  # [1, 2, 3, 4]

# 2. List ichida dublikat bor-yo'qligini tekshirish
def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(has_duplicates([1, 2, 3]))    # False
print(has_duplicates([1, 2, 2, 3])) # True

# 3. Ikki listdagi umumiy elementlarni topish
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(common)  # {4, 5}

# 4. Farq qiladigan elementlarni topish
diff = set(list1) ^ set(list2)
print(diff)  # {1, 2, 3, 6, 7, 8}

# 5. Shart bo'yicha takrorlanmas ma'lumotlarni filtrlash
transactions = [100, 200, 100, 300, 200, 400, 100]
large = {t for t in transactions if t > 150}
print(large)  # {200, 300, 400}

# 6. Kiritmani tekshirish
valid_options = {"yes", "no", "maybe"}
user_input = "yes"
if user_input.lower() in valid_options:
    print("Valid input!")

# 7. Teglar tizimi
post1_tags = {"python", "programming", "tutorial"}
post2_tags = {"python", "web", "flask"}
post3_tags = {"javascript", "web", "react"}

# Python tegiga ega postlar
python_posts = [post1_tags, post2_tags]  # Qo'lda tekshirish

# post1 va post2 ning umumiy teglari
common = post1_tags & post2_tags
print(common)  # {'python'}

# Barcha takrorlanmas teglar
all_tags = post1_tags | post2_tags | post3_tags
print(all_tags)  # {'python', 'programming', 'tutorial', 'web', 'flask', 'javascript', 'react'}
```

### Set va list tezligi (performance)

```python
import time

# Katta ma'lumot yaratish
data_list = list(range(1000000))
data_set = set(data_list)

# List ichida a'zolikni tekshirish
start = time.time()
result = 999999 in data_list
print(f"List: {time.time() - start:.6f} soniya")

# Set ichida a'zolikni tekshirish
start = time.time()
result = 999999 in data_set
print(f"Set: {time.time() - start:.6f} soniya")

# Set a'zolikni tekshirishda ancha tezroq!
```

### Qachon set ishlatish kerak?

<i class="fa-solid fa-circle-check" aria-hidden="true"></i> **Set ishlating**, agar:
- Takrorlanmaydigan (`unique`) elementlarni saqlash kerak bo'lsa
- A'zolikni tekshirish tez-tez kerak bo'lsa
- Matematik amallar kerak bo'lsa (union, intersection)
- List ichidan dublikatlarni olib tashlash kerak bo'lsa

<i class="fa-solid fa-circle-xmark" aria-hidden="true"></i> **Set ishlatmang**, agar:
- Element tartibini saqlash kerak bo'lsa (list yoki dict ishlating)
- Indeks bo'yicha murojaat kerak bo'lsa
- Elementlar hashable bo'lmasa (list, dict)
