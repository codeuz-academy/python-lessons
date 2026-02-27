---
layout: tutorial.njk
lang: uz
title: Python to'plamlar (sets)
order: 18
permalink: /tutorial/uz/python-sets/
---

Set - Python'dagi unique (takrorlanmaydigan) va unordered (tartibsiz) elementlar to'plami. Set'lar membership tekshirishda, dublikatlarni olib tashlashda, va union/intersection/difference kabi matematik amallarda juda samarali.

### Set yaratish

```python
# Using curly braces
fruits = {"apple", "orange", "mango"}
print(fruits)  # {'apple', 'orange', 'mango'}

# Using set() constructor
numbers = set([1, 2, 3, 4, 5])
print(numbers)  # {1, 2, 3, 4, 5}

# Empty set(MUST use set(), not {})
empty = set()
print(empty)  # set()
print(type(empty))  # <class 'set'>

# {} creates a dictionary, not a set!
not_set = {}
print(type(not_set))  # <class 'dict'>
```

### Set xususiyatlari

```python
# 1. Unique elements(no duplicates)
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)  # {1, 2, 3, 4}

# 2. Unordered
letters = {"c", "a", "b"}
print(letters)  # Order can vary

# 3. Cannot access by index
# letters[0]  # Error! TypeError

# 4. Elements must be hashable(immutable)
valid = {1, "hello", (1, 2)}  # OK
# invalid = {1, [1, 2]}  # Error! List is not hashable
```

### Element qo'shish va o'chirish

```python
fruits = {"apple", "orange"}

# Add one element
fruits.add("mango")
print(fruits)  # {'apple', 'orange', 'mango'}

# Add multiple elements
fruits.update(["banana", "grape"])
print(fruits)  # {'apple', 'orange', 'mango', 'banana', 'grape'}

# Remove element(error if not found)
fruits.remove("apple")
print(fruits)

# Remove element(no error if not found)
fruits.discard("durian")  # No error
print(fruits)

# Remove random element
item = fruits.pop()
print(f"Removed: {item}")

# Remove all elements
fruits.clear()
print(fruits)  # set()
```

### Membership amallari

Set membership tekshirishda juda tez (O(1) murakkablik):

```python
numbers = {1, 2, 3, 4, 5}

# Check if exists in set
print(3 in numbers)      # True
print(10 in numbers)     # False
print(10 not in numbers) # True

# Comparison with list for large data
# Set: O(1) - very fast
# List: O(n) - slow for large data
```

### Matematik amallar

#### Union

Ikkala set'dagi barcha elementlarni birlashtiradi:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using | operator
combined = A | B
print(combined)  # {1, 2, 3, 4, 5, 6}

# Using method
combined = A.union(B)
print(combined)  # {1, 2, 3, 4, 5, 6}
```

#### Intersection

Ikkalasida ham bor bo'lgan elementlar:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using & operator
intersection = A & B
print(intersection)  # {3, 4}

# Using method
intersection = A.intersection(B)
print(intersection)  # {3, 4}
```

#### Difference

Birinchi set'da bor, ikkinchisida yo'q elementlar:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# A - B: Elements in A not in B
diff = A - B
print(diff)  # {1, 2}

# B - A: Elements in B not in A
diff = B - A
print(diff)  # {5, 6}

# Using method
diff = A.difference(B)
print(diff)  # {1, 2}
```

#### Symmetric difference

Ikkalasidan birida bor, lekin ikkalasida birga emas elementlar:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using ^ operator
sym_diff = A ^ B
print(sym_diff)  # {1, 2, 5, 6}

# Using method
sym_diff = A.symmetric_difference(B)
print(sym_diff)  # {1, 2, 5, 6}
```

### Subset va superset

```python
A = {1, 2}
B = {1, 2, 3, 4, 5}

# A is subset of B(all elements of A are in B)
print(A.issubset(B))    # True
print(A <= B)           # True
print(A < B)            # True (proper subset)

# B is superset of A(B contains all elements of A)
print(B.issuperset(A))  # True
print(B >= A)           # True
print(B > A)            # True (proper superset)

# Check if no common elements
C = {10, 20, 30}
print(A.isdisjoint(C))  # True (no intersection)
print(A.isdisjoint(B))  # False (has intersection)
```

### Update amallari

Set'ni joyida (in-place) o'zgartiradigan amallar:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Update with union
A_copy = A.copy()
A_copy |= B
print(A_copy)  # {1, 2, 3, 4, 5, 6}

# Update with intersection
A_copy = A.copy()
A_copy &= B
print(A_copy)  # {3, 4}

# Update with difference
A_copy = A.copy()
A_copy -= B
print(A_copy)  # {1, 2}

# Or using methods
A_copy = A.copy()
A_copy.update(B)  # Union
A_copy.intersection_update(B)  # Intersection
A_copy.difference_update(B)  # Difference
```

### `frozenset` (immutable set)

Frozenset - bu set'ning immutable varianti:

```python
# Creating frozenset
fs = frozenset([1, 2, 3, 4])
print(fs)  # frozenset({1, 2, 3, 4})

# Cannot be modified
# fs.add(5)  # Error! AttributeError

# Can be used as dictionary key or set element
my_dict = {fs: "value"}
print(my_dict)

# Mathematical operations still work
fs2 = frozenset([3, 4, 5])
print(fs | fs2)  # frozenset({1, 2, 3, 4, 5})
print(fs & fs2)  # frozenset({3, 4})
```

### Set comprehension

```python
# Set comprehension similar to list comprehension
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# With condition
evens = {x for x in range(20) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

# From string(unique characters)
word = "mississippi"
unique_chars = {c for c in word}
print(unique_chars)  # {'m', 'i', 's', 'p'}
```

### Amaliy misol

```python
# 1. Removing duplicates
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(data))
print(unique)  # [1, 2, 3, 4]

# 2. Check if list has duplicates
def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(has_duplicates([1, 2, 3]))    # False
print(has_duplicates([1, 2, 2, 3])) # True

# 3. Find common elements from two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(common)  # {4, 5}

# 4. Find different elements
diff = set(list1) ^ set(list2)
print(diff)  # {1, 2, 3, 6, 7, 8}

# 5. Filter unique data with condition
transactions = [100, 200, 100, 300, 200, 400, 100]
large = {t for t in transactions if t > 150}
print(large)  # {200, 300, 400}

# 6. Input validation
valid_options = {"yes", "no", "maybe"}
user_input = "yes"
if user_input.lower() in valid_options:
    print("Valid input!")

# 7. Tag system
post1_tags = {"python", "programming", "tutorial"}
post2_tags = {"python", "web", "flask"}
post3_tags = {"javascript", "web", "react"}

# Posts with python tag
python_posts = [post1_tags, post2_tags]  # Manual check

# Common tags between post1 and post2
common = post1_tags & post2_tags
print(common)  # {'python'}

# All unique tags
all_tags = post1_tags | post2_tags | post3_tags
print(all_tags)  # {'python', 'programming', 'tutorial', 'web', 'flask', 'javascript', 'react'}
```

### Set va list tezligi (performance)

```python
import time

# Create large data
data_list = list(range(1000000))
data_set = set(data_list)

# Check membership in list
start = time.time()
result = 999999 in data_list
print(f"List: {time.time() - start:.6f} seconds")

# Check membership in set
start = time.time()
result = 999999 in data_set
print(f"Set: {time.time() - start:.6f} seconds")

# Set is much faster for membership testing!
```

### Qachon set ishlatish kerak?

<i class="fa-solid fa-circle-check" aria-hidden="true"></i> **Set ishlating**, agar:
- Unique elementlarni saqlash kerak bo'lsa
- Membership tekshirish tez-tez kerak bo'lsa
- Matematik amallar kerak bo'lsa (union, intersection)
- List ichidan dublikatlarni olib tashlash kerak bo'lsa

<i class="fa-solid fa-circle-xmark" aria-hidden="true"></i> **Set ishlatmang**, agar:
- Element tartibini saqlash kerak bo'lsa (list yoki dict ishlating)
- Index bo'yicha murojaat kerak bo'lsa
- Elementlar hashable bo'lmasa (list, dict)

