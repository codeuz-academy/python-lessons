---
title: Turlangan massivlar (Typed Arrays — array moduli)
description: Python'ning array moduli yordamida C-ga asoslangan turlangan massivlar — list'ga qaraganda turi qat'iy belgilangan, xotira tejamkor muqobil
order: 11
permalink: /uz/data-structures/typed-arrays/
---

Python'ning o'rnatilgan (built-in) `list` turi Python obyektlariga havolalarni saqlaydi, bu esa 64-bitli apparatda saqlanayotgan qiymatdan qat'i nazar har bir element uchun taxminan **56 bayt** xarajat keltiradi. Standart kutubxonadagi `array` moduli esa **C-ga asoslangan, turi qat'iy belgilangan massiv** taqdim etadi: u xom qiymatlarni uzluksiz (contiguous) xotirada saqlaydi — xuddi C yoki Cython dasturi ishlatadigan joylashuvning o'zi.

## Kitob bilan moslik

Bu sahifa Necaise kitobining massiv/vektor boblari yonidagi **amaliy kengaytma**dir.  
U xuddi shu massiv ADT mantig'ini saqlab qoladi, ammo Python standart kutubxonasida mavjud bo'lgan quyi darajadagi xotira joylashuvini ko'rsatadi.

![Turlangan massiv xotira joylashuvi]({{ '/img/data-structures/typed-array-memory.svg' | url }})

Shu sababli `array` quyidagi holatlarda eng yaxshi tanlovdir:
- Imkon qadar kichik xotira hajmini egallaydigan katta sonlar to'plamiga ehtiyoj bo'lganda.
- C kengaytmalari, `struct` yoki `mmap` bilan o'zaro ishlash kerak bo'lganda.
- Tezkor ko'p hajmli `I/O` zarur bo'lganda (butun massivni bitta chaqiruvda baytlarga serializatsiya qilish mumkin).

## Tur kodlari (Type codes)

Har bir `array` **tur kodi (type code)** bilan yaratiladi, bu kod massivning butun yashash davri uchun element turini qat'iy belgilab qo'yadi.

| Tur kodi | C turi          | Python turi | Minimal hajm |
| --------- | -------------- | ----------- | ------------ |
| `'b'`     | `signed char`  | `int`       | 1 bayt       |
| `'B'`     | `unsigned char`| `int`       | 1 bayt       |
| `'h'`     | `signed short` | `int`       | 2 bayt       |
| `'H'`     | `unsigned short`| `int`      | 2 bayt       |
| `'i'`     | `signed int`   | `int`       | 2 bayt       |
| `'I'`     | `unsigned int` | `int`       | 2 bayt       |
| `'l'`     | `signed long`  | `int`       | 4 bayt       |
| `'L'`     | `unsigned long`| `int`       | 4 bayt       |
| `'q'`     | `signed long long`| `int`   | 8 bayt       |
| `'Q'`     | `unsigned long long`| `int` | 8 bayt       |
| `'f'`     | `float`        | `float`     | 4 bayt       |
| `'d'`     | `double`       | `float`     | 8 bayt       |

<div class="note">
Tur kodlarining hajmi platforma va kompilyatorga qarab farq qilishi mumkin (ayniqsa `l`/`L` uchun). Agar binar moslik muhim bo'lsa, `i`/`I` yoki `q`/`Q` kabi kengligi aniq belgilangan kodlardan foydalaning.
</div>

## Massiv yaratish

```python
import array

# Ishorali (signed) butun sonlardan iborat bo'sh massiv
ints = array.array('i')

# iterable'dan boshlang'ich qiymat berib yaratish
floats = array.array('f', [1.0, 2.5, 3.14])

# range'dan yaratish
counts = array.array('l', range(1_000_000))
```

## Amallar

### append va extend

`append` va `extend` xuddi `list`'dagidek ishlaydi. Elementlar tur kodiga mos kelishi shart.

```python
a = array.array('i', [10, 20, 30])
a.append(40)          # [10, 20, 30, 40]
a.extend([50, 60])    # [10, 20, 30, 40, 50, 60]
```

### Indeks orqali murojaat va kesim olish (slicing)

Indeks orqali tasodifiy murojaat `O(1)` — xuddi `list`'dagidek. Kesim (slice) esa o'sha turdagi yangi `array` qaytaradi.

```python
a = array.array('d', [1.1, 2.2, 3.3, 4.4])
print(a[1])       # 2.2
print(a[-1])      # 4.4
print(a[1:3])     # array('d', [2.2, 3.3])
```

### Qo'shish (insert) va o'chirish (delete)

```python
a = array.array('i', [1, 2, 3, 4])
a.insert(2, 99)   # [1, 2, 99, 3, 4]  — O(n) siljish
a.pop(2)          # 99 ni o'chiradi    — O(n) siljish
a.remove(3)       # birinchi 3 ni o'chiradi — O(n) skan + siljish
```

### Qidirish

```python
a = array.array('i', [10, 20, 30, 20])
print(a.index(20))   # 1  — birinchi uchrash, O(n)
print(a.count(20))   # 2  — uchrashlar sonini sanaydi, O(n)
```

### Teskari aylantirish

```python
a = array.array('i', [1, 2, 3])
a.reverse()
print(a)   # array('i', [3, 2, 1])
```

### Ko'p hajmli bayt `I/O`

`list`'dan asosiy ustunligi: butun `array` xom baytlarga (yoki xom baytlardan) har bir element uchun emas, balki har bir bayt uchun doimiy vaqtda serializatsiya qilinadi — chunki xotira allaqachon uzluksiz va turlangan.

```python
import array

a = array.array('i', [1, 2, 3, 4])

# Baytlarga serializatsiya qilish
raw = a.tobytes()
print(len(raw))   # 16  (4 ta int × har biri 4 bayt)

# Deserializatsiya qilish
b = array.array('i')
b.frombytes(raw)
print(b)          # array('i', [1, 2, 3, 4])
```

### Fayl `I/O`

```python
import array

a = array.array('d', [3.14, 2.71, 1.41])

with open('numbers.bin', 'wb') as f:
    a.tofile(f)

loaded = array.array('d')
with open('numbers.bin', 'rb') as f:
    loaded.fromfile(f, 3)   # aniq 3 ta elementni o'qiydi

print(loaded)   # array('d', [3.14, 2.71, 1.41])
```

## Xotira solishtiruvi: `list` va `array`

{% raw %}
```python
import sys
import array

n = 1_000_000

py_list = list(range(n))
c_array = array.array('l', range(n))

print(f"list  : {sys.getsizeof(py_list):,} bytes")
print(f"array : {sys.getsizeof(c_array):,} bytes")
# 64-bitli CPython'da odatiy chiqish:
# list  : 8,000,056 bytes
# array : 8,000,058 bytes  (l = 8 baytli signed long)
#
# 32-bitli butun sonlar uchun ('i', har biri 4 bayt):
# array : 4,000,058 bytes  — list'ning yarmicha xotira
```
{% endraw %}

Tur kodi ko'rsatkichdan (64-bitda 8 bayt) kamroq bayt ishlatganda tejamkorlik ortib boradi. Ishorali `int` (`'i'`, 4 bayt) xotirani taxminan ikki barobar qisqartiradi; `unsigned char` (`'B'`, 1 bayt) esa uni sakkizdan biriga tushiradi.

## O'rovchi (wrapper) sinf

`array.array`'ni tur kodini majburiy qiladigan va sohaga xos metodlar qo'shadigan sinf ichiga o'rab olishingiz mumkin:

```python
import array


class IntArray:
    """Ishorali 64-bitli butun sonlardan iborat o'lcham o'zgaruvchan massiv."""

    TYPECODE = 'q'  # signed long long

    def __init__(self, iterable=()):
        self._data = array.array(self.TYPECODE, iterable)

    def append(self, value):
        self._data.append(value)

    def get(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError("index out of range")
        return self._data[index]

    def set(self, index, value):
        if index < 0 or index >= len(self._data):
            raise IndexError("index out of range")
        self._data[index] = value

    def insert(self, index, value):
        self._data.insert(index, value)

    def delete(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError("index out of range")
        return self._data.pop(index)

    def tobytes(self):
        return self._data.tobytes()

    @classmethod
    def frombytes(cls, raw):
        obj = cls()
        obj._data.frombytes(raw)
        return obj

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return f"IntArray({list(self._data)})"
```

## Cython va NumPy bilan bog'liqlik

Python'ning `array` moduli Cython va NumPy tayanadigan xuddi shu **bufer protokoli (buffer protocol)**dan foydalanadi. Bu shuni anglatadiki:

- `int[:]` (turlangan memoryview) qabul qiladigan Cython funksiyasi `array.array('i', ...)`'ni **nusxa olmasdan (zero-copy)** qabul qila oladi.
- NumPy `array.array`'ni uning ostidagi xotirani nusxalamasdan o'rab olishi mumkin.
- CPython C API yordamida yozilgan C kengaytmalari massiv xotirasiga to'g'ridan-to'g'ri ko'rsatkich olish uchun `PyBUF_SIMPLE`ni chaqirishi mumkin.

```python
# non-runnable: requires numpy
import array
import numpy as np

a = array.array('d', [1.0, 2.0, 3.0, 4.0])

# Nusxasiz ko'rinish (zero-copy) — NumPy o'sha xotira blokini o'qiydi
arr = np.frombuffer(a, dtype=np.float64)
print(arr)          # [1. 2. 3. 4.]
print(arr.base)     # <memory at 0x...>  — nusxa emas
```

## Qachon NumPy'ni afzal ko'rish kerak

`array.array`'dan quyidagi holatlarda foydalaning:
- Faqat standart kutubxonaga tayanadigan, qo'shimcha bog'liqliklarsiz yechim istasangiz.
- Ma'lumotlar bir o'lchovli bo'lib, vektorlashtirilgan matematikani talab qilmasa.
- Tarmoq paketlari yoki fayl formatlari uchun tezkor binar serializatsiya kerak bo'lsa.

**NumPy**'dan quyidagi holatlarda foydalaning:
- Ko'p o'lchovli massivlar kerak bo'lsa.
- Vektorlashtirilgan arifmetika, broadcasting yoki chiziqli algebra kerak bo'lsa.
- Ilmiy yoki mashinaviy o'qitish (machine-learning) kodi bilan ishlasangiz.

## Qachon `array.array`'dan foydalanmaslik kerak

- Aralash element turlari yoki ichma-ich (nested) tuzilmalar kerak bo'lsa.
- O'rtaga tez-tez ixtiyoriy qo'shish/o'chirish kerak bo'lsa.
- Nomlangan o'lchamlar, maskalar, broadcasting yoki matritsa amallari kerak bo'lsa.

## Murakkablik xulosasi

| Amal              | Vaqt             | Izoh                                  |
| ----------------- | ---------------- | ------------------------------------- |
| Indeks orqali o'qish / yozish | `O(1)` | To'g'ridan-to'g'ri ko'rsatkich siljishi, boxing yo'q |
| Append            | `O(1)` amortizatsiyalangan | `list` bilan bir xil o'sish strategiyasi |
| O'rtaga qo'shish  | `O(n)`           | Elementlar xom xotirada siljiydi      |
| O'rtadan o'chirish | `O(n)`          | Elementlar xom xotirada siljiydi      |
| `tobytes`         | `O(n)`           | Uzluksiz blokning xotira nusxasi (memcopy) |
| `frombytes`       | `O(n)`           | Uzluksiz blokka xotira nusxasi (memcopy) |
| `index` / `count` | `O(n)`           | Ketma-ket skan                        |

## Tipik xatolar

- Aralash turlarni saqlashga urinish — `array` yagona tur kodini majburiy qiladi va mos kelmaganda `TypeError` ko'taradi.
- Big-endian va little-endian tizimlar o'rtasida fayllarni almashganda bayt tartibini unutish. `a.byteswap()` yoki aniq endian prefiksi bilan `struct.pack`'dan foydalaning.
- NumPy allaqachon mavjud bo'lsa ham `array`'ga murojaat qilish — sonli ishlar uchun NumPy ko'proq imkoniyatli va odatda tezroq.
- Toza Python takrorlash (loop)'lari uchun `array.array` `list`'dan tezroq deb o'ylash — tezlik ustunligi Python darajasidagi `for` takrorlashlarida emas, balki ko'p hajmli `I/O` va C kengaytma chaqiruvlarida namoyon bo'ladi.
