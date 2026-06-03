#jump game2

class solution:
    def jump(self, nums):
        return self.min_jumps(nums, 0)
    def min_jumps(self, nums, position):
        if position >= len(nums) - 1:
            return 0
        
        if nums[position] == 0:
            return float('inf')
        
        min_step = float('inf')

        for jump in range(1, nums[position] + 1):
            sub_result = self.min_jumps(nums, position + jump)
            if sub_result != float('inf'):
                min_step = min(min_step, sub_result + 1)

        return min_step
if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    sol = solution()
    print("Minimum number of jumps:", sol.jump(nums))


class solution:
    def jump(self, nums):
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[n - 1]
    
sol = solution()
nums = [2, 3, 1, 1, 4]
print("Minimum jumps:", sol.jump(nums))


class solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps +=1
                current_end = farthest
        return jumps
    
if __name__ == "__main__":
    sol = solution()
    nums = [2, 4, 5, 5, 6]
    print("Minimum jumps:", sol.jump(nums))