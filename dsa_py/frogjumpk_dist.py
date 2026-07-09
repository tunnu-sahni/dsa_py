#frog jump with k distance
#memoization
class solution:
    def solveUtil(self, ind, height, dp, k):
        if ind == 0:
            return 0
        
        if dp[ind] != -1:
            return dp[ind]
        mmSteps = float('inf')
        for j in range(1, k + 1):
            if ind - j >= 0:
                jump = self.solveUtil(ind - j, height, dp, k) + abs(height[ind] - height[ind - j])
                mmSteps = min(jump, mmSteps)

        dp[ind] = mmSteps
        return dp[ind]
    def solve(self, n, height, k):
        dp = [-1] * n
        return self.solveUtil(n - 1, height, dp, k)
    
if __name__ == "__main__":
    height = [30, 10, 50, 70, 20]
    n = len(height)
    k = 2
    sol = solution()
    print(sol.solve(n, height, k))

#tabulation
class solution:
    def solveUtil(self, n, height, dp, k):
        dp[0] = 0
        for i in range(1, n):
            mmSteps = float('inf')
            for j in range(1, k + 1):
                if i - j >= 0:
                    jump = dp[i - j] + abs(height[i] - height[i - j])
                    mmSteps = min(mmSteps, jump)

            dp[i] = mmSteps
        return dp[n - 1]
    def solve(self, n, height, k):
        dp = [-1] * n
        return self.solveUtil(n, height, dp, k)
    
if __name__ == "__main__":
    height = [30, 10, 60, 20, 40]
    n = len(height)
    k = 2
    sol = solution()
    print(sol.solve(n, height, k))
