---
title: Trees (BST)
description: Binary search tree with insert, search, and traversal implementations
order: 8
permalink: /en/data-structures/trees/
---

A Binary Search Tree (BST) keeps values ordered:

- Left subtree values are smaller than node value.
- Right subtree values are larger than node value.

## Book alignment (Chapters 14 and 15)

This page combines the two tree chapters in the book:

- binary-tree structure and traversals
- search-tree ordering rules and dictionary-style operations

Main idea: tree structure gives ordered operations, but runtime quality depends on tree shape (balanced vs skewed).

## Why BST is useful

BST combines search and ordered data operations in one structure:

- Membership check (`contains`).
- Ordered traversal (`inorder`).
- Range-like logic using tree shape.

## Operations

### insert(key)

Start at root. Move left for smaller key, right for larger key, until an empty child is found.

![BST insert]({{ '/img/data-structures/bst-insert.png' | url }})

```python
def insert(self, key):
    self.root = self._insert(self.root, key)


def _insert(self, node, key):
    if node is None:
        return BSTNode(key)
    if key < node.key:
        node.left = self._insert(node.left, key)
    elif key > node.key:
        node.right = self._insert(node.right, key)
    return node
```

### contains(key)

At each node, compare key and follow exactly one branch. This is why search is fast on balanced trees.

![BST search]({{ '/img/data-structures/bst-search.png' | url }})

```python
def contains(self, key):
    current = self.root
    while current is not None:
        if key == current.key:
            return True
        current = current.left if key < current.key else current.right
    return False
```

### delete(key)

Delete has three structural cases:

1. Node has no children: remove directly.
2. Node has one child: promote that child.
3. Node has two children: replace with inorder successor, then delete successor.

![BST delete]({{ '/img/data-structures/bst-delete.png' | url }})

```python
def delete(self, key):
    self.root = self._delete(self.root, key)


def _delete(self, node, key):
    if node is None:
        return None

    if key < node.key:
        node.left = self._delete(node.left, key)
        return node
    if key > node.key:
        node.right = self._delete(node.right, key)
        return node

    if node.left is None:
        return node.right
    if node.right is None:
        return node.left

    successor = self._min_node(node.right)
    node.key = successor.key
    node.right = self._delete(node.right, successor.key)
    return node
```

### inorder() traversal

Visit left subtree, then node, then right subtree. For BST, output is sorted.

```python
def inorder(self):
    result = []

    def visit(node):
        if node is None:
            return
        visit(node.left)
        result.append(node.key)
        visit(node.right)

    visit(self.root)
    return result
```

## Full implementation

```python
class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def contains(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            current = current.left if key < current.key else current.right
        return False

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
            return node
        if key > node.key:
            node.right = self._delete(node.right, key)
            return node

        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        successor = self._min_node(node.right)
        node.key = successor.key
        node.right = self._delete(node.right, successor.key)
        return node

    def _min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            result.append(node.key)
            visit(node.right)

        visit(self.root)
        return result
```

## Other traversals

```python
def preorder(node, out):
    if node is None:
        return
    out.append(node.key)
    preorder(node.left, out)
    preorder(node.right, out)


def postorder(node, out):
    if node is None:
        return
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.key)
```

- Preorder is common for serialization and cloning.
- Postorder is common when children must be processed before parent.

## Complexity summary

| Operation | Average | Worst case |
| --------- | ------- | ---------- |
| Insert | `O(log n)` | `O(n)` |
| Search | `O(log n)` | `O(n)` |
| Delete | `O(log n)` | `O(n)` |
| Traversal | `O(n)` | `O(n)` |

Worst case appears when the tree becomes skewed. Balanced trees (AVL, Red-Black) keep height near `log n`.

## Practical notes

- BST is excellent for ordered data operations.
- If insertion order is nearly sorted, use a self-balancing tree.
- For only min/max priority operations, heap is simpler and usually faster.
- `inorder()` is the easiest way to export BST values in sorted order.

## Typical mistakes

- Ignoring the duplicate-key policy (reject, count, or replace should be explicit).
- Forgetting the two-child delete case.
- Assuming `O(log n)` without considering tree shape.
