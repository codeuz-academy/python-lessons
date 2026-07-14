---
layout: tutorial.njk
lang: uz
title: Pytest Fixtures haqida
description: "pytest fixture, scope va parametrizatsiya bilan tayyorlash, tozalash va test ma'lumotlarini tartibli ulashing."
order: 43
permalink: /uz/tutorial/pytest-fixtures/
---

<img src="/img/tutorial/python-pytest.webp" alt="Pytest Fixtures" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Oldingi testlash darsida `pytest` yordamida asosiy testlarni qanday yozishni o'rgandik. Haqiqiy loyihalarda esa testlar ishlashidan oldin ma'lum bir holatni tayyorlash (masalan, ma'lumotlar bazasiga ulanish yoki soxta ma'lumotlar yaratish) va ish tugagach uni tozalash kerak bo'ladi. `pytest`da bu **fixture**'lar yordamida qulay bajariladi.

## Fixture nima?

Fixture — `pytest` test funksiyalaringiz ishlashidan oldin (va kerak bo'lsa, keyin) ishga tushiradigan funksiya. Fixture'ni so'rash uchun uning nomini test funksiyangizga argument sifatida qo'shasiz.

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

Fixture'lar faqat ma'lumot qaytarish uchun emas; ular resurslarni boshqarish uchun ham mo'ljallangan. Agar `return` o'rniga `yield` kalit so'zidan foydalansangiz, `yield`dan oldingi kod tayyorlash (`setup`), `yield`dan keyingi kod esa test tugagandan so'ng ishlaydigan tozalash (`teardown`) bo'ladi.

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

- `scope="function"`: standart holat, har bir test uchun bir marta ishlaydi.
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

Agar fixture'larni har bir test fayliga qo'lda import qilmasdan bir nechta test faylida ishlatmoqchi bo'lsangiz, ularni test papkangizning ildizida joylashgan `conftest.py` faylida aniqlang. Pytest uni avtomatik topadi.

## Fixture'larni parametrlash

`params` berib, fixture'ni ro'yxatdagi **har bir** qiymat uchun bir martadan ishga tushirish mumkin. Fixture'dan foydalanadigan har bir test har bir parametr uchun bir marta ishlaydi, shuning uchun testni takrorlamasdan ko'plab kirishlarni qamrab olasiz. Joriy qiymat `request.param` orqali mavjud bo'ladi.

```python
# non-runnable: requires pytest
import pytest

@pytest.fixture(params=["sqlite", "postgres", "mysql"])
def database(request):
    return connect(request.param)

def test_connection(database):
    # Bu test uch marta ishlaydi — har bir database backend uchun
    assert database.is_connected()
```

## Foydali built-in fixture'lar

Pytest oldindan tayyor fixture'lar bilan keladi; ularni alohida aniqlamasdan so'rashingiz mumkin:

| Fixture | Vazifasi |
| ------------ | ------------------------------------------------- |
| `tmp_path` | Har bir test uchun noyob vaqtinchalik papka (`Path`). |
| `monkeypatch` | Atributlar, env o'zgaruvchilari yoki `dict` elementlarini xavfsiz patch qilish. |
| `capsys` | `stdout` / `stderr`'ga yozilgan matnni ushlash. |
| `caplog` | Test davomida chiqarilgan log yozuvlarini ushlash. |

```python
# non-runnable: requires pytest
def test_writes_file(tmp_path):
    target = tmp_path / "out.txt"
    target.write_text("hello")
    assert target.read_text() == "hello"

def test_uses_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "test-key")
    assert get_api_key() == "test-key"
```

## Xulosa

Fixture'lar `pytest`ning asosiy imkoniyatlaridan biridir. Ular qayta foydalanishni osonlashtiradi, tayyorlash mantig'ini test mantig'idan ajratadi va `yield` namunasi yordamida tashqi resurslarni xavfsiz boshqarishga yordam beradi.
