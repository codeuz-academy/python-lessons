---
title: Daraxtlar (BST)
description: Qo'shish, qidirish va aylanib chiqish (traversal) amallari bilan binary search tree
order: 8
permalink: /uz/data-structures/trees/
---

Binary Search Tree (BST) qiymatlarni tartiblangan holatda saqlaydi:

- Chap qism daraxt (subtree) qiymatlari tugun (node) qiymatidan kichik bo'ladi.
- O'ng qism daraxt qiymatlari tugun qiymatidan katta bo'ladi.

## Kitobga moslik (14 va 15-boblar)

Bu sahifa kitobdagi daraxtlarga oid ikki bobni birlashtiradi:

- binary daraxt tuzilishi va aylanib chiqishlar (traversal'lar)
- search-tree tartiblash qoidalari va lug'at (`dictionary`) uslubidagi amallar

Asosiy g'oya: daraxt tuzilishi tartiblangan amallarni beradi, lekin bajarilish vaqti (`runtime`) sifati daraxt shakliga (muvozanatli yoki qiyshiq) bog'liq.

## Nega BST foydali

BST qidirish va tartiblangan ma'lumotlar bilan ishlash amallarini bitta tuzilmada birlashtiradi:

- A'zolik (`membership`) tekshiruvi (`contains`).
- Tartiblangan aylanib chiqish (`inorder`).
- Daraxt shakli yordamida oraliq (range) bo'yicha mantiq.

## Amallar

### insert(key)

Ildizdan (root) boshlanadi. Kichikroq kalit (`key`) uchun chapga, kattaroq kalit uchun o'ngga harakatlanadi — to bo'sh bola tugun topilguncha.

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

Har bir tugunda kalitni solishtirib, aniq bitta shoxni kuzatib boriladi. Aynan shu sababli muvozanatli daraxtlarda qidirish tez bo'ladi.

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

O'chirishda uchta tuzilmaviy holat bor:

1. Tugunning bolasi yo'q: to'g'ridan-to'g'ri o'chiriladi.
2. Tugunning bitta bolasi bor: o'sha bolani yuqoriga ko'taradi.
3. Tugunning ikkita bolasi bor: uni inorder vorisi (successor) bilan almashtiradi, so'ngra vorisni o'chiradi.

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

### inorder() aylanib chiqishi

Avval chap qism daraxt, keyin tugunning o'zi, so'ngra o'ng qism daraxt tashrif buyuriladi. BST uchun natija tartiblangan bo'ladi.

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

## To'liq amalga oshirilishi

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

## Boshqa aylanib chiqishlar

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

- Preorder ko'pincha serializatsiya va nusxalashda ishlatiladi.
- Postorder esa bolalar ota tugundan oldin qayta ishlanishi kerak bo'lganda ishlatiladi.

## Murakkablik xulosasi

| Amal | O'rtacha | Eng yomon holat |
| --------- | ------- | ---------- |
| Qo'shish | `O(log n)` | `O(n)` |
| Qidirish | `O(log n)` | `O(n)` |
| O'chirish | `O(log n)` | `O(n)` |
| Aylanib chiqish | `O(n)` | `O(n)` |

Eng yomon holat daraxt qiyshiq bo'lib qolganda yuzaga keladi. Muvozanatli daraxtlar (AVL, Red-Black) balandlikni `log n` ga yaqin saqlaydi.

## Amaliy eslatmalar

- BST tartiblangan ma'lumotlar bilan ishlash amallari uchun juda yaxshi.
- Agar qo'shish tartibi deyarli tartiblangan bo'lsa, o'z-o'zini muvozanatlaydigan daraxtdan foydalaning.
- Faqat min/maks ustuvorlik amallari uchun heap soddaroq va odatda tezroq bo'ladi.
- `inorder()` — BST qiymatlarini tartiblangan holatda eksport qilishning eng oson yo'li.

## Tipik xatolar

- Takrorlanuvchi kalit siyosatini e'tiborsiz qoldirish (rad etish, sanash yoki almashtirish — aniq belgilangan bo'lishi kerak).
- Ikkita bolali o'chirish holatini unutish.
- Daraxt shaklini hisobga olmasdan `O(log n)` deb taxmin qilish.
