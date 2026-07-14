---
layout: tutorial.njk
lang: uz
title: Python satrlar
description: "Satrlarni yarating, kesib oling va formatlang hamda har kuni kerak bo'ladigan satr metodlaridan foydalaning."
order: 12
permalink: /uz/tutorial/python-strings/
---

<img src="/img/tutorial/12-python-string-data-type.webp" alt="Python string ma'lumot turi" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

String — Unicode belgilar ketma-ketligi. Python'da string'larni bir tirnoq, qo'sh tirnoq yoki uch tirnoq (`triple quotes`) bilan yozish mumkin.

```python
print("Hello World")
```

### Yonma-yon yozilgan string literal'lar

Python yonma-yon yozilgan string **literal**larni avtomatik birlashtiradi (concatenate qiladi):

```python
text = "Py" "thon"
print(text)  # Python
```

Bu uzun string'larni bir nechta qatorga bo'lib yozishda qulay:

```python
message = (
    "This is a long message "
    "split across multiple lines."
)
print(message)
```

Bu faqat literal'lar uchun ishlaydi. O'zgaruvchilar uchun `+` yoki f-string ishlating.

### String ichidan qiymat olish

Indexing va slicing'dan foydalaning:

```python
name = "John Doe"
message = "John Doe learns Python"

print("name[0]:", name[0])
print("message[1:4]:", message[1:4])
```

String'lar manfiy indekslarni (oxiridan sanash) va `len()` ni ham qo'llab-quvvatlaydi:

```python
word = "Python"

print(word[-1])   # n
print(word[-3:])  # hon
print(len(word))  # 6
```

### String'larni yangilash

String'lar o'zgarmas (`immutable`). String'ni "o'zgartirish" uchun yangisini yaratasiz:

```python
message = "Hello World"
print(message[:6] + "Python")  # Hello Python
```

### Keng tarqalgan escape belgilar

| Escape | Ma'nosi |
| ---------------- | ------------------------------------ |
| `\n` | Yangi qator |
| `\t` | Gorizontal tab |
| `\r` | Carriage return |
| `\"` | Qo'sh tirnoq |
| `\'` | Bir tirnoq |
| `\\` | Backslash |
| `\b` | Backspace |
| `\f` | Form feed |
| `\v` | Vertical tab |
| `\a` | Bell / alert |
| `\0` | Null belgi |
| `\xhh` | Hex qiymat bo'yicha belgi (masalan `\x41` bu `A`) |
| `\uXXXX` | Unicode belgi (16-bit, masalan `\u00E9` bu `e`) |
| `\UXXXXXXXX` | Unicode belgi (32-bit) |
| `\ooo` | Octal qiymat bo'yicha belgi (masalan `\101` bu `A`) |

### `print()` va string ifodasi

`print()` matnni ko'rsatadi, `repr()` esa string ifodasini (escape sequence'lar bilan) qaytaradi:

```python
text = "First line.\nSecond line."

print(text)
print(repr(text))
```

### String operatorlari

Agar `a = "Hello"` va `b = "Python"` bo'lsa:

| Operator | Misol | Natija |
| --------- | ------------------ | ----------------------------- |
| `+` | `a + b` | `HelloPython` |
| `*` | `a * 2` | `HelloHello` |
| `[]` | `a[1]` | `e` |
| `[:]` | `a[1:4]` | `ell` |
| `in` | `"H" in a` | `True` |
| `not in` | `"Z" not in a` | `True` |

Raw string'lar regex va Windows path'lari uchun foydali:

```python
path = r"C:\new_folder\test"
print(path)
```

> <i class="fa-solid fa-circle-info" aria-hidden="true"></i> **Eslatma:** Raw string literal bitta backslash bilan tugay olmaydi (masalan `r"C:\new_folder\"` noto'g'ri). Agar oxirida backslash kerak bo'lsa, oddiy string ishlating: `"C:\\new_folder\\"`.

### String formatlash

Python bir nechta formatlash usullarini qo'llab-quvvatlaydi:

```python
name = "Zara"
weight = 21

# f-string (tavsiya etiladi)
print(f"My name is {name} and weight is {weight} kg")

# str.format
print("My name is {} and weight is {} kg".format(name, weight))

# %-formatting (legacy, lekin ishlaydi)
print("My name is %s and weight is %d kg" % (name, weight))
```

### `%` formatlash bo'yicha tezkor jadval

| Specifier | Ma'nosi | Misol |
| --------- | ------- | ------- |
| `%s` | String | `"%s" % "Python"` |
| `%d` | Signed integer | `"%d" % 42` |
| `%i` | Signed integer (`%d` bilan bir xil) | `"%i" % 42` |
| `%f` | Float | `"%f" % 3.14` |
| `%.2f` | Aniqlik bilan float | `"%.2f" % 3.14159` |
| `%e` | Eksponensial (kichik harf) | `"%e" % 0.001` |
| `%E` | Eksponensial (katta harf) | `"%E" % 0.001` |
| `%g` | `%f` va `%e` dan qisqaroq ko'rinish | `"%g" % 0.001` |
| `%c` | Bitta belgi | `"%c" % 65` |
| `%x` | Hex (kichik harf) | `"%x" % 255` |
| `%X` | Hex (katta harf) | `"%X" % 255` |
| `%o` | Octal | `"%o" % 8` |

### Triple quotes

Uch tirnoq ko'p qatorli matn uchun qulay:

```python
text = """This is a long string
that spans multiple lines.
It can contain \t and \n characters too."""
print(text)
```

### Python 3 da Unicode string'lar

Python 3 string'lari standart holatda Unicode (UTF-8). Python 2 da Unicode string uchun `u` prefiksi kerak edi, Python 3 da bunga hojat yo'q.

```python
greeting = "Hello"
city = "London"
emoji = "\U0001F600"
print(greeting, city, emoji)
```

Unicode escape'laridan foydalanish yoki belgini bevosita yozish mumkin:

```python
print("\u00E9")         # e (Unicode escape belgisi)
print("cafe\u0301")     # urg'uli cafe
```

### Built-in string metodlar

| Metod | Izoh |
| ---------------------------------------------- | ---------------------------------------------------------------- |
| `capitalize()` | Birinchi harfni katta, qolganini kichik qiladi |
| `center(width, fillchar)` | `width` ichida markazga tekislaydi, `fillchar` bilan to'ldiradi |
| `count(sub, start, end)` | `sub` nechta uchrashini sanaydi |
| `endswith(suffix, start, end)` | String `suffix` bilan tugasa `True` |
| `find(sub, start, end)` | `sub` ning eng kichik indeksini qaytaradi, topilmasa `-1` |
| `index(sub, start, end)` | `find()` kabi, lekin topilmasa `ValueError` beradi |
| `isalnum()` | Hammasi harf/raqam bo'lsa `True` |
| `isalpha()` | Hammasi harf bo'lsa `True` |
| `isdigit()` | Hammasi raqam bo'lsa `True` |
| `isdecimal()` | Hammasi decimal bo'lsa `True` |
| `islower()` | Harfli belgilar kichik bo'lsa `True` |
| `isnumeric()` | Hammasi numeric bo'lsa `True` |
| `isspace()` | Hammasi bo'sh joy bo'lsa `True` |
| `istitle()` | Title-case bo'lsa `True` |
| `isupper()` | Harfli belgilar katta bo'lsa `True` |
| `join(iterable)` | Iterable'ni ajratuvchi sifatida string bilan birlashtiradi |
| `ljust(width, fillchar)` | Chapga tekislaydi |
| `lower()` | Hammasini kichik harfga o'giradi |
| `lstrip(chars)` | Boshidagi belgilarni olib tashlaydi (standart: whitespace) |
| `replace(old, new, count)` | `old` ni `new` ga almashtiradi |
| `rfind(sub, start, end)` | O'ngdan qidirib `find()` kabi ishlaydi |
| `rindex(sub, start, end)` | O'ngdan qidirib `index()` kabi ishlaydi |
| `rjust(width, fillchar)` | O'ngga tekislaydi |
| `rstrip(chars)` | Oxiridagi belgilarni olib tashlaydi (standart: whitespace) |
| `split(sep, maxsplit)` | Ajratuvchi bo'yicha ro'yxatga bo'ladi |
| `splitlines()` | Qator chegaralari bo'yicha bo'ladi |
| `startswith(prefix, start, end)` | String `prefix` bilan boshlansa `True` |
| `strip(chars)` | Bosh va oxirini tozalaydi |
| `swapcase()` | Kichikni kattaga, kattani kichikka o'zgartiradi |
| `title()` | Har bir so'zning birinchi harfini kattalashtiradi |
| `upper()` | Hammasini katta harfga o'giradi |
| `zfill(width)` | Chap tomondan nol bilan to'ldiradi |

```python
text = "  learn python  "
print(text.strip().title())  # Learn Python (natija)
```
