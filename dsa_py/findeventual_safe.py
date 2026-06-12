# find eventual safe states (bfs)

from collections import deque

def eventualSafeNodes(v, adj):
        adjRev = [[] for _ in range(v)]
        indegree = [0] * v

        for i in range(v):
            for neighbor in adj[i]:
                adjRev[neighbor].append(i)
                indegree[i] += 1
        
        q = deque()
        safeNodes = []
        for i in range(v):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            safeNodes.append(node)

            for parent in adjRev[node]:
                indegree[parent] -= 1

                if indegree[parent] == 0:
                    q.append(parent)

        safeNodes.sort()
        return safeNodes
    
adj = [
    [1], [2], [3, 4], [4, 5], [6], [6], [7], [], [1, 9], [10], [8], [9]]

v = 12
safeNodes = eventualSafeNodes(v, adj)
print("The eventual safe nodes are:", *safeNodes)


#alien dictionary

from collections import deque

class solution:
    def topoSort(self, v, adj):
        indegree = [0] * v

        for u in range(v):
            for v in adj[u]:
                indegree[v] += 1

        q = deque()
        for i in range(v):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            node = q.popleft()
            topo.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return topo
    def findOrder(self, dict, N, K):
        adj = [[] for _ in range(K)]
        for i in range(N - 1):
            s1, s2 = dict[i], dict[i + 1]
            length = min(len(s1), len(s2))

            for ptr in range(length):
                if s1[ptr] != s2[ptr]:
                    adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))

                    break

if __name__ == "__main__":
    N, K = 5, 3
    dict = ["baa", "abcd", "abca", "cab", "cad"]

    obj = solution()
    ans = obj.findOrder(dict, N, K)

    for ch in ans:
        print(ch, end=" ")

    print()
