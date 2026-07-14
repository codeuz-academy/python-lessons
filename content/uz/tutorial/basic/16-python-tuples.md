---
layout: tutorial.njk
lang: uz
title: Python tuple
description: "O'zgarmas tuple'lardan qayd, unpacking va funksiyadan bir nechta qiymat qaytarish uchun foydalaning."
order: 16
permalink: /uz/tutorial/python-tuples/
---

<img src="/img/tutorial/16-python-tuple-data-type.webp" alt="Python tuple ma'lumot turi" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Tuple — Python'dagi o'zgarmas ketma-ketlik. Tuple'lar ro'yxatlar kabi ketma-ketlik, lekin asosiy farq shundaki: tuple ichidagi elementlar o'zgarmaydi, ro'yxat esa o'zgarishi mumkin. Tuple `()` qavsdan, ro'yxat esa `[]` qavsdan foydalanadi.

Tuple yaratish uchun vergul bilan ajratilgan qiymatlarni yozish kifoya. Xohlasangiz ularni `()` ichiga ham olishingiz mumkin. Misol:

```python
# Python dasturlash tilida tuple yaratishning oddiy misoli

tup1 = ('physics', 'chemistry', 1993, 2017)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
```

Bo'sh tuple ikki qavs bilan yoziladi, masalan: `tup1 = ()`.
Bitta qiymatli tuple yozishda vergul kerak: `tup1 = (50,)`.
String indekslari kabi, tuple indekslari ham 0 dan boshlanadi; kesim olish (slicing), birlashtirish (concatenation) va boshqa amallar mumkin.

### Python tuple ichidan qiymat olish

Tuple qiymatlarini olish uchun indeks yoki kesim (slice) bilan `[]` dan foydalaning. Misol:

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

Tuple o'zgarmas (immutable), ya'ni tuple elementlarini yangilab bo'lmaydi. Ammo mavjud tuple'larning qismlaridan foydalanib yangi tuple yaratish mumkin:

```python
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Quyidagi amalni tuple'da bajarib bo'lmaydi,
# chunki tuple ichidagi qiymatlar o'zgarmaydi

# tup1[0] = 100;

# Shuning uchun yangi tuple yarating

tup3 = tup1 + tup2
print(tup3)
```

### Python tuple ichidan qiymat o'chirish

Tuple ichidan alohida elementni o'chirib bo'lmaydi. Keraksiz elementlarsiz yangi tuple tuzish mumkin.

Butun tuple'ni o'chirish uchun `del` buyrug'ini ishlating. Misol:

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

Tuple'lar `+` va `*` operatorlariga satrlar kabi javob beradi: bu yerda ular mos ravishda birlashtirish va takrorlash ma'nosini beradi (natija yangi tuple).

Quyida tuple uchun asosiy amallar jadvali:

| Python ifodasi | Natija | Izoh |
| ----------------------------------------- | -------------------------------------- | ------------- |
| `len((1, 2, 3))` | `3` | Uzunlik |
| `(1, 2, 3) + (4, 5, 6)` | `(1, 2, 3, 4, 5, 6)` | Birlashtirish |
| `('Hello!',) \* 4` | `('Hello!', 'Hello!', 'Hello!', 'Hello!')` | Takrorlash |
| `3 in (1, 2, 3)` | `True` | A'zolik (membership) |
| `for x in (1,2,3) : print(x, end = ' ')` | `1 2 3` | Iteratsiya |

### Python tuple: indexing, slicing va matritsa

Tuple'lar ketma-ketlik (sequence) bo'lgani uchun indekslash (indexing) va kesim olish (slicing) satrlar bilan bir xil ishlaydi.

Quyidagi qiymat bo'lsin: `T = ('C++', 'Java', 'Python')`

| Python ifodasi | Natija | Izoh |
| ----------------- | -------------------- | -------------------------- |
| `T[2]` | `'Python'` | Indeks 0 dan boshlanadi |
| `T[-2]` | `'Java'` | Manfiy indeks: o'ngdan sanaydi |
| `T[1:]` | `('Java', 'Python')` | Kesim (slice) qismi olinadi |

### Python tuple uchun o'rnatilgan funksiyalar

Python'da tuple uchun quyidagi o'rnatilgan funksiyalar mavjud:

| Python funksiyasi | Izoh |
| --------------------- | ------------------------------------------------ |
| `len(tuple)` | Tuple uzunligini qaytaradi. |
| `max(tuple)` | Eng katta qiymatli elementni qaytaradi. |
| `min(tuple)` | Eng kichik qiymatli elementni qaytaradi. |
| `tuple(seq)` | Ro'yxatni tuple'ga aylantiradi. |

### Packing va unpacking

Bir nechta qiymatni bitta tuple'ga joylash **packing** deyiladi. Tuple'ni qaytadan alohida o'zgaruvchilarga yoyish esa **unpacking** — o'zgaruvchilar soni elementlar soniga mos kelishi shart.

```python
point = (3, 5)            # packing
x, y = point             # unpacking
print(x, y)              # 3 5
```

Qolgan elementlarni ro'yxatga yig'ish uchun `*` ishlating:

```python
first, *rest = (1, 2, 3, 4)
print(first)   # 1
print(rest)    # [2, 3, 4]
```

Funksiya bir vaqtning o'zida bir nechta qiymat qaytara olishining sababi ham shu — u tuple qaytaradi, siz uni chaqiruv joyida unpack qilasiz.

### Bitta elementli tuple bilan bog'liq nozik nuqta

Tuple'ni qavslar emas, oxiridagi vergul hosil qiladi. Vergulsiz siz shunchaki qiymatning o'zini olasiz:

```python
not_a_tuple = (50)
print(type(not_a_tuple))   # <class 'int'>

one_tuple = (50,)
print(type(one_tuple))     # <class 'tuple'>
```

### Tuple metodlari

Tuple'lar o'zgarmas (immutable), shuning uchun ular faqat ikkita metod taklif etadi — ikkalasi ham faqat o'qish uchun:

```python
colors = ('red', 'green', 'blue', 'green')

print(colors.count('green'))   # 2  (necha marta uchrashi)
print(colors.index('blue'))    # 2  (birinchi mosning pozitsiyasi)
```
