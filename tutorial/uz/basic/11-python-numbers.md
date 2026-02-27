---
layout: tutorial.njk
lang: uz
title: Python son turlari (numbers)
order: 11
permalink: /tutorial/uz/python-numbers/
---

<img src="/img/tutorial/11-tipe-data-number-pada-python.webp" alt="Python son turlari - int, float, complex" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Python'da 3 ta built-in son turi bor:

- `int` (butun son)
- `float` (o'nlik kasr son)
- `complex` (kompleks son)

Sonlar immutable: son qiymatini "o'zgartirish" aslida yangi obyekt yaratadi.

| Tur | Misollar |
| -------- | ------------------------- |
| `int` | `20`, `-13`, `0`, `0x56` |
| `float` | `0.1`, `1.20`, `-92.0`, `6.02e23` |
| `complex` | `3+4j`, `35j`, `3.12e-12j` |

> Python 3 da `020` kabi integer literal'lar noto'g'ri. O'nlik uchun `20`, sakkizlik (octal) uchun `0o24` ishlating.

### Python son turlarini o'zgartirish (conversion)

O'zgartirish uchun o'rnatilgan konstruktorlardan foydalaning:

- `int(x)` `x` ni butun songa o'giradi.
- `float(x)` `x` ni o'nlik kasr songa o'giradi.
- `complex(x)` real qismi `x` bo'lgan kompleks son beradi.
- `complex(x, y)` `x + yj` ko'rinishidagi kompleks son beradi.

### Python matematik funksiyalari

Python built-in funksiyalar va `math` moduli orqali matematik amallarni taqdim etadi.

| Nomi | Ishlatilishi | Izoh |
| ------------ | ----------------- | -------------------------------------------------------------------- |
| Absolyut | `abs(x)` | `x` ning absolyut qiymati |
| Daraja | `pow(x, y)` | `x ** y` ga teng |
| Yaxlitlash | `round(x, n)` | `n` ta raqamgacha yaxlitlaydi (bo'lmasa eng yaqin butun songa) |
| Maksimum | `max(a, b, ...)` | Eng katta qiymat |
| Minimum | `min(a, b, ...)` | Eng kichik qiymat |
| Kvadrat ildiz | `math.sqrt(x)` | `x` ning kvadrat ildizi |
| Ceiling | `math.ceil(x)` | `>= x` bo'lgan eng kichik butun son |
| Floor | `math.floor(x)` | `<= x` bo'lgan eng katta butun son |
| Logarifm | `math.log(x)` | Natural logarifm |

```python
import math

print(abs(-9))
print(pow(2, 5))
print(round(2.675, 2))
print(math.sqrt(16))
```

### Python'da tasodifiy sonlar (random)

`random` moduli simulyatsiya, test va o'yinlarda ko'p ishlatiladi.

| Nomi | Ishlatilishi | Izoh |
| --------- | ----------------------------------- | ----------------------------------------------------------- |
| Choice | `choice(seq)` | Ketma-ketlikdan tasodifiy element |
| RandRange | `randrange(start, stop, step)` | Range'dan tasodifiy qiymat |
| Random | `random()` | `[0.0, 1.0)` oralig'ida tasodifiy float |
| Seed | `seed(x)` | Random seed'ni o'rnatish |
| Shuffle | `shuffle(lst)` | List'ni joyida (in place) aralashtirish |
| Uniform | `uniform(x, y)` | `[x, y]` oralig'ida tasodifiy float |

### Python trigonometrik funksiyalari

`math` trigonometrik yordamchi funksiyalarni beradi:

| Nomi | Ishlatilishi | Izoh |
| ------- | --------------------- | ------------------------------------------------- |
| Cosine | `math.cos(x)` | Radionlarda `x` ning kosinusi |
| Sine | `math.sin(x)` | Radionlarda `x` ning sinusi |
| Tangent | `math.tan(x)` | Radionlarda `x` ning tangensi |
| Degrees | `math.degrees(x)` | Radionlarni gradusga o'tkazish |
| Radians | `math.radians(x)` | Graduslarni radianlarga o'tkazish |

### Python matematik konstantalari

| Nomi | Ishlatilishi | Izoh |
| ---- | ---------- | ----------------------- |
| Pi | `math.pi` | Pi matematik konstantasi |
| e | `math.e` | e matematik konstantasi |

### Floating-point arifmetika: ifodalanish va cheklovlar

Floating-point sonlar ikkilik (binary) yaqinlashuv (approximation) bo'lgani uchun ba'zi o'nlik qiymatlar aniq ifodalanmaydi.

```python
print(0.1 + 0.1 + 0.1)     # 0.30000000000000004
print(0.1 + 0.1 + 0.1 == 0.3)  # False
```

Xavfsizroq taqqoslash:

```python
import math

print(math.isclose(0.1 + 0.1 + 0.1, 0.3))  # True
```

Aniq o'nlik arifmetika (masalan, pul) uchun `decimal` dan foydalaning:

```python
from decimal import Decimal

price = Decimal("0.1") + Decimal("0.1") + Decimal("0.1")
print(price == Decimal("0.3"))  # True
```

Aniq kasrlar uchun `fractions.Fraction` ishlating:

```python
from fractions import Fraction

print(Fraction(1, 10) * 3 == Fraction(3, 10))  # True
```

### `round()` haqida eslatma

Python "round half to even" qoidasidan foydalanadi:

```python
print(round(0.5))  # 0
print(round(1.5))  # 2
print(round(2.5))  # 2
```
