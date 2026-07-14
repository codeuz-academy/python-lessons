---
title: Graf algoritmlari (Graph Algorithms)
description: BFS bilan eng qisqa yo'l, Dijkstra va topologik tartiblash (topological sort) amalga oshirishlari
order: 4
permalink: /uz/algorithms/graph-algorithms/
---

Bu algoritmlar ma'lumotlar tuzilmalari bo'limidagi graf (graph) ko'rinishlaridan foydalanadi.

## BFS bilan eng qisqa yo'l (vaznsiz)

```python
from collections import deque


def shortest_path_unweighted(graph, start, target):
    q = deque([start])
    parent = {start: None}

    while q:
        node = q.popleft()
        if node == target:
            break

        for nxt in graph.neighbors(node):
            if nxt not in parent:
                parent[nxt] = node
                q.append(nxt)

    if target not in parent:
        return []

    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    return path[::-1]
```

Vaqt: `O(V + E)`

## Dijkstra (vaznli, manfiy bo'lmagan)

```python
import heapq


def dijkstra(adj, source):
    dist = {node: float("inf") for node in adj}
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue

        for nei, w in adj[node]:
            nd = d + w
            if nd < dist[nei]:
                dist[nei] = nd
                heapq.heappush(pq, (nd, nei))

    return dist
```

Vaqt: heap yordamida `O((V + E) log V)`.

## Topologik tartiblash (Kahn algoritmi)

Topologik tartiblash **DAG** (yo'naltirilgan asiklik graf) tugunlarini shunday tartiblaydiki, har bir qirra oldingi tugundan keyingi tugunga yo'naladi — bu bog'liqliklarni hisobga olgan xavfsiz tartib (build bosqichlari, kurs talablari). Kahn algoritmi kiruvchi qirralari qolmagan tugunlarni ketma-ket olib tashlaydi.

```python
from collections import deque


def topological_sort(adj):
    in_degree = {node: 0 for node in adj}
    for node in adj:
        for nei in adj[node]:
            in_degree[nei] += 1

    q = deque([node for node in adj if in_degree[node] == 0])
    order = []

    while q:
        node = q.popleft()
        order.append(node)
        for nei in adj[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                q.append(nei)

    if len(order) != len(adj):
        raise ValueError("Graph has a cycle; no topological order exists")

    return order


graph = {
    "shirt": ["tie", "belt"],
    "tie": ["jacket"],
    "belt": ["jacket"],
    "jacket": [],
}
print(topological_sort(graph))   # ['shirt', 'tie', 'belt', 'jacket']
```

Vaqt: `O(V + E)`. Agar grafda sikl bo'lsa, xatolik chiqaradi (yaroqli tartib mavjud emas).
