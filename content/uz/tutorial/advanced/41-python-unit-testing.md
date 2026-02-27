---
layout: tutorial.njk
lang: uz
title: Python unit testing
order: 41
permalink: /uz/tutorial/python-unit-testing/
---

<img src="/img/tutorial/36-panduan-unit-testing-python.webp" alt="Python unit testing" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Unit testing - bu source code'ning alohida unit'larini (funksiya, metod yoki class) test qilish usuli. Maqsad: ularning to'g'ri ishlayotganini tekshirish.

"Lekin hozir kodim ishlayapti-ku!"
Bugun ishlashi mumkin, lekin 6 oy o'tib bitta qatorni o'zgartirasiz va boshqa funksiyalar buzilib ketadi. Unit test'lar - sizning safety net'ingiz.

Python'da ikkita asosiy test framework bor: `unittest` (built-in) va `pytest` (third-party, lekin juda ommabop).

### 1. `unittest` (built-in) bilan

`unittest` JUnit (Java) dan ilhomlangan. U class-based yondashuvdan foydalanadi.

Masalan, quyidagi oddiy funksiyalar bo'lsin:
```python
# calc.py
def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
```

Test faylni yaratamiz:
```python
# test_calc.py
import unittest
from calc import add, divide

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        
        # Test exception
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

Ishga tushirish: `python test_calc.py`

### 2. `pytest` (zamonaviy tavsiya)

`pytest` ixchamroq, kuchliroq va ko'proq "Pythonic". U class'lar o'rniga oddiy funksiyalar va standart `assert` dan foydalanadi.

O'rnatish:
```bash
python -m pip install pytest
```

Pytest bilan test yozish:
```python
# test_calc_pytest.py
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

### 3. Mocking tushunchasi

Mocking - test qilinayotgan tizimning ayrim qismlarini mock obyektlar bilan almashtirish texnikasi. Bu kod API, database yoki file system kabi tashqi tizimlarga bog'liq bo'lganda foydali.

Misol: biz API so'rov yuboradigan funksiyani test qilmoqchimiz, lekin haqiqiy so'rov yubormoqchi emasmiz (sekin va internet talab qiladi).

`unittest.mock` bilan:

```python
from unittest.mock import Mock, patch
import requests

# Function to test
def get_user_data(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    return None

# Test with Mock
@patch('requests.get')
def test_get_user_data(mock_get):
    # Setup mock
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Bob"}
    
    # Put mock response into mock_get
    mock_get.return_value = mock_response
    
    # Run function
    result = get_user_data("http://fakeurl.com")
    
    # Assert
    assert result["name"] == "Bob"
    # Ensure requests.get is actually called with correct URL
    mock_get.assert_called_with("http://fakeurl.com")
```

### 4. Code coverage

Kodingizning qanchasi test bilan qamrab olingan? Coverage vositalari qaysi qatorlar testdan o'tmaganini ko'rsatadi.

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
- **Mocking** unit'larni tashqi dependency'lardan ajratish uchun ishlatiladi.
- Test yozishni odat qiling: oldin test (TDD) yoki hech bo'lmasa kod bilan birga.
