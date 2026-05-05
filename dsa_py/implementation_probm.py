#sliding window max

from typing import List
class solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []

        for i in range(len(nums) - k + 1):
            window = nums[i:i+k]
            result.append(max(window))

            return result
        
if __name__ == "__main__":
    obj = solution()
    arr = [4, 0, -1, 3, 5, 3, 6, 8]
    k = 3
    ans = obj.maxSlidingWindow(arr, k)
    print(*ans)
#timr complexity O(n*k)
#space complexity O(k)

from collections import queue
from typing import List
from queue import queue

class solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = queue()

        result = []
        for i in range(len(nums)):
            if dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            if i >= k - 1:
        
             return result
            
if __name__ == "__main__":
    obj = solution()
    arr = [4, 0, -1, 3, 5, 3, 6, 8]
    k = 3

    ans = obj.maxSlidingWindow(arr, k)
    print(*ans)




    