---
layout: tutorial.njk
lang: uz
title: Python lambda
description: "Python'da Python lambda mavzusini amaliy misollar va tushunarli izohlar bilan o'rganing."
order: 21
permalink: /uz/tutorial/python-lambda/
---

<img src="/img/tutorial/21-python-lambda.webp" alt="Python lambda" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Lambda - Python'da anonim funksiyalarni (nomi yo'q funksiyalarni) yaratishning qisqa usuli. Lambda bir marta ishlatiladigan oddiy amallar uchun juda qulay, ayniqsa `map()`, `filter()` va `sorted()` kabi funksiyalarga argument sifatida berilganda.

### Asosiy sintaksis

```python
# Sintaksis: lambda argumentlar: ifoda

# Oddiy funksiya
def square(x):
    return x ** 2

# Ekvivalent lambda
square = lambda x: x ** 2

print(square(5))  # Natija: 25
```

Lambda faqat bitta expression'ni o'z ichiga oladi va natijani avtomatik qaytaradi.

### Bir nechta argumentli `lambda`

```python
# Bitta argument
double = lambda x: x * 2
print(double(5))  # 10

# Ikkita argument
add = lambda a, b: a + b
print(add(3, 5))  # 8

# Uchta argument
volume = lambda p, l, t: p * l * t
print(volume(2, 3, 4))  # 24

# Argumentsiz
random_greeting = lambda: "Salom!"
print(random_greeting())  # Salom!
```

### Default argumentli `lambda`

```python
# Standart argument
power = lambda x, n=2: x ** n
print(power(3))     # 9 (2-darajasi)
print(power(3, 3))  # 27 (3-darajasi)

# Bir nechta standart argument
greet = lambda name, formal=False: f"Good Morning, {name}" if formal else f"Hi, {name}!"
print(greet("Bob"))            # Hi, Bob!
print(greet("Bob", formal=True))  # Good Morning, Bob
```

### Shartli ifoda bilan `lambda`

```python
# Lambda ichida shart
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(4))  # Even
print(check_even(7))  # Odd

# Ko'p shartlar
letter_grade = lambda n: "A" if n >= 90 else "B" if n >= 80 else "C" if n >= 70 else "D"
print(letter_grade(95))  # A
print(letter_grade(75))  # C
```

### Built-in funksiyalar bilan `lambda`

#### map() - har bir elementni o'zgartirish

```python
numbers = [1, 2, 3, 4, 5]

# Har bir sonni kvadratga oshirish
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Satrga aylantirish
str_numbers = list(map(lambda x: str(x), numbers))
print(str_numbers)  # ['1', '2', '3', '4', '5']

# Ikki list bilan map
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_lists = list(map(lambda x, y: x + y, list1, list2))
print(sum_lists)  # [5, 7, 9]
```

#### filter() - shart bo'yicha filtrlash

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Juft sonlarni filtrlash
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# 5 dan katta sonlarni filtrlash
large = list(filter(lambda x: x > 5, numbers))
print(large)  # [6, 7, 8, 9, 10]

# Bo'sh satrlarni filtrlash
words = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda x: x, words))
print(non_empty)  # ['hello', 'world', 'python']
```

#### `sorted()` - custom key bilan sortlash

```python
# Absolyut qiymat bo'yicha saralash
numbers = [-5, 2, -3, 1, -4]
sorted_nums = sorted(numbers, key=lambda x: abs(x))
print(sorted_nums)  # [1, 2, -3, -4, -5]

# Tuple ro'yxatini saralash
students = [("Alice", 85), ("Bob", 92), ("Carol", 78)]
by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(by_score)  # [('Bob', 92), ('Alice', 85), ('Carol', 78)]

# Dictionary ro'yxatini saralash
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Carol", "age": 30}
]
by_age = sorted(data, key=lambda x: x["age"])
print(by_age)
# [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Carol', 'age': 30}]

# Satrlarni uzunligi bo'yicha saralash
words = ["python", "go", "javascript", "c"]
by_length = sorted(words, key=lambda x: len(x))
print(by_length)  # ['c', 'go', 'python', 'javascript']
```

#### reduce() - bitta qiymatga yig'ish

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Multiply all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5
```

### Ma'lumot tuzilmalarida `lambda`

```python
# Funksiyalar lug'ati
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "Error"
}

print(operations["add"](10, 5))  # 15
print(operations["multiply"](10, 5))    # 50

# Lambda ro'yxati
transformations = [
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x + 10
]

number = 5
for t in transformations:
    print(t(number))  # 10, 25, 15
```

### Darhol bajariladigan `lambda`

Darhol chaqiriladigan lambda:

```python
# Darhol bajariladigan funksiya ifodasi
result = (lambda x, y: x + y)(3, 5)
print(result)  # 8

# Bir martalik amallar uchun foydali
data = (lambda: {"config": "value", "debug": True})()
print(data)  # {'config': 'value', 'debug': True}
```

### `lambda` va oddiy funksiyalar

| Jihat | Lambda | `def` funksiya |
|-------|--------|--------------|
| Nomi | Anonim | Nomi bo'lishi kerak |
| Qatorlar | Bitta expression | Bir nechta statement |
| O'qilish | Oddiy amallar uchun | Murakkab logika uchun |
| Docstring | Yo'q | Bor |
| Type hints | Yo'q | Bor |

```python
# Lambda qachon ishlatish kerak
data = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, data))  # Oddiy bir martalik logika uchun yaxshi

# def qachon ishlatish kerak
def calculate_tax(salary, allowance=0, deduction=0):
    """
    Calculates income tax.

    Args:
        salary: Basic salary
        allowance: Total allowance
        deduction: Total deduction

    Returns:
        Tax amount to be paid
    """
    taxable_income = salary + allowance - deduction
    if taxable_income <= 50000000:
        return taxable_income * 0.05
    elif taxable_income <= 250000000:
        return taxable_income * 0.15
    else:
        return taxable_income * 0.25
```

### Amaliy misol

```python
# 1. Sorting complex data
products = [
    {"name": "Laptop", "price": 15000000, "rating": 4.5},
    {"name": "Mouse", "price": 250000, "rating": 4.8},
    {"name": "Keyboard", "price": 750000, "rating": 4.2}
]

# Narx bo'yicha saralash (o'sish tartibida)
by_price = sorted(products, key=lambda p: p["price"])

# Reyting bo'yicha saralash (kamayish tartibida)
by_rating = sorted(products, key=lambda p: p["rating"], reverse=True)

# 2. Data transformation pipeline
data = ["  Hello  ", "WORLD", "  python  "]
cleaned = list(map(lambda s: s.strip().lower(), data))
print(cleaned)  # ['hello', 'world', 'python']

# 3. Hodisa handlerlari (pseudo-code)
button_actions = {
    "save": lambda: print("Saving..."),
    "delete": lambda: print("Deleting..."),
    "export": lambda: print("Exporting...")
}

action = "save"
button_actions[action]()  # Saving...
```

### Maslahatlar va eng yaxshi amaliyotlar

1. **Lambda'ni oddiy amallar uchun ishlating** - logika bir qatordan oshsa `def` ishlating
2. **Haddan oshirmang** - kod o'qilishi oson bo'lsin
3. **Ichma-ich (nested) lambda'dan qoching** - o'qish va nosozliklarni topish (debug) qiyin
4. **List comprehension'ni ko'rib chiqing** - ko'pincha map+lambda'dan o'qilishi osonroq

```python
# Lambda + map
data = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, data))
print(result)  # [2, 4, 6, 8, 10]

# List comprehension (ko'proq pythonic)
result = [x * 2 for x in data]
print(result)  # [2, 4, 6, 8, 10]
```
