import heapq

class solution:
    def swimInWater(self, grid):
        n = len(grid)

        heap = [(grid[0][0], 0, 0)]

        visited = [[False] * n for _ in range(n)]

        visited[0][0] = True

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            elevation, r, c = heapq.heappop(heap)

            if r == n - 1 and c == n - 1:
                return elevation
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True

                    heapq.heappush(heap, (max(elevation, grid[nr][nc]), nr, nc))
                    return - 1
                
if __name__ == "__main__":
    grid = [
        [0, 2],
        [1, 3]
    ]
    sol = solution()
    print("Minimum time to reach destination: ", sol.swimInWater(grid))