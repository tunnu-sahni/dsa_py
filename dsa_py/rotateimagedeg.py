#rotate image by 90 degree

# class solution:
#     def rotateClockWise(self, matrix):
#         n  = len(matrix)

#         rotated = [[0] * n for _ in range(n)]

#         for i in range(n):
#             for j in range(n):

#                 rotated[j][n - i - 1] = matrix[i][j]

#         return rotated
    

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# obj = solution()
# rotated = obj.rotateClockWise(matrix)

# for row in rotated:
#     print(*row)



# class solution:
#     def rotateClockWise(self, matrix):
#         n = len(matrix)

#         for i in range(n):

#             for j in range(i + 1, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#         for i in range(n):
#             matrix[i].reverse()

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# obj = solution()
# obj.rotateClockWise(matrix)

# for row in matrix:
#     print(*row)



#spiral traversal of matrix


class solution:
    def spiralOrder(self, matrix):
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])

            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
                right -= 1

                if top <= bottom:
                    for i in range(right, left -1, -1):
                        result.append(matrix[bottom][i])
                    bottom -= 1

                if left <= right:
                    for i in range(bottom, top - 1, -1):
                        result.append(matrix[i][left])
                        left += 1

                return result
            
obj = solution()

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(obj.spiralOrder(matrix))







