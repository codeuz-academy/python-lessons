---
title: Abstrakt ma'lumot turlari (ADTs)
description: Necaise kitobining 1-bobidan ilhomlangan kontraktlar, invariantlar va bir nechta amalga oshirish usullari
order: 1
permalink: /uz/data-structures/abstract-data-types/
---

Ushbu bob Necaise kitobidagi **1-bob (Abstract Data Types)** ning asosiy g'oyalariga amal qiladi: avval xatti-harakatni belgilab oling, keyin uni amalga oshiring.

![ADT kontrakt diagrammasi]({{ '/img/data-structures/adt-contract.svg' | url }})

## ADT sizga nima beradi

ADT bu bir **kontrakt** (contract):

- U *qanday amallar mavjudligini* va *ular nima qilishini* belgilaydi.
- U *ma'lumotlar ichki tarzda qanday saqlanishini* yashiradi.
- U mijoz kodini o'zgartirmasdan amalga oshirish usullarini almashtirishga imkon beradi.

Aynan shu ajratish tufayli ADT'lar yirik loyihalarda yaxshi masshtablanadi.

## Kontraktning asosiy qismlari

Har bir amal quyidagilar bilan belgilanishi kerak:

- **Old shartlar (Preconditions)**: amal chaqirilishidan oldin nima rost bo'lishi kerak.
- **Keyingi shartlar (Postconditions)**: amal chaqirilgandan keyin nima rost bo'lishi kerak.
- **Tasvirlash invariantlari (Representation invariants)**: ichki holat uchun har doim rost bo'ladigan xususiyatlar.

`stack` ustidagi `pop()` amali uchun misol:

- Old shart: `stack` bo'sh emas.
- Keyingi shart: yuqori element olib tashlanadi va qaytariladi.
- Invariant hamon saqlanadi: `stack` tartibi LIFO bo'lib qoladi.

## Old shartlar va assertion'lar

Ma'lumotlar tuzilmalarini o'rganayotganda `assert`'lar kontraktlarni aniq qilib ko'rsatish uchun foydali.

```python
class Stack:
    def __init__(self):
        self._items = []

    def pop(self):
        assert len(self._items) > 0, "precondition failed: stack must be non-empty"
        return self._items.pop()
```

Amaliy tizimlarda noto'g'ri amallar uchun odatda aniq `exception'lar` ko'tariladi.

## Bir nechta amalga oshirish, bitta ADT

`queue` ADT'sini turli yo'llar bilan amalga oshirish mumkin:

- `list` asosida
- `deque` asosida
- bog'langan ro'yxat (linked-list) asosida

Har bir amalga oshirish navbat semantikasini (FIFO) saqlab tursa, foydalanuvchiga ko'rinadigan kod o'zgarishsiz qoladi.

```python
def process_jobs(queue):
    while not queue.is_empty():
        job = queue.dequeue()
        handle(job)
```

`process_jobs` ichki saqlash tartibi haqida qayg'urmasligi kerak.

## Nega bu tuzilmalarni kodlashdan oldin muhim

Agar siz avval ADT kontraktini belgilab olsangiz, keyingi boblardagi amalga oshirish ishlari osonlashadi:

- Massivlar/vektorlar amalga oshirishning bir variantiga aylanadi.
- Bog'langan tuzilmalar boshqa bir variant bo'ladi.
- Unumdorlikni sozlash `API`'ni qaytadan yozishga majbur qilmaydi.

Bu ma'lumotlar tuzilmalari bo'limining qolgan qismi uchun poydevor hisoblanadi.
