#remove duplicate in place from sorted array

class solution:
    def removeDuplicates(self, nums):
        seen = set()

        index = 0

        for num in nums:

            if num not in seen:

                seen.add(num)
                nums[index] = num
                index += 1
        return index
    
nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,1,4,4,4,5,6,6,7,7,7]
sol = solution()
k = sol.removeDuplicates(nums)

print("k =", k)
print("Array after removing duplicate:", nums[:k])


class solution:
    def removeDuplicates(self, nums):

        if not nums:
            return 0
        
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
    
nums = [0,0,1,1,1,2,2,3,3,4]
sol = solution()
k = sol.removeDuplicates(nums)

print("Unique count =", k)
print("Array after removing duplicate:", nums[:k])