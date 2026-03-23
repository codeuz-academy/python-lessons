---
title: Multi-Dimensional Arrays & Matrix ADT
description: Two-dimensional arrays, index mapping, and matrix operations inspired by Chapter 4
order: 4
permalink: /en/data-structures/multi-dimensional-arrays/
---

This page follows **Chapter 4 (Multi-Dimensional Arrays)** from the Necaise book.

![Matrix indexing and row-major storage]({{ '/img/data-structures/matrix-indexing.svg' | url }})

## 2-D array model

A two-dimensional array stores values in rows and columns, addressed by `(row, col)`.

Typical ADT operations:

- `num_rows()`
- `num_cols()`
- `clear(value)`
- `get(row, col)`
- `set(row, col, value)`

## Row-major mapping

Even when you write `a[row, col]`, implementations often store data in one flat array.

If `ncols` is the column count:

```text
flat_index = row * ncols + col
```

This mapping explains why index translation is constant time.

## Minimal Python implementation

```python
class Array2D:
    def __init__(self, nrows, ncols, fill=None):
        if nrows <= 0 or ncols <= 0:
            raise ValueError("nrows and ncols must be > 0")
        self._nrows = nrows
        self._ncols = ncols
        self._data = [fill] * (nrows * ncols)

    def num_rows(self):
        return self._nrows

    def num_cols(self):
        return self._ncols

    def _flat_index(self, row, col):
        if row < 0 or row >= self._nrows or col < 0 or col >= self._ncols:
            raise IndexError("index out of range")
        return row * self._ncols + col

    def get(self, row, col):
        return self._data[self._flat_index(row, col)]

    def set(self, row, col, value):
        self._data[self._flat_index(row, col)] = value

    def clear(self, value):
        for i in range(len(self._data)):
            self._data[i] = value
```

## Matrix ADT operations

The same chapter introduces a matrix ADT with structured operations:

- `scale_by(scalar)`
- `transpose()`
- `add(rhs)`
- `subtract(rhs)`
- `multiply(rhs)`

These operations require dimension rules:

- Add/subtract: same shape.
- Multiply: left `ncols` must equal right `nrows`.

## Complexity summary

| Operation | Complexity |
| --------- | ---------- |
| `get`, `set` | `O(1)` |
| `clear` | `O(r * c)` |
| Matrix add/subtract | `O(r * c)` |
| Matrix multiply (naive) | `O(r * k * c)` |
| Transpose | `O(r * c)` |

## Practical note for Python

Use this ADT for learning index mapping and matrix contracts.  
For heavy numerical workloads, prefer NumPy for optimized vectorized operations.
