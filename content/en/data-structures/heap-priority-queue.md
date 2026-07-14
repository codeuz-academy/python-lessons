---
title: Heap & Priority Queue
description: Min-heap implementation with sift operations and priority queue use cases
order: 10
permalink: /en/data-structures/heap-priority-queue/
---

A heap is a complete binary tree stored in an array.

- Min-heap: parent value is less than or equal to child values.
- Max-heap: parent value is greater than or equal to child values.

## Book alignment

The priority-queue ADT appears in **Chapter 8 (Queues)** in the Necaise book.  
This page extends that material with a heap-based implementation, which is the standard production strategy.

Priority queues are usually built on top of heaps.

## Heap invariants

- Shape invariant: tree is complete (filled level by level, left to right).
- Order invariant (min-heap): parent is always less than or equal to each child.

## Index mapping in array-based heap

- `parent(i) = (i - 1) // 2`
- `left(i) = 2 * i + 1`
- `right(i) = 2 * i + 2`

## Operations

### push(value)

Append to the end, then sift up while heap property is violated.

![Heap push]({{ '/img/data-structures/heap-push.png' | url }})

```python
def push(self, value):
    self.data.append(value)
    self._sift_up(len(self.data) - 1)
```

### pop()

Remove root, move last element to root, then sift down until heap property is restored.

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

Return the root element. In min-heap this is the smallest value.

```python
def peek(self):
    if not self.data:
        raise IndexError('peek from empty heap')
    return self.data[0]
```

## Full implementation

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

## Build heap in linear time

If you already have an array, bottom-up heapify builds a heap in `O(n)`.

```python
def heapify(nums):
    h = MinHeap()
    h.data = nums[:]  # copy

    start = (len(h.data) // 2) - 1
    for i in range(start, -1, -1):
        h._sift_down(i)
    return h
```

## Priority queue pattern

Use tuples `(priority, payload)` so the smallest priority is popped first.

```python
h = MinHeap()
h.push((2, "email"))
h.push((1, "payment"))
print(h.pop())  # (1, "payment")
```

For equal priorities, include a tie-breaker counter if stable ordering matters.

## Complexity summary

| Operation | Time |
| --------- | ---- |
| Push | `O(log n)` |
| Pop | `O(log n)` |
| Peek | `O(1)` |
| Build heap | `O(n)` |

## Typical uses

- Dijkstra shortest path.
- Scheduling by priority or deadline.
- Top-k problems on streams.

## Typical mistakes

- Assuming heap array is globally sorted (it is not).
- Forgetting empty-heap checks before `pop`/`peek`.
- Using heap when frequent arbitrary deletions are required.
