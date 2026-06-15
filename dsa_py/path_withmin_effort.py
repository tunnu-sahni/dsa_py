# path with minimum effort

import heapq

def MinimumEffort(heights):
    n = len(heights)
    m = len(heights[0])

    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0

    pq = [(0, 0, 0)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while pq:
        diff, r, c = heapq.heappop(pq)

        if r == n - 1 and c == m - 1:
            return diff
        
        for i in range(4):
            newr, newc = r + dr[i], c + dc[i]

            if 0 <= newr < n and 0 <= newc < m:
                newEffort = max(abs(heights[r][c] - heights[newr][newc]), diff)

                if newEffort < dist[newr][newc]:
                    dist[newr][newc] = newEffort
                    heapq.heappush(pq, (newEffort, newr, newc))

                    return 0
                
def main():
    heights = [
        [1, 2, 2],
        [3, 8, 2],
        [5, 3, 5]
    ]

    res = MinimumEffort(heights)
    print(res)

    if __name__ == "__main__":
        main()