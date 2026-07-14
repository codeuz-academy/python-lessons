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

Topological sort orders the nodes of a **DAG** (directed acyclic graph) so every edge points from an earlier node to a later one — a dependency-safe order (build steps, course prerequisites). Kahn's algorithm repeatedly removes nodes that have no remaining incoming edges.

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

Time: `O(V + E)`. Raises if the graph contains a cycle (no valid ordering exists).
