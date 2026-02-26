---
layout: tutorial.njk
lang: uz
title: Python'da veb dasturlash
order: 28
permalink: /uz/tutorial/python-web-development/
---

<img src="/img/tutorial/24-pengembangan-web-python.webp" alt="Python web development" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Veb dasturlash (web development) - veb-ilovalar va Web uchun API'larni o'ylab topish, yaratish, deploy qilish va ishlatishni (operatsiya) o'z ichiga oladigan keng tushuncha.

### Veb dasturlashda Python

Python server-side veb-ilovalarni qurish uchun ishlatiladi. Oddiy veb-ilova yaratishda framework shart bo'lmasligi mumkin, lekin amaliyotda deyarli hamma tayyor open-source kutubxonalar/frameworklar orqali ishni tezlashtiradi.

Python brauzerda ishlamaydi. Chrome, Firefox va Internet Explorer kabi brauzerlarda bajariladigan til - JavaScript. `pyjs` kabi loyihalar Python'dan JavaScript'ga compile qilishi mumkin. Lekin ko'p Python dasturchilari veb-ilovalarni Python + JavaScript kombinatsiyasida yozadi: Python server tomonda ishlaydi, JavaScript esa client'ga yuklanib brauzerda bajariladi.

Python bilan veb-sayt yaratish oson, lekin avval HTML, CSS va JavaScript asoslarini bilib olgan bo'lishingiz kerak.

### Python web frameworklari

Python'da veb dasturlash uchun eng ommabop va o'rganishga qulay frameworklar: Django, Flask va FastAPI.

#### Flask

Flask - o'rganish oson, o'rnatish oson va sodda (microframework) Python framework.

Afzalliklari:

- ishlatish oson
- built-in development server va debugger
- unit testing qo'llab-quvvatlashi
- RESTful request dispatching
- Jinja2 templating ishlatadi
- secure cookies (client side sessions) qo'llab-quvvatlaydi
- 100% WSGI 1.0 compliant
- Unicode asosida
- keng hujjatlashtirilgan (documented)

Flask o'rnatish:
`pip install Flask`

Flask bilan Hello World veb-ilova:

```python
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

Django - tezkor development va toza, amaliy dizaynni targ'ib qiladigan high-level Python web framework. U veb dasturlashdagi ko'p "bezovtalik"larni o'zi hal qiladi, siz esa g'ildirakni qayta ixtiro qilmasdan ilovangizni yozishga e'tibor qaratasiz.

Django'ning boshqa frameworklarga nisbatan kuchli jihatlaridan biri - scalability. Bu framework katta ilovalar uchun mos.

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

FastAPI - Python 3.7+ uchun API yaratishga mo'ljallangan zamonaviy, tez (high-performance) web framework. U standard Python type hints'ga tayanadi. FastAPI 2025 yilda yuqori tezlik va qulayligi sabab juda ommabop.

FastAPI afzalliklari:

- Juda tez: NodeJS va Go bilan bir darajadagi performance
- Tez yoziladi: development tezligini 2-3 barobar oshiradi
- Kamroq bug: inson xatolarini taxminan 40% ga kamaytiradi
- Avtomatik dokumentatsiya: Swagger UI va ReDoc avtomatik mavjud
- Standard'ga mos: OpenAPI va JSON Schema

FastAPI o'rnatish:
`pip install fastapi uvicorn`

FastAPI bilan Hello World:

```python
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
