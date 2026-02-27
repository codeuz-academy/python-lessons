---
layout: tutorial.njk
lang: uz
title: Python o'zgaruvchilari
order: 7
permalink: /uz/tutorial/python-variables/
---

<img src="/img/tutorial/7-variabel-pada-python.webp" alt="Python o'zgaruvchilari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

O'zgaruvchilar (variables) - qiymatlarni saqlash uchun ajratilgan xotira manzillari. Ya'ni o'zgaruvchi yaratganingizda, xotirada ma'lum joy band qilinadi. O'zgaruvchilar dastur bajarilishi davomida ishlatiladigan ma'lumotlarni saqlaydi va keyinchalik ularning qiymati o'zgartirilishi mumkin.

O'zgaruvchilar turli ma'lumot turlarini saqlashi mumkin. Python'da o'zgaruvchilar dinamik: oldindan ma'lum bir tur bilan e'lon qilish shart emas, va dastur ishlayotganda tur/qiymat o'zgarishi mumkin.

Python o'zgaruvchilarini nomlash bo'yicha asosiy qoidalar:

1. Birinchi belgi harf yoki pastki chiziq `_` bo'lishi kerak.
2. Keyingi belgilar harf, pastki chiziq `_` yoki raqam bo'lishi mumkin.
3. O'zgaruvchi nomlari case-sensitive. Masalan, `firstName` va `firstname` - turli o'zgaruvchilar.

Python'da o'zgaruvchi yaratish juda oson: o'zgaruvchi nomini yozing, so'ng `=` belgisi va qiymatni bering.

**O'zgaruvchi yaratish va chiqarish**

```python
name = "John Doe"
print(name)
```

**Qiymat va tur o'zgartirish**

O'zgaruvchining qiymati va hatto turi dastur ishlayotganda o'zgarishi mumkin:

```python
age = 20
print(age)
print(type(age))

age = "yigirma bir"
print(age)
print(type(age))
```

**O'zgaruvchilarni birlashtirish**

```python
first_name = "Bob"
last_name = "Smith"
full_name = first_name + " " + last_name

age = 22
hobby = "Suzish"

print("Ism:", full_name)
print("Yosh:", age)
print("Hobbi:", hobby)
```

**To'g'ri o'zgaruvchi nomlari**

```python
my_variable = "Salom"
_private = "Hi"
count2 = 100
print(my_variable, _private, count2)
```

**O'zgaruvchilar bilan hisoblash**

```python
length = 10
width = 5
area = length * width
print("Yuza:", area)
```

