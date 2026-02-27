---
layout: tutorial.njk
lang: uz
title: Python fayl I/O (kirish/chiqish)
order: 23
permalink: /tutorial/uz/python-file-io/
---

<img src="/img/tutorial/19-dasar-dasar-io-python.webp" alt="Python fayl I/O" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Bu bo'lim Python 3 da asosiy input/output (I/O) amallarini qamrab oladi.

### `print()` bilan chiqish

`print()` qiymatlarni matnga aylantirib standard output'ga yozadi.

```python
print("Python is a great programming language")
print("A", "B", "C", sep="-")
```

### `input()` bilan klaviaturadan kiritish

Python 3 da `input()` doim string qaytaradi.

```python
name = input("Your name: ")
age = int(input("Your age: "))
print(f"Hello {name}, next year you are {age + 1}")
```

### Fayl o'qish

Fayl avtomatik yopilishi uchun `with` ishlating.

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

O'qish uchun keng tarqalgan metodlar:

- `read()` -> butun kontent
- `readline()` -> bitta qator
- `readlines()` -> qatorlar ro'yxati (list)

### Faylga yozish

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("learn python\n")
    f.write("File I/O is important\n")
```

Fayl mode'lari:

- `"r"` o'qish
- `"w"` yozish (overwrite qiladi)
- `"a"` qo'shib yozish (append)
- `"x"` yangi fayl yaratish
- Binary mode uchun `"b"` qo'shing (`"rb"`, `"wb"`)

### Xavfsiz JSON I/O misoli

```python
import json

data = {"name": "Alice", "level": "intermediate"}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("user.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)
```

