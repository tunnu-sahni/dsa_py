#topological sort or kahns algorighm(dfs)

class solution:
    def dfs(self, node, adj, vis, st):
        vis[node] = 1

        for it in adj[node]:
            if vis[it] == 0:
                self.dfs(it, adj, vis, st)

        st.append(node)

    def topoSort(self, v, adj):
        vis = [0] * v
        st = []

        for i in range(v):
            if vis[i] == 0:
                self.dfs(i, adj, vis, st)

        return st[::-1]
    
if __name__ == "__main__":
    v = 3

    adj = [[] for _ in range(v)]

    adj[1].append(0)
    adj[0].append(1)
    adj[2].append(1)

    obj = solution()
    res = obj.topoSort(v, adj)

    print("Topological Sort:", *res)

#BFS

class solution:
    def topologicalSort(self, v, adj):
        indegree = [0] * v

        for i in range(v):
            for it in adj[i]:
                indegree[it] += 1
        
        from collections import deque
        q = deque()

        for i in range(v):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            node = q.popleft()

            for it in adj[node]:
                indegree[it] -= 1

                if indegree[it] == 0:
                    q.append(it)

        return topo
    
if __name__ == "__main__":
    v = 3

    adj = [[] for _ in range(v)]

    adj[0].append(0)
    adj[1].append(1)
    adj[1].append(0)

    obj = solution()
    ans = obj.topologicalSort(v, adj)

    print(*ans)