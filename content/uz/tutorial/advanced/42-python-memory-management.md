---
layout: tutorial.njk
lang: uz
title: Python xotira boshqaruvi (memory management)
description: "Python obyektlarni reference counting va garbage collection bilan qanday kuzatishi hamda xotira sizishlarini qanday topishini tushuning."
order: 42
permalink: /uz/tutorial/python-memory-management/
---

<img src="/img/tutorial/42-python-memory-management.webp" alt="Python memory management" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python ommabop bo'lishining sabablaridan biri — dasturchi C yoki C++ dagidek qo'lda xotira boshqaruvi (`memory management`) bilan shug'ullanishi shart emas. Python xotira ajratish (`allocation`) va bo'shatishni (`deallocation`) avtomatik bajaradi.

Shunga qaramay, Python xotirani ichkarida qanday boshqarishini tushunish samarali kod yozish uchun muhim, ayniqsa katta ma'lumotlar bilan ishlaganda.

### 1. Heap va Stack

Python ikki xil xotiradan foydalanadi:
- **Stack memory**: funksiya bajarilishi va lokal o'zgaruvchilar uchun.
- **Heap memory**: barcha Python obyekt va instance'lari (`int`, `list`, class obyektlari va hokazo) shu yerda saqlanadi. Uni Python Memory Manager boshqaradi.

### 2. Reference counting

Python xotira boshqaruvidagi asosiy strategiya — **reference counting**.

Har bir obyektning reference count'i bo'ladi: nechta nom yoki tuzilma o'sha obyektga ishora qilayotganini bildiradi.

- Obyekt yaratilsa yoki unga referens berilsa (`a = object`), count oshadi (+1).
- Referens o'chirilsa (`del a`) yoki qamrovdan (scope) chiqsa, count kamayadi (-1).
- Count 0 ga tushsa, obyekt xotirasi darhol bo'shatiladi.

```python
import sys

a = []
# Referens sonini olish (kutilganidan yuqori bo'lishi mumkin, chunki sys.getrefcount'ning argumenti ham vaqtinchalik referens)
print(sys.getrefcount(a)) 

b = a
print(sys.getrefcount(a)) # Increases

del b
print(sys.getrefcount(a)) # Decreases
```

### 3. Garbage collection (GC)

Reference counting'ning bitta muammosi bor: **aylanma referenslar** (`circular references`).

```python
a = []
b = []
a.append(b)
b.append(a) # Circular reference
```

Agar `a` va `b` o'chirilsa ham, ular bir-biriga ishora qilgani uchun reference count hech qachon 0 bo'lmaydi. Shu yerda **Garbage Collector (GC)** ishga tushadi.

Python GC alohida mexanizm bo'lib, vaqti-vaqti bilan ishlaydi va aylanma referenslardan hosil bo'lgan "garbage"ni topib tozalaydi.

GC'ni `gc` moduli bilan qo'lda boshqarish mumkin:

```python
import gc

# Garbage collection'ni majburan ishga tushirish
gc.collect()

# Avtomatik garbage collection'ni o'chirish
gc.disable()
```
*Maslahat: odatda `gc` moduliga kamdan-kam teginasiz, asosan yuqori darajali optimizatsiya uchun kerak bo'ladi.*

### 4. Xotirani tejash bo'yicha maslahatlar

1. **Generator ishlating**: oldingi darsda ko'rganimizdek, generator hamma ma'lumotni RAM'ga yuklamaydi.
2. **Class'larda `__slots__` ishlating**: agar kichik class'dan millionlab instance yaratsangiz, `__slots__` har bir instance uchun dinamik `__dict__`ni o'chirib, RAM'ni tejaydi.

```python
class SaveMemory:
    __slots__ = ['name', 'age'] # Can only have these attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

3. **Global o'zgaruvchilarga ehtiyot bo'ling**: global obyektlar dastur to'xtamaguncha o'chmaydi (qo'lda o'chirmasangiz).

### 5. Identiklik (identity) va tenglik (equality)

Ikkita o'zgaruvchi *teng* qiymatlarni saqlashi mumkin, lekin xotirada *turli obyektlar* bo'lishi mumkin. `==` qiymatlarni solishtiradi; `is` identiklikni (xuddi o'sha obyekt ekanini) solishtiradi. `id()` obyektning xotira manzilini qaytaradi.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  (bir xil tarkib)
print(a is b)   # False (ikkita alohida obyekt)
print(a is c)   # True  (c xuddi a kabi listga ishora qiladi)

print(id(a) == id(c))   # True
```

### 6. Kichik obyektlarni interning qilish

Xotirani tejash uchun CPython ba'zi immutable obyektlarni qayta ishlatadi (intern qiladi) — kichik butun sonlar (taxminan −5 dan 256 gacha) va ko'p qisqa stringlar bitta nusxani baham ko'radi:

```python
x = 100
y = 100
print(x is y)   # True  (kichik int'lar keshlanadi)
```

```pycon
>>> m = 1000
>>> n = 1000
>>> m is n   # ko'pincha False: 1000 CPython'ning kichik-int keshidan tashqarida (-5..256)
False
```

> <i class="fa-solid fa-circle-info" aria-hidden="true"></i> **Eslatma:** Sonlar yoki stringlar kabi qiymatlarni solishtirish uchun hech qachon `is` ishlatmang — interning bu amalga oshirish tafsiloti. `is`'ni faqat `None` kabi singleton'lar uchun ishlating: `if value is None:`.

### Xulosa
- Python asosan **reference counting** ishlatadi.
- **Garbage collector** circular reference'larni tozalaydi.
- Qiymatlar uchun `==`, identiklik uchun esa faqat `is` ishlating (masalan, `is None`).
- Python xotira boshqaruvini tushunsangiz, xotirani tejaydigan kod yozish osonlashadi.
