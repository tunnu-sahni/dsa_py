#articilation point in graph

class solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, tin, low, mark, adj):
        vis[node] = True
        tin[node] = low[node] = self.timer
        self.timer += 1
        child = 0

        for neighbor in adj[node]:
            if neighbor == parent:
                continue

            if not vis[neighbor]:
                self.dfs(neighbor, node, vis, tin, low, mark, adj)

                low[node] = min(low[node], low[neighbor])

                if low[neighbor] >= tin[node] and parent != -1:
                    mark[node] = 1

                child += 1

            else:
                low[node] = min(low[node], tin[neighbor])

        if parent == -1 and child > 1:
            mark[node] = 1

    def articulationPoints(self, n, adj):
        vis = [False] * n
        tin = [0] * n
        low = [0] * n
        mark = [0] * n

        for i in range(n):
            if not vis[i]:
                self.dfs(i, -1, vis, tin, low, mark, adj)

        res = [i for i in range(n) if mark[i]]
        return res if res else [-1]
    
if __name__ == "__main__":
    n = 5
    edges = [
        [0, 1],
        [1, 4],
        [2, 4],
        [2, 3],
        [3, 4]
    ]

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    sol = solution()
    res = sol.articulationPoints(n, adj)
    print(" ".join(map(str, res)))