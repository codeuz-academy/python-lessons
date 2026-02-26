---
layout: tutorial.njk
lang: uz
title: Python metaprogramming
order: 37
permalink: /uz/tutorial/python-metaprogramming/
---

<img src="/img/tutorial/32-metaprogramming.webp" alt="Python metaprogramming" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Metaprogramming - bu dastur boshqa dasturlarni data sifatida ko'ra oladigan tushuncha. Ya'ni dastur boshqa kodni o'qishi, generatsiya qilishi, tahlil qilishi, o'zgartirishi, hatto ish paytida o'zini ham modifikatsiya qilishi mumkin. Qisqacha: **kod yozadigan kod**.

Python'da bu juda chuqur va murakkab mavzu, lekin to'g'ri ishlatilsa juda *kuchli*. Python metaprogramming'ining asosiy elementlaridan biri - **metaclass**.

### 1. Class nima?

Metaclass'ni tushunishdan oldin eslab qoling: Python'da **class ham object**. Siz `class` yozganingizda, Python uni bajaradi va xotirada class object yaratadi.

```python
class ObjectCreator:
    pass

my_obj = ObjectCreator()
print(my_obj) # Instance of ObjectCreator

print(ObjectCreator) # ObjectCreator itself is an object!
```

Class object bo'lgani uchun:
- Uni o'zgaruvchiga saqlashingiz mumkin.
- Argument sifatida uzatishingiz mumkin.
- Dynamic ravishda atribut qo'shishingiz mumkin.

### 2. "Sehrli" `type()` funksiyasi

Odatda `type()`ni data turini ko'rish uchun ishlatamiz:
```python
print(type(1)) # <class 'int'>
```

Lekin `type()` yordamida **class'larni dinamik yaratish** ham mumkin.

Sintaksis: `type(name, bases, attrs)`
*   `name`: class nomi (string).
*   `bases`: parent class'lar tuple'i (inheritance uchun).
*   `attrs`: class atribut va metodlari dictionary'si.

```python
# Regular Way
class Monkey:
    def eat(self):
        print("Eating banana")

# Metaprogramming Way(Exactly same!)
def eat_function(self):
    print("Eating banana")

DynamicMonkey = type('DynamicMonkey', (), {'eat': eat_function})

m = DynamicMonkey()
m.eat() # Output: Eating banana
```

### 3. Metaclass

Metaclass - class'larni yaratadigan "factory".
- **Object** - **Class** ning instance'i.
- **Class** - **Metaclass** ning instance'i.

Python'da default metaclass - `type`.

```python
class MyClass:
    pass

print(type(MyClass)) # <class 'type'>
```

#### Custom metaclass yaratish

Class qanday yaratilishini nazorat qilish uchun o'zingiz metaclass yozishingiz mumkin. Bu ko'pincha class atributlarini validatsiya qilish yoki strict API yaratishda (masalan Django Models) ishlatiladi.

Metaclass yaratish uchun `type`dan meros oling. Class ta'rifida `metaclass=` argumentidan foydalanamiz.

**Misol: barcha atribut nomlarini Uppercase qilish**

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

# Using Metaclass
class Foo(metaclass=UpperAttrMeta):
    bar = 'bip'

print(hasattr(Foo, 'bar')) # False (because changed to BAR)
print(hasattr(Foo, 'BAR')) # True
print(Foo.BAR) # 'bip'
```

### 4. Metaclass qachon kerak?

Javob: **deyarli hech qachon**, agar framework qurmayotgan bo'lsangiz.

> "Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't." - Tim Peters (Python Guru)

Lekin mavzuni tushunish Python qanday ishlashini chuqurroq anglashga yordam beradi.

### Xulosa
- **type()** class'larni dinamik yaratishi mumkin.
- **Metaclass** - class'ning class'i.
- Metaclass class yaratish jarayonini avtomatik o'zgartirish uchun ishlatiladi.
