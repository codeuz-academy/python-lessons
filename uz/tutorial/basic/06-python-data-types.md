---
layout: tutorial.njk
lang: uz
title: Python ma'lumot turlari
order: 6
permalink: /uz/tutorial/python-data-types/
---

<img src="/img/tutorial/6-tipe-data-pada-python.webp" alt="Python ma'lumot turlari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Ma'lumot turi (data type) - kompyuter xotirasida axborotni saqlash uchun ishlatiladigan tur.

Pythonning ma'lumot turlari boshqa dasturlash tillari bilan solishtirganda o'ziga xos.

Quyida Python dasturlash tilidagi asosiy ma'lumot turlari keltirilgan:

| Ma'lumot turi | Misol | Izoh |
| ----------- | ------------------------ | ------------------------------------------------------------------------------------ |
| Boolean | `True` or `False` | Rost `True` (qiymati `1`) yoki yolg'on `False` (qiymati `0`) |
| String | `"Let's learn Python"` | Belgilar/matnlar ketma-ketligi ( `"` yoki `'` bilan o'raladi) |
| Integer | `25` or `1209` | Butun sonlar |
| Float | `3.14` or `0.99` | O'nlik kasr sonlar |
| Hexadecimal | `0x9a` or `0x1d3` | Hex formatdagi sonlar (16-lik sanoq tizimi) |
| Complex | `1 + 5j ` | Haqiqiy va mavhum qismlardan iborat kompleks sonlar |
| List | `['xyz', 786, 2.23]` | Turli turlarni saqlaydigan ketma-ketlik va uning ichidagi qiymatlar o'zgarishi mumkin |
| Tuple | `('xyz', 768, 2.23)` | Turli turlarni saqlaydigan ketma-ketlik, lekin ichidagi qiymatlar o'zgarmaydi |
| Set | `{'apple', 'orange'}` | Tartibsiz (unordered) va takrorlanmaydigan (unique) elementlar to'plami |
| Dictionary | `{'name': 'adi','id':2}` | Key-value juftliklari ko'rinishidagi ma'lumotlar |

Turli ma'lumot turlarini sinab ko'rish uchun quyidagi Python skriptini ishga tushiring.

```python
#Boolean data type
print(True)

#String data type
print("Let's learn Python")
print('Learning Python is Very Easy')

#Integer data type
print(20)

#Float data type
print(3.14)

#Hexadecimal data type
print(0x9a)

#Complex data type
print(5j)

#List data type
print([1,2,3,4,5])
print(["one", "two", "three"])

#Tuple data type
print((1,2,3,4,5))
print(("one", "two", "three"))

#Set data type
print({1,2,3,4,5})
print({"apple", "orange", "mango"})

#Dictionary data type
print({"name":"Bob", 'age':20})
#Dictionary data type checked into profile variable
profile = {"name":"Alice", 'age':21} #process initialization of profile variable
print(profile) #process printing profile variable containing Dictionary data type
print(type(profile)) #function to check data type kind. will appear <class 'dict'> which means dict is dictionary data type
```

