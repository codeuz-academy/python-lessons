---
layout: tutorial.njk
lang: uz
title: Python unit testing
description: "unittest bilan avtomatik testlar yozing va ishga tushiring, shunda o'zgarishlar ishlaydigan kodni jimgina buzmaydi."
order: 41
permalink: /uz/tutorial/python-unit-testing/
---

<img src="/img/tutorial/41-python-unit-testing.webp" alt="Python unit testing" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Unit testing — bu dastur kodining alohida qismlarini (funksiya, metod yoki class) test qilish usuli. Maqsad: ularning to'g'ri ishlayotganini tekshirish.

"Lekin hozir kodim ishlayapti-ku!"
Bugun ishlashi mumkin, lekin 6 oy o'tib bitta qatorni o'zgartirasiz va boshqa funksiyalar buzilib ketadi. Unit test'lar — sizning "xavfsizlik to'ri"ngiz.

Python'da ikkita asosiy test freymvorki (framework) bor: `unittest` (o'rnatilgan/built-in) va `pytest` (uchinchi tomon/third-party, lekin juda ommabop).

### 1. `unittest` (o'rnatilgan/built-in) bilan

`unittest` JUnit (Java) dan ilhomlangan. U sinfga asoslangan (class-based) yondashuvdan foydalanadi.

Masalan, quyidagi oddiy funksiyalar bo'lsin:
```python
# calc.py fayli
def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
```

Test faylni yaratamiz:
<div class="warning">Bu test yuqorida tavsiflangan <code>calc.py</code> faylini yaratgan bo'lishingizni taxmin qiladi.</div>

```python
# non-runnable: requires external environment/setup
# test_calc.py fayli
import unittest
from calc import add, divide

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

        # Exception tekshirish
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

Ishga tushirish: `python test_calc.py`

#### Keng tarqalgan `unittest` assertion'lari

`TestCase` xato yuz berganda foydali xabar chiqaradigan maxsus assertion metodlarini taqdim etadi:

| Metod | Nimani tekshiradi |
| ------------------------------ | ---------------------------------- |
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `x` rost (truthy) |
| `assertFalse(x)` | `x` yolg'on (falsy) |
| `assertIs(a, b)` | `a is b` (xuddi o'sha obyekt) |
| `assertIsNone(x)` | `x is None` |
| `assertIn(a, b)` | `a in b` |
| `assertRaises(Error)` | blok `Error` keltirib chiqaradi |
| `assertAlmostEqual(a, b)` | `a` va `b` 7 xonagacha teng |

#### Setup va teardown

`setUp()` **har bir** test metodidan oldin, `tearDown()` esa har biridan keyin ishlaydi. Testlar o'zini takrorlamasligi uchun ulardan fixture yaratish va tozalashda foydalaning:

```python
# non-runnable: requires external environment/setup
import unittest

class TestList(unittest.TestCase):
    def setUp(self):
        self.items = [1, 2, 3]      # har bir test uchun yangi ma'lumot

    def tearDown(self):
        self.items = None           # har bir testdan keyin tozalash

    def test_length(self):
        self.assertEqual(len(self.items), 3)

    def test_append(self):
        self.items.append(4)
        self.assertIn(4, self.items)
```

### 2. `pytest` (zamonaviy tavsiya)

`pytest` ixchamroq, kuchliroq va ko'proq "Pythonic". U class'lar o'rniga oddiy funksiyalar va standart `assert` dan foydalanadi.

O'rnatish:
```bash
python -m pip install pytest
```

Pytest bilan test yozish:
<div class="warning">Shuningdek, <code>pytest</code> ni o'rnatishingiz va <code>calc.py</code> ni xuddi shu papkada saqlashingiz kerak.</div>

```python
# non-runnable: requires external environment/setup
# test_calc_pytest.py fayli
import pytest
from calc import add, divide

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

Terminal'da `pytest` deb yozing. Pytest `test_` bilan boshlanadigan fayllarni avtomatik topadi.

#### Parametrlangan testlar

Har bir kirish uchun testni takrorlash o'rniga, `@pytest.mark.parametrize` bir xil testni har bir ma'lumot qatori uchun bir martadan ishga tushiradi — har bir holat alohida hisobot beradi:

```python
# non-runnable: requires external environment/setup
import pytest
from calc import add

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 7),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### 3. Mocking tushunchasi

Mocking - test qilinayotgan tizimning ayrim qismlarini mock obyektlar bilan almashtirish texnikasi. Bu kod API, database yoki file system kabi tashqi tizimlarga bog'liq bo'lganda foydali.

Misol: biz API so'rov yuboradigan funksiyani test qilmoqchimiz, lekin haqiqiy so'rov yubormoqchi emasmiz (sekin va internet talab qiladi).

`unittest.mock` bilan:

```python
# non-runnable: requires requests
from unittest.mock import Mock, patch
import requests

# Test qilinadigan funksiya
def get_user_data(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    return None

# Mock bilan test
@patch('requests.get')
def test_get_user_data(mock_get):
    # Mock'ni sozlash
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Bob"}

    # Mock javobni mock_get'ga berish
    mock_get.return_value = mock_response

    # Funksiyani ishga tushirish
    result = get_user_data("http://fakeurl.com")

    # Tekshirish
    assert result["name"] == "Bob"
    # requests.get to'g'ri URL bilan chaqirilganini tekshirish
    mock_get.assert_called_with("http://fakeurl.com")
```

### 4. Kod qamrovi (code coverage)

Kodingizning qanchasi test bilan qamrab olingan? Qamrov (coverage) vositalari qaysi qatorlar testdan o'tmaganini ko'rsatadi.

O'rnatish:
```bash
python -m pip install pytest-cov
```

Ishga tushirish:
```bash
pytest --cov=my_project
```

### Xulosa
- **Unit test** jiddiy ilovalar uchun kerak.
- **pytest** toza sintaksisi sabab ko'pincha afzal.
- **Mocking** unit'larni tashqi bog'liqliklardan (dependencies) ajratish uchun ishlatiladi.
- Test yozishni odat qiling: oldin test (TDD) yoki hech bo'lmasa kod bilan birga.
