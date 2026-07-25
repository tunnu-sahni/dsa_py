# class solution:
#     def solve(self, arr):
#         n = len(arr)
#         if n == 1:
#             return arr[0]
#         prev = arr[0]
#         prev2 = 0

#         for i in range(1, n):
#             pick = arr[i]
#             if i > 1:
#                 pick += prev2
#                 notpick = prev
#                 cur_i = max(pick, notpick)
#                 prev2 = prev
#                 prev = cur_i
#         return prev
#     def robStreet(self, n, arr):
#         if n == 0:
#             return 0
#         if n == 1:
#             return arr[0]
#         arr1 = arr[0:n-1]
#         arr2 = arr[1:n]
#         return max(self.solve(arr1), self.solve(arr2))
# if __name__ == "__main__":
#     arr = [1, 5, 1, 2, 6]
#     n = len(arr)
#     sol = solution()
#     print(sol.robStreet(n, arr))