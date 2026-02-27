---
layout: tutorial.njk
lang: uz
title: Python o'zgaruvchilari
order: 7
permalink: /tutorial/uz/python-variables/
---

<img src="/img/tutorial/7-variabel-pada-python.webp" alt="Python o'zgaruvchilari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

O'zgaruvchilar (variables) - qiymatlarni saqlash uchun ajratilgan xotira manzillari. Ya'ni o'zgaruvchi yaratganingizda, xotirada ma'lum joy band qilinadi. O'zgaruvchilar dastur bajarilishi davomida ishlatiladigan ma'lumotlarni saqlaydi va keyinchalik ularning qiymati o'zgartirilishi mumkin.

O'zgaruvchilar turli ma'lumot turlarini saqlashi mumkin. Python'da o'zgaruvchilar dinamik: oldindan ma'lum bir tur bilan e'lon qilish shart emas, va dastur ishlayotganda tur/qiymat o'zgarishi mumkin.

Python o'zgaruvchilarini nomlash bo'yicha asosiy qoidalar:

1. Birinchi belgi harf yoki pastki chiziq `_` bo'lishi kerak.
2. Keyingi belgilar harf, pastki chiziq `_` yoki raqam bo'lishi mumkin.
3. O'zgaruvchi nomlari case-sensitive. Masalan, `firstName` va `firstname` - turli o'zgaruvchilar.

Python'da o'zgaruvchi yaratish juda oson: o'zgaruvchi nomini yozing, so'ng `=` belgisi va qiymatni bering.

Quyida Python'da o'zgaruvchilardan foydalanish misoli:

```python
#process of entering data into variable
name = "John Doe"
#process of printing variable
print(name)

#value and data type in variable can be changed
age = 20 #initial value
print(age) #print age value
type(age) #check age data type
age = "twenty one" #value after changed
print(age) #print age value
type(age) #check age data type

firstName = "Bob"
lastName = "Smith"
name = firstName + " " + lastName
age = 22
hobby = "Swimming"
print("Profile\n", name, "\n", age, "\n", hobby)

#other variable examples
thisisvariable = "Hello"
this_is_also_variable = "Hi"
_thisisvariablealso = "Hi"
thisisvariable222 = "Bye"

length = 10
width = 5
area = length * width
print(area)
```

