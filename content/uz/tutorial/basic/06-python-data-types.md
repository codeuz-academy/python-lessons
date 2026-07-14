---
layout: tutorial.njk
lang: uz
title: Python ma'lumot turlari
description: "Python'ning o'rnatilgan ma'lumot turlari bilan tanishing va qaysi turda ekanini qanday tekshirishni bilib oling."
order: 6
permalink: /uz/tutorial/python-data-types/
---

<img src="/img/tutorial/6-python-data-types.webp" alt="Python ma'lumot turlari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Ma'lumot turi (data type) — qiymat qanday ko'rinishda saqlanishi va u bilan qanday amallar bajarish mumkinligini belgilaydigan tur.

Python'dagi ma'lumot turlari boshqa dasturlash tillaridagiga o'xshash, lekin ulardan foydalanish uslubi Python'ga xos.

Quyida Python dasturlash tilidagi asosiy ma'lumot turlari keltirilgan:

| Ma'lumot turi | Misol | Izoh |
| ----------- | ------------------------ | ------------------------------------------------------------------------------------ |
| Boolean | `True` yoki `False` | Rost `True` (qiymati `1`) yoki yolg'on `False` (qiymati `0`) |
| String | `"Let's learn Python"` | Belgilar/matnlar ketma-ketligi ( `"` yoki `'` bilan o'raladi) |
| Integer | `25` yoki `1209` | Butun sonlar |
| Float | `3.14` yoki `0.99` | O'nlik kasr sonlar |
| Integer (hex) | `0x9a` yoki `0x1d3` | O'n oltilik (base 16) ko'rinishda yozilgan `int` — alohida tur emas |
| Complex | `1 + 5j ` | Haqiqiy va xayoliy qismlardan iborat kompleks sonlar |
| List | `['xyz', 786, 2.23]` | Turli turlarni saqlaydigan ketma-ketlik va uning ichidagi qiymatlar o'zgarishi mumkin |
| Tuple | `('xyz', 768, 2.23)` | Turli turlarni saqlaydigan ketma-ketlik, lekin ichidagi qiymatlar o'zgarmaydi |
| Set | `{'apple', 'orange'}` | Tartibsiz (unordered) va takrorlanmaydigan (unique) elementlar to'plami |
| Dictionary | `{'name': 'adi','id':2}` | Kalit-qiymat (`key-value`) juftliklari ko'rinishidagi ma'lumotlar |

Turli ma'lumot turlarini sinab ko'rish uchun quyidagi Python skriptlarini ishga tushiring.

#### Boolean

```python
print(True)
print(False)
```

#### String (Matn)

```python
print("Keling Python o'rganamiz")
print('Python o\'rganish juda oson')
```

#### Integer va Float (Butun va kasr sonlar)

```python
print(20)       # butun son
print(3.14)     # kasr son
print(0x9a)     # o'n oltilik (154 chop etadi)
print(5j)       # kompleks son
```

#### List va Tuple (Ro'yxat va tuple)

```python
print([1, 2, 3, 4, 5])           # list (o'zgartirish mumkin)
print(["bir", "ikki", "uch"])

print((1, 2, 3, 4, 5))           # tuple (o'zgartirish mumkin emas)
print(("bir", "ikki", "uch"))
```

#### Set va Dictionary (To'plam va lug'at)

```python
print({1, 2, 3, 4, 5})               # set (takrorlanmas elementlar)
print({"olma", "apelsin", "mango"})

print({"ism": "Ali", "yosh": 20})     # dictionary (kalit-qiymat)

profil = {"ism": "Vali", "yosh": 21}
print(profil)
print(type(profil))  # <class 'dict'>
```

### Turni tekshirish

Qiymat qaysi turga ega ekanini bilish uchun o'rnatilgan (`built-in`) `type()` funksiyasini ishlating. Qiymat berilgan turga tegishli yoki yo'qligini tekshirish uchun `isinstance()` ishlating.

```python
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>

print(isinstance(42, int))     # True
print(isinstance(42, str))     # False
```

### Tur o'zgartirish (Casting)

Python turlarni avtomatik aralashtirmaydi — masalan, sonni satrga qo'sha olmaysiz. Qiymatlarni tur konstruktorlari bilan aniq o'zgartiring: `int()`, `float()`, `str()`, `bool()`, `list()`.

```python
# Stringdan songa
age = int("25")
price = float("3.99")
print(age + 1, price * 2)     # 26 7.98

# Sondan satrga
count = 10
message = "Count: " + str(count)
print(message)                # Count: 10

# Son turlari o'rtasida
print(int(3.9))               # 3  (kesadi, yaxlitlamaydi)
print(float(7))               # 7.0
```

> <i class="fa-solid fa-circle-info" aria-hidden="true"></i> **Eslatma:** Agar matn yaroqli son bo'lmasa, o'zgartirish muvaffaqiyatsiz tugaydi. `int("abc")` `ValueError` keltirib chiqaradi.

Qiymatlarni `bool()` bilan rostlik (truthiness) jihatidan ham tekshirish mumkin. Bo'sh qiymatlar (`0`, `""`, `[]`, `{}`, `None`) yolg'on (falsy); qolgan hammasi rost (truthy).

```python
print(bool(0))      # False
print(bool(""))     # False
print(bool("hi"))   # True
print(bool([1]))    # True
```
