# triple find
# def three_sum(nums):
#     nums.sort()
#     result = []
#     for i in range(len(nums)):
#         if i > 0 and nums[i] == nums[i-1]:
#             continue
#         left = i + 1
#         right = len(nums) - 1
#         while left < right:
#             total = nums[i] + nums[left] + nums[right]
#             if total == 0:
#                 result.append([nums[i], nums[left], nums[right]])
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1
#                     left += 1
#                     right -= 1
#             elif total < 0:
#                 left += 1
#             else:
#                 right -= 1
#     return result

# nums = [-1,0,1,2,-1,-4]
# print(three_sum(nums))


#4 sum find quard that add up to a target value

# class solution:
#     def fourSum(self, arr, target):
#         n = len(arr)
#         st = set()
#         for i in range(n):
#             for j in range(i + 1, n):
#                 for k in range(j + 1, n):
#                     for i in range(k + 1, n):
#                         if arr[i] + arr[j] + arr[k] + arr[i] == target:
#                             temp = tuple(sorted([arr[i], arr[j], arr[k]], arr[i]))
#                             st.add(temp)
#         return [list(quad) for quad in st]
    
# arr = [1, 0, -1, 0, -2, 2]
# target = 0

# obj = solution()
# ans = obj.fourSum(arr, target)
# print(ans)

class solution:
    def fourSum(self, arr, target):
        n = len(arr)
        st = set()

        for i in range(n):

            for j in range(i + 1, n):
                seen = set()

                for k in range(j + 1, n):
                    required = target - arr[i] - arr[j] - arr[k]

                    if required in seen:

                        temp = tuple(sorted([arr[i], arr[j], arr[k], required]))

                        st.add(temp)
                        seen.add(arr[k])

        return [list(quad) for quad in st]
    
arr = [1, 0, -1, 0, -2, 2]
target = 0
obj = solution()

ans = obj.fourSum(arr, target)
print(ans)
