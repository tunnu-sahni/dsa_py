
class BinarySearchInsert:

    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left



obj = BinarySearchInsert()

nums = [1, 3, 5, 6]
target = 5

index = obj.searchInsert(nums, target)

print("The target is found at index:", index)


class Binarysearchinsert:

    def serachInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:

              return mid
            
            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1
        return left
    
obj = Binarysearchinsert()
nums = [1, 3, 5, 6]
target = 2
target = 1
index = obj.serachInsert(nums, target)
print("the target is found at index:", index)