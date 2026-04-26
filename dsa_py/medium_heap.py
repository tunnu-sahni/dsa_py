#Kth largest/smallest element in an array

# from py_compile import main


# class solution:
#     def kthLargestElement(self, nums, k):
#         import heapq
#         pq = []

#         for i in range(k):
#             heapq.heappush(pq, nums[i])
#             if nums[i] > pq[0]:
#                 heapq.heappop(pq)
#         return pq[0]
    
#     def main(self):
#        nums = [-5, 4, 1, 2, -3]
#        k = 3
#        sol = solution()

#        ans = sol.kthLargestElement(nums, k)
#        print("The kth largest element in the array is:", ans)

# if __name__ == "__main__":
#     sol = solution()
#     sol.main()


# import random

# class solution:
#     def kthLargestElement(self, nums, k):
#         if k > len(nums):
#             return -1
        
#         left, right = 0, len(nums) - 1
#         while True:
#             pivotIndex = self.randomIndex(left, right)
#             pivotIndex = self.partionAndReturnIndex(nums, pivotIndex, left, right)

#             if pivotIndex == k - 1:
#                 return nums[pivotIndex]
            
#             elif pivotIndex > k - 1:
#                 right = pivotIndex - 1

#             else:
#                 left = pivotIndex + 1

#         def randomIndex(self, left, right):
#             length = right = left + 1

#             return random.randint(left, right)
        
#         def partionAndReturnIndex(self, nums, pivotIndex, left, right):

#             pivot = nums[pivotINdex]

#             nums[left], nums[pivotIndex] = nums[pivotIndex], nums[left]

#             ind = left + 1

#             for i in range(left + 1, right + 1):
#                 if nums[i] > pivot:
#                     nums[ind], nums[i] = nums[i], nums[ind]

#                     ind += 1

#                 nums[left], nums[ind - 1] = nums[ind - 1], nums[left]

#                 return ind - 1
            
# def main():
#     nums = [-5, 4, 1, 2, -3]
#     k = 5

#     sol = solution()

#     ans = sol.kthLargestElement(nums, k)

#     print("The kth largest element in the array is:", ans)

# if __name__ == "__main__":
#     main()



#kth largest/smallest element in an array

class solution:
    def kthLargestElement(self, nums, k):
        import heapq
        pq = []

        for i in range(k):
            heapq.heappush(pq, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > pq[0]:
                heapq.heappop(pq)

                heapq.heappop(pq)

                heapq.heappush(pq, nums[i])
                return pq[0]
            
def main():
    nums = [-5, 4, 1, 2, -3]
    k = 5

    sol = solution()

    ans = sol.kthLargestElement(nums, k)

    print("The kth largest element in the array is:", ans)

if __name__ == "__main__":
    main()


import random

from pyparsing import nums

class solution:
    def kthLargestElement(self, nums, k):
        if k > len(nums):
            return -1
        
        left, right = 0, len(nums) - 1

        while True:
            pivotIndex = self.randomIndex(left, right)

            pivotIndex = self.partitionAndReturnIndex(nums, pivotIndex, left, right)

            if pivotIndex == k - 1:
                return nums[pivotIndex]
            
            elif pivotIndex > k - 1:
                right = pivotIndex - 1

            else:
                left = pivotIndex + 1

    def randomIndex(self, left, right):
        length = right - left + 1

        return random.randint(left, right)
    
    def partitionAndReturnIndex(self, nums, pivotIndex, left, right):
        pivot = nums[pivotIndex]

        nums[left], nums[pivotIndex] = nums[pivotIndex], nums[left]

        ind = left + 1

        for i in range(left + 1, right + 1):
            if nums[i] > pivot:
                nums[ind], nums[i] = nums[i], nums[ind]

                ind += 1

        nums[left], nums[ind - 1] = nums[ind - 1], nums[left]

        return ind - 1
    
    def main():
        nums = [-5, 4, 1, 2, -3]
        k = 5

        sol = solution()
        ans = sol.kthLargestElement(nums, k)

        print("The kth largest element in the array is:", ans)

if __name__ == "__main__":
    main()
