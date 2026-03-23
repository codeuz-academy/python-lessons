---
layout: tutorial.njk
lang: uz
title: Python shart operatorlari
description: "Python'da Python shart operatorlari mavzusini amaliy misollar va tushunarli izohlar bilan o'rganing."
order: 9
permalink: /uz/tutorial/python-conditions/
---

<img src="/img/tutorial/9-python-if-else-conditions.webp" alt="Python if else shartlari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

### If sharti

Shartlar (`if` condition) dastur bajarilishi davomida yuzaga keladigan holatlarni tekshirish va shu holatga qarab qanday amal bajarilishini tanlash uchun ishlatiladi.

Python'da bir nechta shart operatorlari bor: `if`, `else` va `elif`. `if` sharti shart `True` bo'lsa kodni bajaradi.

Agar shart `False` bo'lsa, `if` bloki bajarilmaydi.

Quyida Python'da `if` shartidan foydalanish misoli:

```python
# If sharti - shart rost bo'lsa kod bajariladi

ball = 9

# Shart rost bo'lsa, quyidagi buyruq bajariladi
if(ball > 7):
    print("To'qqiz yettidan katta")  # Rost shart, bajariladi

# Shart yolg'on bo'lsa, quyidagi buyruq bajarilmaydi
if(ball > 10):
    print("To'qqiz o'ndan katta")  # Yolg'on shart, bajarilmaydi
```

Yuqoridagi misolda dastur ishga tushirilsa, birinchi `if` `True` bo'lgani uchun `"To'qqiz yettidan katta"` matni bir marta chiqariladi. Ikkinchi `if` esa `False`, shuning uchun u yerdagi `print(...)` bajarilmaydi.

### `if` `else` sharti

`if` `else` sharti nafaqat shartga mos bo'lsa nima bajarilishini, balki shartga mos bo'lmasa qaysi kod bajarilishini ham belgilaydi.

`if` `else` shartida: shart `True` bo'lsa `if` ichidagi kod ishlaydi, aks holda (`False`) `else` ichidagi kod ishlaydi.

Quyida Python'da `if` `else` shartidan foydalanish misoli:

```python
# Shart rost bo'lsa if bloki, yolg'on bo'lsa else bloki bajariladi

ball = 3

if(ball > 7):
    print("Tabriklaymiz, siz o'tdingiz")
else:
    print("Kechirasiz, siz o'tmadingiz")
```

Yuqoridagi misolda `if` sharti `False` bo'lgani uchun dastur `"Kechirasiz, siz o'tmadingiz"` matnini chiqaradi.

### Elif sharti

`elif` - bu `if` shartining davomidir. `elif` orqali bir nechta ehtimoliy holatlardan birini tanlaydigan kod yozish mumkin. `else` bilan o'xshash, farqi shundaki, `elif` bir nechta bo'lishi mumkin.

Quyida Python'da `elif` shartidan foydalanish misoli:

```python
# Elif shartidan foydalanish misoli

bugun = "Yakshanba"

if(bugun == "Dushanba"):
    print("Men darsga boraman")
elif(bugun == "Seshanba"):
    print("Men darsga boraman")
elif(bugun == "Chorshanba"):
    print("Men darsga boraman")
elif(bugun == "Payshanba"):
    print("Men darsga boraman")
elif(bugun == "Juma"):
    print("Men darsga boraman")
elif(bugun == "Shanba"):
    print("Men darsga boraman")
elif(bugun == "Yakshanba"):
    print("Men dam olaman")
```

Yuqoridagi misolda dastur `"Men dam olaman"` matnini chiqaradi.

### `match case` (Python 3.10+)

Python 3.10 dan boshlab `match-case` orqali **Structural Pattern Matching** mavjud. Bu boshqa tillardagi `switch-case` ga o'xshaydi va uzun `elif` zanjirlarini almashtirish uchun qulay.

```python
# Match-case misoli (Python 3.10+)

bugun = "Yakshanba"

match bugun:
    case "Dushanba" | "Seshanba" | "Chorshanba" | "Payshanba" | "Juma":
        print("Men darsga boraman")
    case "Shanba":
        print("Men uy vazifasini qilaman")
    case "Yakshanba":
        print("Men dam olaman")
    case _:
        print("Noto'g'ri kun")
```

Pattern matching yanada murakkab ma'lumot tuzilmalarini ham moslashtirish (match) uchun ishlatilishi mumkin:

```python
# Ma'lumot tuzilmasini moslashtirish
def buyruq_bajar(buyruq):
    match buyruq.split():
        case ["chiqish"]:
            print("Dasturdan chiqish")
        case ["salom", ism]:
            print(f"Salom, {ism}!")
        case ["qoshish", x, y]:
            print(f"Natija: {int(x) + int(y)}")
        case _:
            print("Noma'lum buyruq")

buyruq_bajar("salom Ali")       # Natija: Salom, Ali!
buyruq_bajar("qoshish 5 3")     # Natija: Natija: 8
```

### Ternary operator (bir qatorli shart)

Python shartni bir qatorga yozish (conditional expression, ternary operator) ni ham qo'llab-quvvatlaydi:

```python
# Ternary operator
yosh = 20
holat = "Katta" if yosh >= 18 else "Bola"
print(holat)  # Natija: Katta

# Yana bir misol
ball = 85
natija = "O'tdi" if ball >= 60 else "Yiqildi"
print(natija)  # Natija: O'tdi
```

