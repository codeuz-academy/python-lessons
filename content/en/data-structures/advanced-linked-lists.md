---
title: Advanced Linked Lists
description: Doubly linked lists, circular linked lists, and their implementations
order: 7
permalink: /en/data-structures/advanced-linked-lists/
---

Basic singly linked lists only allow traversal in one direction and require `O(n)` time to find the tail if it isn't tracked. Advanced linked list variations solve these problems by adding more references or modifying the structure.

## Book alignment (Chapter 10: Advanced Linked Lists)

This chapter covers:
- **Doubly Linked List**: nodes with `prev` and `next` pointers.
- **Circular Linked List**: tail points back to the head.

These structures trade extra memory (for pointers) and slightly more complex updates for `O(1)` operations at both ends and the ability to traverse backward.

## 1. Doubly Linked List

A doubly linked list node contains three fields: data, a reference to the `next` node, and a reference to the `prev` (previous) node.

### Why use a doubly linked list?

- `O(1)` deletion of a node if you already have a reference to it (no need to traverse from the head to find its predecessor).
- Reversible traversal (can iterate backwards).
- `O(1)` operations at both ends (ideal for implementing a `deque`).

### Node structure

```python
class DListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

### Full implementation

```python
class DoublyLinkedList:
    def __init__(self):
        # Using dummy (sentinel) head and tail nodes simplifies edge cases
        self.head = DListNode(None)
        self.tail = DListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, data):
        """Append to the end of the list in O(1)."""
        new_node = DListNode(data)
        last_real_node = self.tail.prev
        
        last_real_node.next = new_node
        new_node.prev = last_real_node
        new_node.next = self.tail
        self.tail.prev = new_node
        
        self.size += 1

    def prepend(self, data):
        """Add to the front of the list in O(1)."""
        new_node = DListNode(data)
        first_real_node = self.head.next
        
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_real_node
        first_real_node.prev = new_node
        
        self.size += 1

    def remove_node(self, node):
        """Remove a known node in O(1)."""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
        node.prev = None
        node.next = None
        self.size -= 1

    def __iter__(self):
        """Traverse forward."""
        current = self.head.next
        while current != self.tail:
            yield current.data
            current = current.next

    def reverse_iter(self):
        """Traverse backward."""
        current = self.tail.prev
        while current != self.head:
            yield current.data
            current = current.prev
```

> [!TIP]
> Sentinel nodes (dummy head and tail) eliminate the need to constantly check `if self.head is None` when adding or removing elements, making algorithms much cleaner.

## 2. Circular Linked List

In a circular singly linked list, the `next` pointer of the last node points back to the first node instead of `None`. In a circular doubly linked list, the `prev` pointer of the first node points to the last node.

### Why use a circular linked list?

- Perfect for round-robin scheduling algorithms (e.g., CPU time sharing, multiplayer turn-based games).
- You can traverse the entire list starting from any arbitrary node.
- A single pointer to the `tail` is enough to track both ends (`tail.next` is the `head`).

### Full implementation (Singly Circular)

```python
class CListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        # We only keep track of the tail. head is simply tail.next
        self.tail = None
        self.size = 0

    def append(self, data):
        """Add to the end in O(1)."""
        new_node = CListNode(data)
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node  # Points to itself
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node  # Update tail to the new node
        self.size += 1

    def prepend(self, data):
        """Add to the front in O(1)."""
        new_node = CListNode(data)
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            # We don't update self.tail here
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

## Complexity summary

| Operation | Doubly Linked | Circular (tail pointer) | Why |
| --------- | ------------- | ----------------------- | --- |
| Prepend | `O(1)` | `O(1)` | Update head/tail pointers |
| Append | `O(1)` | `O(1)` | Direct access via tail |
| Remove known node| `O(1)` | `O(n)` (singly) | Doubly linked modifies `prev` directly |
| Get by index | `O(n)` | `O(n)` | Must traverse |

## Python standard library alternative

Python ships with `collections.deque` (double-ended queue), which is internally implemented as a doubly linked list of blocks. It should be your go-to whenever you need `O(1)` appends and prepends in production code.

```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)    # Prepend O(1)
d.append(4)        # Append O(1)
```

## Typical mistakes

- **Forgetting to update both pointers** (`prev` and `next`) when modifying a doubly linked list, leading to broken chains.
- **Infinite loops** during traversal of a circular linked list (always keep a fixed reference or size counter to know when to stop).
- Not using dummy nodes in doubly linked lists and ending up with complex edge case `if/else` statements for empty lists.
