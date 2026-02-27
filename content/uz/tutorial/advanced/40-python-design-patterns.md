---
layout: tutorial.njk
lang: uz
title: Python design pattern'lar
order: 40
permalink: /uz/tutorial/python-design-patterns/
---

<img src="/img/tutorial/35-belajar-design-patterns-python.webp" alt="Python design patterns" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Design pattern'lar - dastur dizaynida tez-tez uchraydigan muammolar uchun qayta ishlatiladigan (reusable) yechimlar. Bu tayyor kod emas, balki muammoni qanday yechish bo'yicha *shablon* yoki yo'riqnoma.

Python'da design pattern'larni ko'pincha Java yoki C++ kabi tillarga nisbatan osonroq implement qilish mumkin (ba'zilari hatto built-in sifatida mavjud).

### 1. Singleton pattern

Maqsad: class faqat bitta instance'ga ega bo'lishini kafolatlash.
Misol: database connection, application configuration.

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance...")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2) # True
```

Pythonic alternativ (decorator bilan):

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    pass
```

### 2. Factory pattern

Maqsad: yaratiladigan obyektning aniq class'ini oldindan ko'rsatmasdan obyekt yaratish.
Misol: plugin tizimi, turli formatlarda serializatsiya (JSON, XML).

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    """The Factory Method"""
    pets = dict(dog=Dog(), cat=Cat())
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
```

### 3. Observer pattern (Pub-Sub)

Maqsad: one-to-many bog'liqlikni belgilash: bitta obyekt o'zgarsa, unga bog'liq obyektlar xabardor qilinadi.
Misol: event handling, notification tizimi.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        raise NotImplementedError

class EmailNotifier(Observer):
    def update(self, message):
        print(f"Sending Email: {message}")

class SMSNotifier(Observer):
    def update(self, message):
        print(f"Sending SMS: {message}")

# Foydalanish
subject = Subject()
subject.attach(EmailNotifier())
subject.attach(SMSNotifier())

subject.notify("Server Down!")
# Natija:
# Sending Email: Server Down!
# Sending SMS: Server Down!
```

### 4. Strategy pattern

Maqsad: algoritmlar oilasini aniqlash, har birini alohida kapsulalash va ularni o'zaro almashtiriladigan qilish.
Misol: sortlash strategiyasi, shopping discount, payment gateway.

```python
from typing import Callable

class PaymentProcessor:
    def __init__(self, strategy: Callable[[int], None]):
        self.strategy = strategy
    
    def pay(self, amount):
        self.strategy(amount)

# Strategiyalar
def pay_by_cc(amount):
    print(f"Paying {amount} with Credit Card")

def pay_by_paypal(amount):
    print(f"Paying {amount} with PayPal")

# Runtime'da tanlash
cart = PaymentProcessor(pay_by_cc)
cart.pay(100)

cart = PaymentProcessor(pay_by_paypal)
cart.pay(100)
```

Python'da funksiyalar first-class object bo'lgani uchun, ko'pincha yuqoridagi kabi *funksiya uzatish* Strategy pattern uchun yetarli bo'ladi va murakkab interface class'lar shart emas.

### 5. Decorator pattern

Oldingi darslarda ko'rganimizdek, bu pattern obyektga dinamik ravishda behavior qo'shishga yordam beradi. Python'da `@` sintaksisi bilan bu pattern o'rnatilgan darajada qo'llab-quvvatlanadi.

### Xulosa

- **Singleton**: bitta instance.
- **Factory**: obyektni dinamik yaratish.
- **Observer**: event haqida bir nechta subscriber'ni xabardor qilish.
- **Strategy**: runtime'da algoritmni almashtirish.
- Pattern'larni o'rganing, kod modul'li va maintainable bo'ladi, lekin over-engineering qilmang.
