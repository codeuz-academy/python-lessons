---
title: Searching
description: Linear search, binary search, and search-the-answer-space patterns
order: 3
permalink: /en/algorithms/searching/
---

Searching means locating a target in a dataset.

## Linear Search

Works on any list.

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

- Time: `O(n)`
- Space: `O(1)`

## Binary Search

Requires sorted input.

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

- Time: `O(log n)`
- Space: `O(1)`

## Binary Search Variants

- Lower bound: first index with value `>= target`.
- Upper bound: first index with value `> target`.
- Search answer space (e.g., minimum feasible value problems).
