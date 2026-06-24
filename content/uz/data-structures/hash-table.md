---
title: Hash Table
description: Separate chaining bilan ishlovchi hash table, to'qnashuvlarni hal qilish va rehashing
order: 7
permalink: /uz/data-structures/hash-table/
---

Hash table har bir kalitni `bucket` indeksiga aylantirib, kalitlarni qiymatlarga bog'laydi.

## Kitobga moslik (11-bob: Hash Tables)

Ushbu sahifa kitobdagi hash table bo'limiga moslashtirilgan:

- kalitlar hash funksiyasi orqali o'zgartiriladi
- to'qnashuvlar (collision) muqarrar va ularni oldindan aytsa bo'ladigan tarzda hal qilish kerak
- unumdorlik (`performance`) `load factor` va o'lcham o'zgartirish (resize) siyosatiga bog'liq

Python `dict` ishlatganda ham, o'rtacha va eng yomon holatdagi xatti-harakatni tushunish uchun bu mexanizmlarni bilish muhim.

## Asosiy g'oyalar

- `hash(key)` son qaytaradi.
- `index = hash(key) % capacity` bucket joylashuvini tanlaydi.
- Agar bir nechta kalit bitta `bucket`ga tushsa, bu to'qnashuv (collision) hisoblanadi.

Bu bobda **separate chaining** ishlatiladi (har bir `bucket` kalit-qiymat (`key-value`) juftliklarining kichik ro'yxatini saqlaydi).

## Invariantlar

- `size` saqlangan noyob kalitlarning umumiy soniga teng.
- `bucket`lar har doim `(key, value)` juftliklarining ro'yxati bo'ladi.
- O'lcham o'zgartirilganda barcha kalitlar yangi `capacity` asosida qayta joylashtiriladi.

## Amallar

### set(key, value)

`bucket` indeksini hisoblang, `bucket` ichidan mavjud kalitni qidiring va uni yangilang yoki qo'shing.

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

To'g'ridan-to'g'ri bitta `bucket`ga o'ting, so'ngra faqat shu `bucket` ichini ko'rib chiqing.

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

`bucket` ichidan mos juftlikni toping va uni o'chiring. Boshqa `bucket`larga tegilmaydi.

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

Yangi `bucket`lar ajrating va har bir juftlikni qayta joylashtiring. Bu qayta qurish `bucket` zanjirlarini qisqa saqlaydi.

```python
def _resize(self, new_capacity):
    old_items = [pair for bucket in self.buckets for pair in bucket]
    self.capacity = max(4, new_capacity)
    self.buckets = [[] for _ in range(self.capacity)]
    self.size = 0

    for key, value in old_items:
        self.set(key, value)
```

## To'liq amalga oshirish

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

## Murakkablik xulosasi

| Amal | O'rtacha | Eng yomon holat |
| --------- | ------- | ---------- |
| Qo'shish | `O(1)` | `O(n)` |
| Qidirish | `O(1)` | `O(n)` |
| O'chirish | `O(1)` | `O(n)` |
| O'lcham o'zgartirish | `O(n)` | `O(n)` |

Eng yomon holatdagi xatti-harakat ko'p kalitlar bitta `bucket`ga to'qnashganda paydo bo'ladi. Rehashing bu xavfni kamaytiradi.

## To'qnashuv strategiyasi haqida eslatma

Ikkita keng tarqalgan strategiya mavjud:

- Separate chaining (bu yerda ishlatilgan): har bir `bucket` kichik ro'yxat saqlaydi.
- Open addressing: bitta massivda yaqin atrofdagi joylarni tekshiradi.

Python `dict` qo'shimcha usullar bilan yuqori darajada optimallashtirilgan open-addressing yondashuvidan foydalanadi.

## Amaliy eslatmalar

- O'zgarmas (`immutable`) kalitlardan foydalaning (`str`, `int`, o'zgarmas qiymatlardan iborat tuple).
- Kalit turi o'z mavjudligi davomida `hash(key)` qiymatini barqaror saqlashi kerak.
- Teng kalitlar har doim bir xil hash qiymatini berishi shart.
- O'rtacha kirishni doimiy vaqtga yaqin saqlash uchun `load factor`ni kuzatib boring.

## Odatiy xatolar

- O'lcham o'zgartirish vaqtida barcha kalitlarni qayta hash qilishni unutish.
- Kalit sifatida ishlatilgan obyektni joylashtirilgandan keyin o'zgartirish.
- Adversarial kirish ostida o'rtacha holatdagi `O(1)` kafolatlangan deb hisoblash.
