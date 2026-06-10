# rotten orange min time to rot all orange

from ast import main
from collections import deque

def orangesRotting(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    rotten = deque()
    total = 0
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                total += 1
            
            if grid[i][j] == 2:
                rotten.append((i, j))
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                days = 0

                while rotten:
                    k = len(rotten)
                    count += k

                    for _ in range(k):
                        x, y = rotten.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != 1:
                                continue
                            grid[nx][ny] = 2
                            rotten.append((nx, ny))
                            days += 1
        return days if count == total else -1
    
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
result = orangesRotting(grid)
print("minimum number of minute required", result)

# detect cycle in an undirected graph using dfs

class solution:
    def dfs(self, node, parent, adj, visited):
        visited[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor, node, adj, visited):
                    return True
            
            elif neighbor != parent:
                return True
        
        return False
    def isCycle(self, v, adj):
        visited = [False] * v

        for i in range(v):
            if not visited[i]:
                if self.dfs(i, -1, adj, visited):
                    return True
        
        return False
    
    def main():
        v = 5
        adj = [[] for _ in range(v)]

        adj[0].append(1)
        adj[1].append(0)
        adj[1].append(2)
        adj[2].append(1)
        adj[2].append(3)
        adj[3].append(2)
        adj[3].append(4)
        adj[4].append(3)
        adj[4].append(1)

        sol = solution()
        if sol.isCycle(v, adj):
            print("cycle detected")
        else:
            print("No cycle found")

if __name__ == "__main__":
    main()