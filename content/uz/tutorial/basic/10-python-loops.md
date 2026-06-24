---
layout: tutorial.njk
lang: uz
title: Python takrorlanuvchi operatorlar
description: "for va while sikllari bilan ishni takrorlang va ularni break, continue, range va else bilan boshqaring."
order: 10
permalink: /uz/tutorial/python-loops/
---

<img src="/img/tutorial/10-python-loops.webp" alt="Python sikllari - While, For, Nested Loop" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Odatda dasturdagi operatorlar yuqoridan pastga, ketma-ket bajariladi. Ammo ko'pincha bir xil kod blokini ko'p marta bajarish kerak bo'ladi — list'dagi har bir element uchun yoki biror shart yolg'on bo'lguncha. Buni qo'lda yozish sekin va xatolarga moyil bo'lardi. **Sikllar** (loop) ishni avtomatik takrorlash imkonini beradi.

Python'da ikkita sikl operatori bor:

- `while` sikli — shart `True` bo'lib turguncha takrorlaydi.
- `for` sikli — ketma-ketlikdagi har bir element uchun bir marta takrorlaydi.

Shuningdek, bir siklni ikkinchisining ichiga joylashtirishingiz (**ichma-ich sikl**) va istalgan siklni `break`, `continue` hamda ixtiyoriy `else` bloki bilan boshqarishingiz mumkin.

### `while` sikli

`while` sikli sharti `True` bo'lib turganda o'z tanasini qayta-qayta bajaradi. Sikl ichida biror narsa oxir-oqibat shartni yolg'onga aylantirishiga ishonch hosil qiling, aks holda u cheksiz takrorlanadi.

```python
count = 0
while count < 5:
    print("The count is:", count)
    count = count + 1

print("Good bye!")
```

### `for` sikli

`for` sikli istalgan ketma-ketlikning elementlari bo'ylab yuradi — `list`, `tuple`, `string`, `set` yoki `dict`.

```python
numbers = [1, 2, 3, 4, 5]
for x in numbers:
    print(x)

fruits = ["pineapple", "apple", "orange"]
for food in fruits:
    print("I like to eat", food)
```

String - bu belgilar ketma-ketligi, shuning uchun uni to'g'ridan-to'g'ri aylanib chiqishingiz mumkin:

```python
for letter in "Py":
    print(letter)
```

### `range()` funksiyasi

`range()` sonlar ketma-ketligini hosil qiladi va biror narsani aniq son marta takrorlashning odatiy usuli hisoblanadi. U uchtagacha argument oladi: `range(start, stop, step)`. `stop` qiymati **kiritilmaydi**.

```python
for i in range(5):
    print(i)        # 0 1 2 3 4

for i in range(2, 6):
    print(i)        # 2 3 4 5

for i in range(0, 10, 2):
    print(i)        # 0 2 4 6 8
```

| Chaqiruv | Natija |
| --------------------- | ------------------ |
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 6)` | 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

### Indeks bilan aylanish: `enumerate()`

Pozitsiya va qiymatning ikkalasi ham kerak bo'lganda, hisoblagichni o'zingiz boshqarish o'rniga `enumerate()` ishlating:

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

### `break` operatori

`break` siklni darhol to'xtatadi — shart hali `True` bo'lsa yoki elementlar qolgan bo'lsa ham:

```python
for number in [1, 2, 3, 4, 5]:
    if number == 3:
        break
    print(number)   # 1 2
```

### `continue` operatori

`continue` joriy iteratsiyaning qolgan qismini o'tkazib yuboradi va keyingisiga o'tadi:

```python
for number in range(1, 6):
    if number % 2 == 0:
        continue
    print(number)   # 1 3 5
```

### `else` bloki

Siklda `else` bloki bo'lishi mumkin, u **faqat sikl `break`'ga uchramay tugaganda** ishlaydi. Bu qidiruvga o'xshash sikllar uchun qulay:

```python
for number in [1, 3, 5]:
    if number % 2 == 0:
        print("Found an even number")
        break
else:
    print("No even numbers found")   # bu ishlaydi
```

### `pass` operatori

Sikl tanasi bo'sh bo'lishi mumkin emas. Hali bajariladigan ish bo'lmasa, joy egallovchi sifatida `pass` ishlating:

```python
for x in range(3):
    pass   # TODO: keyinroq to'ldirish
```

### Ichma-ich sikl

Python bir siklni ikkinchisining ichiga joylashtirishga ruxsat beradi. Tashqi siklning har bir o'tishida ichki sikl to'liq bajariladi.

#### Ichma-ich `for` sikli

```python
# Koordinata juftliklarini chiqarish
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()
```

#### Ichma-ich `while` sikli

```python
# 1..3 ko'paytirish jadvali
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
