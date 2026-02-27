---
layout: tutorial.njk
lang: uz
title: Python lug'at (dictionary)
order: 17
permalink: /tutorial/uz/python-dictionaries/
---

<img src="/img/tutorial/15-tipe-data-dictionary-python.webp" alt="Python lug'at (dictionary) ma'lumot turi" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python dictionary list yoki tuple'dan farq qiladi. Chunki u key va value juftliklarini saqlaydi. Har bir key o'z value'sidan ikki nuqta (`:`) bilan ajratiladi, elementlar vergul bilan ajratiladi, va hammasi `{}` ichida bo'ladi. Bo'sh dictionary `{}` ko'rinishida yoziladi.

Dictionary key'lari istalgan turda bo'lishi mumkin, lekin key immutable tur bo'lishi kerak (masalan, string, son yoki tuple).

### Python dictionary ichidan qiymat olish

Dictionary elementlarini olish uchun `[]` ichida key yoziladi. Oddiy misol:

```python
#Example how to create Dictionary in Python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
```

### Python dictionary qiymatlarini yangilash

Dictionary'ni yangi key-value qo'shish, mavjud key qiymatini o'zgartirish yoki elementni o'chirish orqali yangilash mumkin:

```python
#Update python dictionary

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # Modify existing entry
dict['School'] = "DPS School" # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
```

### Python dictionary elementlarini o'chirish

Dictionary ichidan alohida elementlarni o'chirish, hammasini tozalash yoki butun dictionary'ni o'chirish mumkin.

Butun dictionary'ni o'chirish uchun `del` statement ishlatiladi. Misol:

```python
#Example how to delete in Python Dictionary

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # remove entry with key 'Name'
dict.clear() # remove all entries in dict
del dict # delete entire dictionary

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
```

### Python dictionary uchun built-in funksiyalar

Python'da dictionary uchun quyidagi built-in funksiyalar mavjud:

| Python funksiyasi | Izoh |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `len(dict)` | Dictionary uzunligini qaytaradi (elementlar soni). |
| `str(dict) ` | Dictionary'ning chop etiladigan string ko'rinishini beradi |
| `type(variable)` | Berilgan o'zgaruvchining turini qaytaradi. Agar dictionary bo'lsa, dictionary turini qaytaradi. |

### Python dictionary uchun built-in metodlar

Python'da dictionary uchun quyidagi built-in metodlar mavjud:

| Python metodi | Izoh |
| ------------------------------------- | ----------------------------------------------------------------------------------------- |
| `dict.clear() ` | Dictionary'ning hamma elementlarini o'chiradi |
| `dict.copy() ` | Dictionary'ning shallow copy'sini qaytaradi |
| `dict.fromkeys() ` | Seq'dan key olib, value'larni berilgan qiymatga o'rnatib yangi dictionary yaratadi |
| `dict.get(key, default=None) ` | `key` bo'yicha value'ni qaytaradi yoki topilmasa default |
| `dict.items() ` | `(key, value)` juftliklar ro'yxatini qaytaradi |
| `dict.keys() ` | Key'lar ro'yxatini qaytaradi |
| ` dict.setdefault(key, default=None)` | `get()` ga o'xshaydi, lekin key bo'lmasa `dict[key]=default` qiladi |
| `dict.update(dict2) ` | `dict2` dagi key-value'larni dictionary'ga qo'shadi |
| `dict.values() ` | Value'lar ro'yxatini qaytaradi |

