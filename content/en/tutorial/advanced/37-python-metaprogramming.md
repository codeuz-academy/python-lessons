---
layout: tutorial.njk
lang: en
title: Python Metaprogramming
description: "Learn Python Metaprogramming in Python with practical examples and clear explanations."
order: 37
permalink: /en/tutorial/python-metaprogramming/
---

<img src="/img/tutorial/37-python-metaprogramming.webp" alt="Python Metaprogramming" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Metaprogramming is a concept where computer programs have the ability to treat programs as their data. It means that a program can be designed to read, generate, analyze or transform other programs, and even modify itself while running. In short: **code that writes code**.

In Python, this is a very deep and complex topic, but extremely *powerful* if used wisely. One of the main features of metaprogramming in Python is **Metaclasses**.

### 1. What is a Class?
Before understanding metaclasses, remember that in Python, **a Class is also an Object**. When you define a `class`, Python executes it and creates a class object in memory.

```python
class ObjectCreator:
    pass

my_obj = ObjectCreator()
print(my_obj) # Instance of ObjectCreator

print(ObjectCreator) # ObjectCreator itself is an object!
```

Since Class is an object, then:
- You can store it in a variable.
- Pass it as an argument.
- Add attributes to it dynamically.

### 2. The Magical `type()` Function

Usually we use `type()` to check data types.
```python
print(type(1)) # <class 'int'>
```

But, `type()` can also be used to **create classes dynamically**.

Syntax: `type(name, bases, attrs)`
*   `name`: Class name (string).
*   `bases`: Tuple of parent classes (for inheritance).
*   `attrs`: Dictionary of class attributes and methods.

```python
# Regular way
class Monkey:
    def eat(self):
        print("Eating banana")

# Metaprogramming way (exactly same!)
def eat_function(self):
    print("Eating banana")

DynamicMonkey = type('DynamicMonkey', (), {'eat': eat_function})

m = DynamicMonkey()
m.eat() # Output: Eating banana
```

### 3. Metaclass

A Metaclass is the "factory" that creates Classes.
- **Object** is an instance of **Class**.
- **Class** is an instance of **Metaclass**.

By default, the metaclass for all classes in Python is `type`.

```python
class MyClass:
    pass

print(type(MyClass)) # <class 'type'>
```

#### Creating Custom Metaclass
You can create your own metaclass to control how a class is created. This is often used to validate class attributes or create strict APIs (like in Django Models).

To create a metaclass, inherit from `type`. We use the `metaclass=` argument in class definition.

**Example: Forcing all class attribute names to be Uppercase**

```python
class UpperAttrMeta(type):
    # __new__ is called before __init__
    def __new__(upperattr_metaclass, future_class_name, 
                future_class_parents, future_class_attr):
        
        # Create new attribute dictionary with uppercase keys
        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'): # Don't change magic methods
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        
        # Call type.__new__ to create class
        return type(future_class_name, future_class_parents, uppercase_attr)

# Using metaclass
class Foo(metaclass=UpperAttrMeta):
    bar = 'bip'

print(hasattr(Foo, 'bar')) # False (because changed to BAR)
print(hasattr(Foo, 'BAR')) # True
print(Foo.BAR) # 'bip'
```

### 4. When to Use Metaclass?
The answer: **Almost never**, unless you are building a framework.

> "Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't." - Tim Peters (Python Guru)

However, understanding it gives deep insights into how Python works behind the scenes.

### Conclusion
- **type()** can create classes dynamically.
- **Metaclass** is the class of a Class.
- Used to modify Class creation automatically.
