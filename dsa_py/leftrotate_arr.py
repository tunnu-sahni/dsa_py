#left rotate the array by one

# class solution:
#     def solve(arr, n):
#         temp = [0] * n
#         for i in range(1, n):
#             temp[i - 1] = arr[i]
        
#         temp[n - 1] = arr[0]

#         for num in temp:
#             print(num, end=" ")

#         print()

# if __name__ == "__main__":
#     n = 5
#     arr = [1,2,3,4,5]

#     print(arr, n)
    

# class solution:
#     def rotateArrayByOne(self, nums):

#         temp = nums[0]

#         for i in range(1, len(nums)):
#             nums[i - 1] = nums[i]

#         nums[-1] = temp

# if __name__ == "__main__":
#     solution = solution()
#     nums = [1,2,3,4,5]
    
#     solution.rotateArrayByOne(nums)
#     print(nums)


# class solution:
#     def rotateArrayByOne(self, nums):
#         temp = nums[0]

#         for i in range(1, len(nums)):
#             nums[i -1] = nums[i]

#         nums[-1] = temp

# if __name__ == "__main__":
#     sol = solution()
#     nums = [2,3,4,5,6]
#     sol.rotateArrayByOne(nums)
#     print(nums)





#rotate array by k elements

# class solution:
#     def rotateRight(self, arr, k):
#         n = len(arr)
#         if n == 0:
#             return
#         k %= n

#         temp = arr[-k:]

#         for i in range(n - k - 1, -1, -1):
#             arr[i + k] = arr[i]

#         for i in range(k):
#             arr[n -k + i] = temp[i]

# sol = solution()

# arr = [1,2,3,4,5,6,7]
# k = 2
# sol.rotateRight(arr, k)
# print("Array after left rotation:", arr)


# class solution:
#     def reverse(self, nums, start, end):

#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start += 1
#             end -= 1

#     def rotateArray(self, nums,k, direction):
#         n = len(nums)

#         if n == 0 or k == 0:
#             return nums
        
#         k = k % n
#         if direction == "right":

#             self.reverse(nums, 0, n - 1)
#             self.reverse(nums, k, n - 1)
#             self.reverse(nums, k, n - 1)

#         elif direction == "left":

#             self.reverse(nums, 0, k - 1)
#             self.reverse(nums, k, n - 1)
#             self.reerse(nums, 0, n - 1)

#         return nums
    
# sol = solution()

# nums = [1,2,3,4,5,6,7]
# k = 2
# direction = "right"

# result = sol.rotateArray(nums, k, direction)

# print(result)


#move all zeros to the end of the array


# class solution:
#     def moveZeros(self, arr):
#         temp = [0] * len(arr)

#         index = 0

#         for num in arr:
#             if num != 0:
#                 temp[index] = num
#                 index += 1

#         for i in range(len(arr)):
#             arr[i] = temp[i]

#         return arr
    
# def main():
#     arr = [0,1,0,3, 12]
#     sol = solution()
#     result = sol.moveZeros(arr)

#     print("Array after moving zeros:", end=" ")
#     for num in result:
#         print(num, end=" ")
#     print()

# main() 


class solution:
    def moveZeros(self, nums):
        j = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return
        
        for i in range(j + 1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

sol = solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeros(nums)

print(" ".join(map(str, nums)))


