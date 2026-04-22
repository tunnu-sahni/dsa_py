# class solution:
#     def exist(self, board, word):
#         rows = len(board)
#         cols = len(board[0])

#         def dfs(i, j, idx):
#             if idx == len(word):
#                 return True
            
#             if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[idx]:
#                 return False
            
#             temp = board[i][j]
#             board[i][j] = "#"

#             found = dfs(i + 1, j, idx + 1) or dfs(i - 1, j, idx + 1) or dfs(i, j + 1, idx + 1) or dfs(i, j - 1, idx + 1)
#             board[i][j] = temp
#             return found

#         for i in range(rows):
#             for j in range(cols):
#                 if dfs(i, j, 0):
#                     return True
#         return False
    
# if __name__ == "__main__":
#     sol = solution()
#     board = [
#         ['A', 'B', 'C', 'E'],
#         ['S', 'F', 'C', 'S'],
#         ['A', 'D', 'E', 'E']

#     ]

#     word = "ABCDE"
#     print(sol.exist(board, word))

#     print(sol.exist(board, "SEE"))



# word break

class solution:
    def isSafe(self, x, y, n, maze, visited):
        return (0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y] == 0)
    
    def solve(self, x, y, n, maze, visited, path, res):

        if x == n - 1 and y == n - 1:
            res.append(path)
            return
        
        visited[x][y] = 1

        if self.isSafe(x + 1, y, n, maze, visited):
            self.solve(x + 1, y, n, maze, visited, path + "D", res)

            if self.isSafe(x, y, - 1, n, maze, visited):
                self.solve(x, y - 1, n, maze, visited, path + "L", res)

                visited[x][y] = 0

    def findpath(self, maze, n):
        res = []
        visited = [[0] * n for _ in range(n)]
        if maze[0][0] == 1:
            self.solve(0, 0, n, maze, visited, "", res)
            return res
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

n = len(maze)
obj = solution()
paths = obj.findpath(maze, n)
print(" ".join(paths))