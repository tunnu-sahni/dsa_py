#minimum spanning tree

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False
        
        self.parent[py] = px
        return True
    
    def kruskal(n, edges):
        edges.sort(key=lambda x: x[2])

        dsu = DSU(n)
        mst_weight = 0
        mst_edges = []

        for u, v, w in edges:
            if dsu.union(u, v):
                mst_weight += w
                mst_edges.append((u, v, w))

        return mst_weight, mst_edges
    
n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 2, 5),
    (1, 3, 15),
    (2, 3, 4)
]

weight, mst = (n, edges)

print("MST Weight =", weight)
print("Edges =", mst)