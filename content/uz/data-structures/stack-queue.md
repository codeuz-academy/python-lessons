---
title: Stack va Queue
description: LIFO stack va FIFO queue'ni amalga oshirish hamda keng tarqalgan andozalar
order: 6
permalink: /uz/data-structures/stack-queue/
---

Stack va queue cheklangan kirishli ma'lumotlar tuzilmalaridir.

- Stack: LIFO (oxirgi kirgan birinchi chiqadi — last in, first out)
- Queue: FIFO (birinchi kirgan birinchi chiqadi — first in, first out)

## Kitobga moslik (8 va 9-boblar)

Necaise ketma-ketligi quyidagilarni keltiradi:

- queue ADT va circular-array/bog'langan ro'yxat yordamida amalga oshirish
- priority queue variantlari (chegaralangan va chegarasiz prioritetlar)
- stack ADT va klassik stack qo'llanilishlari

Kitobdan foydali farqlash:

- queue tartibi kelish vaqtiga asoslanadi (FIFO)
- priority queue tartibi prioritetga asoslanadi (teng prioritetlarda FIFO saqlanadi)
- stack'ga kirish doim bir uchidan amalga oshiriladi (LIFO)

## To'g'ri Python konteynerini tanlash

- Stack: oddiy `list` samarali (oxiridan `append`/`pop` `O(1)`).
- Queue: ishlab chiqarish (production) uchun `collections.deque`'ni afzal ko'ring.
- Bog'langan ro'yxat asosidagi queue ko'rsatkichlar (pointer) mexanikasini tushunish uchun foydali.

## Stack amallari

### push(value)

Tepaga qo'shadi. Python ro'yxati bilan bu oxiriga `append` qilishdir.

![Stack push amali]({{ '/img/data-structures/stack-push.png' | url }})

```python
def push(self, value):
    self.items.append(value)
```

### pop()

Tepadagi elementni olib tashlaydi va qaytaradi. Bu push'ning teskarisidir.

![Stack pop amali]({{ '/img/data-structures/stack-pop.png' | url }})

```python
def pop(self):
    if not self.items:
        raise IndexError('pop from empty stack')
    return self.items.pop()
```

### peek()

Tepadagi qiymatni olib tashlamasdan o'qiydi.

```python
def peek(self):
    if not self.items:
        raise IndexError('peek from empty stack')
    return self.items[-1]
```

## Queue amallari

### enqueue(value)

Orqaga qo'shadi. Bog'langan ro'yxat asosidagi queue buni doimiy vaqtda bajaradi.

![Queue enqueue amali]({{ '/img/data-structures/queue-enqueue.png' | url }})

```python
def enqueue(self, value):
    node = Node(value)
    if self.rear is None:
        self.front = self.rear = node
    else:
        self.rear.next = node
        self.rear = node
    self.size += 1
```

### dequeue()

Old qismdan olib tashlaydi va qaytaradi. Agar queue bo'shab qolsa, `front` va `rear`'ni qayta tiklang.

![Queue dequeue amali]({{ '/img/data-structures/queue-dequeue.png' | url }})

```python
def dequeue(self):
    if self.front is None:
        raise IndexError('dequeue from empty queue')

    value = self.front.value
    self.front = self.front.next
    if self.front is None:
        self.rear = None
    self.size -= 1
    return value
```

### peek()

Old qismdagi qiymatni olib tashlamasdan o'qiydi.

```python
def peek(self):
    if self.front is None:
        raise IndexError('peek from empty queue')
    return self.front.value
```

## To'liq amalga oshirish

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            raise IndexError('pop from empty stack')
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError('peek from empty stack')
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            raise IndexError('dequeue from empty queue')

        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return value

    def peek(self):
        if self.front is None:
            raise IndexError('peek from empty queue')
        return self.front.value

    def is_empty(self):
        return self.front is None
```

## Real loyihalarda deque asosidagi queue

```python
from collections import deque

q = deque()
q.append(10)      # enqueue
q.append(20)
print(q.popleft())  # dequeue -> 10
```

Production kodida ham tezlik, ham soddalik kerak bo'lganda `deque`'dan foydalaning.

## Murakkablik xulosasi

| Amal | Stack | Queue |
| --------- | ----- | ----- |
| Qo'shish | `O(1)` push | `O(1)` enqueue |
| Olib tashlash | `O(1)` pop | `O(1)` dequeue |
| Peek | `O(1)` | `O(1)` |

## Tipik qo'llanilishlar

- Stack: ifodalarni tahlil qilish, undo/redo, chuqurlik bo'yicha (depth-first) o'tish.
- Queue: kenglik bo'yicha (breadth-first) o'tish, vazifalarni rejalashtirish, tezligi cheklangan ishlov berish.

## Andoza misoli: stack yordamida qavslarning to'g'riligini tekshirish

```python
def is_valid_parentheses(text):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for ch in text:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0
```

## Tipik xatolar

- Queue'dan dequeue uchun `list.pop(0)`'dan foydalanish (bu `O(n)`).
- `pop` yoki `peek`'dan oldin bo'shliqni tekshirishni unutish.
- Bir algoritmda queue/stack semantikasini aralashtirib yuborish.
