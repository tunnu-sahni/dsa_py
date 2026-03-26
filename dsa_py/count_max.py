# count maximum consecutive ones in the array

class solution:
    def findMaxConsecutive(self, nums):
        cnt = 0
        maxi = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1

            else:
                cnt = 0
            maxi = max(maxi, cnt)

        return maxi
    
nums = [1, 1, 0, 1, 1, 1]

obj = solution()
ans = obj.findMaxConsecutive(nums)

print("the maximum consecutive 1's are", ans)