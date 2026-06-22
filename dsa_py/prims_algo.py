#prims algorithm

import heapq

def prim(graph, start):
    visited = set()

    heap = [(0, start)]

    mst_weight = 0

    while heap:
        weight, node = heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)
        mst_weight += weight

        for nei, w in graph[node]:
            if nei not in visited:
                heapq.heappush(heap, (w, nei))

    return mst_weight

graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15),],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

print(prim(graph, 0))