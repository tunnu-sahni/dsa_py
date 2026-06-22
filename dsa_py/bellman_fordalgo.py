#bellman ford algorithm

class solution:
    def bellman_ford(V, edges, S):
        dist = [int(1e8)] * V
        dist[S] = 0

        for _ in range(V - 1):
            for u, v, wt in edges:
                if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        for u, v, wt, in edges:
            if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
                return [-1]
        return dist
    
if __name__  == "__main__":
    V = 6
    S = 0
    edges = [
        [3, 2, 6],
        [5, 3, 1],
        [0, 1, 5],
        [1, 5, -3],
        [1, 2, -2],
        [3, 4, -2],
        [2, 4, 3]
    ]
    dist = (V, edges,S)
    print(" ".join(map(str, dist)))