---
layout: tutorial.njk
lang: uz
title: Python izohlar
description: "Kod ishlashiga ta'sir qilmasdan uni tushuntirish uchun bir va ko'p qatorli izohlardan foydalaning."
order: 5
permalink: /uz/tutorial/python-comments/
---

<img src="/img/tutorial/5-python-comments.webp" alt="Python izohlari (comments)" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

Izohlar (comments) — bu dastur kodi ichidagi qaydlar bo'lib, Python ularni bajarish vaqtida e'tiborga olmaydi.

Izohlar orqali niyatni (intent), farazlarni (assumptions) va muhim detallarni tushuntiring.

### Bir qatorli izohlar

`#` dan foydalaning:

```python
# Bu izoh
print("Salom Dunyo")  # Qatordagi izoh
```

### Ko'p qatorli tushuntirishlar

Python'da alohida "multi-line comment" sintaksisi yo'q. Keng tarqalgan uslub - bir nechta `#` qatorlardan foydalanish:

```python
# Bu blok nima uchun biror narsa qilishimizni tushuntiradi,
# faqat kod nima qilishini emas.
# Izohlarni qisqa va foydali qiling.
```

Uch tirnoqli matnlar (`""" ... """`) - bu string, haqiqiy comment emas. Odatda docstring uchun ishlatiladi.

### Docstring namunasi

```python
def greet(name):
    """Return greeting text for a name."""
    return f"Hello, {name}"
```

### To'liq misol

Quyidagi skript comment'lar real kod bilan qanday ishlashini ko'rsatadi. Faqat `print()` chaqiruvlari natija beradi:

```python
# Salomlashish
print("Salom Dunyo")

# Quyidagi qator izohga olingan, shuning uchun ishlamaydi
# print("Bu chop etilmaydi")

print("Bob")    # ismni chop etadi
print(123)      # raqamni chop etadi
```

Natija:

```text
Salom Dunyo
Bob
123
```

