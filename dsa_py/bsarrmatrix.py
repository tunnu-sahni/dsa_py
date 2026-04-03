# search in a row and column-wise sorted matrix

# from typing import List

# class MatrixSearch:
#     def __init__(self, matrix: List[List[int]]):

#         self.matrix = matrix

#     def search_element(self, target: int) -> bool:

#         n = len(self.matrix)
#         m = len(self.matrix[0])

#         for i in range(n):
#             for j in range(m):

#                 if self.matrix[i][j] == target:

#                     return True
                
#         return False
    
# if __name__ == "__main__":

#     matrix = [
#         [1, 4, 7, 11, 15],
#         [2, 5, 8, 12, 19],
#         [3, 6, 9, 16, 22],
#         [10, 13, 14, 17, 24],
#         [18, 21, 23, 26, 30]
#     ]

#     ms = MatrixSearch(matrix)

#     found = ms.search_element(8)

#     print(found)


# from typing import List

# class MatrixSearch:

#     def __int__(self, matrix: List[List[int]]):

#         self.matrix = matrix

#     def binary_search(self, nums: List[int], target: int) -> bool:

#         low = 0
#         high = len(nums) - 1

#         while low <= high:

#             mid = (low + high) // 2

#             if nums[mid] == target:
#                 return True
            
#             elif target > nums[mid]:
#                 low = mid + 1

#         return False
    
#     def search_element(self, target: int) -> bool:

#         for i, row in enumerate(self.matrix):
#                                  found_in_row = self.binary_search(row, target)

#                                  if found_in_row:
#                                       return True
                                 

#         return False
    
# if __name__ == "__main__":
     
#      matrix = [
#           [1, 4, 7, 11, 15],
#           [2, 5, 8, 12, 19],
#           [3, 6, 9, 16, 22],
#           [10, 13, 14, 17, 24],
#           [18, 21, 23, 26, 30]
#      ]

#      ms = MatrixSearch(matrix)

#      found = ms.search_element(8)

#      print(found)
                          

# from typing import List

# class MatrixSearch:
#     def __init__(self, matrix: List[List[int]]):

#         self.matrix = matrix

#     def search_element(self, target: int) -> bool:

#         n = len(self.matrix)
#         m = len(self.matrix[0])

#         row = 0
#         col = m - 1

#         while row < n and col >= 0:
#             current = self.matrix[row][col]

#             if current == target:
#                 return True
#             elif current < target:
#                 row += 1

#             else:
#                 col -= 1

#         return False
    
# if __name__ == "__main__":
#     matrix = [
#         [1, 4, 7, 11, 15],
#         [2, 5, 8, 12, 19],
#         [3, 6, 9, 16, 22],
#         [10, 13, 14, 17, 24],
#         [18, 21, 23, 26, 30]
#     ]

#     ms = MatrixSearch(matrix)
#     found = ms.search_element(8)
#     print(found)



# # #find peak element (2d matrix)


# class solution:
#     def maxElement(self, arr, col):
#         n = len(arr)
#         max_val = float('-inf')
#         index = -1

#         for i in range(n):
#             if arr[i][col] > max_val:
#                 max_val = arr[i][col]
#                 index = i
#         return index
    
#     def findPeakGrid(self, arr):
#         n = len(arr)
#         m = len(arr[0])

#         low = 0
#         high = m - 1

#         while low <= high:
#             mid = (low + high) // 2

#             row = self.maxElement(arr, mid)

#             left = arr[row][mid - 1] if mid - 1 >= 0 else float('-inf')

#             right = arr[row][mid + 1] if mid + 1 < m else float('-inf')

#             if arr[row][mid] > left and arr[row][mid] > right:
#                 return [row, mid]
#             elif left > arr[row][mid]:

#                 high = mid - 1

#             else:
#                 low = mid + 1

#         return [-1, -1]
    
#     max = [
#         [4, 2, 5, 1, 4, 5],
#         [2, 9, 3, 2, 3, 2],
#         [1, 7, 6, 0, 1, 3],
#         [3, 6, 2, 3, 7, 2]
#     ]

#     sol = solution()

#     peak = sol.findPeakGrid(max)

#     print(f"the row of peak element is {peak[0]} and"f"column of the peak element is {peak[1]}")



# median of row wise sorted matrix

# class solution:
#     def findMedian(self, matrix):

#         element = []

#         for row in matrix:

#             for val in row:

#                 element.append(val)
        
#         element.sort()

#         return element[len(element) // 2]
    
# matrix = [
#     [1, 3, 5],
#     [2, 6, 9],
#     [3, 6, 9]
# ]

# obj = solution()

# print(obj.findMedian(matrix))



# import bisect

# class solution:
#     def countLessEqual(self, row, mid):
#         return bisect.bisect_right(row, mid)
    
#     def findMedian(self, matrix):
#         row = len(matrix)
#         col = len(matrix[0])

#         low = min(row[0] for row in matrix)

#         high = max(row[-1] for row in matrix)

#         while low < high:
#             mid = (low + high) // 2
#             count = 0

#             for row in matrix:
#                 count += self.countLessEqual(row, mid)

#                 if count < (row * col  + 1) // 2:
#                     low = mid + 1

#                 else:
#                     high = mid
#             return low
# matrix = [
#     [1, 3, 5],
#     [2, 6, 9],
#     [3, 6, 9]
# ]

# obj = solution()
# print("Median:", obj.findMedian(matrix))



class solution:
    def findMedian(self, matrix):

        element = []

        for row in matrix:

            for val in row:

                element.append(val)

        element.sort()

        return element[len(element) // 2]
    

matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
obj = solution()
print(obj.findMedian(matrix))


import bisect

class solution:
    def countLessEqual(self, row, mid):
        return bisect.bisect_right(row, mid)
    
    def findMedian(self, matrix):
        rows = (len(matrix))
        cols = len(matrix[0])

        low = min(rows[0] for rows in matrix)
        high = max(rows[-1] for rows in matrix)

        while low < high:
            mid = (low + high) // 2
            count = 0

            for rows in matrix:
                count += self.countLessEqual(rows, mid)
            if count < (rows * cols + 1) // 2:
                low = mid + 1

            else:
                high = mid

        return low
    
matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
obj = solution()

print("Median:", obj.findMedian(matrix))


