---
layout: tutorial.njk
lang: uz
title: Python funksiyalar
description: "Funksiyalarni aniqlang, argument bering, qiymat qaytaring hamda default, *args, **kwargs, scope, rekursiya va docstring'lardan foydalaning."
order: 20
permalink: /uz/tutorial/python-functions/
---

<img src="/img/tutorial/20-python-functions.webp" alt="Python funksiyalari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Funksiya - ma'lum bir vazifani bajarish uchun qayta ishlatiladigan (reusable) kod bloki. Funksiyalar katta dasturni kichikroq, nomlangan bo'laklarga ajratishga, takrorlanishdan qochishga hamda kodni o'qish, test qilish va saqlashni osonlashtirishga yordam beradi.

Python'da funksiyalarning ikki turi mavjud:

- **Built-in funksiyalar** — allaqachon mavjud, masalan `print()`, `len()`, `sum()` va `range()`.
- **Foydalanuvchi aniqlagan funksiyalar** — siz `def` bilan o'zingiz yaratadigan funksiyalar.

### Python funksiyalarini aniqlash

`def` kalit so'zi, so'ng funksiya nomi va parametrlar yoziladi:

```python
def print_message(text):
    """Print a message to the console."""
    print(text)
```

Muhim qoidalar:

- Funksiya bloklari `def` bilan boshlanadi.
- Parametrlar `()` ichida yoziladi.
- Funksiya tanasi indentatsiya bilan ajratiladi.
- `return` qiymatni chaqiruvchiga qaytaradi.
- Agar `return` bo'lmasa, funksiya `None` qaytaradi.

### Funksiyani chaqirish

Funksiyani aniqlash uni ishga tushirmaydi. Uni **chaqirish** kerak — buning uchun funksiya nomidan keyin qavslar yoziladi:

```python
def greet():
    print("Hello, Python!")

greet()   # Hello, Python!
greet()   # Hello, Python!
```

Ichidagi kod faqat funksiya chaqirilganda ishlaydi va uni kerak bo'lganicha ko'p marta chaqirishingiz mumkin.

### Parametrlar va argumentlar

**Parametr** - bu aniqlashda qavslar ichida yoziladigan o'zgaruvchi. **Argument** - bu funksiyani chaqirganda yuboriladigan haqiqiy qiymat.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))
print(greet("Bob", greeting="Hi"))
```

Odatda funksiya to'g'ri sondagi argumentlar bilan chaqirilishi shart:

```python
def add(a, b):
    return a + b

print(add(3, 4))   # 7
```

`add(3)` yoki `add(3, 4, 5)` deb chaqirish `TypeError` xatosini keltirib chiqaradi.

### `return` operatori

`return` funksiyani tugatadi va qiymatni chaqiruvchiga qaytaradi. `return`'siz (yoki bo'sh `return` bilan) funksiya `None` qaytaradi.

```python
def square(n):
    return n * n

result = square(5)
print(result)   # 25


def no_return():
    pass

print(no_return())   # None
```

#### Bir nechta qiymat qaytarish

Funksiya bir vaqtning o'zida bir nechta qiymatni tuple sifatida qaytarishi mumkin, uni esa unpack qilib olish mumkin:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9, 2])
print(low, high)   # 1 9
```

### Keyword argumentlar

Argumentlarni nom bo'yicha berishingiz mumkin. U holda tartib muhim emas:

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(name="Milo", animal="cat")
```

### Default argument qiymatlari

Parametrga default qiymat bering, shunda chaqiruvchi uni tashlab ketishi mumkin:

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25  (exponent default 2 bo'ladi)
print(power(5, 3))   # 125
```

> <i class="fa-solid fa-circle-info" aria-hidden="true"></i> **Eslatma:** Default qiymat sifatida mutable obyektdan (list yoki dict kabi) foydalanmang. Default bir marta yaratiladi va barcha chaqiruvlar o'rtasida ulashiladi. Buning o'rniga `None` ishlating va obyektni funksiya ichida yarating.

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))   # [1]
print(add_item(2))   # [2]
```

### Maxsus parametr turlari (Python 3)

Python positional-only va keyword-only parametrlarni qo'llab-quvvatlaydi:

```python
def combine(a, b, /, sep="-", *, upper=False):
    text = f"{a}{sep}{b}"
    return text.upper() if upper else text

print(combine("py", "thon"))
print(combine("py", "thon", sep="_", upper=True))
```

- `/` dan oldingi parametrlar positional-only.
- `*` dan keyingi parametrlar keyword-only.

### O'zgaruvchan uzunlikdagi argumentlar

Istalgan sondagi positional argumentlarni qabul qilish uchun `*args`, istalgan sondagi keyword argumentlar uchun `**kwargs` ishlating:

```python
def total(*numbers):
    return sum(numbers)


def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

print(total(1, 2, 3, 4))
show_info(name="Alice", age=22)
```

Funksiya ichida `args` - tuple, `kwargs` esa dictionary bo'ladi.

### Docstring'lar

Docstring - funksiyaning birinchi qatoriga joylashtirilgan string literal. U funksiya nima qilishini hujjatlashtiradi va `help()` yoki `__doc__` atributi orqali ish vaqtida mavjud bo'ladi.

```python
def area(width, height):
    """Return the area of a rectangle."""
    return width * height

print(area.__doc__)   # Return the area of a rectangle.
```

### `pass` operatori

Funksiya tanasi bo'sh bo'lishi mumkin emas. Kodni keyinroq yozmoqchi bo'lsangiz, joy egallovchi sifatida `pass` ishlating:

```python
def todo_later():
    pass
```

### O'zgaruvchi ko'rinish doirasi (scope)

O'zgaruvchi qayerda yaratilgani uning qayerda ishlatilishi mumkinligini belgilaydi. Python nomlarni **LEGB** qoidasi bo'yicha qidiradi: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

Funksiya ichida yaratilgan o'zgaruvchi **local** bo'ladi — u faqat funksiya ishlaganda mavjud bo'ladi:

```python
def show():
    message = "inside"   # local o'zgaruvchi
    print(message)

show()
# print(message)  # NameError: message bu yerda aniqlanmagan
```

#### `global` kalit so'zi

Funksiya ichidan modul darajasidagi o'zgaruvchiga qiymat berish uchun uni `global` deb e'lon qiling:

```python
count = 0

def increment():
    global count
    count += 1

increment()
increment()
print(count)   # 2
```

#### `nonlocal` kalit so'zi

`nonlocal` ichki funksiyaga tashqi (enclosing) funksiyadagi o'zgaruvchini o'zgartirishga imkon beradi:

```python
def outer():
    value = "start"

    def inner():
        nonlocal value
        value = "changed"

    inner()
    return value

print(outer())   # changed
```

### Ichma-ich funksiyalar

Funksiyani boshqa funksiya ichida aniqlashingiz mumkin. Ichki funksiya tashqi funksiyaning o'zgaruvchilarini o'qiy oladi:

```python
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

say_hi = make_greeter("Hi")
print(say_hi("Sam"))   # Hi, Sam!
```

### Rekursiya

Rekursiv funksiya o'zini o'zi chaqiradi. Har bir rekursiyada uni to'xtatadigan **bazaviy holat** (base case) bo'lishi shart, aks holda u cheksiz ishlaydi:

```python
def factorial(n):
    if n <= 1:          # bazaviy holat
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
```

### Funksiyalarda type hint'lar

Parametrlar va qaytariladigan qiymatni annotatsiya qilishingiz mumkin. Hint'lar o'quvchilar va vositalar uchun hujjat bo'lib xizmat qiladi; Python ularni ish vaqtida majburlamaydi.

```python
def greet(name: str, times: int = 1) -> str:
    return f"Hello {name}! " * times

print(greet("Ada", 2))
```

Batafsil [Type Hints](/uz/tutorial/python-type-hints/) darsida bering.

### `lambda` (anonim funksiya)

Qisqa, bir qatordan iborat funksiyalar uchun:

```python
square = lambda x: x * x
print(square(5))
```

Murakkab logika uchun kod o'qilishini saqlab qolish maqsadida `def` ishlating. Batafsil [Lambda](/uz/tutorial/python-lambda/) darsiga qarang.
