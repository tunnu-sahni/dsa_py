# dynamic programing memeoization

class solution:
    def fib(self, n, dp):
        if n <= 1:
            return n
        
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = self.fib(n -1, dp) + self.fib(n - 2, dp)
        return dp[n]
    
if __name__ == "__main__":
    n = 10
    dp = [-1] * (n + 1)
    sol = solution()
    print(sol.fib(n, dp))