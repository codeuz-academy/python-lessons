---
layout: tutorial.njk
lang: uz
title: Python decorator'lar va closure'lar
description: "Decorator va closure'lar bilan funksiyalarni asl kodiga tegmasdan o'rang va kengaytiring."
order: 34
permalink: /uz/tutorial/python-decorators/
---

<img src="/img/tutorial/34-python-decorators-closures.webp" alt="Python decorators va closures" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Decorator va Closure — Python'dagi ikki advanced tushuncha bo'lib, juda *kuchli*. Dastlab qo'rqinchli tuyulishi mumkin, lekin Django, Flask, FastAPI kabi mashhur freymvorklarda ko'p "magic" (ichki mexanizm) aynan shu asosga qurilgan.

Tasavvur qiling: sizda sovg'a (funksiya) bor. Siz uni chiroyli qog'ozga o'rab berasiz (decorator). Sovg'aning ichidagini o'zgartirmaysiz, lekin tashqaridan unga qo'shimcha xususiyat qo'shasiz. Decorator mohiyati ham shu: funksiya kodini o'zgartirmasdan, uning xatti-harakatini o'zgartirish.

Decorator'ga o'tishdan oldin, avval **Closure** tushunchasini tushunib olaylik.

### 1. Closures

Closure - bu o'zi yaratilgan qamrovdagi (scope) o'zgaruvchilarni "eslab qoladigan" funksiya. Ya'ni tashqi qamrov (scope) ishlashni tugatgan bo'lsa ham, closure o'sha qiymatlarni saqlab qoladi.

#### Nested function tushunchasi
Python'da funksiyalar ichida funksiya yaratish mumkin:

```python
def outer(x):
    def inner(y):
        return x + y
    return inner
```

#### Closure yaratish
Quyidagi misolga qarang:

```python
def multiplier_maker(n):
    def multiplier(x):
        return x * n
    return multiplier

# Closure yaratish
times_three = multiplier_maker(3)
times_five = multiplier_maker(5)

print(times_three(10))  # Natija: 30
print(times_five(10))  # Natija: 50
```

Bu yerda `multiplier_maker` ishlashni tugatgan bo'lsa ham, `times_three` funksiya `n = 3` qiymatini "eslab" qoladi. Bu - Closure.

### 2. Decorators

Decorator aslida funksiya qabul qilib, uning o'rniga boshqa funksiya — o'rovchi (wrapper) qaytaradigan Closure.

#### Oddiy decorator
```python
def my_decorator(func):
    def wrapper():
        print("Before function is called")
        func()
        print("After function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello World!")

say_hello()
```

#### Natija:
```
Before function is called
Hello World!
After function is called
```

### 3. Argumentli decorator (`*args`, `**kwargs`)

Decorator har qanday parametrli funksiya bilan ishlashi uchun `*args` va `**kwargs` ishlating.

```python
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Function call: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function
def add(a, b):
    return a + b

print(add(3, 5)) 
# Natija:
# Function call: add
# 8
```

### 4. Real dunyo misollari

#### Timer decorator (bajarilish vaqtini o'lchash)
Unumdorlikni (performance) optimallashtirish uchun foydali.

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)  # Eng yaxshi amaliyot: asl funksiyaning meta-ma'lumotlarini (metadata) saqlash
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} {end - start:.4f} soniyada bajarildi")
        return result
    return wrapper

@timer
def heavy_process():
    time.sleep(1)
    return "Done"

heavy_process()
```

#### Authentication decorator (Flask misoli)
Muayyan sahifalarga kirishdan oldin foydalanuvchi login bo'lganini tekshiradi.

```python
# non-runnable: requires external environment/setup
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper

@app.route('/dashboard')
@login_required
def dashboard():
    return "Dashboard Page"
```

### Xulosa
- **Closure**: tashqi qamrov (scope) holatini eslab qoladigan funksiya.
- **Decorator**: closure yordamida funksiyaga tashqaridan xatti-harakat qo'shishning chiroyli usuli.
