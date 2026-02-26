---
layout: tutorial.njk
lang: uz
title: Python memory management
order: 42
permalink: /uz/tutorial/python-memory-management/
---

<img src="/img/tutorial/37-memory-handling-python.webp" alt="Python memory management" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python ommabop bo'lishining sabablaridan biri - dasturchi C yoki C++ dagidek qo'lda memory management bilan shug'ullanishi shart emas. Python xotira ajratish (allocation) va bo'shatishni (deallocation) avtomatik bajaradi.

Shunga qaramay, Python xotirani ichkarida qanday boshqarishini tushunish samarali kod yozish uchun muhim, ayniqsa katta data bilan ishlaganda.

### 1. Heap va Stack

Python ikki xil xotiradan foydalanadi:
- **Stack memory**: funksiya bajarilishi va lokal o'zgaruvchilar uchun.
- **Heap memory**: barcha Python object va instance'lar (int, list, class va hokazo) shu yerda saqlanadi. Uni Python Memory Manager boshqaradi.

### 2. Reference counting

Python xotira boshqaruvidagi asosiy strategiya - **reference counting**.

Har bir object'ning reference count'i bo'ladi: nechta o'zgaruvchi o'sha object'ga ishora qilayotganini bildiradi.

- Object yaratilsa yoki unga referens berilsa (`a = object`), count oshadi (+1).
- Referens o'chirilsa (`del a`) yoki scope'dan chiqsa, count kamayadi (-1).
- Count 0 ga tushsa, object xotirasi darhol bo'shatiladi.

```python
import sys

a = []
# Get ref count(usually higher than expected because the argument to sys.getrefcount itself is also a temporary reference)
print(sys.getrefcount(a)) 

b = a
print(sys.getrefcount(a)) # Increases

del b
print(sys.getrefcount(a)) # Decreases
```

### 3. Garbage collection (GC)

Reference counting'ning bitta muammosi bor: **circular references**.

```python
a = []
b = []
a.append(b)
b.append(a) # Circular reference
```

Agar `a` va `b` o'chirilsa ham, ular bir-biriga ishora qilgani uchun reference count hech qachon 0 bo'lmaydi. Shu yerda **Garbage Collector (GC)** ishga tushadi.

Python GC alohida mexanizm bo'lib, vaqti-vaqti bilan ishlaydi va circular reference'lardan hosil bo'lgan "garbage"ni topib tozalaydi.

GC'ni `gc` moduli bilan qo'lda boshqarish mumkin:

```python
import gc

# Force run garbage collection
gc.collect()

# Disable automatic garbage collection
gc.disable()
```
*Maslahat: odatda `gc` moduliga kamdan-kam teginasiz, asosan yuqori darajali optimizatsiya uchun kerak bo'ladi.*

### 4. Xotirani tejash bo'yicha maslahatlar

1. **Generator ishlating**: oldingi darsda ko'rganimizdek, generator hamma data'ni RAM'ga yuklamaydi.
2. **Class'larda `__slots__` ishlating**: agar kichik class'dan millionlab instance yaratsangiz, `__slots__` har bir instance uchun dinamik `__dict__`ni o'chirib, RAM'ni tejaydi.

```python
class SaveMemory:
    __slots__ = ['name', 'age'] # Can only have these attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

3. **Global o'zgaruvchilarga ehtiyot bo'ling**: global object'lar dastur to'xtamaguncha o'chmaydi (qo'lda o'chirmasangiz).

### Xulosa
- Python asosan **reference counting** ishlatadi.
- **Garbage collector** circular reference'larni tozalaydi.
- Python xotira boshqaruvini tushunib, "memory-efficient" kod yozish mumkin.
