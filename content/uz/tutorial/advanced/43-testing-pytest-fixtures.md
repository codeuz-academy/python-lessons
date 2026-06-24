---
layout: tutorial.njk
lang: uz
title: Pytest Fixtures haqida
description: "pytest fixture, scope va parametrizatsiya bilan tayyorlash, tozalash va test ma'lumotlarini toza ulashing."
order: 43
permalink: /uz/tutorial/pytest-fixtures/
---

<img src="/img/tutorial/python-pytest.webp" alt="Pytest Fixtures" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Oldingi kirish testlash darsimizda biz `pytest` yordamida asosiy testlarni qanday yozishni o'rgandik. Biroq, haqiqiy loyihalarda testlar ishlashidan oldin ma'lum bir holatni o'rnatish (masalan, ma'lumotlar bazasiga ulanish yoki soxta ma'lumotlar yaratish) va ish tugagach uni tozalash kerak bo'ladi. `pytest` da bu **Fixtures** (Fiksturalar) yordamida nafis tarzda amalga oshiriladi.

## Fixture nima?

Fixture - bu `pytest` sizning haqiqiy test funksiyalaringiz ishlashidan oldin (va xohishga ko'ra keyin) ishlatadigan funksiya. Fixture'ni so'rash uchun shunchaki uning nomini test funksiyangizga argument sifatida qo'shasiz.

```python
# non-runnable: requires pytest
import pytest

@pytest.fixture
def sample_user():
    return {"id": 1, "username": "jane_doe", "role": "admin"}

def test_user_is_admin(sample_user):
    # pytest sample_user funksiyasi qaytargan qiymatni shu yerga avtomatik yuboradi
    assert sample_user["role"] == "admin"
```

## Setup va Teardown (Yield)

Fixture'lar faqat ma'lumot qaytarish uchun emas; ular resurslarni boshqarish uchun ham mo'ljallangan. Agar `return` o'rniga `yield` kalit so'zidan foydalansangiz, `yield` dan oldingi kod tayyorlash (setup), `yield` dan keyingi kod esa test tugagandan so'ng ishlaydigan tozalash (teardown) bo'ladi.

```python
# non-runnable: requires pytest
import pytest

@pytest.fixture
def database_connection():
    # Tayyorlash (Setup)
    db = connect_to_database()
    print("Database connected")
    
    yield db  # Test aynan shu yerda bajariladi
    
    # Tozalash (Teardown)
    db.close()
    print("Database connection closed")

def test_insert_user(database_connection):
    database_connection.insert("dummy user")
    assert database_connection.count() == 1
```

## Fixture Scope'lari

Standart holatda fixture **har bir test** funksiyasi uchun bir marta ishlaydi (`scope="function"`). Agar fixture'ni ishga tushirish qimmatga tushsa (masalan, docker konteynerini ishga tushirish), uni kamroq tez-tez ishlashi uchun qamrovini (scope) o'zgartirishingiz mumkin.

- `scope="function"`: (Standart) Har bir test uchun bir marta ishlaydi.
- `scope="class"`: Har bir test sinfi uchun bir marta ishlaydi.
- `scope="module"`: Har bir fayl uchun bir marta ishlaydi.
- `scope="session"`: Test to'plamining bir bajarilishi davomida bir marta ishlaydi.

```python
# non-runnable: requires pytest
@pytest.fixture(scope="session")
def expensive_api_client():
    # Buni 100 ta test so'rasa ham, faqat bir marta bajariladi
    client = ExpensiveAPIClient()
    client.authenticate()
    yield client
    client.logout()
```

## Bir nechta Fixture'dan foydalanish

Testlar bir nechta fixture'ni so'rashi mumkin.

```python
# non-runnable: requires pytest
@pytest.fixture
def user():
    return User(name="Alice")

@pytest.fixture
def shopping_cart():
    return Cart()

def test_add_to_cart(user, shopping_cart):
    shopping_cart.add(user, "Laptop")
    assert "Laptop" in shopping_cart.items
```

## `conftest.py` fayli

Agar fixture'larni har bir test fayliga qo'lda import qilmasdan bir nechta test fayllarida mavjud bo'lishini xohlasangiz, ularni test papkangizning ildizida joylashgan `conftest.py` nomli faylda aniqlang. Pytest uni sehrli tarzda o'zi topib oladi.

## Xulosa

Fixture'lar `pytest`ning yuragi hisoblanadi. Ular qayta ishlatishni rag'batlantiradi, tayyorlash mantig'ini test mantig'idan ajratadi va `yield` namunasi yordamida tashqi resurslarni boshqarishni nihoyatda xavfsiz hamda intuitiv qiladi.
