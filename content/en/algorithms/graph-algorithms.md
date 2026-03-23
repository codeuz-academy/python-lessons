---
title: Graph Algorithms
description: BFS shortest path, Dijkstra, and topological sort implementations
order: 4
permalink: /en/algorithms/graph-algorithms/
---

These algorithms use graph representations from the data structures section.

## BFS Shortest Path (Unweighted)

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

Time: `O(V + E)`

## Dijkstra (Weighted, Non-negative)

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

Time: `O((V + E) log V)` using heap.

## Topological Sort (Kahn's Algorithm)

- Works on DAGs only.
- Produces dependency-safe order.
