---
title: Bag
description: Bag (multiset) ma'lumotlar tuzilmasi — takror elementlarga ruxsat beruvchi tartibsiz to'plam, son va a'zolik so'rovlari bilan
order: 2
permalink: /uz/data-structures/bag/
---

**Bag** (yana **multiset** deb ham ataladi) — bu takror elementlarga ruxsat beruvchi tartibsiz to'plam. To'plam (`set`) dan farqli o'laroq, u har bir element necha marta uchraganini hisoblab boradi. Ro'yxat (`list`) dan farqli o'laroq esa, u qo'shilish tartibini saqlamaydi va indeks orqali murojaatni qo'llab-quvvatlamaydi.

## Kitobga moslik (2-bob: Ma'lumotlar tuzilmalari)

Ushbu sahifa quyidagi bob qismlariga asoslangan:

- `2.1` Bag'lar
- `2.4` `Iterator'lar`
- `2.7-2.10` Map'lar va map ustidagi amallar (mazmuniy bog'liqlik)

Necaise'ning taqdimotida bag toza ADT sifatida tavsiflanadi: u faqat konteyner uchun xavfsiz amallarni (`add`, `remove`, a'zolik, aylanib chiqish) ochib beradi va past darajadagi saqlash tafsilotlarini noto'g'ri ishlatishning oldini oladi.

![Bag chastotalari]({{ '/img/data-structures/bag-frequencies.svg' | url }})

## Bag va map o'rtasidagi bog'liqlik

Amaliy bag implementatsiyasi odatda `element -> son` ko'rinishidagi map asosida quriladi.

- Bag API multiset'ga yo'naltirilgan bo'lib qoladi.
- Map API esa kalit/qiymat saqlash va almashtirishni boshqaradi.
- `Iterator` qo'llab-quvvatlash ichki tuzilmani ochib bermasdan xavfsiz aylanib chiqishni ta'minlaydi.

## Asosiy g'oya

Bag ikkita asosiy savolga javob beradi:

- **Bu element mavjudmi?** → `contains(item)`
- **Uning nechta nusxasi bor?** → `count(item)`

Ichki jihatdan bag element → chastota ko'rinishidagi hash map asosida quriladi. Bu ko'pchilik kirish ma'lumotlari uchun qo'shish, o'chirish va sanashni doimiy vaqtda bajarish imkonini beradi.

## Bag'dan qachon foydalanish kerak

- Chastotalarni sanash (so'z histogrammalari, belgilar chastotalari).
- Bir to'plam boshqasining ichki bag'i (sub-bag) ekanligini tekshirish.
- Multiset arifmetikasi (birlashma, kesishma, ayirma).
- Tartib muhim bo'lmagan, lekin takrorlar muhim bo'lgan har qanday joyda.

## Bag'dan qachon foydalanmaslik kerak

- Sizga tartibga sezgir amallar kerak bo'lganda (saralash, daraja, indeks orqali murojaat).
- Sizga diapazon so'rovlari (`<= x`, `a` va `b` orasida) kerak bo'lganda — bu yerda daraxt asosidagi tuzilmalar yaxshiroq ishlaydi.
- Aylanib chiqish natijasida barqaror qo'shilish tartibi kerak bo'lganda.

## Amallar

### add(item)

`item` uchun saqlangan sonni bittaga oshiradi.

```python
def add(self, item):
    self._counts[item] = self._counts.get(item, 0) + 1
    self._size += 1
```

### remove(item)

`item` uchun sonni bittaga kamaytiradi. Agar son nolga yetsa, yozuv o'chiriladi. Agar element mavjud bo'lmasa, `ValueError` ni ko'taradi.

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

`item` necha marta uchraganini qaytaradi. Mavjud bo'lmagan elementlar uchun `0` qaytaradi.

```python
def count(self, item):
    return self._counts.get(item, 0)
```

### contains(item)

Agar element kamida bir marta uchrasa, `True` qaytaradi.

```python
def contains(self, item):
    return self._counts.get(item, 0) > 0
```

### is_sub_bag(other)

Agar `self` dagi har bir element `other` da kamida shuncha marta uchrasa, `True` qaytaradi.

```python
def is_sub_bag(self, other):
    for item, cnt in self._counts.items():
        if other.count(item) < cnt:
            return False
    return True
```

### union(other)

Har bir elementning soni ikki bag'dagi sonlardan **maksimumi** bo'lgan yangi bag qaytaradi.

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

Har bir elementning soni ikki bag'dagi sonlardan **minimumi** bo'lgan yangi bag qaytaradi.

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

## To'liq implementatsiya

{% raw %}
```python
class Bag:
    """Unordered collection with duplicate tracking (multiset)."""

    def __init__(self, iterable=()):
        self._counts = {}
        self._size = 0
        for item in iterable:
            self.add(item)

    # ── asosiy ──────────────────────────────────────────────────────────

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

    # ── to'plamga o'xshash amallar ────────────────────────────────────────────

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

## Foydalanish misollari

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

# Sub-bag tekshiruvi
a = Bag(["apple", "apple"])
print(a.is_sub_bag(b))         # True

# Kesishma
x = Bag(["apple", "apple", "banana", "date"])
y = Bag(["apple", "banana", "banana"])
print(x.intersection(y))       # Bag({'apple': 1, 'banana': 1})

# Birlashma
print(x.union(y))              # Bag({'apple': 2, 'banana': 2, 'date': 1})
```

## Hayotiy misollar

- Oqimli kuzatuv (observability) tizimlarida log darajalarini (`ERROR`, `WARN`, `INFO`) sanash.
- Elektron tijorat savatchalarida element ID si bo'yicha inventar miqdorlari.
- Qidiruv indekslash va matn tahlili uchun so'z chastotasi vektorlari.

## Murakkablik xulosasi

| Amal           | Vaqt   | Nima uchun                           |
| -------------- | ------ | ------------------------------------ |
| `add`          | `O(1)` | Hash map'ga qo'shish / oshirish      |
| `remove`       | `O(1)` | Hash map'da kamaytirish / o'chirish  |
| `count`        | `O(1)` | Hash map'da qidirish                 |
| `contains`     | `O(1)` | Hash map'da qidirish                 |
| `is_sub_bag`   | `O(k)` | k = self'dagi turli elementlar soni  |
| `union`        | `O(k)` | k = ikki bag'dagi turli elementlar   |
| `intersection` | `O(k)` | k = self'dagi turli elementlar soni  |
| `__iter__`     | `O(n)` | n = elementlarning umumiy soni       |

Xotira `O(k)`, bu yerda k — **turli** elementlar soni.

## Python standart kutubxonasidagi muqobil

Python `collections.Counter` ni taqdim etadi, bu ishlab chiqarish darajasidagi bag hisoblanadi:

```python
from collections import Counter

c = Counter(["apple", "apple", "banana"])
print(c["apple"])        # 2
print(c.most_common(1))  # [('apple', 2)]
c.subtract(["apple"])
print(c["apple"])        # 1
```

`Counter` mos ravishda yig'indi, ayirma, kesishma va birlashmaga to'g'ri keladigan `+`, `-`, `&`, `|` operatorlarini qo'llab-quvvatlaydi.

## Tipik xatolar

- Bag'ni tartibli deb hisoblash — u joylashuvga asoslangan murojaatni bermaydi.
- `remove` mavjud bo'lmagan elementlarda xato ko'tarishini unutish; ishonchingiz komil bo'lmasa, avval `count` ni tekshiring.
- Chastota bilan ishlash uchun oddiy `list` dan foydalanish, holbuki `Counter` yoki `Bag` ifodaliroq va qidirishlar uchun tezroq.
