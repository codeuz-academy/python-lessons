---
title: Bog'langan ro'yxat (Linked List)
description: Singly linked list'ning prepend, append, delete va reverse amallari bilan amalga oshirilishi
order: 5
permalink: /uz/data-structures/linked-list/
---

Bog'langan ro'yxat (linked list) qiymatlarni tugun'larda (node) saqlaydi va har bir tugun keyingi tugunga ishora qiladi. Massivlardan farqli o'laroq, tugunlar uchun ketma-ket joylashgan (contiguous) xotira talab qilinmaydi.

## Kitobga moslik (7-bob: Bog'langan tuzilmalar)

Bu sahifa bobning tuzilishiga amal qiladi:

- obyektlar/ishoralar (references) va singly linked tuzilishi
- prepend/remove amallari
- iterator asosida o'tib chiqish (traversal)
- `append` uchun tail ishorasi orqali optimallashtirish
- tartiblangan bog'langan ro'yxat xatti-harakati (qidirish/o'chirish vaqtida erta to'xtash)

Bobdan olinadigan muhim xulosa: o'tib chiqish va qidirish chiziqli (linear), lekin lokal tuzilma o'zgarishlari uchun ishoralarni qayta ulash arzon.

## Bog'langan ro'yxatlardan qachon foydalanish kerak

- Boshiga (head) yaqin joyga tez-tez qo'shasiz yoki o'chirasiz.
- Bashorat qilinadigan `O(1)` prepend amalini xohlaysiz.
- Tasodifiy kirish (random access) tezligini o'zgartirish moslashuvchanligi evaziga almashtira olasiz.
- Tuzilmani o'zgartirish vaqtida barqaror tugun ishoralari kerak.

## Bog'langan ro'yxatlardan qachon foydalanmaslik kerak

- Indeks bo'yicha tez tasodifiy kirish kerak.
- Qiymat bo'yicha ko'p a'zolik (membership) tekshiruvlarini bajarasiz (har biri `O(n)`).
- Har bir element uchun xotira sarfi (overhead) o'zgartirish moslashuvchanligidan ko'ra muhimroq.

## Tugun modeli

Har bir tugun quyidagilarga ega:

- `value`: foydali ma'lumot (payload).
- `next`: keyingi tugunga ishora.

Saqlanishi kerak bo'lgan o'zgarmaslar (invariants):

- Agar ro'yxat bo'sh bo'lsa, `head` ham, `tail` ham `None` bo'ladi.
- Agar ro'yxat bo'sh bo'lmasa, `tail.next` har doim `None` bo'ladi.
- `size` har doim tugunlarning haqiqiy soniga mos keladi.

## Amallar

### prepend(value)

Yangi tugun yarating, uni joriy head'ga yo'naltiring, so'ngra `head`'ni shu yangi tugunga ko'chiring.

![Linked list prepend]({{ '/img/data-structures/linked-list-prepend.png' | url }})

```python
def prepend(self, value):
    node = Node(value, self.head)
    self.head = node
    if self.tail is None:
        self.tail = node
    self.size += 1
```

### append(value)

`tail` ishorasi mavjud bo'lganda, append amali to'g'ridan-to'g'ri bajariladi: `tail.next`'ni yangi tugunga ulang, so'ngra `tail`'ni ko'chiring.

![Linked list append]({{ '/img/data-structures/linked-list-append.png' | url }})

```python
def append(self, value):
    node = Node(value)
    if self.tail is None:
        self.head = self.tail = node
    else:
        self.tail.next = node
        self.tail = node
    self.size += 1
```

### find(value)

`head`'dan boshlab, mos kelish topilguncha yoki ro'yxat tugaguncha tugunma-tugun yurib chiqing.

![Linked list find]({{ '/img/data-structures/linked-list-find.png' | url }})

```python
def find(self, value):
    index = 0
    current = self.head
    while current is not None:
        if current.value == value:
            return index
        current = current.next
        index += 1
    return -1
```

### delete(value)

`previous` va `current`'ni kuzatib boring. `current.value` mos kelganda, `previous.next = current.next` qilib `current`'ni o'tkazib yuboring.

![Linked list delete]({{ '/img/data-structures/linked-list-delete.png' | url }})

```python
def delete(self, value):
    previous = None
    current = self.head

    while current is not None:
        if current.value == value:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next

            if current is self.tail:
                self.tail = previous

            self.size -= 1
            return True

        previous = current
        current = current.next

    return False
```

### reverse()

Tugunlar bo'ylab bir marta yuring va har bir `next` ishorasini oldingi tugunga teskari qilib qo'ying.

![Linked list reverse]({{ '/img/data-structures/linked-list-reverse.png' | url }})

```python
def reverse(self):
    previous = None
    current = self.head
    self.tail = self.head

    while current is not None:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt

    self.head = previous
```

## To'liq amalga oshirilishi

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, value):
        node = Node(value, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def find(self, value):
        index = 0
        current = self.head
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def delete(self, value):
        previous = None
        current = self.head

        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                if current is self.tail:
                    self.tail = previous

                self.size -= 1
                return True

            previous = current
            current = current.next

        return False

    def reverse(self):
        previous = None
        current = self.head
        self.tail = self.head

        while current is not None:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        self.head = previous

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result
```

## Murakkablik xulosasi

| Amal | Vaqt | Sababi |
| --------- | ---- | --- |
| Prepend | `O(1)` | Head ishorasini yangilash |
| Append (tail ishorasi bilan) | `O(1)` | Tail ishorasini yangilash |
| Find | `O(n)` | Ketma-ket o'tib chiqish |
| Qiymat bo'yicha o'chirish | `O(n)` | Qidirish + qayta ulash |
| Reverse | `O(n)` | Tugunlar bo'ylab bir marta o'tish |

## Sikl aniqlash (Floyd algoritmi)

Ikki ishora turli tezlikda harakatlanadi. Agar sikl mavjud bo'lsa, tez ishora sekin ishora bilan uchrashadi.

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False
```

- Vaqt: `O(n)`
- Xotira: `O(1)`

## Amaliy eslatmalar

- Ikki tomonlama bog'langan ro'yxat (doubly linked list) o'rtadan o'chirishni osonlashtirish uchun `prev` ishorasini qo'shadi.
- Sentinel (soxta) head/tail tugunlari maxsus holatlar uchun shartlanishni kamaytirishi mumkin.
- Navbat/stek (queue/stack) xatti-harakati uchun odatda Python'ning `collections.deque`'i afzalroq.

## Tipik xatolar

- Oxirgi tugunni o'chirayotganda `tail`'ni yangilashni unutish.
- Bo'sh ro'yxat va bitta tugunli ro'yxatni maxsus holatlar sifatida hisobga olmaslik.
- Bog'langan ro'yxat massivlar kabi tez indeks bo'yicha kirishni qo'llab-quvvatlaydi deb o'ylash.
