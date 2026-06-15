---
layout: tutorial.njk
lang: uz
title: Python'da veb dasturlash
description: "Python'da veb-ilovalar qurish haqida umumiy ko'rinish va Flask, Django hamda FastAPI qanday farqlanishi."
order: 28
permalink: /uz/tutorial/python-web-development/
---

<img src="/img/tutorial/28-python-web-development.webp" alt="Python'da veb dasturlash" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Veb dasturlash (web development) — veb-ilovalar va veb uchun API'larni o'ylab topish, yaratish, joylashtirish (deploy) va ishlatishni o'z ichiga oladigan keng tushuncha.

### Veb dasturlashda Python

Python asosan server tomonda (server-side) veb-ilovalarni qurish uchun ishlatiladi. Oddiy veb-ilova yaratishda freymvork shart bo'lmasligi mumkin, lekin amaliyotda ko'pchilik tayyor ochiq kodli (open-source) kutubxonalar va freymvorklar orqali ishni tezlashtiradi.

An'anaviy ravishda Python brauzerda emas, server tomonda ishlaydi. Brauzerlar natively bajaradigan til — JavaScript, shuning uchun ko'p Python veb-ilovalar ikkalasini birga ishlatadi: Python server tomonda, JavaScript esa mijoz tomonga (client) yuklanib brauzerda bajariladi. (Pyodide kabi vositalar endi WebAssembly orqali Python'ni brauzerda ham ishlatishi mumkin, lekin bu hali istisno hisoblanadi.)

Python bilan veb-sayt yaratish oson, lekin avval HTML, CSS va JavaScript asoslarini bilib olgan bo'lishingiz kerak.

### Python veb freymvorklari

Python'da veb dasturlash uchun eng ommabop va o'rganishga qulay freymvorklar: Django, Flask va FastAPI.

#### Flask

Flask — o'rganish oson, o'rnatish oson va sodda mikrofreymvork (microframework).

Afzalliklari:

- ishlatish oson
- o'rnatilgan development server va xatolarni topish vositasi (debugger)
- unit test'larni qo'llab-quvvatlaydi
- RESTful so'rovlarni yo'naltirish (request dispatching)
- Jinja2 shablonlari (templating) bilan ishlaydi
- xavfsiz cookie'lar va mijoz tomoni sessiyalari (client-side sessions) ni qo'llab-quvvatlaydi
- WSGI 1.0 standarti bilan 100% mos (compliant)
- Unicode asosida
- hujjatlari keng (documented)

Flask o'rnatish:
`pip install Flask`

Flask bilan Hello World veb-ilovasi:

```python
# non-runnable: requires external environment/setup
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()
```

Server'ni ishga tushirish:
`python hello.py`

Brauzerda [http://localhost:5000/](http://localhost:5000/) ni oching, `Hello World!` ko'rinadi.

#### Django

Django — tezkor ishlab chiqish (development) va toza, amaliy dizaynni targ'ib qiladigan yuqori darajali (high-level) Python veb freymvorki. U veb dasturlashdagi ko'p "bezovtalik"larni o'zi hal qiladi, siz esa g'ildirakni qayta ixtiro qilmasdan ilovangizni yozishga e'tibor qaratasiz.

Django'ning boshqa freymvorklarga nisbatan kuchli jihatlaridan biri — masshtablilik (scalability). Bu freymvork katta ilovalar uchun mos.

Django o'rnatish:
`pip install Django`

O'rnatilgandan so'ng, yangi Django loyiha yarating:

```bash
django-admin startproject myproject
cd myproject
python manage.py runserver
```

Brauzerda [http://127.0.0.1:8000/](http://127.0.0.1:8000/) ni ochsangiz Django welcome sahifasini ko'rasiz.

#### FastAPI

FastAPI — Python 3.8+ uchun API yaratishga mo'ljallangan zamonaviy, yuqori unumdor (high-performance) Python veb freymvorki. U standart Python type hint'lariga tayanadi. Tezligi va qulayligi sabab eng ko'p ishlatiladigan Python veb freymvorklaridan biriga aylangan.

FastAPI afzalliklari:

- Yuqori unumdorlik: ASGI standarti, Starlette va Uvicorn ustiga qurilgan
- Tez yoziladi: type hint'lar ortiqcha kodni kamaytiradi va muharrirda avtomatik to'ldirishni beradi
- Kamroq xato (bug): so'rovlarni avtomatik tekshirish noto'g'ri ma'lumotni erta ushlaydi
- Avtomatik hujjatlashtirish: Swagger UI va ReDoc kodingizdan generatsiya qilinadi
- Standartga mos: OpenAPI va JSON Schema ustiga qurilgan

FastAPI o'rnatish:
`pip install fastapi uvicorn`

FastAPI bilan Hello World:

```python
# non-runnable: requires fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

Server'ni ishga tushirish:
`uvicorn main:app --reload`

Natijani ko'rish uchun [http://127.0.0.1:8000/](http://127.0.0.1:8000/) ni oching, interaktiv API dokumentatsiya uchun esa [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) ni ko'ring.
