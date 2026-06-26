#bridges in graph using tarjens algorithm of time in and low time

from typing import List

class solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node: int, parent: int, vis: List[int], adj: List[List[int]], tin: List[int], low: List[int], bridges: List[List[int]]) -> None:
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1

        for neighbor in adj[node]:
            if neighbor == parent:
                continue

            if vis[neighbor] == 0:
                self.dfs(neighbor, node, vis, adj, tin, low, bridges)

                low[node] = min(low[node], low[neighbor])

                if low[neighbor] > tin[node]:
                    bridges.append([neighbor, node])

            else:
                low[node] = min(low[node], low[neighbor])


    def criticalConnections(self, n: int, connectioins: List[List[int]]) -> List[List[int]]:

        adj = [[] for _ in range(n)]
        for u, v in connectioins:
            adj[u].append(v)
            adj[v].append(u)

        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        bridges = []

        self.dfs(0, -1, vis, adj, tin,low, bridges)
        return bridges
    
if __name__ == "__main__":
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    obj = solution()
    print("Critical connections (brisges):", obj.criticalConnections(n, connections))   