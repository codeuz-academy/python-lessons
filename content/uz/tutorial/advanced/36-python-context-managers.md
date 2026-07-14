---
layout: tutorial.njk
lang: uz
title: Python kontekst menejerlar (context managers)
description: "with operatori va o'zingizning kontekst menejerlaringiz bilan tayyorlash va tozalashni ishonchli boshqaring."
order: 36
permalink: /uz/tutorial/python-context-managers/
---

<img src="/img/tutorial/36-python-context-managers.webp" alt="Python context managers" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Kontekst menejer (`context manager`) — resurslarni ishonchli boshqarish uchun ishlatiladigan Python imkoniyati. U fayl, tarmoq ulanishi yoki ma'lumotlar bazasi ulanishi kabi resurslar to'g'ri ochilib-yopilishini kafolatlaydi, hatto jarayon o'rtasida xato bo'lsa ham.

Siz ham fayl ochib, keyin yopishni unutganmisiz? Python'da buni `with` kalit so'zi bilan oson oldini olish mumkin.

### 1. `with` kalit so'zi

Kontekst menejerdan foydalanishning eng keng tarqalgan usuli — `with` buyrug'i.

**Kontekst menejersiz (resurs yopilmay qolishi mumkin):**
```python
file = open("data.txt", "w")
try:
    file.write("Hello World")
finally:
    file.close() # Uni qo'lda yopishimiz shart
```

**Kontekst menejer bilan (xavfsiz va toza):**
```python
with open("data.txt", "w") as file:
    file.write("Hello World")

# Fayl bu yerda avtomatik yopiladi, hatto yozish paytida xato bo'lsa ham.
```

### 2. O'zingiz kontekst menejer yaratish

O'zingizning kontekst menejeringizni `__enter__` va `__exit__` metodlariga ega sinf orqali yaratishingiz mumkin.

`__enter__`: `with` blokiga kirilganda ishlaydi. Qaytgan qiymat `as ...` dagi o'zgaruvchiga beriladi.
`__exit__`: `with` blokidan chiqilganda ishlaydi (normal tugash yoki xato).

#### Misol: ma'lumotlar bazasi ulanish menejeri (simulyatsiya)

```python
class ManageDB:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"--> Opening connection to {self.db_name}")
        return self # Bu obyekt 'db' o'zgaruvchisiga aylanadi

    def query(self, sql):
        print(f"Executing query: {sql}")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"<-- Closing connection to {self.db_name}")
        # Xato bo'lsa, exc_type None bo'lmaydi
        if exc_type:
            print(f"Xato yuz berdi: {exc_value}")
        # Xatoni bostirishni xohlasangiz True qaytaring (dastur buzilmaydi)
        # Xato ko'tarilishini xohlasangiz False qaytaring (standart)

# Foydalanish
with ManageDB("users_db") as db:
    db.query("SELECT * FROM users")
    
# Natija:
# --> Opening connection to users_db
# Executing query: SELECT * FROM users
# <-- Closing connection to users_db
```

### 3. `contextlib` dan foydalanish

Python `contextlib` modulini beradi. U generator va `@contextmanager` dekoratori yordamida kontekst menejer yaratishni osonlashtiradi. Bu sinf yaratishdan ixchamroq.

```python
from contextlib import contextmanager

@contextmanager
def open_my_file(name):
    try:
        print("Opening file...")
        f = open(name, "w")
        yield f
    finally:
        print("Closing file...")
        f.close()

# Foydalanish
with open_my_file("test.txt") as f:
    f.write("Test 123")
```

`yield`dan oldingi kod `__enter__`, `finally` blokidagi kod esa `__exit__`.

### 4. Amaliy misol: bajarilish vaqtini o'lchash

Kod bloki qancha vaqt ishlaganini o'lchash uchun kontekst menejer yozish mumkin.

```python
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Execution time: {end - start:.4f} seconds")

with timer():
    # Og'ir jarayonni simulyatsiya qilish
    time.sleep(1)
    x = sum(range(1000000))

# Natija: Execution time: 1.0xxx seconds
```

### 5. Bir vaqtning o'zida bir nechta resursni boshqarish

Bitta `with` operatori vergul bilan ajratilgan bir nechta kontekst menejerni boshqarishi mumkin. Har biri chapdan o'ngga ishga tushiriladi va teskari tartibda yopiladi:

```python
with open("a.txt", "w") as a, open("b.txt", "w") as b:
    a.write("file A")
    b.write("file B")
# ikkala fayl ham bu yerda yopiladi
```

Uzun ro'yxatlar uchun ularni qavslarga olib, qatorlarga bo'ling:

```python
with (
    open("a.txt", "w") as a,
    open("b.txt", "w") as b,
):
    a.write("A")
    b.write("B")
```

### 6. `contextlib.suppress` bilan xatolarni bostirish

Muayyan xatoni rostdan ham e'tiborsiz qoldirmoqchi bo'lsangiz, `contextlib.suppress` bo'sh `try/except`'dan tozaroq:

```python
import os
from contextlib import suppress

# Fayl mavjud bo'lsa o'chiramiz, bo'lmasa e'tiborsiz qoldiramiz
with suppress(FileNotFoundError):
    os.remove("maybe_missing.txt")

print("Continued without crashing")
```

### Xulosa
- Fayl yoki ulanish bilan ishlaganda imkon qadar `with` ishlating.
- `__enter__` va `__exit__` bilan o'zingiz resurs boshqaruvini yarating.
- Funksional va ixcham usul uchun `@contextmanager` dan foydalaning.
- Bir nechta kontekst menejerni bitta `with`'da birlashtiring va kutilgan xatolarni e'tiborsiz qoldirish uchun `suppress` ishlating.
