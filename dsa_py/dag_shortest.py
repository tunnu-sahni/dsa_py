# # shortest path in directed acyclic graph

# from collections import defaultdict, deque
# class solution:
#     def topoSort(self, node, visited, stack, adj):
#         visited[node] = True

#         for neighbor, weight in adj[node]:
#             if not visited[neighbor]:
#                 self.topoSort(neighbor, visited, stack, adj)

#         stack.append(node)

#     def shortestPath(self, N, M, edges):

#         adj = defaultdict(list)
#         for u, v, wt in edges:
#             adj[u].append((v, wt))

#         visited = [False] * N
#         stack = []

#         for i in range(N):
#             if not visited[i]:
#                 self.topoSort(i, visited, stack, adj)

#         dist = [float('inf')] * N
#         dist[0] = 0

#         while stack:
#             node = stack.pop()

#             if dist[node] != float('inf'):
#                 for neighbor, weight in adj[node]:
#                     if dist[node] + weight < dist[neighbor]:
#                         dist[neighbor] = dist[node] + weight

#         for i in range(N):
#             if dist[i] == float('inf'):
#                 dist[i] = -1

#         return dist
    
# if __name__ == "__main__":
#     N = 6
#     M = 7

#     edges = [
#         [0, 1], [0, 4, 1], [4, 5, 4], [4, 2, 2],[1, 2, 3], [2, 3, 6], [5, 3, 1]
#     ]
#     obj = solution()
#     result = obj.shortestPath(N, M, edges)

#     print(' '.join(map(str, result)))

# dijkstra algorighm

import heapq
class solution:
    def dijkstra(self, v, adj, s):
        pq = []

        dist = [float('inf')] * v
        dist[s] = 0

        heapq.heappush(pq, (0, s))

        while pq:
            dist, node = heapq.heappop(pq)
        
        for adjNode, weight, in adj[node]:
            if dist + weight < dist[adjNode]:
                dist[adjNode] = dist + weight
                heapq.heappush(pq, (dist[adjNode], adjNode))

        return dist
    
if __name__ == "__main__":
    v = 3
    E = 3
    s = 2

    adj = [[] for _ in range(v)]

    adj[0].append((1, 1))
    adj[0].append((2, 6))
    adj[1].append((2, 3))
    adj[1].append((9, 1))
    adj[2].append((1, 3))
    adj[2].append((0, 6))

    obj = solution()
    res = obj.dijkstra(v, adj, s)
    print(" ".join(map(str, res)))