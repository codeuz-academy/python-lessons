---
title: Graph Representation
description: Adjacency list implementation with BFS, DFS, and topological sort
order: 11
permalink: /en/data-structures/graph-representation/
---

Graph representation affects both memory and traversal speed.

## Book alignment

Graph representation is included here as an **extension topic**.  
It is not a standalone data-structure chapter in the current Necaise TOC, but it connects naturally to search/traversal algorithms and real-world modeling.

## Choosing representation

- Adjacency list: best default for sparse graphs.
- Adjacency matrix: useful for dense graphs and fast edge existence checks.

This chapter focuses on adjacency list.

## Adjacency list vs matrix

| Representation | Space | Edge check `u -> v` | Iterate neighbors |
| -------------- | ----- | ------------------- | ----------------- |
| Adjacency list | `O(V + E)` | `O(deg(u))` | `O(deg(u))` |
| Adjacency matrix | `O(V^2)` | `O(1)` | `O(V)` |

## Operations

### add_edge(u, v)

Ensure both vertices exist, then append neighbor into adjacency list. In undirected graphs, write both directions.

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

Remove neighbor from one direction, and from both directions when graph is undirected.

```python
def remove_edge(self, u, v):
    if u in self.adj and v in self.adj[u]:
        self.adj[u].remove(v)
    if not self.directed and v in self.adj and u in self.adj[v]:
        self.adj[v].remove(u)
```

### bfs(start)

Breadth-first search explores by layers: all distance-1 nodes, then distance-2 nodes, and so on.

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

Depth-first search goes as deep as possible before backtracking.

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

### topological_sort() for DAG

Kahn algorithm repeatedly selects nodes with indegree zero. If nodes remain with nonzero indegree, the graph has a cycle.

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

## Full implementation

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

## Practical extensions

- Weighted graph: store `(neighbor, weight)` tuples instead of plain neighbors.
- No-duplicate adjacency: store neighbor sets (`set`) if duplicate edges should be ignored.
- Disconnected traversals: loop over all vertices and run BFS/DFS from unvisited ones.

## Complexity summary

For adjacency list:

- Add edge: `O(1)` average
- Remove edge: `O(deg(u))`
- BFS: `O(V + E)`
- DFS: `O(V + E)`
- Topological sort: `O(V + E)`

<div class="warning">
Topological sort works only on Directed Acyclic Graphs (DAGs).
</div>
