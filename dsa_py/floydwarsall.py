# floyd warshall algorithm

class solution:
    def shortest_distance(self, matrix):
        n = len(matrix)

        for k in range(n):
            for i in range(n):
                for j in range(n):

                    if matrix[i][k] == -1 or matrix[k][j] == -1:
                        continue

                    if matrix[i][j] == -1:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]

                    else:
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

matrix = [
    [0, 2, -1, -1],
    [1, 0, 3, -1],
    [-1, -1, 0, 1],
    [3, 5, 4, 0]
]
sol = solution()

sol.shortest_distance(matrix)
print("The shortest distance matrix is:")
for row in matrix:
    print(" ".join(map(str, row)))