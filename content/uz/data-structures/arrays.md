---
title: Massivlar (Arrays)
description: Dinamik massivlar, indeks amallari va keng tarqalgan andozalar
order: 3
permalink: /uz/data-structures/arrays/
---

Massivlar (arrays) — bu xotiraning ketma-ket joylashgan bloklaridir. Python'da `list` xuddi dinamik massivdek ishlaydi: ixtiyoriy elementga murojaat tez bo'ladi, oxiriga qo'shish (append) esa odatda tez bajariladi.

## Kitobga moslik (3-bob: Massivlar va vektorlar)

Necaise kitobidan olib qaralganda, ushbu sahifa quyidagilarga mos keladi:

- `3.1` massiv tuzilishi va indeksga asoslangan murojaat.
- `3.4` vektor ADT (kengayadigan ketma-ketlik konteyneri).
- `3.5` kengaytiriladigan konteyner dizayni (sig'imning o'sishi, o'lcham o'zgarganda nusxalash).
- `3.6` vektor amalga oshirilishining tafsilotlari.

Bu yerda asosiy dizayn nuqtasi ikki tushunchani ajratishdir:

- mantiqiy uzunlik (`size`) va
- ajratilgan xotira (`capacity`).

Aynan shu ajratish nima uchun oxiriga qo'shish amortizatsiyalangan `O(1)` ekanligini tushuntiradi.

![Massiv amallarining umumiy ko'rinishi]({{ '/img/data-structures/array-operations.png' | url }})

## Tasavvur modeli

Quyidagi g'oyalarni aniq tutib turing:

- `size`: haqiqiy (yaroqli) elementlar soni.
- `capacity`: ajratilgan kataklar (ko'pincha `size`'dan kattaroq).
- O'lchamni o'zgartirish vaqti-vaqti bilan sodir bo'ladi va ma'lumotlarni nusxalaydi, bu esa oxiriga qo'shishni amortizatsiyalangan `O(1)` qiladi.

## Massivlardan qachon foydalanish kerak

- Sizga pozitsiya bo'yicha to'g'ridan-to'g'ri indekslash kerak bo'lganda.
- Ma'lumotlarni chapdan o'ngga ko'rib chiqqanda.
- Ikki ko'rsatkich (two pointers) yoki suriluvchi oyna (sliding window) kabi andozaga asoslangan usullardan foydalanganingizda.
- Sizga kesh uchun qulay, ketma-ket joylashgan xotira kerak bo'lganda.

## Massivlardan qachon foydalanmaslik kerak

- Tez-tez ishlaydigan kod yo'llarida o'rtaga tez-tez qo'shish/o'chirish amallarini bajarsangiz.
- Sizga boshiga tez qo'shish (prepend) kerak bo'lsa (`deque` odatda yaxshiroq).
- Tuzilmani qayta tartiblash paytida tugunlarga barqaror murojaatlar kerak bo'lsa (bog'langan tuzilmalarda buni qilish osonroq).

## Amallar

### get(index)

Massiv xotirasi ketma-ket joylashgani uchun elementning manzili to'g'ridan-to'g'ri `index` asosida hisoblanadi. Hech qanday qadamlab o'tish (traversal) kerak emas.

![Massivdan olish amali]({{ '/img/data-structures/array-get.png' | url }})

```python
def get(self, index):
    if index < 0 or index >= len(self.data):
        raise IndexError("index out of range")
    return self.data[index]
```

### append(value)

`append` qiymatni oxiriga joylashtiradi. Ko'pchilik qo'shishlar doimiy vaqtda bajariladi. Kamdan-kam hollarda asosiy xotira kengayadi va ma'lumotlarni nusxalaydi, bu esa amortizatsiyalangan `O(1)` ni beradi.

![Massivga qo'shish amali]({{ '/img/data-structures/array-append.png' | url }})

```python
def append(self, value):
    self.data.append(value)
```

### insert(index, value)

`index`'dan oxirigacha bo'lgan elementlar bir katakka o'ngga suriladi, so'ngra yangi qiymat `index`'ga joylashtiriladi. Narxi suriladigan elementlar soniga chiziqli bog'liq.

![Massivga oraga qo'shish amali]({{ '/img/data-structures/array-insert.png' | url }})

```python
def insert(self, index, value):
    if index < 0 or index > len(self.data):
        raise IndexError("index out of range")
    self.data.insert(index, value)
```

### delete(index)

`index`'dagi element olib tashlanadi va undan keyingi barcha elementlar bir katakka chapga suriladi.

![Massivdan o'chirish amali]({{ '/img/data-structures/array-delete.png' | url }})

```python
def delete(self, index):
    if index < 0 or index >= len(self.data):
        raise IndexError("index out of range")
    return self.data.pop(index)
```

## To'liq amalga oshirilishi

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

## Murakkablik jadvali

| Amal | Vaqt | Nima uchun |
| --------- | ---- | --- |
| Indeks bo'yicha o'qish | `O(1)` | Manzilni to'g'ridan-to'g'ri hisoblash |
| Indeks bo'yicha yangilash | `O(1)` | Mavjud katakni ustiga yozish |
| Oxiriga qo'shish (append) | `O(1)` amortizatsiyalangan | Vaqti-vaqti bilan o'lcham o'zgarishi va nusxalash |
| O'rtaga qo'shish | `O(n)` | O'ngga surish |
| O'rtadan o'chirish | `O(n)` | Chapga surish |
| Tartiblanmagan massivda qidirish | `O(n)` | Ketma-ket ko'rib chiqish |

## Keng tarqalgan andozalar

### Ikki ko'rsatkich (Two pointers)

Tartiblangan massivlar va palindrom tekshiruvlari uchun foydali. Bir ko'rsatkich boshidan, ikkinchisi oxiridan boshlanadi; ular bir-biriga qarab harakatlanadi.

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

- Vaqt: `O(n)`
- Xotira: `O(1)`

### Suriluvchi oyna (Sliding window)

Takroriy yig'indini hisoblashning oldini olish uchun `k` o'lchamli joriy oynani kuzatib boring. Oynani har safar bir qadamga suring.

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

- Vaqt: `O(n)`
- Xotira: `O(1)`

### Chastotani sanash (Frequency counting)

Har bir elementning uchrash sonini sanash. Anagram tekshiruvlari, takror elementlarni aniqlash va gistogramma masalalari uchun foydali.

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

- Vaqt: `O(n)`
- Xotira: `O(n)`

### Prefiks yig'indilar (Prefix sums)

To'plangan yig'indilarni oldindan hisoblab qo'ying, shunda `O(n)` tayyorgarlikdan keyin oraliq yig'indi so'rovlariga `O(1)` da javob berasiz.

```python
def build_prefix(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
    return prefix


def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]
```

- Tayyorgarlik: `O(n)`
- So'rov: `O(1)`

## Chegaraviy holatlar ro'yxati

- Barcha indeksga asoslangan metodlar uchun chegara tekshiruvlari.
- O'chirish/o'qish uchun bo'sh massiv xatti-harakati.
- Oyna algoritmlari uchun `k > len(nums)` ko'rinishidagi himoya tekshiruvi.
- O'rtaga qayta-qayta qo'shish/o'chirish bajarilish vaqtini egallab olishi mumkin bo'lgan katta hajmli kirishlar.

## Tipik xatolar

- Chegara tekshiruvlarini unutib qo'yish.
- Bog'langan ro'yxat yoki `deque` yaxshiroq bo'lishi mumkin bo'lgan tez ishlaydigan kod yo'llarida o'rtaga qo'shishdan foydalanish.
- Oxiriga qo'shishni amortizatsiyalangan `O(1)` deb emas, balki har doim qat'iy `O(1)` deb taxmin qilish.
