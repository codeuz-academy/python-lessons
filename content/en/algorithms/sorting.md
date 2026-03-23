---
title: Sorting
description: Merge sort and quick sort implementations with comparison table
order: 2
permalink: /en/algorithms/sorting/
---

Sorting arranges elements into increasing or decreasing order.

## Comparison of Common Sorts

| Algorithm   | Average      | Worst        | Stable | In-place |
| ----------- | ------------ | ------------ | ------ | -------- |
| Bubble Sort | `O(n^2)`     | `O(n^2)`     | Yes    | Yes      |
| Merge Sort  | `O(n log n)` | `O(n log n)` | Yes    | No       |
| Quick Sort  | `O(n log n)` | `O(n^2)`     | No     | Mostly   |
| Heap Sort   | `O(n log n)` | `O(n log n)` | No     | Yes      |

## Merge Sort Implementation

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

## In-place Quick Sort (Lomuto)

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

## Advanced Sorting Variants

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
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
        
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(i, 0)
        
    return nums
```

- **Time:** `O(n log n)`
- **Space:** `O(1)` (in-place)
- *Note: Heap sort is excellent when `O(1)` stable memory is strictly required, unlike Merge sort `O(n)`.*

### Counting Sort

Counting sort operates by counting the occurrences of numbers, breaking the `O(n log n)` comparison barrier, but it only works efficiently with a bounded integer range.

```python
def counting_sort(nums):
    if not nums:
        return nums
        
    max_val = max(nums)
    min_val = min(nums)
    
    # Store counts of each character
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(nums)
    
    # Count occurrences
    for num in nums:
        count[num - min_val] += 1
        
    # Calculate cumulative prefix sums
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    # Place elements in their sorted position
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
        
    # Copy sorted elements back
    for i in range(len(nums)):
        nums[i] = output[i]
        
    return nums
```

- **Time:** `O(n + k)` where `k` is the range `(max - min)`.
- **Space:** `O(n + k)`
- *Note: Fast for small ranges of integers. Extensively used inside Radix Sort.*
