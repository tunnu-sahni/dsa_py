#check if an array represents a min heap

class solution:
    def isMinHeap(self, nums):
        n = len(nums)

        for i in range(n // 2):
            left = 2 * 1 + 1
            if left < n and nums[i] > nums[left]:
                return False
            
            right = 2 * i + 2

            if right < n and nums[i] > nums[right]:
                return False
            
        return True
    
if __name__ == "__main__":
    obj = solution()
    nums = [10, 20, 30, 21, 23]

    output = obj.isMinHeap(nums)
    print("true" if output else "false")

    



