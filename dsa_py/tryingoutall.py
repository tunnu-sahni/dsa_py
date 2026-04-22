# #word search

# def exist(board, word):
#     rows = len(board)
#     cols = len(board[0])

#     def dfs(r, c, i):
#         if i == len(word):
#             return True
#         if r < 0 or c < 0 or r >= rows or c >= cols or board[i][c] != word[i]:
#             return False
        
#         temp = board[r][c]
#         board[r][c] = "#"

#         found = (dfs(r+1, c, i+1) or
#                 dfs(r-1, c, i+1) or
#                 dfs(r, c+1, i+1) or
#                 dfs(r, c-1, i+1))
        
#         board[r][c] = temp

#         return found
    
#     for i in range(rows):
#         for j in range(cols):
#             if dfs(i, j, 0):
#                 return True
#     return False

# board = [
#     ["A", "B", "C", "E"],
#     ["S", "F", "C", "S"],
#     ["A", "D", "E", "E", "E"]
# ]

# print(exist(board, "ABCCED"))
# print(exist(board,"ABCCDEEEEFSA" ))


# #N QUEEN PROBLEM

# class solution:
#     def isSafe(self, row, col, board, n):
#         for j in range(col):
#             if board[row][j] == 'Q':
#                 return False
            
#             i, j = row, col
#             while i >= 0 and j >= 0:
#                 if board[i][j] == 'Q':
#                     return False
                
#                 i -= 1
#                 j -= 1

#             i, j = row, col

#             while i < n and j >= 0:
#                 if board[i][j] == 'Q':
#                     return False
#                 i += 1
#                 j -= 1

#             return False
#     def solve(self, col, board, ans, n):
#         if col == n:
#             temp = [''.join(row) for row in board]
#             ans.append(temp)
#             return
        
#         for row in range(n):
#             if self.isSafe(row, col, board, n):
#                 board[row][col] = 'Q'
#                 self.solve(col + 1, board, ans, n)
#                 board[row][col] = '.'
            
#     def solveNQueens(self, n):
#         board = [['.' for _ in range(n)] for _ in range(n)]
#         ans = []
#         self.solve(0, board, ans, n)
#         return ans
    
# if __name__ == "__main__":
#     obj = solution()
#     n = 4

#     res = obj.solveNQueens(n)

#     for board in res:
#         for row in board:
#             print(row)
#         print()

class solution:
    def solve(self, col, board, n, leftRow, upperDiagonal, lowerDiagonal, ans):
        if col == n:
            ans.append(["".join(row) for row in board])
            return 
        
        for row in range(n):
            if leftRow[row] == 0 and lowerDiagonal[row + col] == 0 and \
               upperDiagonal[n - 1 + col - row] == 0:
                
                board[row][col] = 'Q'
                leftRow[row] = lowerDiagonal[row + col] = upperDiagonal[n - 1 + col - row] = 1

                self.solve(col + 1, board, n, leftRow, upperDiagonal, lowerDiagonal, ans)

                board[row][col] = '.'
                leftRow[row] = lowerDiagonal[row + col] = upperDiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n):
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        leftRow = [0] * n
        lowerDiagonal = [0] * (2 * n - 1)
        upperDiagonal = [0] * (2 * n - 1)
        self.solve(0, board, n, leftRow, upperDiagonal, lowerDiagonal, ans)
        return ans
    
sol = solution()
res = sol.solveNQueens(4)
for board in res:
    for row in board:
        print(row)
    print()