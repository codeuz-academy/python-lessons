---
layout: tutorial.njk
lang: uz
title: Python lug'at (dictionary)
description: "Lug'atlar bilan kalitlarni qiymatlarga bog'lang va ularni xavfsiz o'qish, yangilash va aylanib chiqishni o'rganing."
order: 17
permalink: /uz/tutorial/python-dictionaries/
---

<img src="/img/tutorial/17-python-dictionary-data-type.webp" alt="Python lug'at (dictionary) ma'lumot turi" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python lug'ati (`dictionary`) ro'yxat yoki tuple'dan farq qiladi: u kalit-qiymat (`key-value`) juftliklarini saqlaydi. Har bir kalit o'z qiymatidan ikki nuqta (`:`) bilan ajratiladi, elementlar vergul bilan ajratiladi va hammasi `{}` ichida yoziladi. Bo'sh dictionary `{}` ko'rinishida yaratiladi.

Dictionary kalitlari turli turlarda bo'lishi mumkin, lekin kalit o'zgarmas (`immutable`) tur bo'lishi kerak (masalan, satr, son yoki tuple).

### Python dictionary ichidan qiymat olish

Dictionary elementlarini olish uchun `[]` ichida kalit yoziladi. Oddiy misol:

O'zgaruvchini `dict` deb nomlamang — bu Python'ning o'rnatilgan `dict()` funksiyasini berkitib qo'yadi. Ma'noli nom ishlating:

```python
# Python'da dictionary yaratish misoli

person = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("person['Name']: ", person['Name'])
print("person['Age']: ", person['Age'])
```

### `get()` bilan xavfsiz murojaat

Mavjud bo'lmagan kalitni `[]` orqali o'qish `KeyError` keltirib chiqaradi. `get()` metodi buning o'rniga `None` yoki siz tanlagan standart qiymatni qaytaradi, shu sababli xavfsizroq:

```python
person = {'Name': 'Zara', 'Age': 7}

print(person.get('Name'))          # Zara
print(person.get('City'))          # None
print(person.get('City', 'N/A'))   # N/A
```

### Kalit mavjudligini tekshirish

Kalitga murojaat qilishdan oldin uni tekshirish uchun `in` operatoridan foydalaning:

```python
person = {'Name': 'Zara', 'Age': 7}

print('Name' in person)       # True
print('City' in person)       # False
print('City' not in person)   # True
```

### Dictionary bo'ylab aylanish

Kalitlar, qiymatlar yoki bir vaqtning o'zida kalit-qiymat juftliklari bo'ylab aylanishingiz mumkin:

```python
person = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

for key in person:                 # standart holatda kalitlar
    print(key)

for value in person.values():      # qiymatlar
    print(value)

for key, value in person.items():  # kalit va qiymat birga
    print(key, "->", value)
```

### Python dictionary qiymatlarini yangilash

Dictionary'ni yangi kalit-qiymat qo'shish, mavjud kalit qiymatini o'zgartirish yoki elementni o'chirish orqali yangilash mumkin:

```python
# Python dictionary'ni yangilash

person = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
person['Age'] = 8  # Mavjud qiymatni o'zgartirish
person['School'] = "High School"  # Yangi element qo'shish

print("person['Age']: ", person['Age'])
print("person['School']: ", person['School'])
```

### Python dictionary elementlarini o'chirish

Dictionary ichidan alohida elementlarni o'chirish, hammasini tozalash yoki butun dictionary'ni o'chirish mumkin.

Butun dictionary'ni o'chirish uchun `del` buyrug'i ishlatiladi. Misol:

```python
# Python dictionary'dan o'chirish misoli

person = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del person['Name']  # bitta elementni kalit bo'yicha o'chirish
print("'Name' o'chirilgandan keyin: ", person)

person.clear()  # barcha elementlarni tozalash (bo'sh dictionary qoladi)
print("clear() dan keyin: ", person)

del person  # dictionary obyektini butunlay o'chirish
# Shu qatordan keyin `person` ga murojaat qilish NameError beradi.
```

### Python dictionary uchun o'rnatilgan funksiyalar

Python'da dictionary uchun quyidagi o'rnatilgan funksiyalar mavjud:

| Python funksiyasi | Izoh |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `len(dict)` | Dictionary uzunligini qaytaradi (elementlar soni). |
| `str(dict) ` | Dictionary'ning chop etiladigan string ko'rinishini beradi |
| `type(variable)` | Berilgan o'zgaruvchining turini qaytaradi. Agar dictionary bo'lsa, dictionary turini qaytaradi. |

### Python dictionary uchun o'rnatilgan metodlar

Python'da dictionary uchun quyidagi o'rnatilgan metodlar mavjud:

| Python metodi | Izoh |
| ------------------------------------- | ----------------------------------------------------------------------------------------- |
| `dict.clear() ` | Dictionary'ning hamma elementlarini o'chiradi |
| `dict.copy() ` | Dictionary'ning yuzaki nusxasini (shallow copy) qaytaradi |
| `dict.fromkeys() ` | Ketma-ketlikdan (seq) kalitlar olib, qiymatlarni berilgan qiymatga o'rnatib yangi dictionary yaratadi |
| `dict.get(key, default=None) ` | `key` bo'yicha qiymatni qaytaradi yoki topilmasa `default` qiymatni beradi |
| `dict.items() ` | `(kalit, qiymat)` juftliklarining view'ini qaytaradi |
| `dict.keys() ` | Kalitlarning view'ini qaytaradi |
| ` dict.setdefault(key, default=None)` | `get()` ga o'xshaydi, lekin `key` bo'lmasa `dict[key]=default` qiladi |
| `dict.update(dict2) ` | `dict2` dagi kalit-qiymat juftliklarini dictionary'ga qo'shadi |
| `dict.values() ` | Qiymatlarning view'ini qaytaradi |
