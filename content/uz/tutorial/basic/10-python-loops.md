---
layout: tutorial.njk
lang: uz
title: Python takrorlanuvchi operatorlar
description: "for va while sikllari bilan ishni takrorlang va ularni break, continue va else bilan boshqaring."
order: 10
permalink: /uz/tutorial/python-loops/
---

<img src="/img/tutorial/10-python-loops.webp" alt="Python tsikllari - while, for, nested loop" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Odatda dasturlash tillarida buyruqlar ketma-ket bajariladi: funksiya ichidagi birinchi buyruq avval, keyingisi undan keyin va hokazo. Ammo ba'zi vaziyatlarda bir xil ishni ko'p marta takrorlash kerak bo'ladi. Buni qo'lda yuzlab yoki minglab qator kod yozib bajarish samarasiz. Shuning uchun Python'da takrorlash (loop) ishlatiladi.

Python'da takrorlash 3 turga bo'linadi:

- `while` loop
- `for` loop
- Nested loop

### `while` loop

`while` loop shart `True` bo'lib turganida buyruqlarni qayta-qayta bajaradi.

Quyida `while` loop misoli:

```python
# While loop misoli

hisoblagich = 0
while (hisoblagich < 9):
  print("Hisob: ", hisoblagich)
  hisoblagich = hisoblagich + 1

print("Xayr!")
```

### `for` loop

Python'dagi `for` list yoki string kabi ketma-ketlik (sequence) elementlarini takrorlab chiqish (iterate) uchun ishlatiladi.

Quyida `for` loop misoli:

```python
# Oddiy for loop misoli
sonlar = [1, 2, 3, 4, 5]
for x in sonlar:
  print(x)

# For loop misoli
mevalar = ["ananas", "olma", "apelsin"]
for meva in mevalar:
  print("Men yeyishni yoqtiraman:", meva)
```

### Nested loop

Python'da bir loop ichida boshqa loop ishlatish mumkin (nested loop). Quyidagi misollar tushuncha uchun:

#### Nested `for` loop

```python
# Koordinata juftlarini chop etish
for qator in range(1, 4):
  for ustun in range(1, 4):
    print(f"({qator},{ustun})", end=" ")
  print()
```

#### Nested `while` loop

```python
# Ko'paytirish jadvali 1..3
qator = 1
while qator <= 3:
  ustun = 1
  while ustun <= 3:
    print(f"{qator}x{ustun}={qator * ustun}", end="  ")
    ustun += 1
  print()
  qator += 1

print("Xayr!")
```

