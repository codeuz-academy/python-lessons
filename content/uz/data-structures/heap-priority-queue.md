---
title: Heap va Navbat (Priority Queue)
description: Sift operatsiyalari bilan min-heap implementatsiyasi va navbat (priority queue) qo'llanish holatlari
order: 9
permalink: /uz/data-structures/heap-priority-queue/
---

Heap — bu massivda saqlanadigan to'liq ikkilik daraxt (complete binary tree).

- Min-heap: ota tugun qiymati farzand tugunlar qiymatidan kichik yoki teng bo'ladi.
- Max-heap: ota tugun qiymati farzand tugunlar qiymatidan katta yoki teng bo'ladi.

## Kitobga moslik

Navbat (priority queue) ADT'si Necaise kitobining **8-bobida (Queues)** keltirilgan.  
Ushbu sahifa bu materialni heap'ga asoslangan implementatsiya bilan kengaytiradi — bu esa amaliyotda standart yondashuv hisoblanadi.

Navbatlar (priority queue) odatda heap'lar ustiga quriladi.

## Heap invariantlari

- Shakl invarianti: daraxt to'liq (complete) — ya'ni qatma-qat, chapdan o'ngga to'ldiriladi.
- Tartib invarianti (min-heap): ota tugun har doim har bir farzandidan kichik yoki teng.

## Massivga asoslangan heap'da indekslar mosligi

- `parent(i) = (i - 1) // 2`
- `left(i) = 2 * i + 1`
- `right(i) = 2 * i + 2`

## Operatsiyalar

### push(value)

Oxiriga qo'shing, so'ng heap xususiyati buzilgan bo'lsa, yuqoriga ko'tarib (sift up) joylashtiring.

![Heap push]({{ '/img/data-structures/heap-push.png' | url }})

```python
def push(self, value):
    self.data.append(value)
    self._sift_up(len(self.data) - 1)
```

### pop()

Ildizni (root) olib tashlang, oxirgi elementni ildizga ko'chiring, so'ng heap xususiyati tiklanguncha pastga tushiring (sift down).

![Heap pop]({{ '/img/data-structures/heap-pop.png' | url }})

```python
def pop(self):
    if not self.data:
        raise IndexError('pop from empty heap')

    root = self.data[0]
    last = self.data.pop()
    if self.data:
        self.data[0] = last
        self._sift_down(0)
    return root
```

### peek()

Ildiz (root) elementini qaytaradi. Min-heap'da bu eng kichik qiymat bo'ladi.

```python
def peek(self):
    if not self.data:
        raise IndexError('peek from empty heap')
    return self.data[0]
```

## To'liq implementatsiya

```python
class MinHeap:
    def __init__(self):
        self.data = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def push(self, value):
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            raise IndexError('pop from empty heap')

        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return root

    def peek(self):
        if not self.data:
            raise IndexError('peek from empty heap')
        return self.data[0]

    def _sift_up(self, i):
        while i > 0:
            parent = self._parent(i)
            if self.data[parent] <= self.data[i]:
                return
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            i = parent

    def _sift_down(self, i):
        n = len(self.data)
        while True:
            left = self._left(i)
            right = self._right(i)
            smallest = i

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest == i:
                return

            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest
```

## Heap'ni chiziqli vaqtda qurish

Agar sizda allaqachon massiv bo'lsa, pastdan yuqoriga (bottom-up) heapify usuli heap'ni `O(n)` vaqtda quradi.

```python
def heapify(nums):
    h = MinHeap()
    h.data = nums[:]  # nusxa olish

    start = (len(h.data) // 2) - 1
    for i in range(start, -1, -1):
        h._sift_down(i)
    return h
```

## Navbat (priority queue) namunasi

`(priority, payload)` ko'rinishidagi `tuple`'lardan foydalaning — shunda eng kichik prioritetli element birinchi bo'lib olinadi.

```python
h = MinHeap()
h.push((2, "email"))
h.push((1, "payment"))
print(h.pop())  # (1, "payment")
```

Prioritetlar teng bo'lganda, agar barqaror tartib muhim bo'lsa, tenglikni hal qiluvchi (tie-breaker) hisoblagich qo'shing.

## Murakkablik xulosasi

| Operatsiya | Vaqt |
| --------- | ---- |
| Push | `O(log n)` |
| Pop | `O(log n)` |
| Peek | `O(1)` |
| Heap qurish | `O(n)` |

## Odatiy qo'llanishlari

- Dijkstra eng qisqa yo'l algoritmi.
- Prioritet yoki muddat (deadline) bo'yicha rejalashtirish.
- Oqimlar (stream) ustida top-k masalalari.

## Odatiy xatolar

- Heap massivi to'liq tartiblangan deb o'ylash (aslida unday emas).
- `pop`/`peek` dan oldin heap bo'shligini tekshirishni unutish.
- Tez-tez ixtiyoriy o'chirishlar kerak bo'lganda heap'dan foydalanish.
