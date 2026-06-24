---
layout: tutorial.njk
lang: uz
title: Python fayl I/O (kirish/chiqish)
description: "open(), fayl rejimlari va with operatori yordamida matn va binar fayllarni xavfsiz o'qing va yozing."
order: 23
permalink: /uz/tutorial/python-file-io/
---

<img src="/img/tutorial/23-python-file-io.webp" alt="Python fayl I/O" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Bu bo'lim Python 3'dagi asosiy kirish/chiqish (I/O) amallarini qamrab oladi — ekranga chiqarish, klaviaturadan ma'lumot olish va diskdagi fayllar bilan ishlash.

### `print()` bilan chiqarish

`print()` qiymatlarni matnga aylantiradi va standart chiqishga yozadi.

```python
print("Python is a great programming language")
print("A", "B", "C", sep="-")
```

### `input()` bilan klaviaturadan kiritish

Python 3'da `input()` har doim string qaytaradi.

```python
# Odatda input() dan keladigan qiymatlarni simulyatsiya qilamiz
name = "Alice"
age = 24
print(f"Hello {name}, next year you are {age + 1}")
```

### Faylni ochish

Hammasi built-in `open()` funksiyasidan boshlanadi. U fayl yo'lini va nima qilmoqchi ekaningizni bildiruvchi **rejimni** (mode) oladi hamda fayl obyektini qaytaradi.

```python
f = open("notes.txt", "w", encoding="utf-8")
f.write("learn python\n")
f.close()   # ochgan narsangizni doim yoping
```

Matn fayllari uchun har doim `encoding="utf-8"` bering, shunda kodingiz har bir operatsion tizimda bir xil ishlaydi.

### Fayl rejimlari

| Rejim | Ma'nosi |
| ------ | ----------------------------------------------------- |
| `"r"` | O'qish (default). Fayl bo'lmasa xato beradi. |
| `"w"` | Yozish. Faylni yaratadi yoki **ustiga yozadi**. |
| `"a"` | Qo'shish. Oxiriga qo'shadi, mavjud kontentni saqlaydi. |
| `"x"` | Yangi fayl yaratish. Allaqachon mavjud bo'lsa xato beradi. |
| `"r+"` | O'qish va yozish. |
| `"b"` | Binar rejim, boshqalar bilan birga (`"rb"`, `"wb"`). |
| `"t"` | Matn rejimi (default), boshqalar bilan birga. |

### `with` operatori (tavsiya etiladi)

Fayl ish tugagach har doim yopilishi kerak. `with` operatori uni siz uchun avtomatik yopadi — hatto blok ichida xato yuz bersa ham — shuning uchun `close()`'ni o'zingiz chaqirishingiz shart emas.

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("learn python\n")
    f.write("File I/O is important\n")
# fayl bu yerda avtomatik yopiladi
```

### Fayllarni o'qish

Matnni o'qishning bir nechta usuli bor — hammasini birdan yoki qatorma-qator olishingizga qarab.

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()        # butun fayl bitta string sifatida
    print(content)
```

Asosiy o'qish metodlari:

- `read()` → butun fayl string sifatida
- `read(n)` → birinchi `n` ta belgi
- `readline()` → bitta qator (oxiridagi yangi qator belgisi bilan)
- `readlines()` → har bir elementi bitta qator bo'lgan list

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    first = f.readline()
    print("First line:", first.strip())

with open("notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("Number of lines:", len(lines))
```

### Fayl bo'ylab aylanish

Faylni qayta ishlashning eng toza va xotira uchun eng qulay usuli — uni to'g'ridan-to'g'ri aylanib chiqish. U bir vaqtning o'zida bitta qatorni o'qiydi, bu hatto juda katta fayllar uchun ham ishlaydi.

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### Yozish va qo'shish

`"w"` bilan ochish faylni ustiga yozadi; `"a"` mavjud kontentni saqlab, oxiriga qo'shadi. Stringlar listini yozish uchun `writelines()` ishlating.

```python
# Ustiga yozish
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("line 1\n")

# Qo'shish
with open("notes.txt", "a", encoding="utf-8") as f:
    f.writelines(["line 2\n", "line 3\n"])

with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

### Binar fayllar bilan ishlash

Xom baytlarni o'qish yoki yozish uchun rejimga `"b"` qo'shing — rasmlar, audio yoki istalgan matnsiz fayl uchun. Binar rejimda siz `str` emas, `bytes` bilan ishlaysiz.

```python
data = bytes([80, 121])   # "Py" uchun baytlar

with open("data.bin", "wb") as f:
    f.write(data)

with open("data.bin", "rb") as f:
    print(f.read())   # b'Py'
```

### Fayllarni tekshirish va o'chirish

`os` va `pathlib` modullari faylning mavjudligini tekshirish, hajmini olish va uni o'chirish imkonini beradi.

```python
import os

with open("temp.txt", "w", encoding="utf-8") as f:
    f.write("temporary\n")

print(os.path.exists("temp.txt"))   # True
print(os.path.getsize("temp.txt"))  # bayt hajmi

os.remove("temp.txt")
print(os.path.exists("temp.txt"))   # False
```

Zamonaviy `pathlib` API'si shu amallarni obyektga yo'naltirilgan uslubda taklif etadi:

```python
from pathlib import Path

path = Path("greeting.txt")
path.write_text("Hello from pathlib\n", encoding="utf-8")

print(path.read_text(encoding="utf-8"))
print(path.exists())   # True

path.unlink()          # faylni o'chirish
```

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
