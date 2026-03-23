---
layout: tutorial.njk
lang: uz
title: Python lug'at (dictionary)
description: "Python'da Python lug'at (dictionary) mavzusini amaliy misollar va tushunarli izohlar bilan o'rganing."
order: 17
permalink: /uz/tutorial/python-dictionaries/
---

<img src="/img/tutorial/17-python-dictionary-data-type.webp" alt="Python lug'at (dictionary) ma'lumot turi" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python dictionary list yoki tuple'dan farq qiladi, chunki u kalit-qiymat (key-value) juftliklarini saqlaydi. Har bir kalit o'z qiymatidan ikki nuqta (`:`) bilan ajratiladi, elementlar vergul bilan ajratiladi va hammasi `{}` ichida bo'ladi. Bo'sh dictionary `{}` ko'rinishida yoziladi.

Dictionary kalitlari istalgan turda bo'lishi mumkin, lekin kalit o'zgarmas (immutable) tur bo'lishi kerak (masalan, string, son yoki tuple).

### Python dictionary ichidan qiymat olish

Dictionary elementlarini olish uchun `[]` ichida kalit yoziladi. Oddiy misol:

```python
# Python'da dictionary yaratish misoli

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
```

### Python dictionary qiymatlarini yangilash

Dictionary'ni yangi kalit-qiymat qo'shish, mavjud kalit qiymatini o'zgartirish yoki elementni o'chirish orqali yangilash mumkin:

```python
# Python dictionary'ni yangilash

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # Mavjud qiymatni o'zgartirish
dict['School'] = "DPS School" # Yangi element qo'shish

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
```

### Python dictionary elementlarini o'chirish

Dictionary ichidan alohida elementlarni o'chirish, hammasini tozalash yoki butun dictionary'ni o'chirish mumkin.

Butun dictionary'ni o'chirish uchun `del` statement ishlatiladi. Misol:

```python
# Python dictionary'dan o'chirish misoli

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # 'Name' kalitli elementni o'chirish
dict.clear() # dictionary'dagi barcha elementlarni tozalash
del dict # butun dictionary'ni o'chirish

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
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
| `dict.items() ` | `(kalit, qiymat)` juftliklari ro'yxatini qaytaradi |
| `dict.keys() ` | Kalitlar ro'yxatini qaytaradi |
| ` dict.setdefault(key, default=None)` | `get()` ga o'xshaydi, lekin `key` bo'lmasa `dict[key]=default` qiladi |
| `dict.update(dict2) ` | `dict2` dagi kalit-qiymat juftliklarini dictionary'ga qo'shadi |
| `dict.values() ` | Qiymatlar ro'yxatini qaytaradi |

