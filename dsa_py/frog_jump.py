#frog jump(dp 3)
#memoization approach
class Solution:
    # Solve function using recursion with memoization
    # ind -> current index the frog needs to reach
    # height -> list of heights
    # dp -> memo table where dp[i] stores min cost to reach i
    def solve(self, ind, height, dp):
        # If at the first stone, cost is 0
        if ind == 0:
            return 0

        # Return memoized result if already computed
        if dp[ind] != -1:
            return dp[ind]

        # Initialize jumpTwo with a large value
        jumpTwo = float('inf')

        # Compute cost when jumping from previous stone (ind - 1)
        jumpOne = self.solve(ind - 1, height, dp) + abs(height[ind] - height[ind - 1])

        # Compute cost when jumping from two stones back (ind - 2) if possible
        if ind > 1:
            jumpTwo = self.solve(ind - 2, height, dp) + abs(height[ind] - height[ind - 2])

        # Memoize and return the minimum of the two choices
        dp[ind] = min(jumpOne, jumpTwo)
        return dp[ind]

    # Helper to handle edge cases and start recursion
    def frogJump(self, height):
        # Handle empty input
        if not height:
            return 0

        # Prepare dp with -1 indicating uncomputed states
        n = len(height)
        dp = [-1] * n

        # Start from the last index
        return self.solve(n - 1, height, dp)


if __name__ == "__main__":
    # Define the heights array
    height = [30, 10, 60, 10, 60, 50]

    # Create Solution instance
    sol = Solution()

    # Compute and print the minimum energy
    print(sol.frogJump(height))  # Expected: 40
#tabulation approach

class solution:

    def frogJump(self, height):

        if not height:
            return 0
        
        n = len(height)
        dp = [float('inf')] * n
        dp[0] = 0

        for ind in range(1, n):
            jump_one = dp[ind - 1] + abs(height[ind] - height[ind - 1])
            jump_two = float('inf')
            if ind > 1:
                jump_two = dp[ind - 2] + abs(height[ind] - height[ind - 2])

            dp[ind] = min(jump_one, jump_two)

        return dp[-1]
    
if __name__ == "__main__":
    height = [30, 10, 40, 10, 60, 50]

    sol = solution()
    print(sol.frogJump(height))

#space optimization approach

class solution:

    def frogJump(self, height):

        if not height:
            return 0
        
        n = len(height)
        if n == 1:
            return 0
        prev = 0
        prev2 = 0

        for i in range(1, n):
            jump_one = prev + abs(height[i] - height[i - 1])
            if i > 1:
                jump_two = prev2 + abs(height[i] - height[i - 2])

            else:
                jump_two = float('inf')

            prev2 = prev
            prev = min(jump_one, jump_two)

        return prev
    
if __name__ == "__main__":
    height = [20, 40, 50, 20, 50]

    sol = solution()

    print(sol.frogJump(height))