# most stones removed with same row or column

class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
                self.parent[x] = x

        if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):
          self.parent[self.find(x)] = self.find(y)

class solution:
    def removsStones(self, stones):
         dsu = DSU()

         for x, y in stones:
            dsu.union(x, y + 10001)

            components = set()
            for x, y in stones:
                 components.add(dsu.find(x))

            return len(stones) - len(components)

stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]

obj = solution()
print(obj.removsStones(stones))
        
