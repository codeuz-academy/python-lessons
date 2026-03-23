---
title: Qidirish (Searching)
description: Ketma-ket qidirish (Linear search), Ikkilamchi qidirish (Binary search) va boshqa qidirish algoritmlari
order: 3
permalink: /uz/algorithms/searching/
---

Qidirish (Searching) deganda berilgan ma'lumotlar to'plami (dataset) ichidan maqsadli elementni (target) aniqlash tushuniladi.

## Ketma-ket qidirish (Linear Search)

Har qanday (tartiblangan yoki tartiblanmagan) massiv ustida ishlayveradi.

```python
def linear_search(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1

nums = [4, 1, 7, 9]
print(linear_search(nums, 7))  # 2
print(linear_search(nums, 5))  # -1
```

- Vaqt murakkabligi: `O(n)`
- Xotira murakkabligi: `O(1)`

## Ikkilamchi qidirish (Binary Search)

Faqat oldindan tartiblangan (sorted) ma'lumotlar ustida ishlaydi.

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1

sorted_nums = [1, 3, 5, 7, 9]
print(binary_search(sorted_nums, 7))  # 3
print(binary_search(sorted_nums, 4))  # -1
```

- Vaqt murakkabligi: `O(log n)`
- Xotira murakkabligi: `O(1)`

## Ikkilamchi qidirish variantlari

- Quyi chegara (Lower bound): Qiymati `>= target` bo'lgan birinchi indeksni topish.
- Yuqori chegara (Upper bound): Qiymati `> target` bo'lgan birinchi indeksni topish.
- Javoblar maydonini qidirish (Search answer space, masalan, minimal mos mumkin bo'lgan javobni topish).
