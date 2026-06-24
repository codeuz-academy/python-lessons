---
layout: tutorial.njk
lang: uz
title: Python o'zgaruvchilar
description: "Python o'zgaruvchilari obyektlarga bog'langan nomlar sifatida qanday ishlaydi, nomlash qoidalari va qisqartmalar bilan."
order: 7
permalink: /uz/tutorial/python-variables/
---

<img src="/img/tutorial/7-python-variables.webp" alt="Python o'zgaruvchilari" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

O'zgaruvchilar (variables) - qiymatlarni saqlash uchun ajratilgan xotira manzillari. Ya'ni o'zgaruvchi yaratganingizda, xotirada ma'lum joy band qilinadi. O'zgaruvchilar dastur bajarilishi davomida ishlatiladigan ma'lumotlarni saqlaydi va keyinchalik ularning qiymati o'zgartirilishi mumkin.

O'zgaruvchilar turli ma'lumot turlarini saqlashi mumkin. Python'da o'zgaruvchilar dinamik: oldindan ma'lum bir tur bilan e'lon qilish shart emas, va dastur ishlayotganda tur/qiymat o'zgarishi mumkin.

Python o'zgaruvchilarini nomlash bo'yicha asosiy qoidalar:

1. Birinchi belgi harf yoki pastki chiziq `_` bo'lishi kerak.
2. Keyingi belgilar harf, pastki chiziq `_` yoki raqam bo'lishi mumkin.
3. O'zgaruvchi nomlari case-sensitive (katta-kichik harf farqlanadi). Masalan, `firstName` va `firstname` - turli o'zgaruvchilar.

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

### Bir nechta o'zgaruvchiga qiymat berish

Python bitta qatorda bir nechta o'zgaruvchiga qiymat berishi mumkin — bu unpack qilish va almashtirish uchun qulay:

```python
# Har bir o'zgaruvchiga o'z qiymati
x, y, z = 1, 2, 3
print(x, y, z)        # 1 2 3

# Bir nechta o'zgaruvchiga bir xil qiymat
a = b = c = 0
print(a, b, c)        # 0 0 0

# Vaqtinchalik o'zgaruvchisiz ikkita o'zgaruvchini almashtirish
x, y = y, x
print(x, y)           # 2 1
```

### Nomlash konvensiyalari

Yuqoridagi qoidalar nima *ruxsat etilganini* aytadi; konvensiyalar esa nima *o'qilishi qulay* ekanini aytadi. Python kodi quyidagi keng tarqalgan uslublarga amal qiladi:

- O'zgaruvchilar va funksiyalar uchun `snake_case` ishlating: `user_name`, `total_price`.
- O'zgarmaydigan qiymatlar uchun `UPPER_CASE` ishlating: `PI = 3.14159`.
- Nomni harf bilan boshlang va `x` yoki `tmp` o'rniga ma'noli so'z tanlang.
- Python kalit so'zlarini (`if`, `for`, `class`, `True`, …) nom sifatida ishlata olmaysiz.

```python
PI = 3.14159          # konvensiya bo'yicha konstanta
radius = 4
print(PI * radius ** 2)
```

> <i class="fa-solid fa-circle-info" aria-hidden="true"></i> **Eslatma:** Python'da haqiqiy konstantalar yo'q. `UPPER_CASE` faqat boshqa dasturchilarga bu qiymat o'zgartirilmasligi kerakligini bildiruvchi signal.

### O'zgaruvchini o'chirish

O'zgaruvchi nomini o'chirish uchun `del` ishlating. Undan keyin unga murojaat qilish `NameError` keltirib chiqaradi.

```python
score = 100
print(score)   # 100
del score
# print(score)  # NameError: name 'score' is not defined
```

