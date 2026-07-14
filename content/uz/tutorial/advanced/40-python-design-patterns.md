---
layout: tutorial.njk
lang: uz
title: Python design pattern'lar
description: "Keng tarqalgan design pattern'larni idiomatik Python'da qo'llang va ular qachon foyda, qachon xalaqit berishini ajrating."
order: 40
permalink: /uz/tutorial/python-design-patterns/
---

<img src="/img/tutorial/40-python-design-patterns.webp" alt="Python design patterns" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Design pattern'lar — dastur dizaynida tez-tez uchraydigan muammolar uchun qayta ishlatiladigan yechim andozalari. Bu tayyor kod emas, balki muammoni qanday yechish bo'yicha *shablon* yoki yo'riqnoma.

Python'da design pattern'larni ko'pincha Java yoki C++ kabi tillarga nisbatan osonroq amalga oshirish mumkin (ba'zilari hatto o'rnatilgan (built-in) imkoniyat sifatida mavjud).

### Design pattern'lar toifalari

Klassik "Gang of Four" pattern'lari uchta oilaga bo'linadi:

- **Creational** — obyektlar qanday yaratiladi (Singleton, Factory, Builder).
- **Structural** — obyektlar kattaroq tuzilmalarga qanday birlashtiriladi (Decorator, Adapter, Facade).
- **Behavioral** — obyektlar qanday aloqa qiladi va mas'uliyatni baham ko'radi (Observer, Strategy, Iterator).

Quyidagi pattern'lar haqiqiy Python kodida eng ko'p uchraydiganlaridir.

### 1. Singleton pattern

Maqsad: sinf (`class`) faqat bitta obyektga (`instance`) ega bo'lishini kafolatlash.
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

Maqsad: bir-ko'p (`one-to-many`) bog'liqlikni belgilash: bitta obyekt o'zgarsa, unga bog'liq obyektlar xabardor qilinadi.
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

Python'da funksiyalar birinchi darajali obyekt (`first-class object`) bo'lgani uchun, ko'pincha yuqoridagi kabi *funksiya uzatish* Strategy pattern uchun yetarli bo'ladi va murakkab interfeys sinflari shart emas.

### 5. Decorator pattern

Bu strukturaviy pattern obyektni o'rab olib, unga dinamik ravishda xatti-harakat qo'shishga imkon beradi. Python funksiya dekoratorlarini `@` sintaksisi bilan bevosita qo'llab-quvvatlaydi ([Dekoratorlar](/uz/tutorial/python-decorators/) darsiga qarang), lekin xuddi shu g'oya obyektlarni o'rashda ham qo'llaniladi:

```python
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

coffee = Coffee()
with_milk = MilkDecorator(coffee)

print(coffee.cost())     # 5
print(with_milk.cost())  # 7
```

### Xulosa

- **Singleton**: bitta instance.
- **Factory**: obyektni dinamik yaratish.
- **Observer**: hodisa (event) haqida bir nechta obunachini (subscriber) xabardor qilish.
- **Strategy**: bajarilish vaqtida (runtime) algoritmni almashtirish.
- Pattern'larni o'rganing: ular kodni modulli va qo'llab-quvvatlashga qulay qiladi, lekin ularni ortiqcha ishlatib kodni murakkablashtirmang.
