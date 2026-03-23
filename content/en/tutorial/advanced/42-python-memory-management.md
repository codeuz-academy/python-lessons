---
layout: tutorial.njk
lang: en
title: Python Memory Management
description: "Learn Python Memory Management in Python with practical examples and clear explanations."
order: 42
permalink: /en/tutorial/python-memory-management/
---

<img src="/img/tutorial/42-python-memory-management.webp" alt="Python Memory Management" class="w-full rounded-lg shadow-md mb-6" loading="lazy">

One of the reasons Python is so popular is because developers don't have to worry about manual memory management like in C or C++. Python handles memory allocation and deallocation automatically.

However, understanding how Python manages memory behind the scenes is crucial for writing efficient code, especially when dealing with large amounts of data.

### 1. Heap and Stack

Python uses two types of memory:
- **Stack Memory**: Used for static function execution and local variables.
- **Heap Memory**: All Python objects and instances (like integers, lists, classes) are stored here. This is private and managed by the Python Memory Manager.

### 2. Reference Counting

Python's main strategy in memory management is **Reference Counting**.

Every object in Python has a "reference count". This number indicates how many variables refer to that object.

- When an object is created or referenced (`a = object`), the count increases (+1).
- When a reference is deleted (`del a`) or goes out of scope, the count decreases (-1).
- When the count reaches 0, the object's memory is immediately freed.

```python
import sys

a = []
# Get ref count(usually higher than expected because the argument to sys.getrefcount itself is also a temporary reference)
print(sys.getrefcount(a)) 

b = a
print(sys.getrefcount(a)) # Increases

del b
print(sys.getrefcount(a)) # Decreases
```

### 3. Garbage Collection (GC)

Reference counting has one fatal flaw: **Circular References**.

```python
a = []
b = []
a.append(b)
b.append(a) # Circular reference
```

If `a` and `b` are deleted, their reference count will never be 0 because they point to each other. This is where **Garbage Collector (GC)** comes in.

Python's GC is a separate mechanism that runs periodically to detect and clean up this "garbage" circular references.

You can manually control GC using the `gc` module:

```python
import gc

# Force run garbage collection
gc.collect()

# Disable automatic garbage collection
gc.disable()
```
*Tip: You rarely need to touch the `gc` module except for high-level optimization.*

### 4. Tips for Saving Memory

1. **Use Generators**: As discussed in the previous tutorial, generators do not load all data into RAM.
2. **Use `__slots__` in Classes**: If you create millions of instances of small classes, `__slots__` can save RAM significantly by disabling the dynamic `__dict__` per instance.

```python
class SaveMemory:
    __slots__ = ['name', 'age'] # Can only have these attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

3. **Be careful with Global Variables**: Global objects will never be deleted until the program stops, unless deleted manually.

### Conclusion
- Python uses **Reference Counting** as the main method.
- **Garbage Collector** is in charge of cleaning up circular references.
- You can write "memory-efficient" Python code by understanding how it works.
