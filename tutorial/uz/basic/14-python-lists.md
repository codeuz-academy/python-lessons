---
layout: tutorial.njk
lang: uz
title: Python ro'yxat (list)
order: 14
permalink: /tutorial/uz/python-lists/
---

<img src="/img/tutorial/13-tipe-data-list-python.webp" alt="Python ro'yxat (list) ma'lumot turi" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python'da eng asosiy data structure'laridan biri - ketma-ketlik (sequence), xususan list. Ketma-ketlikdagi har bir element o'z pozitsiyasi (index) bilan belgilanadi. List'dagi birinchi index - 0, ikkinchisi - 1 va hokazo.

Python'da sequence'ning 6 ta built-in turi bor, lekin eng ko'p ishlatiladigani list va tuple. List'lar uchun umumiy amallar: indexing, slicing, qo'shish, ko'paytirish va membership tekshirish. Shuningdek, list uzunligini yoki eng katta/eng kichik elementni topish uchun built-in funksiyalar mavjud.

### Python list yaratish

List - Python'dagi eng moslashuvchan (versatile) ma'lumot turi. U vergul bilan ajratilgan qiymatlar (items)ni `[]` ichida yozish orqali yaratiladi. Muhim jihati: list ichidagi elementlar bir xil turda bo'lishi shart emas.

List yaratish uchun `[]` ichida vergul bilan ajratib yozing. Quyida oddiy misol:

```python
#Simple example of creating list in python programming language
list1 = ['chemistry', 'physics', 1993, 2017]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
```

### Python list ichidan qiymat olish

List qiymatlarini olish uchun index/slice bilan `[]` dan foydalaning.

Quyida misol:

```python
#Way to access value in Python list

list1 = ['physics', 'chemistry', 1993, 2017]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
```

Yuqoridagi koddan keyin natija quyidagicha bo'ladi:

`list1[0]: physics`
`list2[1:5]: [2, 3, 4, 5]`

### Python list qiymatlarini yangilash

List ichidagi bitta yoki bir nechta qiymatni tayinlash operatorining chap tomonida slice berib yangilash mumkin. Shuningdek, `append()` metodi orqali list'ga element qo'shish mumkin. Misol:

```python
list = ['physics', 'chemistry', 1993, 2017]
print("Value at index 2 : ", list[2])

list[2] = 2001
print("New value at index 2 : ", list[2])
```

### Python list ichidan qiymat o'chirish

List ichidagi qiymatlarni o'chirish uchun elementni aniq bilsangiz `del` ishlatishingiz mumkin. Qaysi element o'chirilishini aniq bilmasangiz `remove()` metodi foydali. Misol:

```python
#Example of how to delete value in python list

list = ['physics', 'chemistry', 1993, 2017]

print(list)
del list[2]
print("After value at index 2 is deleted : ", list)
```

### Python list ustida asosiy amallar

List'lar `+` va `*` operatorlariga string'lar kabi javob beradi: bu yerda ular concatenation va repetition ma'nosini beradi (natija yangi list bo'ladi).

Aslida, list'lar oldingi bo'limdagi string'lar kabi umumiy sequence amallarini qo'llab-quvvatlaydi. Quyida asosiy amallar jadvali:

| Python ifodasi | Natija | Izoh |
| ---------------------------------------- | -------------------------------------- | ------------- |
| `len([1, 2, 3, 4])` | `4` | Uzunlik |
| `[1, 2, 3] + [4, 5, 6]` | `[1, 2, 3, 4, 5, 6]` | Birlashtirish |
| `['Hello!'] * 4` | `['Hello!', 'Hello!', 'Hello!', 'Hello!']` | Takrorlash |
| `2 in [1, 2, 3]` | ` True` | Membership |
| `for x in [1,2,3] : print(x,end = ' ')` | `1 2 3` | Iteratsiya |

### Python list: indexing, slicing va "matrix"

List'lar sequence bo'lgani uchun indexing va slicing string'lar bilan bir xil ishlaydi.

Quyidagi qiymat bo'lsin:

`L = ['C++', 'Java', 'Python']`

| Python ifodasi | Natija | Izoh |
| ----------------- | -------------------- | -------------------------- |
| `L[2]` | `'Python'` | Index 0 dan boshlanadi |
| `L[-2]` | `'Java'` | Manfiy index: o'ngdan sanaydi |
| `[1:]` | `['Java', 'Python']` | Slice qismi olinadi |

### Python list uchun built-in metod va funksiyalar

Python'da list uchun quyidagi built-in funksiyalar mavjud:

| Python funksiyasi | Izoh |
| ---------------------- | ----------------------------------------------- |
| `len(list) ` | List uzunligini qaytaradi. |
| `max(list) ` | Eng katta qiymatli elementni qaytaradi. |
| `min(list) ` | Eng kichik qiymatli elementni qaytaradi. |
| `list(seq) ` | Tuple'ni list'ga aylantiradi. |

Python'da list uchun quyidagi built-in metodlar mavjud:

| Python metodi | Izoh |
| -------------------------- | ------------------------------------------------------------- |
| `list.append(obj) ` | `obj` ni list oxiriga qo'shadi |
| `list.count(obj) ` | `obj` nechta marta uchraganini qaytaradi |
| `list.extend(seq) ` | `seq` elementlarini list oxiriga qo'shadi |
| `list.index(obj) ` | `obj` uchragan eng kichik index'ni qaytaradi |
| `list.insert(index, obj) ` | `obj` ni berilgan index'ga qo'shadi |
| `list.pop(obj = list[-1])` | Oxirgi elementni yoki berilgan `obj` ni olib tashlab qaytaradi |
| `list.remove(obj) ` | `obj` ni olib tashlaydi |
| `list.reverse() ` | List'ni joyida teskari qiladi |
| `list.sort([func]) ` | List'ni tartiblaydi; berilsa compare `func` ishlatadi |

