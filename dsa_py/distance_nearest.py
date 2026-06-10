# distance of nearest cell having 1

from collections import deque

class solution:
    def nearest(self, grid):
        n = len(grid)
        m = len(grid[0])

        vis = [[0] * m for _ in range(n)]

        dist = [[0] * m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    vis[i][j] = 1
                
                else:
                    vis[i][j] = 0

                    del_row = [-1, 0, 1, 0]
                    del_col = [0, 1, 0, -1]

                    while q:
                        row, col, steps = q.popleft()
                        dist[row][col] = steps

                        for i in range(4):
                            nrow = row + del_row[i]
                            ncol = col + del_col[i]

                            if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0:
                                vis[nrow][ncol] = 1
                                q.append((nrow, ncol, steps + 1))

                                return dist
                            
if __name__ == "__main__":
    grid = [[0, 1, 1, 0], [1, 1,0, 0], [0, 0, 1, 1]]

    sol = solution()
    ans = sol.nearest(grid)

    for row in ans:
        print(row)


# sorrounded regions

class solution:
    def dfs(self, row, col, vis, mat, dr, dc):
        vis[row][col] = 1
        n, m = len(mat), len(mat[0])

        for k in range(4):
            nrow, ncol = row + dr[k], col + dc[k]

            if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0 and mat[nrow][ncol] == '0':
                self.dfs(nrow, ncol, vis, mat, dr, dc)

                def fill(self, n, m, mat):
                    if n == 0 or m == 0:
                        return
                    
                    dr, dc = [-1, 0, 1,0], [0, 1, 0, -1]

                    vis = [[0] * m for _ in range(n)]

                    for j in range(m):
                        if vis[0][j] == 0 and mat[0][j] == '0':
                            self.dfs(0, j, vis, mat, dr, dc)

                            if vis[n - 1][j] == 0 and mat[n - 1][j] == '0':
                                self.dfs(n - 1, j, vis, mat, dr, dc)
                    
                    for i in range(n):
                        if vis[i][0] == 0 and mat[i][0] == '0':
                            self.dfs(i, 0, vis, mat, dr,dc)

                        if vis[i][m - 1] == 0 and mat[i][m - 1] == '0':
                            self.dfs(i, m - 1, vis, mat, dr, dc)

                    for i in range(n):
                        for j in range(m):
                            if vis[i][j] == 0 and mat[i][j] == '0':
                                mat[i][j] = 'x'

                    return mat
                
if __name__ == "__main__":
    mat = [
        ['x', 'x', 'x', 'x'],
        ['x', '0', 'x', 'x'],
        ['x', '0', '0', 'x'],
        ['x', '0', 'x', 'x'],
        ['x', 'x', '0', '0']
    ]
    sol = solution()
    ans = sol.fill(len(mat), len(mat[0]), mat)
    for row in ans:
        print(*row)


