---
layout: tutorial.njk
lang: uz
title: Pytest Fixtures haqida
description: "pytest fixture, scope va parametrizatsiya bilan tayyorlash, tozalash va test ma'lumotlarini toza ulashing."
order: 43
permalink: /uz/tutorial/pytest-fixtures/
---

<img src="/img/tutorial/python-pytest.webp" alt="Pytest Fixtures" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Oldingi testlash darsimizda biz `pytest` yordamida asosiy testlarni qanday yozishni o'rgandik. Biroq, haqiqiy loyihalarda testlar ishlashidan oldin ma'lum bir holatni o'rnatish (masalan, ma'lumotlar bazasiga ulanish) va keyin uni tozalash kerak bo'ladi. `pytest` da bu **Fixtures** (Fiksturalar) yordamida amalga oshiriladi.

## Fixture nima?

Fixture - bu test funksiyalaringiz ishlashidan oldin (va xohishga ko'ra keyin) ishlaydigan funksiya.

```python
import pytest

@pytest.fixture
def sample_user():
    return {"id": 1, "username": "jane_doe", "role": "admin"}

def test_user_is_admin(sample_user):
    assert sample_user["role"] == "admin"
```

## Setup va Teardown (Yield)

Agar `return` o'rniga `yield` ishlatsangiz, `yield` gacha bo'lgan qism testdan oldin (setup), keyingi qism testdan so'ng (teardown/tozalash) ishlaydi.

```python
import pytest

@pytest.fixture
def database_connection():
    db = connect_to_database()
    yield db  # Test shu yerda bajariladi
    db.close()

def test_insert_user(database_connection):
    database_connection.insert("dummy user")
    assert database_connection.count() == 1
```

Tayyor funksiyalarni har doim qulay joyda foydalanishingiz mumkin.
