---
layout: tutorial.njk
lang: uz
title: Python context manager'lar
order: 36
permalink: /uz/tutorial/python-context-managers/
---

<img src="/img/tutorial/31-context-manager-python.webp" alt="Python context managers" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Context manager - resurslarni boshqarish uchun juda chiroyli Python imkoniyati. Ular fayl, network connection yoki database connection kabi resurslar to'g'ri ochilib-yopilishini kafolatlaydi, hatto jarayon o'rtasida xato bo'lsa ham.

Siz ham fayl ochib, keyin yopishni unutganmisiz? Python'da buni `with` kalit so'zi bilan oson oldini olish mumkin.

### 1. `with` kalit so'zi

Context manager ishlatishning eng keng tarqalgan usuli - `with` statement.

**Context manager'siz (leak xavfi):**
```python
file = open("data.txt", "w")
try:
    file.write("Hello World")
finally:
    file.close() # We must manually close it
```

**Context manager bilan (xavfsiz va toza):**
```python
with open("data.txt", "w") as file:
    file.write("Hello World")

# Fayl bu yerda avtomatik yopiladi, hatto yozish paytida xato bo'lsa ham.
```

### 2. O'zingiz context manager yaratish

O'zingizning context manager'ingizni `__enter__` va `__exit__` metodlariga ega class orqali yaratishingiz mumkin.

`__enter__`: `with` blokiga kirilganda ishlaydi. Qaytgan qiymat `as ...` dagi o'zgaruvchiga beriladi.
`__exit__`: `with` blokidan chiqilganda ishlaydi (normal tugash yoki error).

#### Misol: database connection manager (simulyatsiya)

```python
class ManageDB:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"--> Opening connection to {self.db_name}")
        return self # This object becomes 'db' variable

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

Python `contextlib` modulini beradi. U generator va `@contextmanager` decorator yordamida context manager yaratishni osonlashtiradi. Bu class yaratishdan ixchamroq.

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

Kod bloki qancha vaqt ishlaganini o'lchash uchun context manager yozish mumkin.

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

### Xulosa
- Fayl yoki connection bilan ishlaganda imkon qadar `with` ishlating.
- `__enter__` va `__exit__` bilan o'zingiz resurs boshqaruvini yarating.
- Funksional va ixcham usul uchun `@contextmanager` dan foydalaning.

