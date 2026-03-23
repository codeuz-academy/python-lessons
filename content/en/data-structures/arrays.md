---
title: Arrays
description: Dynamic arrays, index operations, and common patterns
order: 3
permalink: /en/data-structures/arrays/
---

Arrays are contiguous blocks of memory. In Python, `list` behaves like a dynamic array: random access is fast, and append is usually fast.

## Book alignment (Chapter 3: Arrays and Vectors)

From the Necaise book, this page maps to:

- `3.1` array structure and index-based access.
- `3.4` vector ADT (growable sequence container).
- `3.5` expandable container design (capacity growth, copy on resize).
- `3.6` vector implementation details.

The key design point is to separate:

- logical length (`size`) and
- allocated storage (`capacity`).

That separation explains why appends are amortized `O(1)`.

![Array operation overview]({{ '/img/data-structures/array-operations.png' | url }})

## Mental model

Keep these ideas clear:

- `size`: number of valid elements.
- `capacity`: allocated slots (often larger than `size`).
- Resize happens occasionally and copies data, which makes append amortized `O(1)`.

## When to use arrays

- You need direct indexing by position.
- You scan data from left to right.
- You use pattern-based techniques such as two pointers or sliding window.
- You want cache-friendly, contiguous storage.

## When not to use arrays

- You do frequent middle inserts/deletes in hot code paths.
- You need fast prepend (`deque` is usually better).
- You need stable references to nodes while rearranging structure (linked structures are easier).

## Operations

### get(index)

Array memory is contiguous, so the element address is computed directly from `index`. No traversal is needed.

![Array get operation]({{ '/img/data-structures/array-get.png' | url }})

```python
def get(self, index):
    if index < 0 or index >= len(self.data):
        raise IndexError("index out of range")
    return self.data[index]
```

### append(value)

`append` places the value at the end. Most appends are constant time. Rarely, the backing storage grows and copies data, which gives amortized `O(1)`.

![Array append operation]({{ '/img/data-structures/array-append.png' | url }})

```python
def append(self, value):
    self.data.append(value)
```

### insert(index, value)

Elements from `index` to the end shift right by one slot, then the new value is placed at `index`. Cost is linear in the number of shifted elements.

![Array insert operation]({{ '/img/data-structures/array-insert.png' | url }})

```python
def insert(self, index, value):
    if index < 0 or index > len(self.data):
        raise IndexError("index out of range")
    self.data.insert(index, value)
```

### delete(index)

Element at `index` is removed, and all later elements shift left by one slot.

![Array delete operation]({{ '/img/data-structures/array-delete.png' | url }})

```python
def delete(self, index):
    if index < 0 or index >= len(self.data):
        raise IndexError("index out of range")
    return self.data.pop(index)
```

## Full implementation

```python
class DynamicArray:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def get(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("index out of range")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= len(self.data):
            raise IndexError("index out of range")
        self.data[index] = value

    def insert(self, index, value):
        if index < 0 or index > len(self.data):
            raise IndexError("index out of range")
        self.data.insert(index, value)

    def delete(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("index out of range")
        return self.data.pop(index)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"DynamicArray({self.data})"
```

## Complexity summary

| Operation | Time | Why |
| --------- | ---- | --- |
| Read by index | `O(1)` | Direct address calculation |
| Update by index | `O(1)` | Overwrite existing slot |
| Append | `O(1)` amortized | Occasional resize and copy |
| Insert in middle | `O(n)` | Shift right |
| Delete in middle | `O(n)` | Shift left |
| Search unsorted array | `O(n)` | Sequential scan |

## Common patterns

### Two pointers

Useful for sorted arrays and palindrome checks. One pointer starts at the beginning and the other at the end; they move toward each other.

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

- Time: `O(n)`
- Space: `O(1)`

### Sliding window

Track a running window of size `k` to avoid repeated summing. Shift the window one step at a time.

```python
def max_sum_k(nums, k):
    if k > len(nums):
        return None

    window_sum = sum(nums[:k])
    best = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        best = max(best, window_sum)

    return best
```

- Time: `O(n)`
- Space: `O(1)`

### Frequency counting

Count occurrences of each element. Useful for anagram checks, duplicate detection, and histogram problems.

```python
def is_anagram(a, b):
    if len(a) != len(b):
        return False

    count = {}
    for ch in a:
        count[ch] = count.get(ch, 0) + 1

    for ch in b:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False

    return True
```

- Time: `O(n)`
- Space: `O(n)`

### Prefix sums

Precompute cumulative sums to answer range-sum queries in `O(1)` after `O(n)` setup.

```python
def build_prefix(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix


def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

- Setup: `O(n)`
- Query: `O(1)`

## Edge-case checklist

- Bounds checks for all index-based methods.
- Empty array behavior for delete/read.
- `k > len(nums)` style guard for window algorithms.
- Large inputs where repeated middle insert/delete may dominate runtime.

## Typical mistakes

- Forgetting bounds checks.
- Using middle insert in hot paths where linked list or `deque` may be better.
- Assuming append is always strict `O(1)` instead of amortized `O(1)`.
