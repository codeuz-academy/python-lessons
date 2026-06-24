---
title: Big-O va tahlil
description: O'sish tezligi tahlili, baholash qoidalari va keng tarqalgan murakkablik shablonlari
order: 1
permalink: /uz/algorithms/big-o/
---

Big-O kirish hajmi `n` ortib borgan sayin o'sish tezligini (growth rate) tasvirlaydi.

## Nima uchun muhim

- Yechimlarni qurilmadan (hardware) qat'i nazar solishtirishga yordam beradi.
- Katta kirishlarda dasturning xatti-harakatini oldindan aytib beradi.
- Ma'lumotlar tuzilmasini (data structure) tanlashda yo'l ko'rsatadi.

## Murakkablikni tez baholash qoidalari

1. Faqat eng kuchli hadni qoldiring (`n^2 + n -> n^2`).
2. O'zgarmaslarni (constant) tashlab yuboring (`5n -> n`).
3. Ketma-ket bloklar qo'shiladi (`O(a + b)`).
4. Ichma-ich takrorlash (`loop`)'lar ko'paytiriladi (`O(a * b)`).

## Misollar

```python
def sum_all(nums):
    total = 0
    for x in nums:
        total += x
    return total
```

Vaqt: `O(n)`
Xotira: `O(1)`

```python
def all_pairs(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            result.append((nums[i], nums[j]))
    return result
```

Vaqt: `O(n^2)`
Xotira: chiqish hajmi tufayli `O(n^2)`.

## Amortizatsiyalangan tahlil (Amortized Analysis)

Ba'zi amallar goho qimmatga tushadi, lekin o'rtacha hisobda arzon bo'ladi.

- Dinamik massivga element qo'shish (append): goho qayta o'lcham olish `O(n)`, o'rtacha esa `O(1)` (amortizatsiyalangan).

## Shablonlar xaritasi

| Shablon                                | Odatdagi murakkablik |
| -------------------------------------- | -------------------- |
| Bitta takrorlash (`loop`)              | `O(n)`               |
| Bir xil kirish ustida ichma-ich `loop` | `O(n^2)`             |
| Har qadamda 2 ga bo'lish               | `O(log n)`           |
| `loop` + ikkilik amal                  | `O(n log n)`         |

## Mashqlar

1. Ro'yxat ichidan eng katta qiymatni topish murakkabligini tahlil qiling.
2. Ichki takrorlash faqat `k` marta ishlaydigan ichma-ich `loop`'lar murakkabligini tahlil qiling.
3. Ketma-ket qidirish (linear search) va ikkilamchi qidirish (binary search) murakkabligini solishtiring.
