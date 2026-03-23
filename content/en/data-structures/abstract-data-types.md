---
title: Abstract Data Types (ADTs)
description: Contracts, invariants, and multiple implementations inspired by Chapter 1
order: 1
permalink: /en/data-structures/abstract-data-types/
---

This chapter follows the core ideas from **Chapter 1 (Abstract Data Types)** in the Necaise book: define behavior first, then implement it.

![ADT contract diagram]({{ '/img/data-structures/adt-contract.svg' | url }})

## What an ADT gives you

An ADT is a **contract**:

- It defines *what operations exist* and *what they do*.
- It hides *how data is stored internally*.
- It lets you swap implementations without changing client code.

This separation is the main reason ADTs scale in larger projects.

## Core contract pieces

Every operation should be specified with:

- **Preconditions**: what must be true before the call.
- **Postconditions**: what must be true after the call.
- **Representation invariants**: properties that are always true for internal state.

Example for `pop()` on a stack:

- Precondition: stack is not empty.
- Postcondition: top element is removed and returned.
- Invariant still holds: stack order remains LIFO.

## Preconditions and assertions

When learning data structures, assertions are useful for making contracts explicit.

```python
class Stack:
    def __init__(self):
        self._items = []

    def pop(self):
        assert len(self._items) > 0, "precondition failed: stack must be non-empty"
        return self._items.pop()
```

In production systems, you usually raise specific exceptions for invalid operations.

## Multiple implementations, same ADT

A queue ADT can have different implementations:

- `list` based
- `deque` based
- linked-list based

As long as each implementation preserves queue semantics (FIFO), user-facing code stays the same.

```python
def process_jobs(queue):
    while not queue.is_empty():
        job = queue.dequeue()
        handle(job)
```

`process_jobs` should not care about internal storage layout.

## Why this matters before coding structures

If you define the ADT contract first, then implementation work in later chapters is easier:

- Arrays/vectors become one possible implementation choice.
- Linked structures become another.
- Performance tuning does not force API rewrites.

This is the foundation for the rest of the data structures section.
