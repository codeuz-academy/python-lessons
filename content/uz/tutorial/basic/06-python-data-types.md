---
layout: tutorial.njk
lang: uz
title: Python ma'lumot turlari
description: "Python'da Python ma'lumot turlari mavzusini amaliy misollar va tushunarli izohlar bilan o'rganing."
order: 6
permalink: /uz/tutorial/python-data-types/
---

<img src="/img/tutorial/6-python-data-types.webp" alt="Python ma'lumot turlari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Ma'lumot turi (data type) - kompyuter xotirasida axborotni saqlash uchun ishlatiladigan tur.

Pythonning ma'lumot turlari boshqa dasturlash tillari bilan solishtirganda o'ziga xos.

Quyida Python dasturlash tilidagi asosiy ma'lumot turlari keltirilgan:

| Ma'lumot turi | Misol | Izoh |
| ----------- | ------------------------ | ------------------------------------------------------------------------------------ |
| Boolean | `True` or `False` | Rost `True` (qiymati `1`) yoki yolg'on `False` (qiymati `0`) |
| String | `"Let's learn Python"` | Belgilar/matnlar ketma-ketligi ( `"` yoki `'` bilan o'raladi) |
| Integer | `25` or `1209` | Butun sonlar |
| Float | `3.14` or `0.99` | O'nlik kasr sonlar |
| Hexadecimal | `0x9a` or `0x1d3` | Hex formatdagi sonlar (16-lik sanoq tizimi) |
| Complex | `1 + 5j ` | Haqiqiy va xayoliy qismlardan iborat kompleks sonlar |
| List | `['xyz', 786, 2.23]` | Turli turlarni saqlaydigan ketma-ketlik va uning ichidagi qiymatlar o'zgarishi mumkin |
| Tuple | `('xyz', 768, 2.23)` | Turli turlarni saqlaydigan ketma-ketlik, lekin ichidagi qiymatlar o'zgarmaydi |
| Set | `{'apple', 'orange'}` | Tartibsiz (unordered) va takrorlanmaydigan (unique) elementlar to'plami |
| Dictionary | `{'name': 'adi','id':2}` | Key-value juftliklari ko'rinishidagi ma'lumotlar |

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

