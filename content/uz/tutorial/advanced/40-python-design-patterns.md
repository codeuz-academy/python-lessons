---
layout: tutorial.njk
lang: uz
title: Python design pattern'lar
description: "Python'da Python design pattern'lar mavzusini amaliy misollar va tushunarli izohlar bilan o'rganing."
order: 40
permalink: /uz/tutorial/python-design-patterns/
---

<img src="/img/tutorial/40-python-design-patterns.webp" alt="Python design patterns" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Design pattern'lar - dastur dizaynida tez-tez uchraydigan muammolar uchun qayta ishlatiladigan (reusable) yechimlar. Bu tayyor kod emas, balki muammoni qanday yechish bo'yicha *shablon* yoki yo'riqnoma.

Python'da design pattern'larni ko'pincha Java yoki C++ kabi tillarga nisbatan osonroq amalga oshirish mumkin (ba'zilari hatto o'rnatilgan (built-in) imkoniyat sifatida mavjud).

### 1. Singleton pattern

Maqsad: sinf (class) faqat bitta obyektga (instance) ega bo'lishini kafolatlash.
Misol: ma'lumotlar bazasi ulanishi (database connection), ilova sozlamalari (application configuration).

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

Pythoncha muqobil (decorator bilan):

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
Misol: plagin (plugin) tizimi, turli formatlarda serializatsiya (JSON, XML).

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
Misol: hodisalarni qayta ishlash (event handling), bildirishnoma tizimi.

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
Misol: sortlash strategiyasi, chegirma (discount), to'lov shlyuzi (payment gateway).

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

# Bajarilish vaqtida (runtime) tanlash
cart = PaymentProcessor(pay_by_cc)
cart.pay(100)

cart = PaymentProcessor(pay_by_paypal)
cart.pay(100)
```

Python'da funksiyalar birinchi darajali obyekt (first-class object) bo'lgani uchun, ko'pincha yuqoridagi kabi *funksiya uzatish* Strategy pattern uchun yetarli bo'ladi va murakkab interfeys sinflari (interface class'lar) shart emas.

### 5. Decorator pattern

Oldingi darslarda ko'rganimizdek, bu pattern obyektga dinamik ravishda xatti-harakat qo'shishga yordam beradi. Python'da `@` sintaksisi bilan bu pattern o'rnatilgan darajada qo'llab-quvvatlanadi.

### Xulosa

- **Singleton**: bitta instance.
- **Factory**: obyektni dinamik yaratish.
- **Observer**: hodisa (event) haqida bir nechta obunachini (subscriber) xabardor qilish.
- **Strategy**: bajarilish vaqtida (runtime) algoritmni almashtirish.
- Pattern'larni o'rganing, kod modul'li va qo'llab-quvvatlash oson bo'ladi, lekin ortiqcha murakkablashtirmang.
