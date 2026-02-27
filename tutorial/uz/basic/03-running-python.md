---
layout: tutorial.njk
lang: uz
title: Pythonni ishga tushirish
order: 3
permalink: /tutorial/uz/running-python/
---

<img src="/img/tutorial/3-panduan-cepat-menjalankan-python.webp" alt="Pythonni qanday ishga tushirish" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Pythonni odatda ikki usulda ishga tushirish mumkin:

1. Tezkor tajribalar uchun **interaktiv rejim (REPL)**.
2. `.py` fayllarni ishga tushirish uchun **skript rejimi**.

> <i class="fa-solid fa-circle-info" aria-hidden="true"></i> **Eslatma:** Siz ushbu veb-saytda ham har bir kod parchasini interaktiv tarzda ishga tushirib va tahrirlab ko'rishingiz mumkin.

### Tezkor boshlash (OS bo'yicha)

#### Linux / macOS

1. **Terminal** ni oching.
2. Python o'rnatilganini tekshiring:

   ```bash
   python3 --version
   ```

3. Interaktiv rejimni (REPL) ishga tushiring:

   ```bash
   python3
   ```

4. Skript faylini ishga tushiring:

   ```bash
   python3 hello.py
   ```

#### Windows

1. **PowerShell** yoki **Command Prompt** ni oching.
2. Python o'rnatilganini tekshiring (quyidagilardan birini sinang):

   ```bash
   py --version
   # or
   python --version
   ```

3. Interaktiv rejimni (REPL) ishga tushiring:

   ```bash
   py
   # or
   python
   ```

4. Skript faylini ishga tushiring:

   ```bash
   py hello.py
   # or
   python hello.py
   ```

### Pythonni interaktiv rejimda (REPL) ishga tushirish

Pythonni ishga tushiring:

```bash
# Linux/macOS
python3

# Windows (mavjud bo'lsa, tavsiya etiladi)
py
```

Siz `>>>` promptini ko'rasiz. Misol:

```python
>>> print("Welcome to Python")
Welcome to Python
>>> 2 + 3
5
```

`>>>` - REPL prompti, Python sintaksisining bir qismi emas. `>>>` ni `.py` faylga yoki veb-saytdagi kod muharririga yozmang.

Fayl/muharrirlar uchun quyidagi ko'rinishdan foydalaning:

```python
print("Welcome to Python")
print(2 + 3)
```

REPL'dan chiqish:

- `exit()`
- <kbd>Ctrl</kbd>+<kbd>D</kbd> (Linux/macOS)
- <kbd>Ctrl</kbd>+<kbd>Z</kbd> so'ng <kbd>Enter</kbd> (Windows)

### Python skript faylini ishga tushirish

`hello.py` yarating:

```python
print("Learn Python")
print("at belajarpython.com")
```

Terminal'dan ishga tushiring:

```bash
# Linux/macOS
python3 hello.py

# Windows
py hello.py
# or: python hello.py
```

### Ixtiyoriy: Windows'da IDLE bilan ishga tushirish

Agar GUI muharrirni xohlasangiz:

1. Start menyusidan **IDLE (Python 3.x)** ni oching.
2. Tezkor buyruqlar uchun shell oynasidan foydalaning (`>>>`).
3. Skript fayllar uchun **File > New File** ni bosing.
4. Faylni `.py` sifatida saqlang, so'ng **Run > Run Module (F5)** orqali ishga tushiring.

![Windows'da Python Shell](/img/menjalankan-python-windows.png 'Windows Python Shell')

![Windows'da Python muharriri](/img/menjalankan-python-windows-editor.png 'Windows Python Editor')

### Command-Line argumentlar

Python command-line argumentlarni `sys.argv` orqali oladi:

```python
import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
```

Ishga tushiring:

```bash
# Linux/macOS
python3 app.py one two

# Windows
py app.py one two
```

### Pythonni ishga tushirishning boshqa usullari

Pythonning buyruq satri uchun bir nechta foydali opsiyalari bor:

> <i class="fa-solid fa-circle-info" aria-hidden="true"></i> **Eslatma:** Quyidagi misollarda `python` o'rniga Linux/macOS'da `python3`, Windows'da esa `py` dan foydalaning.

- Qisqa buyruqni ishga tushirish:

  ```bash
  python -c "print('Hello from -c')"
  ```

- Modulni skript sifatida ishga tushirish (tavsiya etiladigan uslub):

  ```bash
  python -m pip --version
  python -m venv .venv
  python -m http.server 8000
  ```

- Skriptni ishga tushirib, keyin interaktiv rejimda qolish:

  ```bash
  python -i app.py
  ```

> <i class="fa-solid fa-lightbulb" aria-hidden="true"></i> **Maslahat:** Windows'da `py` launcher aniq versiyani tanlay oladi:

```bash
py -3.13 --version
py -3.13 -m pip --version
```

### Interaktiv tahrirlash va tarix (history)

Ko'plab terminallarda REPL buyruqlar tarixini va oddiy tahrirlashni qo'llab-quvvatlaydi:

- Oldingi buyruqlar: yuqoriga/pastga strelkalar
- Qator ichida kursorni siljitish: chapga/o'ngga strelkalar

### Bajariladigan skriptlar (Unix-like)

Skriptni to'g'ridan-to'g'ri bajariladigan qilish mumkin:

```python
#!/usr/bin/env python3
print("Hello from executable script")
```

So'ng:

```bash
chmod +x hello.py
./hello.py
```

### Source fayl kodirovkasi

Python 3 standart holatda UTF-8 dan foydalanadi. Shunga qaramay, kodirovkani aniq e'lon qilish mumkin.

Encoding cookie faylning **birinchi yoki ikkinchi qatorida** bo'lishi kerak. Agar shebang ishlatsangiz, encoding cookie'ni 2-qatorga qo'ying:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
name = "learn python"
print(name)
```

Shebang bo'lmasa, uni birinchi qatorga yozishingiz mumkin:

```python
# -*- coding: utf-8 -*-
name = "learn python"
print(name)
```

