---
layout: tutorial.njk
lang: uz
title: "Loyiha: FastAPI yordamida backend"
description: "Kichik FastAPI backend'ini boshidan oxirigacha quring: route va modellardan serverni ishga tushirishgacha."
order: 44
permalink: /uz/tutorial/project-fastapi/
---

<img src="/img/tutorial/python-fastapi.webp" alt="FastAPI Backend Development" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Siz endi Python tilining asoslarini, ma'lumotlar tuzilmalarini, algoritmlarni va testlashni o'rganib oldingiz. Endi haqiqiy loyiha qurish vaqti keldi. Ushbu amaliy darsda biz **FastAPI** yordamida yuqori unumdorlikka ega REST API backend'ini quramiz.

## Nimaga FastAPI?

FastAPI — bu standart Python `type hint`'lariga asoslangan, Python 3.8+ uchun API'lar qurishga mo'ljallangan zamonaviy, tez (yuqori unumdorlikka ega) veb freymvork.

- **Tez**: Unumdorlik jihatidan Node.js va Go bilan raqobatlasha oladi.
- **Oson**: Avtomatik interaktiv API hujjatlari.
- **Tekshirish**: Pydantic yordamida so'rov tanasini avtomatik o'qish va tekshirish.

## 1. O'rnatish

Avval FastAPI va `uvicorn` nomli ASGI serverini o'rnating.

```bash
python -m pip install fastapi uvicorn
```

`main.py` nomli yangi fayl yarating.

<div class="warning">Ushbu kodni ishga tushirish uchun avval Python paket menejeri yordamida bog'liqliklarni o'rnatishingiz kerak.</div>

```python
# non-runnable: requires fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Serverni quyidagicha ishga tushiring:

```bash
uvicorn main:app --reload
```

## 2. Pydantic bilan ma'lumotlarni tekshirish

FastAPI ma'lumotlarni avtomatik tekshirish uchun kursda avval ko'rib chiqqan `type hint`'lardan `Pydantic` kutubxonasi bilan birgalikda foydalanadi. Keling, yangi foydalanuvchi ma'lumotlarini qabul qiladigan endpoint yarataylik.

<div class="warning">Quyidagi tekshirish kodini ishga tushirish uchun <code>pydantic</code> ham o'rnatilganligiga ishonch hosil qiling.</div>

```python
# non-runnable: requires fastapi
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Ma'lumotlar bazasi o'rnidagi oddiy ro'yxat
db = []

# Pydantic yordamida ma'lumot sxemasini aniqlash
class User(BaseModel):
    id: int
    name: str
    age: int
    email: Optional[str] = None

@app.post("/users/")
def create_user(user: User):
    for u in db:
        if u.id == user.id:
            raise HTTPException(status_code=400, detail="User already exists")
    db.append(user)
    return {"status": "success", "user": user}

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
```

Agar kimdir maydonlari to'ldirilmagan POST so'rovini yuborsa yoki `age` qiymatini `20` o'rniga `"twenty"` deb belgilasa, FastAPI darhol avtomatik 422 Unprocessable Entity xatosini qaytaradi. Tekshirish kodini qo'lda yozishingiz shart emas.

## 3. Avtomatik hujjatlash kuchi

Aniq `type hint`'lar tufayli FastAPI OpenAPI spetsifikatsiyasi asosida ikkita interaktiv hujjat interfeysini avtomatik yaratadi:

- **Swagger UI**: `http://127.0.0.1:8000/docs` manzilida joylashgan.
- **ReDoc**: `http://127.0.0.1:8000/redoc` manzilida joylashgan.

Endpoint'larni Postman yoki `curl`'dan foydalanmasdan darhol sinab ko'rish uchun brauzeringizda Swagger UI'ni oching.

## 4. Async endpoint'lar va query parametrlar

FastAPI ASGI asosida qurilgan, shuning uchun path funksiyasini `async def` deb e'lon qilish mumkin. Handler I/O (ma'lumotlar bazasi yoki tashqi API) kutadigan holatlarda undan foydalaning — server kutish davomida boshqa so'rovlarni qayta ishlay oladi. Asosiy tushunchalar uchun [Async / Await](/uz/tutorial/python-async-await/) darsiga qarang.

Path'ning bir qismi **bo'lmagan** funksiya argumentlari avtomatik ravishda **query parametr** bo'ladi. Standart qiymatli parametr ixtiyoriy; standart qiymatsiz parametr esa majburiy.

```python
# non-runnable: requires fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/search/")
async def search(q: str, limit: int = 10):
    # GET /search/?q=python&limit=5
    return {"query": q, "limit": limit}
```

Bu yerda `q` majburiy, `limit` esa standart `10`. FastAPI turlarni ham tekshiradi: `limit=abc` berilsa, 422 xato qaytaradi.

## 5. API'ni test qilish

FastAPI `TestClient` (httpx asosida) taqdim etadi, shuning uchun endpoint'larni `pytest` bilan serverni alohida ishga tushirmasdan test qilishingiz mumkin. Bu test darslaridagi bilimlarni birlashtiradi.

```python
# non-runnable: requires fastapi
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

## Xulosa

FastAPI Python'ning `type annotation`'lari va asinxron imkoniyatlarini amaliy loyihalarga tayyor freymvorkda birlashtiradi. Shu yerdan boshlab FastAPI backend'ingizni `SQLAlchemy` kabi ORM yordamida haqiqiy ma'lumotlar bazasiga ulashingiz va route'larni OAuth2 kabi standart xavfsizlik protokollari bilan himoyalashingiz mumkin.
