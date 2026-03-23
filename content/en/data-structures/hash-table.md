---
title: Hash Table
description: Hash table with separate chaining, collision handling, and rehashing
order: 7
permalink: /en/data-structures/hash-table/
---

A hash table maps keys to values by converting each key into a bucket index.

## Book alignment (Chapter 11: Hash Tables)

This page is aligned to the hash-table chapter in the book:

- keys are transformed by a hash function
- collisions are unavoidable and must be resolved predictably
- performance depends on load factor and resize policy

Even when using Python `dict`, understanding these mechanisms is essential for reasoning about average vs worst-case behavior.

## Core ideas

- `hash(key)` gives a number.
- `index = hash(key) % capacity` chooses bucket position.
- If multiple keys map to the same bucket, that is a collision.

This chapter uses **separate chaining** (each bucket stores a small list of key-value pairs).

## Invariants

- `size` equals the total number of unique keys stored.
- Buckets are always lists of `(key, value)` pairs.
- On resize, all keys are reinserted using the new capacity.

## Operations

### set(key, value)

Compute bucket index, search the bucket for an existing key, and either update or append.

![Hash table set operation]({{ '/img/data-structures/hash-table-set.png' | url }})

```python
def set(self, key, value):
    index = self._index(key)
    bucket = self.buckets[index]

    for i, (stored_key, _) in enumerate(bucket):
        if stored_key == key:
            bucket[i] = (key, value)
            return

    bucket.append((key, value))
    self.size += 1
    if self.load_factor > self.max_load_factor:
        self._resize(self.capacity * 2)
```

### get(key)

Jump directly to one bucket, then scan only inside that bucket.

![Hash table get operation]({{ '/img/data-structures/hash-table-get.png' | url }})

```python
def get(self, key):
    bucket = self.buckets[self._index(key)]
    for stored_key, stored_value in bucket:
        if stored_key == key:
            return stored_value
    raise KeyError(key)
```

### delete(key)

Find matching pair in the bucket and remove it. Other buckets are untouched.

![Hash table delete operation]({{ '/img/data-structures/hash-table-delete.png' | url }})

```python
def delete(self, key):
    bucket = self.buckets[self._index(key)]
    for i, (stored_key, _) in enumerate(bucket):
        if stored_key == key:
            del bucket[i]
            self.size -= 1
            return True
    return False
```

### resize(new_capacity)

Allocate new buckets and reinsert every pair. This rebuild keeps bucket chains short.

```python
def _resize(self, new_capacity):
    old_items = [pair for bucket in self.buckets for pair in bucket]
    self.capacity = max(4, new_capacity)
    self.buckets = [[] for _ in range(self.capacity)]
    self.size = 0

    for key, value in old_items:
        self.set(key, value)
```

## Full implementation

```python
class HashTable:
    def __init__(self, capacity=16, max_load_factor=0.75):
        self.capacity = max(4, capacity)
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        self.max_load_factor = max_load_factor

    @property
    def load_factor(self):
        return self.size / self.capacity

    def _index(self, key):
        return hash(key) % self.capacity

    def set(self, key, value):
        index = self._index(key)
        bucket = self.buckets[index]

        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1
        if self.load_factor > self.max_load_factor:
            self._resize(self.capacity * 2)

    def get(self, key):
        bucket = self.buckets[self._index(key)]
        for stored_key, stored_value in bucket:
            if stored_key == key:
                return stored_value
        raise KeyError(key)

    def delete(self, key):
        bucket = self.buckets[self._index(key)]
        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def contains(self, key):
        bucket = self.buckets[self._index(key)]
        return any(stored_key == key for stored_key, _ in bucket)

    def _resize(self, new_capacity):
        old_items = [pair for bucket in self.buckets for pair in bucket]
        self.capacity = max(4, new_capacity)
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for key, value in old_items:
            self.set(key, value)
```

## Complexity summary

| Operation | Average | Worst case |
| --------- | ------- | ---------- |
| Insert | `O(1)` | `O(n)` |
| Lookup | `O(1)` | `O(n)` |
| Delete | `O(1)` | `O(n)` |
| Resize | `O(n)` | `O(n)` |

Worst-case behavior appears when many keys collide into one bucket. Rehashing reduces that risk.

## Collision strategy note

Two common strategies exist:

- Separate chaining (used here): each bucket stores a small list.
- Open addressing: probes nearby slots in one array.

Python `dict` uses a highly optimized open-addressing approach with additional tricks.

## Practical notes

- Use immutable keys (`str`, `int`, tuple of immutables).
- Key type should keep `hash(key)` stable over its lifetime.
- Equal keys must always produce the same hash value.
- Track load factor to keep average access near constant time.

## Typical mistakes

- Forgetting to rehash all keys during resize.
- Mutating an object used as a key after insertion.
- Assuming average-case `O(1)` is guaranteed under adversarial input.
