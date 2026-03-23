---
title: Stack & Queue
description: LIFO stack and FIFO queue implementations with common patterns
order: 6
permalink: /en/data-structures/stack-queue/
---

Stack and queue are restricted-access data structures.

- Stack: LIFO (last in, first out)
- Queue: FIFO (first in, first out)

## Book alignment (Chapters 8 and 9)

The Necaise sequence presents:

- queue ADT and circular-array/linked implementations
- priority queue variants (bounded and unbounded priorities)
- stack ADT and classic stack applications

Useful distinction from the book:

- queue order is arrival-based (FIFO)
- priority queue order is priority-based (ties remain FIFO)
- stack access is always from one end (LIFO)

## Choosing the right Python container

- Stack: plain `list` is efficient (`append`/`pop` from end are `O(1)`).
- Queue: prefer `collections.deque` for production queues.
- Linked-list queue implementation is useful for understanding pointer mechanics.

## Stack operations

### push(value)

Insert at the top. With a Python list, this is append at the end.

![Stack push operation]({{ '/img/data-structures/stack-push.png' | url }})

```python
def push(self, value):
    self.items.append(value)
```

### pop()

Remove and return the top element. This is the inverse of push.

![Stack pop operation]({{ '/img/data-structures/stack-pop.png' | url }})

```python
def pop(self):
    if not self.items:
        raise IndexError('pop from empty stack')
    return self.items.pop()
```

### peek()

Read the top value without removing it.

```python
def peek(self):
    if not self.items:
        raise IndexError('peek from empty stack')
    return self.items[-1]
```

## Queue operations

### enqueue(value)

Insert at the rear. Linked-list queue keeps this in constant time.

![Queue enqueue operation]({{ '/img/data-structures/queue-enqueue.png' | url }})

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

Remove and return from the front. If the queue becomes empty, reset both `front` and `rear`.

![Queue dequeue operation]({{ '/img/data-structures/queue-dequeue.png' | url }})

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

Read the front value without removing it.

```python
def peek(self):
    if self.front is None:
        raise IndexError('peek from empty queue')
    return self.front.value
```

## Full implementation

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

## Deque-based queue in real projects

```python
from collections import deque

q = deque()
q.append(10)      # enqueue
q.append(20)
print(q.popleft())  # dequeue -> 10
```

Use `deque` when you need both speed and simplicity in production code.

## Complexity summary

| Operation | Stack | Queue |
| --------- | ----- | ----- |
| Insert | `O(1)` push | `O(1)` enqueue |
| Remove | `O(1)` pop | `O(1)` dequeue |
| Peek | `O(1)` | `O(1)` |

## Typical uses

- Stack: expression parsing, undo/redo, depth-first traversal.
- Queue: breadth-first traversal, task scheduling, rate-limited processing.

## Pattern example: valid parentheses using stack

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

## Typical mistakes

- Using `list.pop(0)` for queue dequeue (this is `O(n)`).
- Forgetting empty checks before `pop` or `peek`.
- Mixing queue/stack semantics in the same algorithm.
