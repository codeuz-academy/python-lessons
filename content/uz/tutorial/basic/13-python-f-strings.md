---
layout: tutorial.njk
lang: uz
title: Python f-string'lar
order: 13
permalink: /uz/tutorial/python-f-strings/
---

F-string'lar (formatted string literals) - Python'da string formatlashning zamonaviy va eng samarali usuli. Python 3.6 da kiritilgan f-string'lar toza sintaksis va yaxshi unumdorlik sababli string formatlash uchun de-fakto standartga aylandi.

### F-string asosiy sintaksisi

F-string'lar qo'shtirnoqdan oldin `f` yoki `F` harfi bilan boshlanadi, Python ifodalari esa jingalak qavslar `{}` ichida yoziladi:

```python
ism = "Ali"
yosh = 25

# F-string ishlatish
print(f"Salom, mening ismim {ism} va yoshim {yosh}")
# Natija: Salom, mening ismim Ali va yoshim 25

# Katta F harfi bilan ham ishlaydi
print(F"Xush kelibsiz, {ism}!")
```

### Eski usullar bilan solishtirish

F-string'lar paydo bo'lishidan oldin string formatlashning bir nechta yo'li bor edi:

```python
ism = "Vali"
ball = 95.5

# Eski usul 1: Birlashtirish (+)
print("Ism: " + ism + ", Ball: " + str(ball))

# Eski usul 2: % formatlash
print("Ism: %s, Ball: %.1f" % (ism, ball))

# Eski usul 3: .format()
print("Ism: {}, Ball: {}".format(ism, ball))

# Zamonaviy usul: f-string (tavsiya etiladi)
print(f"Ism: {ism}, Ball: {ball}")
```

F-string'lar o'qilishi oson va bajarilishi tezroq!

### F-string ichida ifodalar

F-string jingalak qavslar ichida istalgan Python ifodasini hisoblay oladi:

```python
# Matematik amallar
a = 10
b = 5
print(f"Qo'shish: {a + b}")        # Natija: Qo'shish: 15
print(f"Ko'paytirish: {a * b}")     # Natija: Ko'paytirish: 50
print(f"Bo'lish: {a / b:.2f}")      # Natija: Bo'lish: 2.00

# Metodlarni chaqirish
ism = "python"
print(f"Katta harf: {ism.upper()}")       # Natija: Katta harf: PYTHON
print(f"Bosh harf: {ism.capitalize()}")   # Natija: Bosh harf: Python

# Funksiyalarni chaqirish
import math
print(f"Ildiz 16: {math.sqrt(16)}")   # Natija: Ildiz 16: 4.0

# Ro'yxat va indekslash
mevalar = ["olma", "apelsin", "mango"]
print(f"Birinchi meva: {mevalar[0]}")  # Natija: Birinchi meva: olma
```

### Sonlarni formatlash

F-string format specifier'lar yordamida sonlarni ko'rsatishni boshqaradi:

```python
# O'nlik format
pi = 3.14159265359
print(f"Pi: {pi:.2f}")           # Natija: Pi: 3.14
print(f"Pi: {pi:.4f}")           # Natija: Pi: 3.1416

# Minglik ajratgich formati
aholi = 1500000
print(f"Aholi: {aholi:,}")       # Natija: Aholi: 1,500,000
print(f"Aholi: {aholi:_}")       # Natija: Aholi: 1_500_000

# Foiz formati
nisbat = 0.756
print(f"Foiz: {nisbat:.1%}")     # Natija: Foiz: 75.6%

# Minimal kenglik formati
son = 42
print(f"Son: {son:5}")           # Natija: Son:    42 (kenglik 5)
print(f"Son: {son:05}")          # Natija: Son: 00042 (nol bilan to'ldirish)

# Ikkilik, sakkizlik, o'n oltilik format
num = 255
print(f"Ikkilik: {num:b}")             # Natija: Ikkilik: 11111111
print(f"Sakkizlik: {num:o}")           # Natija: Sakkizlik: 377
print(f"O'n oltilik: {num:x}")         # Natija: O'n oltilik: ff
print(f"O'n oltilik (katta): {num:X}") # Natija: O'n oltilik (katta): FF
```

### Tekislash (alignment)

```python
text = "Python"

# Chapga tekislash (standart)
print(f"{text:<15}")     # Natija: "Python         "

# O'ngga tekislash
print(f"{text:>15}")     # Natija: "         Python"

# Markazga tekislash
print(f"{text:^15}")     # Natija: "    Python     "

# To'ldiruvchi belgilar bilan
print(f"{text:*^15}")    # Natija: "****Python*****"
print(f"{text:-<15}")    # Natija: "Python---------"
```

### Dictionary bilan f-string

```python
student = {
    "name": "Sara",
    "id": "12345",
    "gpa": 3.85
}

print(f"Ism: {student['name']}, GPA: {student['gpa']}")
# Natija: Ism: Sara, GPA: 3.85
```

### F-string bilan debugging (Python 3.8+)

`=` specifier debugging uchun juda qulay:

```python
x = 10
y = 20

# Eski usul
print(f"x = {x}, y = {y}")

# Yangi usul = bilan (Python 3.8+)
print(f"{x=}, {y=}")              # Natija: x=10, y=20
print(f"{x + y=}")                # Natija: x + y=30
print(f"{x * 2=}")                # Natija: x * 2=20
```

### Multiline f-string

```python
name = "Alice"
job = "Developer"
city = "New York"

# Uch tirnoq bilan
bio = f"""
User Profile
===============
Name      : {name}
Job       : {job}
City      : {city}
"""

print(bio)
```

### Jingalak qavslarni escape qilish

Agar literal `{` va `}` ni chiqarish kerak bo'lsa, ikki marta yozing:

{% raw %}
```python
print(f"This is curly braces: {{}}")    # Natija: This is curly braces: {}
print(f"Python Set: {{{1, 2, 3}}}")   # Natija: Python Set: {1, 2, 3}
```
{% endraw %}

### Amaliy misol

```python
# Oddiy jadval yaratish
mahsulotlar = [
    ("Noutbuk", 15000000),
    ("Sichqoncha", 250000),
    ("Klaviatura", 750000),
]

print(f"{'Mahsulot':<15}{'Narx':>15}")
print("-" * 30)
for nomi, narx in mahsulotlar:
    print(f"{nomi:<15}{narx:>15,}")

# Natija:
# Mahsulot              Narx
# ------------------------------
# Noutbuk          15,000,000
# Sichqoncha          250,000
# Klaviatura          750,000
```

