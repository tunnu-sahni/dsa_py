# cheapest flights within k stops

from collections import deque

def cheapestFlights(n, flights, src, dst, k):
    adj = {i: [] for i in range(n)}
    for flights in flights:

        adj[flights[0]].append([flights[1], flights[2]])

        q = deque([(0, src, 0)])

        dist = [float('inf')] * n 
        dist[src] = 0

        while q:
            stops, node, cost = q.popleft()

            if stops > k:
                continue

            for adjNode, edw in adj[node]:
                if cost + edw < dist[adjNode] and stops <= k:
                    dist[adjNode] = cost + edw
                    q.append((stops + 1, adjNode, cost + edw))

                    if dist[dst] == float('inf'):
                        return -1
                    
                    return dist[dst]
                
def main():
    n = 4
    src = 0
    dst = 3
    k = 1
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]

    ans = cheapestFlights(n, flights, src, dst, k)

    print(ans)

if __name__ == "__main__":
    main()
            