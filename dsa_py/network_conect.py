# number of operation to make network connect

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])

            return self.parent[x]
        
        def union(self, x, y):
            px = self.find(x)
            py = self.find(y)
            if px == py:
                return
            if self.rank[px] < self.rank[py]:
                self.parent[px] = py
            elif self.rank[px] > self.rank[py]:
                self.parent[py] = px

            else:
                self.parent[py] = px
                self.rank[px] += 1

class solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return-1
        
        dsu = DSU(n)

        for u, v in connections:
            dsu.union(u, v)
            components = set()
            for i in range(n):

                components.add(dsu.find(i))
                return len(components) - 1
            
n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 4]]
sol = solution()
print(sol.makeConnected(n, connections))