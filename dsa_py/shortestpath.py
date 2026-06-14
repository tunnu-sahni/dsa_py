# shortest path in unditrcted graph

from collections import deque, defaultdict

class solution:
    def shortestPath(self, edges, N, M, src):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist = [float('inf')] * N
        dist[src] = 0

        q = deque()
        q.append(src)

        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if dist[node] + 1 < dist[neighbor]:
                    dist[neighbor] = dist[node] + 1

                    q.append(neighbor)

        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1

        return dist
    
N = 6
M = 5
edges = [
    [0, 1],[0, 3], [3, 4], [4, 5], [5, 6], [1, 2]
]

obj = solution()
result = obj.shortestPath(edges, N, M, 0)
print(" ".join(map(str, result)))