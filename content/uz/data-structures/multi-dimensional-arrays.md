---
title: Ko'p o'lchamli massivlar va Matritsa ADT
description: Ikki o'lchamli massivlar, indeks moslashtirish va matritsa amallari (Chapter 4 asosida)
order: 4
permalink: /uz/data-structures/multi-dimensional-arrays/
---

Ushbu sahifa Necaise kitobidagi **Chapter 4 (Multi-Dimensional Arrays)** bobiga asoslanadi.

![Matrix indexing and row-major storage]({{ '/img/data-structures/matrix-indexing.svg' | url }})

## 2 o'lchamli massiv modeli

Ikki o'lchamli massiv qiymatlarni qatorlar (rows) va ustunlar (columns) ko'rinishida saqlaydi va ularga `(row, col)` orqali murojaat qilinadi.

Odatdagi ADT amallari:

- `num_rows()`
- `num_cols()`
- `clear(value)`
- `get(row, col)`
- `set(row, col, value)`

## Qatorga asoslangan moslashtirish (Row-major mapping)

Siz `a[row, col]` deb yozsangiz ham, ko'pincha implementatsiyalar ma'lumotni bitta yassi (flat) massivda saqlaydi.

Agar `ncols` ustunlar soni bo'lsa:

```text
flat_index = row * ncols + col
```

Aynan shu moslashtirish nima uchun indeksni hisoblash doimiy vaqtda (constant time) bajarilishini tushuntiradi.

## Minimal Python implementatsiyasi

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

## Matritsa ADT amallari

Xuddi shu bobda tuzilgan amallarga ega matritsa ADT'si keltiriladi:

- `scale_by(scalar)`
- `transpose()`
- `add(rhs)`
- `subtract(rhs)`
- `multiply(rhs)`

Bu amallar o'lchamlar bo'yicha qoidalarni talab qiladi:

- Qo'shish/ayirish: bir xil shaklda (shape) bo'lishi kerak.
- Ko'paytirish: chap matritsaning `ncols` qiymati o'ng matritsaning `nrows` qiymatiga teng bo'lishi shart.

Quyida ushbu amallardan ikkitasi to'liq keltirilgan; ayirish va elementlararo (element-wise) ko'paytirish xuddi shu ichma-ich sikl shaklidan foydalanadi.

```python
def transpose(matrix):
    return [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]


def add(a, b):
    return [[a[r][c] + b[r][c] for c in range(len(a[0]))] for r in range(len(a))]


m = [[1, 2, 3], [4, 5, 6]]
print(transpose(m))     # [[1, 4], [2, 5], [3, 6]]
print(add(m, m))        # [[2, 4, 6], [8, 10, 12]]
```

## Murakkablik bo'yicha xulosa

| Amal | Murakkablik |
| --------- | ---------- |
| `get`, `set` | `O(1)` |
| `clear` | `O(r * c)` |
| Matritsani qo'shish/ayirish | `O(r * c)` |
| Matritsani ko'paytirish (sodda usul) | `O(r * k * c)` |
| Transpozitsiya | `O(r * c)` |

## Python uchun amaliy maslahat

Ushbu ADT'dan indeks moslashtirish va matritsa amallarining qoidalarini o'rganish uchun foydalaning.  
Og'ir hisob-kitob ishlari uchun esa optimallashtirilgan vektorlashtirilgan amallarni taqdim etadigan NumPy'dan foydalanganingiz ma'qul.
