---
title: Linked List
description: Singly linked list implementation with prepend, append, delete, and reverse
order: 5
permalink: /en/data-structures/linked-list/
---

A linked list stores values in nodes, and each node points to the next node. Unlike arrays, nodes do not need contiguous memory.

## Book alignment (Chapter 7: Linked Structures)

This page follows the chapter flow:

- objects/references and singly linked layout
- prepend/remove operations
- iterator-based traversal
- tail reference optimization for `append`
- sorted linked-list behavior (early stop during search/delete)

One important chapter takeaway: traversal and search are linear, but pointer rewiring for local structural updates is cheap.

## When to use linked lists

- You insert or delete near the head frequently.
- You want predictable `O(1)` prepend.
- You can trade random access speed for update flexibility.
- You need stable node references while changing structure.

## When not to use linked lists

- You need fast random index access.
- You do many membership checks by value (`O(n)` each).
- Memory overhead per element matters more than update flexibility.

## Node model

Each node has:

- `value`: payload data.
- `next`: pointer to the next node.

Invariants to maintain:

- If list is empty, both `head` and `tail` are `None`.
- If list is non-empty, `tail.next` is always `None`.
- `size` always matches actual node count.

## Operations

### prepend(value)

Create a new node, point it to the current head, then move `head` to this new node.

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

With a `tail` pointer, append is direct: link `tail.next` to the new node, then move `tail`.

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

Start from `head` and walk node by node until a match is found or the list ends.

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

Track `previous` and `current`. When `current.value` matches, skip `current` by setting `previous.next = current.next`.

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

Move through nodes once and flip each `next` pointer to the previous node.

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

## Full implementation

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

## Complexity summary

| Operation | Time | Why |
| --------- | ---- | --- |
| Prepend | `O(1)` | Head pointer update |
| Append (with tail pointer) | `O(1)` | Tail pointer update |
| Find | `O(n)` | Sequential traversal |
| Delete by value | `O(n)` | Search + relink |
| Reverse | `O(n)` | One pass through nodes |

## Cycle detection (Floyd's algorithm)

Two pointers move at different speeds. If a cycle exists, the fast pointer will meet the slow pointer.

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

- Time: `O(n)`
- Space: `O(1)`

## Practical notes

- A doubly linked list adds `prev` pointer to make delete from middle easier.
- Sentinel (dummy) head/tail nodes can reduce special-case branching.
- Python's `collections.deque` is usually preferable for queue/stack behavior.

## Typical mistakes

- Forgetting to update `tail` when deleting the last node.
- Not handling empty list and single-node list as special states.
- Assuming linked list supports fast index access like arrays.
