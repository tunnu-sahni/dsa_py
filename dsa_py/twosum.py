#kadanes algorithm maximum subarray sum in an array

# from typing import List

# class solution:
#     def maxSubArray(self, nums: list[int]) -> int:

#         maxi = float('-inf')

#         for i in range(len(nums)):

#             for j in range(i, len(nums)):
#                 sum = 0

#                 for k in range(i , j + 1):
#                     sum += nums[k]

#                 maxi = max(maxi, sum)

#         return maxi
    
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# sol = solution()
# maxSum = sol.maxSubArray(arr)

# print("the maximum subarray sum is:", maxSum)



#stock buy and sell


# class solution:
#     def stockbuySell(self, prices):
#         maxProfit = 0

#         for i in range(len(prices)):
#             for j in range(i + 1, len(prices)):

#                 profit = prices[j] - prices[i]

#                 maxprofit = max(maxProfit, profit)

#         return maxProfit
    
# sol = solution()
# prices = [7, 1, 5, 3, 6, 4]
# print("max profit:", sol.stockbuySell(prices))


class solution:

    def stockbuySell(self, prices):
        min_price = float('inf')

        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
        return max_profit

obj = solution()
prices = [7, 1, 5, 3, 6, 4]
print(obj.stockbuySell(prices))       