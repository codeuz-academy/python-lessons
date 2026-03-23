---
layout: tutorial.njk
lang: uz
title: "Loyiha: FastAPI yordamida Backend"
description: "Python'da Loyiha: FastAPI yordamida Backend mavzusini amaliy misollar va tushunarli izohlar bilan o'rganing."
order: 44
permalink: /uz/tutorial/project-fastapi/
---

<img src="/img/tutorial/python-fastapi.webp" alt="FastAPI Backend Development" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Siz Python tilining asosiy qismlarini, ma'lumotlar tuzilmalarini, algoritmlarni va testlashni o'rgandingiz. Endi olingan bilimlarni haqiqiy loyihada - haqiqiy API yaratishda ishlatish vaqti keldi! Ushbu loyihada biz **FastAPI** yordamida kuchli va tez ishlash xususiyatlariga ega REST API yaratishni ko'ramiz.

## Nimaga FastAPI?

FastAPI Python 3.8 va undan yuqori versiyalar uchun zamonaviy va tez ishlaydigan web-frameworkdir. U standart Python Type Hintlariga asoslangan bo'lib:
- **Tez**: Tezlik jihatdan Node.js va Goga yetib oldi.
- **Oson**: Backend uchun oson hujjatlash vositalari.
- **Tekshirish**: Type Hintlar orqali ma'lumotlarni Pydantic yordamida to'g'ri tekshirish imkoni.

## 1. O'rnatish

```bash
python -m pip install fastapi uvicorn
```

`main.py` faylini yarating:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Serverni ishga tushiring:
```bash
uvicorn main:app --reload
```

## 2. API uchun ma'lumotlar sxemasi

Pydanticni qo'llab, oddiy foydalanuvchi ma'lumotlarini qabul qiladigan va tekshiradigan API yozib ko'ramiz.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
db = []

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
```

Pydantic noto'g'ri qiymat kelsa avtomatik 422 Unprocessable Entity xatosini ko'rsatadi.

## Xulosa

FastAPI Python imkoniyatlarini yanada osonlashtiradi, loyihani shu yerdan MySQL / PostgreSQL ma'lumotlar bazalariga `SQLAlchemy` yoki boshqa ORM asboblari yordamida kengaytirishga ishonishingiz mumkin.
