# network delay time

import heapq
class solution:
    def networkDelayTime(self, times, n, k):
        adj = [[] for _ in range(n + 1)]

        for u, v, w in times:
            adj[u].append((v, w))

            pq = [(0, k)]

            dist = [float('inf')] * (n + 1)
            dist[k] = 0

            while pq:
                time, node = heapq.heappop(pq)

                for nbr, wt in adj[node]:
                    if dist[nbr] > time + wt:
                        dist[nbr] = time + wt
                        heapq.heappush(pq, (dist[nbr], nbr))

                        ans = max(dist[1:])
                        return -1 if ans == float('inf') else ans
                    
if __name__ == "__main__":
    sol = solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n, k = 4, 2
    print(sol.networkDelayTime(times, n, k))

# number of ways to arrive at destination

import heapq

def countPaths(n, roads, src, dst, k):
    adj = {i: [] for i in range(n)}
    for road in roads:
        adj[road[0]].append([road[1], road[2]])

        pq = [(0, 0)]

        dist = [float('inf')] * n
        dist[src] = 0
        ways = [0] * n
        ways[src] = 1

        mod = int(1e9 + 7)

        while pq:
            dis, node = heapq.heappop(pq)
            for adjNode, edw in adj[node]:
                if dis + edw < dist[adjNode]:
                    dist[adjNode] = dis + edw
                    heapq.heappush(pq, (dis + edw, adjNode))
                    ways[adjNode] = ways[node]

                elif dis + edw == dist[adjNode]:
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod

            return ways[dst] % mod
        
def main():
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]

    ans = countPaths(n, roads, 0, 3, 1)

    print(ans)

if __name__ == "__main__":
    main()