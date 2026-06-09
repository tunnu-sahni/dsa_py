class solution:
    def dfs(self, node, adj_list, visited):
        visited[node] = True

        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj_list, visited)

    def numprovinces(self, adj, v):
        adj_list = [[] for _ in range(v)]
        for i in range(v):
            for j in range(v):
                if adj[i][j] == 1 and i != j:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
                    visited = [False] * v
                    count = 0

                    for i in range(v):
                        if not visited[i]:
                            count += 1
                            self.dfs(i, adj_list, visited)
                    return count
            
if __name__ == "__main__":
    adj = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    v = 3
    sol = solution()
    print(sol.numprovinces(adj, v))



# connected component

from collections import deque

class solution:
    def countcomponents(self, v, edges):
        adj = [[] for _ in range(v)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * v
        componets = 0

        for i in range(v):
            if not visited[i]:
                components += 1

                q = deque()
                q.append(i)
                visited[i] = True

                while q:
                    node = q.popleft()

                    for nbr in adj[node]:
                        if not visited[nbr]:
                          visited[nbr] = True
                          q.append(nbr)
                          return components
                        
v = 5
edges = [[0, 1],[1, 2],[3, 4]]

sol = solution()
print("Number of connected components: ", sol.countcomponents(v, edges))