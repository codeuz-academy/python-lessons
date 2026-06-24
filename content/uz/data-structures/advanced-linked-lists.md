---
title: Ilg'or bog'langan ro'yxatlar (Advanced Linked Lists)
description: Ikki tomonlama bog'langan ro'yxatlar, aylanma bog'langan ro'yxatlar va ularning amalga oshirilishi
order: 6
permalink: /uz/data-structures/advanced-linked-lists/
---

Oddiy bir tomonlama bog'langan ro'yxatlar (singly linked list) faqat bitta yo'nalishda aylanib o'tishga imkon beradi va agar oxirgi tugun alohida saqlanmagan bo'lsa, uni topish uchun `O(n)` vaqt talab qiladi. Ilg'or bog'langan ro'yxat variantlari bu muammolarni qo'shimcha havolalar qo'shish yoki tuzilmani o'zgartirish orqali hal qiladi.

## Kitobga moslik (10-bob: Ilg'or bog'langan ro'yxatlar)

Bu bobda quyidagilar ko'rib chiqiladi:
- **Ikki tomonlama bog'langan ro'yxat (Doubly Linked List)**: `prev` va `next` ko'rsatkichlariga ega tugunlar.
- **Aylanma bog'langan ro'yxat (Circular Linked List)**: oxirgi tugun yana bosh tugunga ishora qiladi.

Bu tuzilmalar har ikki uchda `O(1)` amallarni bajarish va orqaga qarab aylanib o'tish imkoniyatini qo'lga kiritish evaziga qo'shimcha xotira (ko'rsatkichlar uchun) sarflaydi va yangilashlarni biroz murakkablashtiradi.

## 1. Ikki tomonlama bog'langan ro'yxat (Doubly Linked List)

Ikki tomonlama bog'langan ro'yxat tuguni uchta maydondan iborat: ma'lumot, `next` tugunga havola va `prev` (oldingi) tugunga havola.

### Nima uchun ikki tomonlama bog'langan ro'yxat ishlatiladi?

- Agar sizda tugunga havola allaqachon bo'lsa, uni `O(1)` da o'chirish mumkin (oldingisini topish uchun boshidan aylanib o'tish shart emas).
- Teskari aylanib o'tish (orqaga qarab iteratsiya qilish mumkin).
- Har ikki uchda `O(1)` amallar (`deque` ni amalga oshirish uchun ideal).

### Tugun tuzilmasi

```python
class DListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

### To'liq amalga oshirilishi

```python
class DoublyLinkedList:
    def __init__(self):
        # Dummy (qo'riqchi) bosh va oxirgi tugunlardan foydalanish chekka holatlarni soddalashtiradi
        self.head = DListNode(None)
        self.tail = DListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, data):
        """Ro'yxat oxiriga O(1) da qo'shish."""
        new_node = DListNode(data)
        last_real_node = self.tail.prev
        
        last_real_node.next = new_node
        new_node.prev = last_real_node
        new_node.next = self.tail
        self.tail.prev = new_node
        
        self.size += 1

    def prepend(self, data):
        """Ro'yxat boshiga O(1) da qo'shish."""
        new_node = DListNode(data)
        first_real_node = self.head.next
        
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_real_node
        first_real_node.prev = new_node
        
        self.size += 1

    def remove_node(self, node):
        """Ma'lum bo'lgan tugunni O(1) da o'chirish."""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
        node.prev = None
        node.next = None
        self.size -= 1

    def __iter__(self):
        """Oldinga qarab aylanib o'tish."""
        current = self.head.next
        while current != self.tail:
            yield current.data
            current = current.next

    def reverse_iter(self):
        """Orqaga qarab aylanib o'tish."""
        current = self.tail.prev
        while current != self.head:
            yield current.data
            current = current.prev
```

> [!TIP]
> Qo'riqchi tugunlar (dummy bosh va oxirgi) element qo'shish yoki o'chirishda har safar `if self.head is None` ni tekshirish zaruriyatini yo'qotadi va algoritmlarni ancha toza qiladi.

## 2. Aylanma bog'langan ro'yxat (Circular Linked List)

Aylanma bir tomonlama bog'langan ro'yxatda oxirgi tugunning `next` ko'rsatkichi `None` o'rniga yana birinchi tugunga ishora qiladi. Aylanma ikki tomonlama bog'langan ro'yxatda esa birinchi tugunning `prev` ko'rsatkichi oxirgi tugunga ishora qiladi.

### Nima uchun aylanma bog'langan ro'yxat ishlatiladi?

- Round-robin rejalashtirish algoritmlari uchun juda mos keladi (masalan, CPU vaqtini taqsimlash, navbatga asoslangan ko'p o'yinchili o'yinlar).
- Butun ro'yxatni istalgan ixtiyoriy tugundan boshlab aylanib o'tish mumkin.
- Har ikki uchni kuzatib turish uchun `tail` ga bitta ko'rsatkichning o'zi yetarli (`tail.next` — bu `head`).

### To'liq amalga oshirilishi (Bir tomonlama aylanma)

```python
class CListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        # Biz faqat oxirgi tugunni kuzatamiz. head — bu shunchaki tail.next
        self.tail = None
        self.size = 0

    def append(self, data):
        """Oxiriga O(1) da qo'shish."""
        new_node = CListNode(data)
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node  # O'ziga ishora qiladi
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node  # Oxirgi tugunni yangi tugunga yangilaymiz
        self.size += 1

    def prepend(self, data):
        """Boshiga O(1) da qo'shish."""
        new_node = CListNode(data)
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            # Bu yerda self.tail ni yangilamaymiz
        self.size += 1

    def __iter__(self):
        if self.tail is None:
            return
        
        current = self.tail.next
        while True:
            yield current.data
            current = current.next
            if current == self.tail.next:
                break
```

## Murakkablik xulosasi

| Amal | Ikki tomonlama | Aylanma (oxirgi tugun ko'rsatkichi) | Sababi |
| --------- | ------------- | ----------------------- | --- |
| Boshiga qo'shish | `O(1)` | `O(1)` | Bosh/oxirgi ko'rsatkichlarni yangilash |
| Oxiriga qo'shish | `O(1)` | `O(1)` | Oxirgi tugun orqali to'g'ridan-to'g'ri kirish |
| Ma'lum tugunni o'chirish | `O(1)` | `O(n)` (bir tomonlama) | Ikki tomonlama `prev` ni to'g'ridan-to'g'ri o'zgartiradi |
| Indeks bo'yicha olish | `O(n)` | `O(n)` | Aylanib o'tish kerak |

## Python standart kutubxonasidagi muqobil

Python `collections.deque` (ikki uchli navbat) bilan birga keladi, u ichki tomondan bloklardan iborat ikki tomonlama bog'langan ro'yxat sifatida amalga oshirilgan. Ishlab chiqarish kodida `O(1)` da oxiriga va boshiga qo'shish kerak bo'lganda har doim shuni birinchi tanlovingiz qiling.

```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)    # Boshiga qo'shish O(1)
d.append(4)        # Oxiriga qo'shish O(1)
```

## Odatiy xatolar

- Ikki tomonlama bog'langan ro'yxatni o'zgartirishda **ikkala ko'rsatkichni ham** (`prev` va `next`) yangilashni unutish, bu esa zanjirning uzilishiga olib keladi.
- Aylanma bog'langan ro'yxatni aylanib o'tishda **cheksiz tsikllar** (qachon to'xtashni bilish uchun har doim qat'iy havola yoki o'lcham hisoblagichini saqlang).
- Ikki tomonlama bog'langan ro'yxatlarda dummy tugunlardan foydalanmaslik va bo'sh ro'yxatlar uchun murakkab `if/else` chekka holatlariga duch kelish.
