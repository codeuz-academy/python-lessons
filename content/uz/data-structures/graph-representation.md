---
title: Grafni ifodalash (Graph Representation)
description: Qo'shnilik ro'yxati (adjacency list) yordamida amalga oshirish — BFS, DFS va topologik saralash bilan
order: 10
permalink: /uz/data-structures/graph-representation/
---

Grafni qanday ifodalash ham xotira sarfiga, ham aylanib chiqish (traversal) tezligiga ta'sir qiladi.

## Kitobga moslik

Grafni ifodalash bu yerga **qo'shimcha mavzu** sifatida kiritilgan.  
U joriy Necaise mundarijasida alohida ma'lumotlar tuzilmasi bobi emas, ammo qidirish/aylanib chiqish algoritmlari va real dunyo modellashtirilishi bilan tabiiy ravishda bog'lanadi.

## Ifodalash usulini tanlash

- Qo'shnilik ro'yxati (adjacency list): siyrak (sparse) graflar uchun eng yaxshi standart variant.
- Qo'shnilik matritsasi (adjacency matrix): zich (dense) graflar va qirralar mavjudligini tez tekshirish uchun foydali.

Ushbu bob qo'shnilik ro'yxatiga e'tibor qaratadi.

## Qo'shnilik ro'yxati va matritsa

| Ifodalash usuli | Joy | Qirra tekshiruvi `u -> v` | Qo'shnilarni aylanib chiqish |
| -------------- | ----- | ------------------- | ----------------- |
| Qo'shnilik ro'yxati | `O(V + E)` | `O(deg(u))` | `O(deg(u))` |
| Qo'shnilik matritsasi | `O(V^2)` | `O(1)` | `O(V)` |

## Amallar

### add_edge(u, v)

Avval ikkala tugun (vertex) mavjudligiga ishonch hosil qiling, so'ng qo'shnini qo'shnilik ro'yxatiga qo'shing. Yo'naltirilmagan graflarda har ikkala yo'nalishni ham yozing.

![Graph add edge]({{ '/img/data-structures/graph-add-edge.png' | url }})

```python
def add_edge(self, u, v):
    self.add_vertex(u)
    self.add_vertex(v)
    self.adj[u].append(v)
    if not self.directed:
        self.adj[v].append(u)
```

### remove_edge(u, v)

Qo'shnini bitta yo'nalishdan o'chiring, graf yo'naltirilmagan bo'lsa esa har ikkala yo'nalishdan o'chiring.

```python
def remove_edge(self, u, v):
    if u in self.adj and v in self.adj[u]:
        self.adj[u].remove(v)
    if not self.directed and v in self.adj and u in self.adj[v]:
        self.adj[v].remove(u)
```

### bfs(start)

Kenglik bo'yicha qidirish (Breadth-first search) qatlamlar bo'ylab tekshiradi: avval 1-masofadagi barcha tugunlar, keyin 2-masofadagi tugunlar va hokazo.

![Graph BFS and DFS]({{ '/img/data-structures/graph-bfs-dfs.png' | url }})

```python
from collections import deque


def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph.neighbors(node):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

    return order
```

### dfs(start)

Chuqurlik bo'yicha qidirish (Depth-first search) orqaga qaytishdan oldin imkon qadar chuqurroq kiradi.

```python
def dfs(graph, start):
    visited = set()
    order = []

    def walk(node):
        visited.add(node)
        order.append(node)
        for nxt in graph.neighbors(node):
            if nxt not in visited:
                walk(nxt)

    walk(start)
    return order
```

### DAG uchun topological_sort()

Kahn algoritmi kirish darajasi (indegree) nolga teng bo'lgan tugunlarni takror-takror tanlaydi. Agar kirish darajasi noldan farqli tugunlar qolib ketsa, demak grafda sikl (cycle) bor.

```python
from collections import deque


def topological_sort(adj):
    indegree = {node: 0 for node in adj}
    for node in adj:
        for nxt in adj[node]:
            indegree[nxt] = indegree.get(nxt, 0) + 1

    queue = deque([node for node, deg in indegree.items() if deg == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in adj.get(node, []):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    if len(order) != len(indegree):
        raise ValueError('graph contains cycle')
    return order
```

## To'liq amalga oshirish

```python
class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def remove_edge(self, u, v):
        if u in self.adj and v in self.adj[u]:
            self.adj[u].remove(v)
        if not self.directed and v in self.adj and u in self.adj[v]:
            self.adj[v].remove(u)

    def neighbors(self, v):
        return self.adj.get(v, [])
```

## Amaliy kengaytmalar

- Vaznli graf (weighted graph): oddiy qo'shnilar o'rniga `(neighbor, weight)` `tuple`'larini saqlang.
- Takrorsiz qo'shnilik: agar takror qirralarni e'tiborsiz qoldirish kerak bo'lsa, qo'shnilarni to'plam (`set`) ko'rinishida saqlang.
- Bog'lanmagan aylanib chiqishlar: barcha tugunlar bo'ylab takrorlang va tekshirilmagan tugunlardan BFS/DFS ishga tushiring.

## Murakkablik xulosasi

Qo'shnilik ro'yxati uchun:

- Qirra qo'shish: o'rtacha `O(1)`
- Qirra o'chirish: `O(deg(u))`
- BFS: `O(V + E)`
- DFS: `O(V + E)`
- Topologik saralash: `O(V + E)`

<div class="warning">
Topologik saralash faqat Yo'naltirilgan Asiklik Graflar (Directed Acyclic Graphs, DAG) ustida ishlaydi.
</div>
