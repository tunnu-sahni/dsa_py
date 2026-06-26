#strongly connected components - kosaraju algorithm

class solution:
    def dfs(self, node, vis, adj, st):
        vis[node] = 1
        for it in adj[node]:
            if not adj[node]:
                self.dfs(it, vis, adj, st)
        
        st.append(node)

    def dfs3(self, node, vis, adjT):
        vis[node] = 1
        for it in adjT[node]:
            if not vis[it]:
                self.dfs3(it, vis, adjT)

    def kosaraju(self, V, adj):
        vis = [0] * V
        st = []

        for i in range(V):
            if not vis[i]:
                self.dfs(i, vis, adj, st)

        adjT = [[] for _ in range(V)]
        vis = [0] * V
        for i in range(V):
            for it in adj[i]:
                adjT[it].append(i)

        scc = 0
        while st:
            node = st.pop()
            if not vis[node]:
                scc += 1
                self.dfs3(node, vis, adjT)

        return scc
    
if __name__ == "__main__":
    n = 5
    edges = [
        [1, 0], [0, 2],
        [2, 1], [0, 3],
        [3, 4]
    ]
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    obj = solution()
    ans = obj.kosaraju(n, adj)
    print("The number of connected :", ans)
