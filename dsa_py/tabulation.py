#tabulation dynamic

class solution:

    def fib(self, n):

        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    
if __name__ == "__main__":
    n = 10
    sol = solution()
    print(sol.fib(n))

# space optimization

class solution:

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        prev2 = 0
        prev = 1

        for i in range(2, n + 1):
            curr = prev + prev2
            prev2 = prev
            prev = curr

        return prev
    
def main():
    s = solution()
    n = 10
    print(s.fib(n))

if __name__ == "__main__":
    main()