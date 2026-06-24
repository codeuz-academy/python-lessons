---
title: Saralash (Sorting)
description: Merge sort va quick sort'ning amaliy ko'rinishlari hamda taqqoslash jadvali
order: 2
permalink: /uz/algorithms/sorting/
---

Saralash (Sorting) elementlarni o'sish yoki kamayish tartibida joylashtiradi.

## Keng tarqalgan saralash usullarini taqqoslash

| Algoritm    | O'rtacha     | Eng yomon    | Barqaror | Joyida ishlovchi |
| ----------- | ------------ | ------------ | -------- | ---------------- |
| Bubble Sort | `O(n^2)`     | `O(n^2)`     | Ha       | Ha               |
| Merge Sort  | `O(n log n)` | `O(n log n)` | Ha       | Yo'q             |
| Quick Sort  | `O(n log n)` | `O(n^2)`     | Yo'q     | Asosan ha        |
| Heap Sort   | `O(n log n)` | `O(n log n)` | Yo'q     | Ha               |

## Merge Sort amaliyoti

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(a, b):
    i = j = 0
    out = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1

    out.extend(a[i:])
    out.extend(b[j:])
    return out
```

## Joyida ishlovchi Quick Sort (Lomuto)

```python
def quick_sort(nums):
    def sort(lo, hi):
        if lo >= hi:
            return

        p = partition(lo, hi)
        sort(lo, p - 1)
        sort(p + 1, hi)

    def partition(lo, hi):
        pivot = nums[hi]
        i = lo
        for j in range(lo, hi):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        return i

    sort(0, len(nums) - 1)
    return nums
```

## Ilg'or saralash variantlari

### Heap Sort

```python
def heap_sort(nums):
    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right
            
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(n, largest)

    n = len(nums)
    # Max heap (eng katta uyum) quramiz
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
        
    # Elementlarni birma-bir chiqarib olamiz
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(i, 0)
        
    return nums
```

- **Vaqt:** `O(n log n)`
- **Xotira:** `O(1)` (joyida ishlaydi)
- *Eslatma: Heap sort, Merge sort'ning `O(n)` xotirasidan farqli o'laroq, qat'iy ravishda `O(1)` o'zgarmas xotira talab qilinganda juda qo'l keladi.*

### Counting Sort

Counting sort sonlarning takrorlanish sonini hisoblash orqali ishlaydi va shu yo'l bilan `O(n log n)` taqqoslash to'sig'ini yorib o'tadi, biroq u faqat chegaralangan butun sonlar oralig'ida samarali ishlaydi.

```python
def counting_sort(nums):
    if not nums:
        return nums
        
    max_val = max(nums)
    min_val = min(nums)
    
    # Har bir elementning takrorlanishlarini saqlaymiz
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(nums)
    
    # Takrorlanishlarni sanaymiz
    for num in nums:
        count[num - min_val] += 1
        
    # Yig'indi (prefiks) summalarini hisoblaymiz
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    # Elementlarni saralangan o'rniga joylashtiramiz
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
        
    # Saralangan elementlarni qaytarib ko'chiramiz
    for i in range(len(nums)):
        nums[i] = output[i]
        
    return nums
```

- **Vaqt:** `O(n + k)`, bu yerda `k` — oraliq `(max - min)`.
- **Xotira:** `O(n + k)`
- *Eslatma: Butun sonlarning kichik oraliqlari uchun tez. Radix Sort ichida keng qo'llaniladi.*
