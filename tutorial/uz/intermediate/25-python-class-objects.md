---
layout: tutorial.njk
lang: uz
title: Python object va class
order: 25
permalink: /tutorial/uz/python-class-objects/
---

<img src="/img/tutorial/21-belajar-oop-object-class-python.webp" alt="Python OOP - object va class" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Class'lar data va behavior'ni bitta qayta ishlatiladigan tuzilma ichida modellashtirishga yordam beradi.

### OOP bo'yicha qisqa lug'at

| Atama | Ma'nosi |
| ---- | ------- |
| Class | Atribut va metodlarni aniqlaydigan shablon (blueprint) |
| Object / Instance | Class'dan yaratilgan aniq obyekt (instance) |
| Attribute | Obyekt yoki class'da saqlanadigan ma'lumot |
| Class attribute | Class'ning barcha instance'lari uchun umumiy o'zgaruvchi |
| Instance attribute | Har bir obyektga xos o'zgaruvchi (`self.x`) |
| Method | Class ichida aniqlangan funksiya |
| Instantiation | Class'dan obyekt yaratish jarayoni |
| Inheritance | Mavjud class'dan yangi class qurish |
| Encapsulation | Data va behavior'ni guruhlash; kirishni convention orqali boshqarish |
| Polymorphism | Bir xil interfeys, turli xatti-harakat |
| Operator overloading | `+`, `==`, `len()` kabi operatorlar uchun maxsus metodlar orqali behavior belgilash |

### Oddiy class va obyekt

```python
class Employee:
    company = "PythonCompany"  # class attribute

    def __init__(self, name, salary):
        self.name = name        # instance attribute
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
```

Obyekt yaratish:

```python
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.display()
emp2.display()
print(Employee.company)
```

### Instance attribute va class attribute farqi

- **Instance attribute** har bir obyektga tegishli (`self.name`).
- **Class attribute** esa barcha instance'lar uchun umumiy (`company`).

### Metod turlari

```python
class Example:
    total = 0

    def __init__(self, value):
        self.value = value
        Example.total += 1

    def instance_method(self):
        return self.value

    @classmethod
    def class_method(cls):
        return cls.total

    @staticmethod
    def static_method(a, b):
        return a + b
```

### Inheritance (meros olish)

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")


class Developer(Person):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def greet(self):
        print(f"Hello, I am {self.name} and I code in {self.language}")
```

### Encapsulation (convention)

Python qat'iy private atributlarni majburan tekshirmaydi, lekin odat (convention) ishlatiladi:

- `_name` -> ichki foydalanish (internal)
- `__name` -> name-mangled atribut

### Data saqlashga yo'naltirilgan class'lar uchun `@dataclass`

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
```

`@dataclass` asosan data saqlaydigan class'larda ortiqcha takroriy kodni kamaytiradi.

### Operator overloading

Maxsus (dunder) metodlar orqali operatorlar obyektlaringiz bilan qanday ishlashini belgilash mumkin:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
```

### To'liq ishlaydigan misol

```python
class Employee:
    emp_count = 0

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def total(cls):
        return cls.emp_count


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.display()
emp2.display()
print(f"Total employees: {Employee.total()}")
```
