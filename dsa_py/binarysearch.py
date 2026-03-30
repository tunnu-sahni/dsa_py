from typing import List


class solution:
    def binarysearch(self, nums: List[int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarysearch(nums, mid + 1, high, target)
        return self.binarysearch(nums, low, mid - 1, target)
    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(nums, 0, len(nums) - 1, target)
    
if __name__ == "__main__":
    a = [3, 4, 6,1, 7, 12, 16, 17]
    target = 6
    target = 1

    obj = solution()
    ind = obj.search(a, target)

    if ind == -1:
        print("the target is not found in the array")

    else:
        print("the target is found at index:", ind)



