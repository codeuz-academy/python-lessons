---
layout: tutorial.njk
lang: uz
title: Python kortej (tuple)
order: 16
permalink: /uz/tutorial/python-tuples/
---

<img src="/img/tutorial/14-tipe-data-tuple-python.webp" alt="Python kortej (tuple) ma'lumot turi" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Tuple - bu Python'dagi immutable ketma-ketlik. Tuple'lar list'lar kabi sequence, lekin asosiy farq shundaki: tuple ichidagi elementlar o'zgarmaydi, list esa o'zgarishi mumkin. Tuple `()` qavsdan, list esa `[]` qavsdan foydalanadi.

Tuple yaratish - vergul bilan ajratilgan qiymatlarni yozish kifoya. Xohlasangiz ularni `()` ichiga ham olishingiz mumkin. Misol:

```python
# Python dasturlash tilida tuple yaratishning oddiy misoli

tup1 = ('physics', 'chemistry', 1993, 2017)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
```

Bo'sh tuple ikki qavs bilan yoziladi, masalan: `tup1 = ()`.
Bitta qiymatli tuple yozishda vergul kerak: `tup1 = (50,)`.
String index'lari kabi, tuple index'lari ham 0 dan boshlanadi; slicing, concatenation va boshqa amallar mumkin.

### Python tuple ichidan qiymat olish

Tuple qiymatlarini olish uchun index/slice bilan `[]` dan foydalaning. Misol:

```python
# Tuple qiymatlarini olish usuli

tup1 = ('physics', 'chemistry', 1993, 2017)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
```

Yuqoridagi koddan keyin natija quyidagicha bo'ladi:

`tup1[0]: physics`
`tup2[1:5]: (2, 3, 4, 5)`

### Python tuple qiymatlarini yangilash

Tuple immutable, ya'ni tuple elementlarini yangilab bo'lmaydi. Ammo mavjud tuple'larning qismlaridan foydalanib yangi tuple yaratish mumkin:

```python
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Quyidagi amalni tuple'da bajarib bo'lmaydi

# Chunki tuple ichidagi qiymatlar o'zgarmaydi

# tup1[0] = 100;

# Shuning uchun yangi tuple yarating

tup3 = tup1 + tup2
print(tup3)
```

### Python tuple ichidan qiymat o'chirish

Tuple ichidan alohida elementni o'chirib bo'lmaydi. Keraksiz elementlarsiz yangi tuple tuzish mumkin.

Butun tuple'ni o'chirish uchun `del` statement ishlating. Misol:

```python
tup = ('physics', 'chemistry', 1993, 2017)
print(tup)

# del bilan tuple'ni o'chirish

del tup

# keyin kerakli elementlar bilan yangi tuple yaratish

tup = ('Language', 'Literacy', 2020)
print("After deleting tuple :", tup)
```

### Python tuple ustida asosiy amallar

Tuple'lar `+` va `*` operatorlariga string'lar kabi javob beradi: concatenation va repetition (natija yangi tuple).

Quyida tuple uchun asosiy amallar jadvali:

| Python ifodasi | Natija | Izoh |
| ----------------------------------------- | -------------------------------------- | ------------- |
| `len((1, 2, 3))` | `3` | Uzunlik |
| `(1, 2, 3) + (4, 5, 6)` | `(1, 2, 3, 4, 5, 6)` | Birlashtirish |
| `('Hello!',) \* 4` | `('Hello!', 'Hello!', 'Hello!', 'Hello!')` | Takrorlash |
| `3 in (1, 2, 3)` | `True` | Membership |
| `for x in (1,2,3) : print(x, end = ' ')` | `1 2 3` | Iteratsiya |

### Python tuple: indexing, slicing va "matrix"

Tuple'lar sequence bo'lgani uchun indexing va slicing string'lar bilan bir xil ishlaydi.

Quyidagi qiymat bo'lsin: `T = ('C++', 'Java', 'Python')`

| Python ifodasi | Natija | Izoh |
| ----------------- | -------------------- | -------------------------- |
| `T[2]` | `'Python'` | Index 0 dan boshlanadi |
| `T[-2]` | `'Java'` | Manfiy index: o'ngdan sanaydi |
| `T[1:]` | `('Java', 'Python')` | Slice qismi olinadi |

### Python tuple uchun built-in funksiyalar

Python'da tuple uchun quyidagi built-in funksiyalar mavjud:

| Python funksiyasi | Izoh |
| --------------------- | ------------------------------------------------ |
| `len(tuple)` | Tuple uzunligini qaytaradi. |
| `max(tuple)` | Eng katta qiymatli elementni qaytaradi. |
| `min(tuple)` | Eng kichik qiymatli elementni qaytaradi. |
| `tuple(seq)` | List'ni tuple'ga aylantiradi. |

