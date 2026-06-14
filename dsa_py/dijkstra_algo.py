# dijkstra algorithm using proirity queue

import heapq
class solution:
    def dijkstra(self, v, adj, src):
        dist = [float('inf')] * v
        dist[src] = 0

        pq = [(0, src)]

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue

            for next, wt in adj[node]:
                if dist[node] + wt < dist[next]:
                    dist[next] = dist[node] + wt
                    heapq.heappush(pq, (dist[next], next))

            return dist
v = 5
adj = [[] for _ in range(v)]

adj[0].append((1, 2))
adj[0].append((2, 4))
adj[1].append((2, 1))
adj[1].append((3, 7))
adj[2].append((4, 3))
adj[3].append((4, 2))

obj = solution()
dist = obj.dijkstra(v, adj, 0)

for i in range(v):
    print(f"Distance from 0 to {i} = {dist[i]}")

#time comlpexity O(V+ElogV)
#space complexity O(V+E)

# shortest distance in a binary maze

from collections import deque

def shortestPath(grid, source, destination):
    if source == destination:
        return 0
    
    n = len(grid)
    m = len(grid[0])

    dist = [[float('inf')] * m for _ in range(n)]
    dist[source[0][source[1]]] = 0

    q = deque([(0, source[0], source[1])])

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while q:
        dis, r, c = q.popleft()

        for i in range(4):
            newr, newc = r + dr[i], c + dc[i]

            if 0 <= newr < n and 0 <= newc < m and grid[newr][newc] == 1 and dis + 1 < dist[newr][newc]:
                dist[newr][newc] = dis + 1

                if (newr, newc) == destination:
                    return dis + 1
                
                q.append((dis + 1, newr, newc))

        return - 1
    
def main():
    source = (0, 1)
    destination = (2, 2)
    grid = [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 0, 1]
    ]

    res = shortestPath(grid, source, destination)

    print(res)

if __name__ == "__main__":
    main()