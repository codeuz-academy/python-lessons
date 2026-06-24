---
layout: tutorial.njk
lang: uz
title: Python iterator'lar va generator'lar
description: "Iterator va generator'lar bilan dangasa ketma-ketliklar quring va ma'lumotni bir vaqtda to'liq yuklamasdan qayta ishlang."
order: 35
permalink: /uz/tutorial/python-iterators-generators/
---

<img src="/img/tutorial/35-python-iterators-generators.webp" alt="Python iterators va generators" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python'da iterator va generator'lar xotira tejamkorligi (memory efficiency) uchun juda muhim. Ular katta hajmdagi ma'lumotni (hatto cheksiz ketma-ketliklarni ham) hammasini bir yo'la RAM'ga yuklamasdan, bo'laklab qayta ishlashga imkon beradi.

Qalin kitobni o'qish misolini oling: iterator sizga sahifa-sahifa o'qishga (faqat bitta sahifani xotirada ushlab turishga) yordam beradi. 1000 sahifani birdan yodlab olish shart emas.

### 1. Iterators

Iterator - bu sanab bo'ladigan qiymatlarni o'z ichiga oladigan obyekt. U ustidan iteratsiya qilish mumkin, ya'ni barcha qiymatlarni ketma-ket ko'rib chiqish mumkin.

Texnik jihatdan, Python'da iterator — iterator protokolini amalga oshiradigan obyekt bo'lib, `__iter__()` va `__next__()` metodlariga ega bo'ladi.

#### Iterator yaratish misoli
Quyida 1 dan boshlab ma'lum limit'gacha son qaytaradigan oddiy iterator:

```python
class MyNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers(3)
myiter = iter(myclass)

print(next(myiter)) # Natija: 1
print(next(myiter)) # Natija: 2
print(next(myiter)) # Natija: 3
# print(next(myiter)) # StopIteration xatosi chiqaradi
```

`for` loop ishlatganda, Python `__iter__()` va `StopIteration` exception'ni avtomatik boshqaradi.

```python
for x in MyNumbers(3):
    print(x)
```

### 2. Generators

Generator - iterator yaratishning sodda usuli. `__iter__()` va `__next__()` bilan katta class yozish o'rniga, oddiy funksiya yozasiz va qiymat qaytaradigan joyda `yield` ishlatasiz.

Har safar `yield` chaqirilganda funksiya "pauza" qiladi, o'zgaruvchilar holatini saqlab qoladi va keyingi chaqiriqda o'sha joydan davom etadi.

#### Oddiy generator misoli
```python
def number_generator(limit):
    num = 1
    while num <= limit:
        yield num
        num += 1

gen = number_generator(3)
# Generator ham iterator!
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
```

#### Generator afzalligi: xotirani tejash
Masalan, 1 million sonni qayta ishlashingiz kerak.

**List bilan (xotira yeydi):**
```python
def get_list():
    result = []
    for i in range(1000000):
        result.append(i)
    return result

# Bu butun sonlar ro'yxati uchun taxminan 40MB+ xotira sarflaydi
```

**Generator bilan (xotirani tejaydi):**
```python
def get_generator():
    for i in range(1000000):
        yield i

# Bu deyarli qo'shimcha xotira sarflamaydi, chunki sonlar so'ralganda bittadan hosil qilinadi.
```

### 3. Generator expression

*List Comprehension* ga o'xshaydi, lekin `()` ishlatiladi. Natija list emas, generator obyekt bo'ladi.

```python
# List comprehension (to'liq list'ni xotirada yaratadi)
squares_list = [x**2 for x in range(10)]
print(squares_list) # [0, 1, 4, ..., 81]

# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in range(10))
print(squares_gen) # <generator object ...>

# Tarkibini ko'rish uchun iteratsiya qilish kerak
for i in squares_gen:
    print(i, end=" ")
```

### 4. Amaliy holat: katta fayllarni o'qish
Masalan, 10GB server log faylini qayta ishlash kerak bo'lsa:

**Noto'g'ri (bunday qilmang):**
<div class="warning">Bu kod parchasi konseptual anti-pattern'ni ko'rsatadi va katta <code>server.log</code> fayli mavjud deb hisoblaydi. Fayl bo'lmasa, bajarilganda xato yuzaga keladi.</div>

```python
def read_file_wrong(filename):
    file = open(filename)
    content = file.read() # Xavfli! Butun 10GB ni RAM ga yuklaydi.
    return content.split("\n")
```

**To'g'ri (generator ishlating):**
<div class="warning">Bu to'g'ri pattern, lekin agar <code>server.log</code> papkangizda mavjud bo'lmasa, FileNotFoundError chiqaradi.</div>

```python
def read_file_right(filename):
    with open(filename, "r", encoding="utf-8") as handle:
        for line in handle:
            yield line

with open("server.log", "w", encoding="utf-8") as handle:
    handle.write("INFO Started\\n")
    handle.write("ERROR Disk nearly full\\n")
    handle.write("INFO Completed\\n")

# 10GB faylni xotira muammolarsiz o'qishimiz mumkin
for line in read_file_right("server.log"):
    if "ERROR" in line:
        print(line)
```

### Xulosa
- **Iterator**: iteratsiya qilinadigan obyekt (`__next__`).
- **Generator**: qiymatlarni birma-bir (lazy) beradigan funksiya (`yield`).
- Katta dataset yoki cheksiz data stream bilan ishlaganda generatorlardan foydalaning.
