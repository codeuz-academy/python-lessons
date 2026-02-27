---
layout: tutorial.njk
lang: uz
title: Python tsikllari (loops)
order: 10
permalink: /uz/tutorial/python-loops/
---

<img src="/img/tutorial/10-tutorial-loop-pada-python.webp" alt="Python tsikllari - while, for, nested loop" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Odatda dasturlash tillarida buyruqlar ketma-ket bajariladi: funksiya ichidagi birinchi buyruq avval, keyingisi undan keyin va hokazo. Ammo ba'zi vaziyatlarda bir xil ishni ko'p marta takrorlash kerak bo'ladi. Buni qo'lda yuzlab yoki minglab qator kod yozib bajarish samarasiz. Shuning uchun Python'da takrorlash (loop) ishlatiladi.

Python'da takrorlash 3 turga bo'linadi:

- `while` loop
- `for` loop
- Nested loop

### `while` loop

`while` loop shart `True` bo'lib turganida buyruqlarni qayta-qayta bajaradi.

Quyida `while` loop misoli:

```python
#Example of using While Loop
#Note: Determining scope in Python can use tabs instead of using brackets

count = 0
while (count < 9):
  print("The count is: ", count)
  count = count + 1

print("Good bye!")
```

### `for` loop

Python'dagi `for` list yoki string kabi ketma-ketlik (sequence) elementlarini aylanish (iterate) uchun ishlatiladi.

Quyida `for` loop misoli:

```python
#Example of simple for loop
numbers = [1,2,3,4,5]
for x in numbers:
  print(x)

#Example of for loop
fruits = ["pineapple", "apple", "orange"]
for food in fruits:
  print("I like to eat", food)
```

### Nested loop

Python'da bir loop ichida boshqa loop ishlatish mumkin (nested loop). Quyidagi misollar tushuncha uchun:

#### Nested `for` loop

```python
# Example: print coordinate pairs
for row in range(1, 4):
  for col in range(1, 4):
    print(f"({row},{col})", end=" ")
  print()
```

#### Nested `while` loop

```python
# Example: multiplication table 1..3
row = 1
while row <= 3:
  col = 1
  while col <= 3:
    print(f"{row}x{col}={row * col}", end="  ")
    col += 1
  print()
  row += 1

print("Good bye!")
```

