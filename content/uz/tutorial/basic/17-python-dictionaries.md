---
layout: tutorial.njk
lang: uz
title: Python lug'at (dictionary)
description: "Lug'atlar bilan kalitlarni qiymatlarga bog'lang va ularni xavfsiz o'qish, yangilash va aylanib chiqishni o'rganing."
order: 17
permalink: /uz/tutorial/python-dictionaries/
---

<img src="/img/tutorial/17-python-dictionary-data-type.webp" alt="Python lug'at (dictionary) ma'lumot turi" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python dictionary list yoki tuple'dan farq qiladi, chunki u kalit-qiymat (key-value) juftliklarini saqlaydi. Har bir kalit o'z qiymatidan ikki nuqta (`:`) bilan ajratiladi, elementlar vergul bilan ajratiladi va hammasi `{}` ichida bo'ladi. Bo'sh dictionary `{}` ko'rinishida yoziladi.

Dictionary kalitlari istalgan turda bo'lishi mumkin, lekin kalit o'zgarmas (immutable) tur bo'lishi kerak (masalan, string, son yoki tuple).

### Python dictionary ichidan qiymat olish

Dictionary elementlarini olish uchun `[]` ichida kalit yoziladi. Oddiy misol:

O'zgaruvchini `dict` deb nomlamang — bu Python'ning o'rnatilgan `dict()` funksiyasini berkitib qo'yadi. Ma'noli nom ishlating:

```python
# Python'da dictionary yaratish misoli

person = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("person['Name']: ", person['Name'])
print("person['Age']: ", person['Age'])
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

Butun dictionary'ni o'chirish uchun `del` statement ishlatiladi. Misol:

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
| `dict.get(key, default=None) ` | `key` bo'yicha qiymatni qaytaradi yoki topilmasa `default` |
| `dict.items() ` | `(kalit, qiymat)` juftliklarining view'ini qaytaradi |
| `dict.keys() ` | Kalitlarning view'ini qaytaradi |
| ` dict.setdefault(key, default=None)` | `get()` ga o'xshaydi, lekin `key` bo'lmasa `dict[key]=default` qiladi |
| `dict.update(dict2) ` | `dict2` dagi kalit-qiymat juftliklarini dictionary'ga qo'shadi |
| `dict.values() ` | Qiymatlarning view'ini qaytaradi |

