---
layout: tutorial.njk
lang: en
title: Python Object & Class
description: "Learn Python Object & Class in Python with practical examples and clear explanations."
order: 25
permalink: /en/tutorial/python-class-objects/
---

<img src="/img/tutorial/25-python-oop-classes-objects.webp" alt="Python OOP - Object and Class" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Classes let you model data and behavior together in one reusable structure.

### OOP Quick Glossary

| Term | Meaning |
| ---- | ------- |
| Class | Blueprint that defines attributes and methods |
| Object / Instance | Concrete value created from a class |
| Attribute | Data stored on an object or class |
| Class attribute | Variable shared by all instances of a class |
| Instance attribute | Variable unique to each object (`self.x`) |
| Method | Function defined inside a class |
| Instantiation | Process of creating an object from a class |
| Inheritance | Building a new class from an existing class |
| Encapsulation | Grouping data and behavior; controlling access by convention |
| Polymorphism | Same interface, different behavior across classes |
| Operator overloading | Defining custom behavior for operators like `+`, `==`, `len()` via special methods |

### Basic Class and Object

```python
class Employee:
    company = "PythonCompany"  # class attribute

    def __init__(self, name, salary):
        self.name = name        # instance attribute
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
```

Create objects:

```python
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.display()
emp2.display()
print(Employee.company)
```

### Instance vs Class Attributes

- **Instance attributes** belong to each object (`self.name`).
- **Class attributes** are shared by all instances (`company`).

### Method Types

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

### Inheritance

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

### Encapsulation Convention

Python does not enforce strict private attributes, but conventions are used:

- `_name` -> internal use by convention
- `__name` -> name-mangled attribute

### `@dataclass` for Data-Focused Classes

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
```

`@dataclass` reduces boilerplate for classes that mostly store data.

### Operator Overloading

Special (dunder) methods let you define how operators work with your objects:

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

### Complete Runnable Example

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
