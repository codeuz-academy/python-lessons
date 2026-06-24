---
layout: tutorial.njk
lang: en
title: Python Design Patterns
description: "Apply common design patterns in idiomatic Python, and recognize when they help or get in the way."
order: 40
permalink: /en/tutorial/python-design-patterns/
---

<img src="/img/tutorial/40-python-design-patterns.webp" alt="Python Design Patterns" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Design Patterns are common solutions that can be reused for problems that occur frequently in software design. It is not finished code, but rather a *template* or guide on how to solve a problem.

In Python, Design Patterns are often easier to implement (or even already built-in) compared to other languages like Java or C++.

### Categories of Design Patterns

The classic "Gang of Four" patterns are grouped into three families:

- **Creational** — how objects are created (Singleton, Factory, Builder).
- **Structural** — how objects are composed into larger structures (Decorator, Adapter, Facade).
- **Behavioral** — how objects communicate and share responsibility (Observer, Strategy, Iterator).

The patterns below are the ones you meet most often in real Python code.

### 1. Singleton Pattern

Goal: Ensure a class only has one instance.
Example usage: Database connection, application configuration.

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

Pythonic alternative using Decorator:

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

### 2. Factory Pattern

Goal: Create objects without specifying the exact logical class of the object that will be created.
Example usage: Plugin system, data serialization of various formats (JSON, XML).

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

### 3. Observer Pattern (Pub-Sub)

Goal: Define a one-to-many dependency, so that when one object changes, all its dependencies are notified.
Example usage: Event handling, notification system.

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

# Usage
subject = Subject()
subject.attach(EmailNotifier())
subject.attach(SMSNotifier())

subject.notify("Server Down!")
# Output:
# Sending Email: Server Down!
# Sending SMS: Server Down!
```

### 4. Strategy Pattern

Goal: Define a family of algorithms, encapsulate each one, and make them interchangeable.
Example usage: Sorting strategy, Shopping discount, Payment gateway.

```python
from typing import Callable

class PaymentProcessor:
    def __init__(self, strategy: Callable[[int], None]):
        self.strategy = strategy
    
    def pay(self, amount):
        self.strategy(amount)

# Strategies
def pay_by_cc(amount):
    print(f"Paying {amount} with Credit Card")

def pay_by_paypal(amount):
    print(f"Paying {amount} with PayPal")

# Runtime selection
cart = PaymentProcessor(pay_by_cc)
cart.pay(100)

cart = PaymentProcessor(pay_by_paypal)
cart.pay(100)
```

In Python, because functions are first-class objects, Strategy Pattern is often enough by *passing functions* like above, without needing to create complicated interface classes.

### 5. Decorator Pattern

This structural pattern allows adding behavior to an object dynamically by wrapping it. Python has *built-in* support for the function form with the `@` syntax (see the [Decorators](/en/tutorial/python-decorators/) tutorial), but the same idea applies to wrapping objects:

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

### Conclusion

- **Singleton**: Only one instance.
- **Factory**: Dynamic object creation.
- **Observer**: Event notification to multiple subscribers.
- **Strategy**: Swapping algorithms at runtime.
- Learn these patterns so your code is more modular and *maintainable*, but remember: don't over-engineer!
