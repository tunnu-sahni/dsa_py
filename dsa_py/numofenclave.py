# number of enclaves

from collections import deque

class solution:
    def numberOfEnclsves(self, grid):
        if not grid or not grid[0]:
            return 0
        
        n , m = len(grid), len(grid[0])

        vis = [[False] * m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):

                if i == 0 or j == 0 or i ==n - 1 or j == m - 1:
                    if grid[i][j] == 1 and not vis[i][j]:
                        vis[i][j] = True
                        q.append((i , j))

        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]

        while q:
            row, col = q.popleft()
            for k in range(4):
                nrow = row + delrow[k]
                ncol = col + delcol[k]

                if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol] and grid[nrow][ncol] == 1:
                    vis[nrow][ncol] = True
                    q.append((nrow, ncol))

            cnt = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1 and not vis[i][j]:
                        cnt += 1
            return cnt
        
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    obj = solution()
    print(obj.numberOfEnclsves(grid))

# number of island

class solution:
    def dfs(self, row, col, baseRow, baseCol, grid, vis, shape):
        vis[row][col] = True
        shape.append((row - baseRow, col - baseCol))

        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]

            if (0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]) and not vis[nrow][ncol] and grid[nrow][ncol] == 1):
                self.dfs(nrow, ncol, baseRow, baseCol, grid, vis, shape)
    
    def countDistinctIsland(self, grid):
        n, m = len(grid), len(grid[0])
        vis = [[False for _ in range(m)] for _ in range(n)]
        st = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    shape = []
                    self.dfs(i, j, i, j, grid, vis, shape)
                    st.add(tuple(shape))
        return len(st)
    
grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]
obj = solution()
print(obj.countDistinctIsland(grid))