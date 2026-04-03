
# class solution:

#     def lower_bound(self, arr, n, x):
#         low, high = 0, n - 1
#         ans = n

#         while low <= high:
#             mid = (low + high) // 2
#             if arr[mid] >= x:
#                 ans = mid

#                 high = mid - 1

#             else:
#                 low = mid + 1

#         return ans
    
#     def row_with_max_1s(self, matrix, n, m):
#         cnt_max = 0

#         index = -1

#         for i in range(n):
#             cnt_ones = m - self.lower_bound(matrix[i], m, 1)

#             if cnt_ones > cnt_max:
#                 cnt_max = cnt_ones
#                 index = i

#         return index
    
# if __name__ == "__main__":
#     matrix = [[1, 1, 1],[0, 0, 1],[0, 0, 0]]
#     n, m = 3, 3

#     obj = solution()
#     print("the row with maximum no. of 1's is:", obj.row_with_max_1s(matrix,n,m))



# #search in a sorted 2d matrix

# class solution:
#     def searchMatrix(self, matrix, target):

#         n = len(matrix)

#         m = len(matrix[0])

#         for i in range(i):
#             for j in range(m):

#                 if matrix[i][j] == target:
#                     return True
                
#         return False
    
# if __name__ == "__main__":
#     matrix [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12]
#     ]

#     obj = solution()

#     if obj.searchMatrix(matrix, 8):
#         print("true")

#     else:
#         print("false")



class solution:
    def binarySearch(self, nums, target):

        n = len(nums)

        low, high = 0, n - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            
            elif target > nums[mid]:
                low = mid + 1

            else:
                high = mid - 1

        return False
    
    def searchMatrix(self, matrix, target):

        n = len(matrix)

        m = len(matrix[0])

        for i in range(n):

            if matrix[i][0] <= target <= matrix[i][m - 1]:
                return self.binarySearch(matrix[i], target)
                
                return False
            

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    obj = solution()

    if obj.searchMatrix(matrix, 8):
        print("true")

    else:
        print("false")



class solution:
    def searchMatrix(self, matrix, target):

        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = n * m - 1

        while low <= high:
            mid = (low + high) // 2

            row = mid // m
            col = mid % m

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] < target:
                low = mid + 1

            else:
                high = mid - 1
        return False
    
if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    obj = solution()

    print("true" if obj.searchMatrix(matrix, 8) else "false")





