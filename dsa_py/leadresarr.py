#leaders in array

# class solution:
#     def leaders(self, nums):
#         ans = []

#         for i in range(len(nums)):
#             leader = True

#             for j in range(i + 1, len(nums)):
#                 if nums[j] >= nums[i]:
                
#                    leader = False
#                    break

#         if leader:
#             ans.append(nums[i])

#         return ans
    
# nums = [1, 2, 5, 3, 1, 2, 3, 2]
# finder = solution()

# ans = finder.leaders(nums)

# print("leaders in the array are:", end="")
# for leader in ans:
#     print(leader, end=" " )
#     print()


class solution:
    def leaders(self, nums):
        ans = []

        if not nums:
            return ans
        max_val = nums[-1]
        ans.append([-1])

        for i in range(len(nums) -2, -1, -1):
            if nums[i] > max_val:
                ans.append(nums[i])
                max_val = nums[i]
        ans.reverse()
        return ans
    
nums = [10, 22, 12, 3, 0, 6]

finder = solution()
ans = finder.leaders(nums)

print("the leaders in the array are:", end="")
for leader in ans:
    print(leader, end=" ")
    print()