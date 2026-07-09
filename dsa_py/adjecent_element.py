#maximum sum of non-adjecent element
class solution:
    def solve(self, arr, i, dp):
        if i < 0:
            return 0
        if i == 0:
            return arr[0]
        
        if dp[i] != -1:
            return dp[i]
        pick = arr[i] + self.solve(arr, i - 2, dp)
        notpick = self.solve(arr, i - 1, dp)
        dp[i] = max(pick, notpick)
        return dp[i]
    
    def maximumNonAdjacentSum(self, arr):
        n = len(arr)
        dp = [-1] * n
        return self.solve(arr, n - 1, dp)
    
arr = [2, 1, 4, 9]
obj = solution()
print(obj.maximumNonAdjacentSum(arr)) 

class solution:
    def maximumNonAdjacentSum(self, arr):
        n = len(arr)
        if n == 1:
            return arr[0]
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, n):
            dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]
arr = [2, 1, 4, 9]
sol = solution()
print(sol.maximumNonAdjacentSum(arr))

class solution:
    def maxSum(self, nums):
        if not nums:
            return 0
        
        prev2 = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            include = nums[i] + prev2
            exclude = prev
            curr = max(include, exclude)
            prev2 = prev
            prev = curr

        return prev
    
arr = [3, 2, 5, 10, 7]
obj = solution()
print(obj.maxSum(arr))