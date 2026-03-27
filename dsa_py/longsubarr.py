#longest subarray with given sum k(positive)


# class solution:
#     def longestSubarray(self, nums, k):
#         n = len(nums)
#         maxLength = 0
#         for startIndex in range(n):
#             for endIndex in range(startIndex, n):
#                 currentSum = 0
#                 for i in range(startIndex, endIndex + 1):
#                     currentSum += nums[i]
                
#                 if currentSum == k:
#                     maxLength = max(maxLength, endIndex - startIndex + 1)
#         return maxLength
    
# if __name__ == "__main__":
#     nums = [-1, 1, 1]
#     k = 1
#     sol = solution()
#     length = sol.longestSubarray(nums, k)

#     print("the length of the longest subarray is:", length)



class solution:
    def longestSubarray(self, nums, k):
        n = len(nums)

        maxLen = 0

        left = 0
        right = 0
        sum = nums[0]

        while right < n:
            while left <= right and sum > k:
                sum -= nums[left]
                left += 1

            if sum == k:
                maxLen = max(maxLen, right - left + 1)
                right += 1
                if right < n:
                    sum += nums[right]
            return maxLen
        
nums = [10, 5, 2, 7, 1, 9]
k = 15
sol = solution()
ans = sol.longestSubarray(nums, k)

print(f"the length of longest subarray having sum k is: {ans}")
