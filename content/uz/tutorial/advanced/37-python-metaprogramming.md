---
layout: tutorial.njk
lang: uz
title: Python metadasturlash (metaprogramming)
description: "Metaclass, __new__ va atribut hook'lari bilan class'larni ish vaqtida tekshiring va shakllantiring."
order: 37
permalink: /uz/tutorial/python-metaprogramming/
---

<img src="/img/tutorial/37-python-metaprogramming.webp" alt="Python metaprogramming" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

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
# Oddiy usul
class Monkey:
    def eat(self):
        print("Eating banana")

# Metaprogramming usuli (aynan bir xil!)
def eat_function(self):
    print("Eating banana")

DynamicMonkey = type('DynamicMonkey', (), {'eat': eat_function})

m = DynamicMonkey()
m.eat() # Natija: Eating banana
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
    # __new__ __init__ dan oldin chaqiriladi
    def __new__(upperattr_metaclass, future_class_name, 
                future_class_parents, future_class_attr):
        
        # Katta harfli kalitlar bilan yangi atribut lug'ati yaratish
        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'): # Magic metodlarni o'zgartirmaymiz
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        
        # Class yaratish uchun type.__new__ ni chaqirish
        return type(future_class_name, future_class_parents, uppercase_attr)

# Metaclass ishlatish
class Foo(metaclass=UpperAttrMeta):
    bar = 'bip'

print(hasattr(Foo, 'bar')) # False (chunki BAR ga o'zgardi)
print(hasattr(Foo, 'BAR')) # True
print(Foo.BAR) # 'bip'
```

### 4. Dinamik atributga murojaat

Metaprogramming faqat klasslar haqida emas — atributlarni ish vaqtida *nom* bo'yicha o'qish va o'rnatish ham mumkin, buning uchun built-in `getattr()`, `setattr()` va `hasattr()` ishlatiladi:

```python
class Config:
    pass

cfg = Config()
setattr(cfg, "debug", True)        # string nomdan atribut o'rnatish

print(getattr(cfg, "debug"))       # True
print(getattr(cfg, "verbose", False))  # False  (bo'lmaganda default)
print(hasattr(cfg, "debug"))       # True
```

`__getattr__` hook'i atribut odatiy yo'l bilan **topilmaganda** chaqiriladi, bu klassga istalgan nomga dinamik javob berish imkonini beradi:

```python
class Echo:
    def __getattr__(self, name):
        return f"You asked for '{name}'"

e = Echo()
print(e.anything)   # You asked for 'anything'
print(e.foo)        # You asked for 'foo'
```

### 5. Yengilroq muqobil: `__init_subclass__`

To'liq metaclass'lar kamdan-kam kerak bo'ladi. Faqat klass **subclass qilinganda** reaksiya bildirmoqchi bo'lsangiz, `__init_subclass__` ancha soddaroq:

```python
class Plugin:
    registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registry.append(cls.__name__)

class Audio(Plugin):
    pass

class Video(Plugin):
    pass

print(Plugin.registry)   # ['Audio', 'Video']
```

### 6. Metaclass qachon kerak?

Javob: **deyarli hech qachon**, agar freymvork (framework) qurmayotgan bo'lsangiz.

> "Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't." - Tim Peters (Python Guru)

Lekin mavzuni tushunish Python qanday ishlashini chuqurroq anglashga yordam beradi.

### Xulosa
- **type()** class'larni dinamik yaratishi mumkin.
- **Metaclass** - class'ning class'i.
- Metaclass class yaratish jarayonini avtomatik o'zgartirish uchun ishlatiladi.
