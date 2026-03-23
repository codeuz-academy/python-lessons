---
layout: tutorial.njk
lang: uz
title: Python ro'yxat (list)
description: "Python'da Python ro'yxat (list) mavzusini amaliy misollar va tushunarli izohlar bilan o'rganing."
order: 14
permalink: /uz/tutorial/python-lists/
---

<img src="/img/tutorial/14-python-list-data-type.webp" alt="Python ro'yxat (list) ma'lumot turi" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python'dagi eng asosiy ma'lumot tuzilmalaridan biri — ketma-ketlik (sequence), xususan list. Ketma-ketlikdagi har bir element o'z o'rni (indeksi) bilan belgilanadi. List'dagi birinchi indeks 0, ikkinchisi 1 va hokazo.

Python'da ketma-ketliklarning (sequence) 6 ta o'rnatilgan (built-in) turi bor, lekin eng ko'p ishlatiladigani list va tuple. List'lar uchun umumiy amallar: indeks bo'yicha murojaat (indexing), kesim olish (slicing), qo'shish, ko'paytirish va a'zolikni tekshirish (membership). Shuningdek, list uzunligini yoki eng katta/eng kichik elementni topish uchun o'rnatilgan funksiyalar mavjud.

### Python list yaratish

List — Python'dagi eng moslashuvchan ma'lumot turlaridan biri. U vergul bilan ajratilgan elementlarni `[]` ichida yozish orqali yaratiladi. Muhim jihati: list ichidagi elementlar bir xil turda bo'lishi shart emas.

List yaratish uchun `[]` ichida vergul bilan ajratib yozing. Quyida oddiy misol:

```python
# Python dasturlash tilida list yaratishning oddiy misoli
list1 = ['chemistry', 'physics', 1993, 2017]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
```

### Python list ichidan qiymat olish

List qiymatlarini olish uchun indeks yoki kesim (slice) bilan `[]` dan foydalaning.

Quyida misol:

```python
# Python list ichidan qiymat olish usuli

list1 = ['physics', 'chemistry', 1993, 2017]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
```

Yuqoridagi koddan keyin natija quyidagicha bo'ladi:

`list1[0]: physics`
`list2[1:5]: [2, 3, 4, 5]`

### Python list qiymatlarini yangilash

List ichidagi bitta yoki bir nechta qiymatni tayinlash operatorining chap tomonida kesim (slice) berib yangilash mumkin. Shuningdek, `append()` metodi orqali list'ga element qo'shish mumkin. Misol:

```python
list = ['physics', 'chemistry', 1993, 2017]
print("Value at index 2 : ", list[2])

list[2] = 2001
print("New value at index 2 : ", list[2])
```

### Python list ichidan qiymat o'chirish

List ichidagi qiymatlarni o'chirish uchun elementni aniq bilsangiz `del` ishlatishingiz mumkin. Qaysi element o'chirilishini aniq bilmasangiz `remove()` metodi foydali. Misol:

```python
# Python list ichidan qiymat o'chirishga misol

list = ['physics', 'chemistry', 1993, 2017]

print(list)
del list[2]
print("After value at index 2 is deleted : ", list)
```

### Python list ustida asosiy amallar

List'lar `+` va `*` operatorlariga string'lar kabi javob beradi: bu yerda ular mos ravishda birlashtirish va takrorlash ma'nosini beradi (natija yangi list bo'ladi).

Aslida, list'lar oldingi bo'limdagi string'lar kabi umumiy ketma-ketlik (sequence) amallarini qo'llab-quvvatlaydi. Quyida asosiy amallar jadvali:

| Python ifodasi | Natija | Izoh |
| ---------------------------------------- | -------------------------------------- | ------------- |
| `len([1, 2, 3, 4])` | `4` | Uzunlik |
| `[1, 2, 3] + [4, 5, 6]` | `[1, 2, 3, 4, 5, 6]` | Birlashtirish |
| `['Hello!'] * 4` | `['Hello!', 'Hello!', 'Hello!', 'Hello!']` | Takrorlash |
| `2 in [1, 2, 3]` | ` True` | A'zolik (membership) |
| `for x in [1,2,3] : print(x,end = ' ')` | `1 2 3` | Iteratsiya |

### Python list: indexing, slicing va matritsa

List'lar ketma-ketlik (sequence) bo'lgani uchun indekslash (indexing) va kesim olish (slicing) string'lar bilan bir xil ishlaydi.

Quyidagi qiymat bo'lsin:

`L = ['C++', 'Java', 'Python']`

| Python ifodasi | Natija | Izoh |
| ----------------- | -------------------- | -------------------------- |
| `L[2]` | `'Python'` | Indeks 0 dan boshlanadi |
| `L[-2]` | `'Java'` | Manfiy indeks: o'ngdan sanaydi |
| `L[1:]` | `['Java', 'Python']` | Kesim (slice) qismi olinadi |

### Python list uchun o'rnatilgan funksiyalar va metodlar

Python'da list uchun quyidagi o'rnatilgan funksiyalar mavjud:

| Python funksiyasi | Izoh |
| ---------------------- | ----------------------------------------------- |
| `len(list) ` | List uzunligini qaytaradi. |
| `max(list) ` | Eng katta qiymatli elementni qaytaradi. |
| `min(list) ` | Eng kichik qiymatli elementni qaytaradi. |
| `list(seq) ` | Tuple'ni list'ga aylantiradi. |

Python'da list uchun quyidagi o'rnatilgan metodlar mavjud:

| Python metodi | Izoh |
| -------------------------- | ------------------------------------------------------------- |
| `list.append(obj) ` | `obj` ni list oxiriga qo'shadi |
| `list.count(obj) ` | `obj` nechta marta uchraganini qaytaradi |
| `list.extend(seq) ` | `seq` elementlarini list oxiriga qo'shadi |
| `list.index(obj) ` | `obj` uchragan eng kichik indeksni qaytaradi |
| `list.insert(index, obj) ` | `obj` ni berilgan indeksga qo'shadi |
| `list.pop(obj = list[-1])` | Oxirgi elementni yoki berilgan `obj` ni olib tashlab qaytaradi |
| `list.remove(obj) ` | `obj` ni olib tashlaydi |
| `list.reverse() ` | List'ni joyida teskari qiladi |
| `list.sort([func]) ` | List'ni tartiblaydi; berilsa taqqoslash `func` ishlatadi |

