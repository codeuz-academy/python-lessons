---
layout: tutorial.njk
lang: uz
title: Python exception'lar (exceptions)
description: "Python'da Python exception'lar (exceptions) mavzusini amaliy misollar va tushunarli izohlar bilan o'rganing."
order: 24
permalink: /uz/tutorial/python-exceptions/
---

<img src="/img/tutorial/24-python-exceptions.webp" alt="Python exceptions" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Exception'lar — dastur bajarilishi vaqtida (runtime) yuz beradigan xatolar bo'lib, dastur oqimini to'xtatib qo'yishi mumkin. Python bunday holatlarni xavfsiz boshqarish uchun `try`/`except` ni beradi.
Exception'larni to'g'ri tutish dasturingizni yanada ishonchli qiladi va foydalanuvchi uchun tushunarliroq xatolik xabarlarini chiqaradi.

### Asosiy exception'larni boshqarish

```python
for raw_value in ["5", "0", "oops"]:
    try:
        value = int(raw_value)
        print(10 / value)
    except ValueError:
        print("Input must be a number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
```

Imkon qadar aniq exception turlarini tuting. `except Exception:` kabi juda keng tutishni faqat zarurat bo'lganda ishlating va kontekst aniq bo'lishi uchun log yozing yoki xatoni qayta ko'taring (re-raise).

### `else` va `finally`

- `else` exception bo'lmaganda ishlaydi.
- `finally` doim ishlaydi (tozalash kodi).

```python
f = None

try:
    f = open("data.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("File not found")
else:
    print(f.read())
finally:
    if f is not None:
        f.close()
```

Fayl bilan ishlashda ko'pincha `with open(...)` soddaroq. `finally` ni `with` boshqarmaydigan resurslar uchun tozalashni kafolatlash kerak bo'lganda ishlating.

### Exception ko'tarish (raising)

Kiritma (input) yoki holat (state) noto'g'ri bo'lsa `raise` ishlating:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

Xatoni erta ko'tarish noto'g'ri ma'lumot dastur ichiga chuqurroq kirib ketishini oldini oladi.

### Custom exception'lar

```python
class InvalidUsernameError(Exception):
    pass


def register(username):
    if len(username) < 3:
        raise InvalidUsernameError("Username must be at least 3 characters")
```

Yirik ilovalarda custom exception'lar xatolarni boshqarishni aniqroq qiladi, ayniqsa turli xatoliklar uchun turli javob qaytarish kerak bo'lganda.

### Keng tarqalgan o'rnatilgan (built-in) exception'lar

| Nomi | Odatdagi holat |
| --------------------- | ------------------------------------------------------ |
| `Exception` | Ko'p exception'lar uchun bazaviy sinf (class) |
| `ValueError` | Tur to'g'ri, lekin qiymat noto'g'ri |
| `TypeError` | Amal/funksiya uchun tur noto'g'ri |
| `KeyError` | Lug'atda (dictionary) kalit topilmadi |
| `IndexError` | Indeks chegaradan tashqarida |
| `FileNotFoundError` | Fayl yo'li topilmadi |
| `PermissionError` | Fayl/resursga ruxsat yo'q |
| `OSError` | OS darajasidagi xatolar |
| `ImportError` / `ModuleNotFoundError` | Import muvaffaqiyatsiz |
| `AssertionError` | `assert` tekshiruvi muvaffaqiyatsiz bo'ldi |
| `StopIteration` | Iterator tugadi |
| `EOFError` | Kiritma tugadi |

### Assertions (`assert`)

Assertion'lar ishlab chiqish jarayonida ichki mantiqiy tekshiruv (sanity check) uchun foydali:

```python
def divide(a, b):
    assert b != 0, "b must not be zero"
    return a / b
```

Assertion'lar dasturchi xatolarini tutish uchun; foydalanuvchi kiritmasini tekshirish uchun emas. Assertion'lar optimizatsiya flaglari bilan o'chirilishi mumkin (masalan `python -O`).

### Python 3 uchun eslatmalar

- `IOError` va `EnvironmentError` - `OSError` ning alias'i.
- Python 3 da `StandardError` yo'q.
- Concurrent kod uchun Python `ExceptionGroup` va `except*` ni ham qo'llab-quvvatlaydi.

### Ko'p uchraydigan xatolar

- `except:` ni yalang'och ishlatib, haqiqiy xatolarni yashirib yuborish.
- Noto'g'ri exception turini tutish (tutuvchi/handler umuman ishlamaydi).
- Log yozmasdan xatoni yutib yuborish (nosozliklarni topish/debug qiyinlashadi).
