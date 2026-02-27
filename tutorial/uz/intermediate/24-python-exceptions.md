---
layout: tutorial.njk
lang: uz
title: Python exception'lar (exceptions)
order: 24
permalink: /tutorial/uz/python-exceptions/
---

<img src="/img/tutorial/20-belajar-exception-python.webp" alt="Python exceptions" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Exception'lar - bu runtime xatolar bo'lib, dastur oqimini (flow) to'xtatib qo'yadi. Python bunday holatlarni xavfsiz boshqarish uchun `try`/`except` ni beradi.
Exception'larni to'g'ri tutish dasturingizni yanada ishonchli qiladi va foydalanuvchi uchun tushunarliroq xatolik xabarlarini chiqaradi.

### Asosiy exception handling

```python
try:
    value = int(input("Enter a number: "))
    print(10 / value)
except ValueError:
    print("Input must be a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Imkon qadar aniq (specific) exception turlarini tuting. `except Exception:` kabi keng tutishni faqat kerak bo'lganda ishlating va konteks aniq bo'lishi uchun log qiling yoki qayta ko'taring (re-raise).

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

Input/state noto'g'ri bo'lsa `raise` ishlating:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

Xatoni erta ko'tarish noto'g'ri data dastur ichiga chuqurroq kirib ketishini oldini oladi.

### Custom exception'lar

```python
class InvalidUsernameError(Exception):
    pass


def register(username):
    if len(username) < 3:
        raise InvalidUsernameError("Username must be at least 3 characters")
```

Yirik ilovalarda custom exception'lar error handling'ni aniqroq qiladi, ayniqsa turli xatoliklar uchun turli javob qaytarish kerak bo'lganda.

### Keng tarqalgan built-in exception'lar

| Nomi | Odatdagi holat |
| --------------------- | ------------------------------------------------------ |
| `Exception` | Ko'p exception'lar uchun bazaviy class |
| `ValueError` | Tur to'g'ri, lekin qiymat noto'g'ri |
| `TypeError` | Amal/funksiya uchun tur noto'g'ri |
| `KeyError` | Dictionary'da key topilmadi |
| `IndexError` | Index chegaradan tashqarida |
| `FileNotFoundError` | Fayl yo'li topilmadi |
| `PermissionError` | Fayl/resursga ruxsat yo'q |
| `OSError` | OS darajasidagi xatolar |
| `ImportError` / `ModuleNotFoundError` | Import muvaffaqiyatsiz |
| `AssertionError` | `assert` statement yiqildi |
| `StopIteration` | Iterator tugadi |
| `EOFError` | Input tugadi |

### Assertions (`assert`)

Assertion'lar development paytida ichki sanity check uchun foydali:

```python
def divide(a, b):
    assert b != 0, "b must not be zero"
    return a / b
```

Assertion'lar dasturchi xatolarini tutish uchun; foydalanuvchi input'ini tekshirish uchun emas. Assertion'lar optimizatsiya flag'lari bilan o'chirilishi mumkin (masalan `python -O`).

### Python 3 uchun eslatmalar

- `IOError` va `EnvironmentError` - `OSError` ning alias'i.
- Python 3 da `StandardError` yo'q.
- Concurrent kod uchun Python `ExceptionGroup` va `except*` ni ham qo'llab-quvvatlaydi.

### Ko'p uchraydigan xatolar

- `except:` ni yalang'och ishlatib, real bug'larni yashirib yuborish.
- Noto'g'ri exception turini tutish (handler umuman ishlamaydi).
- Log qilmasdan xatoni yutib yuborish (debug qiyinlashadi).
