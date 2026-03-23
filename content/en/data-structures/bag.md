---
title: Bag
description: Bag (multiset) data structure — unordered collection that allows duplicates, with count and membership queries
order: 2
permalink: /en/data-structures/bag/
---

A **Bag** (also called a **multiset**) is an unordered collection that allows duplicate elements. Unlike a set, it keeps track of how many times each item appears. Unlike a list, it does not maintain insertion order or support index access.

## Book alignment (Chapter 2: Data Structures)

This page is based on the chapter parts:

- `2.1` Bags
- `2.4` Iterators
- `2.7-2.10` Maps and map operations (conceptual relation)

The Necaise presentation treats bag as a clean ADT that exposes only container-safe operations (`add`, `remove`, membership, traversal), preventing misuse of lower-level storage details.

![Bag frequencies]({{ '/img/data-structures/bag-frequencies.svg' | url }})

## Bag and map relationship

A practical bag implementation is usually backed by a map from `item -> count`.

- Bag API remains multiset-focused.
- Map API manages key/value storage and replacement.
- Iterator support provides safe traversal without exposing internals.

## Core idea

A bag answers two fundamental questions:

- **Does this item exist?** → `contains(item)`
- **How many copies are there?** → `count(item)`

Internally a bag is built on a hash map from item → frequency. This gives constant-time add, remove, and count for most inputs.

## When to use a bag

- Frequency counting (word histograms, character frequencies).
- Checking whether one collection is a sub-bag of another.
- Multiset arithmetic (union, intersection, difference).
- Anywhere order does not matter but duplicates do.

## When not to use a bag

- You need order-sensitive operations (sorting, rank, index access).
- You need range queries (`<= x`, between `a` and `b`) where tree-based structures work better.
- You need stable insertion order for iteration output.

## Operations

### add(item)

Increment the stored count for `item` by one.

```python
def add(self, item):
    self._counts[item] = self._counts.get(item, 0) + 1
    self._size += 1
```

### remove(item)

Decrement the count for `item`. If the count reaches zero the entry is deleted. Raises `ValueError` if the item is absent.

{% raw %}
```python
def remove(self, item):
    if self._counts.get(item, 0) == 0:
        raise ValueError(f"{item!r} not in bag")
    self._counts[item] -= 1
    if self._counts[item] == 0:
        del self._counts[item]
    self._size -= 1
```
{% endraw %}

### count(item)

Return the number of times `item` appears. Returns `0` for absent items.

```python
def count(self, item):
    return self._counts.get(item, 0)
```

### contains(item)

Return `True` if the item appears at least once.

```python
def contains(self, item):
    return self._counts.get(item, 0) > 0
```

### is_sub_bag(other)

Return `True` if every item in `self` appears at least as many times in `other`.

```python
def is_sub_bag(self, other):
    for item, cnt in self._counts.items():
        if other.count(item) < cnt:
            return False
    return True
```

### union(other)

Return a new bag where each item's count is the **maximum** of the two bags.

```python
def union(self, other):
    result = Bag(self)
    for item, cnt in other._counts.items():
        if cnt > result.count(item):
            result._counts[item] = cnt
    result._size = sum(result._counts.values())
    return result
```

### intersection(other)

Return a new bag where each item's count is the **minimum** of the two bags.

```python
def intersection(self, other):
    result = Bag()
    for item, cnt in self._counts.items():
        keep = min(cnt, other.count(item))
        if keep > 0:
            result._counts[item] = keep
    result._size = sum(result._counts.values())
    return result
```

## Full implementation

{% raw %}
```python
class Bag:
    """Unordered collection with duplicate tracking (multiset)."""

    def __init__(self, iterable=()):
        self._counts = {}
        self._size = 0
        for item in iterable:
            self.add(item)

    # ── core ──────────────────────────────────────────────────────────

    def add(self, item):
        self._counts[item] = self._counts.get(item, 0) + 1
        self._size += 1

    def remove(self, item):
        if self._counts.get(item, 0) == 0:
            raise ValueError(f"{item!r} not in bag")
        self._counts[item] -= 1
        if self._counts[item] == 0:
            del self._counts[item]
        self._size -= 1

    def count(self, item):
        return self._counts.get(item, 0)

    def contains(self, item):
        return self._counts.get(item, 0) > 0

    # ── set-like operations ────────────────────────────────────────────

    def is_sub_bag(self, other):
        return all(other.count(item) >= cnt for item, cnt in self._counts.items())

    def union(self, other):
        result = Bag(self)
        for item, cnt in other._counts.items():
            if cnt > result.count(item):
                result._counts[item] = cnt
        result._size = sum(result._counts.values())
        return result

    def intersection(self, other):
        result = Bag()
        for item, cnt in self._counts.items():
            keep = min(cnt, other.count(item))
            if keep > 0:
                result._counts[item] = keep
        result._size = sum(result._counts.values())
        return result

    def difference(self, other):
        """Items in self that are not covered by other, by count."""
        result = Bag()
        for item, cnt in self._counts.items():
            keep = max(0, cnt - other.count(item))
            if keep > 0:
                result._counts[item] = keep
        result._size = sum(result._counts.values())
        return result

    # ── dunder ────────────────────────────────────────────────────────

    def __len__(self):
        return self._size

    def __contains__(self, item):
        return self.contains(item)

    def __iter__(self):
        """Yield each item repeated by its count."""
        for item, cnt in self._counts.items():
            for _ in range(cnt):
                yield item

    def __repr__(self):
        pairs = ", ".join(f"{k!r}: {v}" for k, v in self._counts.items())
        return f"Bag({{{pairs}}})"
```
{% endraw %}

## Usage examples

```python
b = Bag(["apple", "banana", "apple", "cherry", "apple"])

print(b.count("apple"))        # 3
print(b.count("grape"))        # 0
print("banana" in b)           # True
print(len(b))                  # 5

b.add("banana")
print(b.count("banana"))       # 2

b.remove("apple")
print(b.count("apple"))        # 2

# Sub-bag check
a = Bag(["apple", "apple"])
print(a.is_sub_bag(b))         # True

# Intersection
x = Bag(["apple", "apple", "banana", "date"])
y = Bag(["apple", "banana", "banana"])
print(x.intersection(y))       # Bag({'apple': 1, 'banana': 1})

# Union
print(x.union(y))              # Bag({'apple': 2, 'banana': 2, 'date': 1})
```

## Real-world examples

- Counting log levels (`ERROR`, `WARN`, `INFO`) in streaming observability pipelines.
- Inventory quantities by item ID in e-commerce carts.
- Word frequency vectors for search indexing and text analytics.

## Complexity summary

| Operation      | Time   | Why                                  |
| -------------- | ------ | ------------------------------------ |
| `add`          | `O(1)` | Hash map insert / increment          |
| `remove`       | `O(1)` | Hash map decrement / delete          |
| `count`        | `O(1)` | Hash map lookup                      |
| `contains`     | `O(1)` | Hash map lookup                      |
| `is_sub_bag`   | `O(k)` | k = distinct items in self           |
| `union`        | `O(k)` | k = distinct items in both bags      |
| `intersection` | `O(k)` | k = distinct items in self           |
| `__iter__`     | `O(n)` | n = total item count                 |

Space is `O(k)` where k is the number of **distinct** items.

## Python standard library alternative

Python ships `collections.Counter`, which is a production-grade bag:

```python
from collections import Counter

c = Counter(["apple", "apple", "banana"])
print(c["apple"])        # 2
print(c.most_common(1))  # [('apple', 2)]
c.subtract(["apple"])
print(c["apple"])        # 1
```

`Counter` supports `+`, `-`, `&`, `|` operators which correspond to sum, difference, intersection, and union respectively.

## Typical mistakes

- Treating a bag as ordered — it gives no position-based access.
- Forgetting that `remove` raises on absent items; check `count` first if unsure.
- Using a plain `list` for frequency work when `Counter` or `Bag` is more expressive and faster for lookups.
